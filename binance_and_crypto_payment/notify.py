import base64
import hashlib
import hmac
import urllib.parse

from .utils import php_http_build_query


class CryptoPaymentNotify:

    REQUIRED_FIELDS = [
        "order_id", "ext_transaction_id", "transaction_id", "status_code",
        "note", "confirm_rcv_amnt", "confirm_rcv_amnt_curr",
        "coin_rcv_amnt", "coin_rcv_amnt_curr", "txn_time"
    ]

    def __init__(self, public_key: str, secret_key: str):
        self.public_key = public_key
        self.secret_key = secret_key

    def process(self, request):
        try:
            public_key, signature = self._decode_auth(request)
            self._validate_public_key(public_key)

            data = self._extract_data(request)

            status = self._validate_status(data["status_code"])
            if status == "cancelled":
                return {
                    "status": False,
                    "type": "cancelled",
                    "message": "Order Cancelled"
                }

            self._verify_signature(data, signature)

            return {
                "status": True,
                "type": "success",
                "data": data
            }

        except ValueError as e:
            return {
                "status": False,
                "type": "error",
                "message": str(e)
            }

    # ---------------- PRIVATE METHODS ---------------- #

    def _decode_auth(self, request):
        auth_header = request.headers.get("Authorization")

        if auth_header:
            auth_str = auth_header.replace("Bearer ", "")
        else:
            auth_str = request.POST.get("authStr")

        if not auth_str:
            raise ValueError("authStr not found")

        try:
            decoded = base64.b64decode(auth_str).decode()
            return decoded.split(":", 1)
        except Exception:
            raise ValueError("Invalid authorization format")

    def _validate_public_key(self, received_key):
        if self.public_key != received_key:
            raise ValueError("Public key mismatch")

    def _extract_data(self, request):
        POST = request.POST
        data = {key: POST.get(key, "") for key in self.REQUIRED_FIELDS}

        if not data["order_id"] or not data["transaction_id"]:
            raise ValueError("Required fields missing")

        try:
            data["status_code"] = int(data["status_code"])
        except ValueError:
            raise ValueError("Invalid status code")

        return data

    def _verify_signature(self, data, signature_received):
        sorted_data = dict(sorted(data.items()))
        flat = php_http_build_query(sorted_data)
        query_string = urllib.parse.urlencode(flat)

        correct_signature = hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

        if not hmac.compare_digest(correct_signature, signature_received):
            raise ValueError("Signature not matched")

    def _validate_status(self, status_code):
        if status_code == 20000:
            return "cancelled"

        if status_code != 200:
            raise ValueError("Order not complete")

        return "success"