import requests
import hashlib
import hmac
import base64
import urllib.parse
from .utils import php_http_build_query


class CryptoPaymentRequest:

    API_URL = "https://api-v2.payerurl.com/api/payment"

    def __init__(self, public_key: str, secret_key: str):
        self.public_key = public_key
        self.secret_key = secret_key

    def payment(self, invoice_id, amount, currency="usd", items=None, data=None):
        if not invoice_id or not amount or not isinstance(data, dict):
            raise ValueError("Invalid input data")

        params = {
            "order_id": invoice_id,
            "amount": amount,
            "items": items or [],
            "currency": currency.lower(),
            "billing_fname": data.get("first_name", ""),
            "billing_lname": data.get("last_name", ""),
            "billing_email": data.get("email", ""),
            "redirect_to": data["redirect_url"],
            "notify_url": data["notify_url"],
            "cancel_url": data["cancel_url"],
            "type": "pyp",
        }

        flat = php_http_build_query(params)
        flat = dict(sorted(flat.items()))
        query_string = urllib.parse.urlencode(flat)

        signature = hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

        auth = "Bearer " + base64.b64encode(
            f"{self.public_key}:{signature}".encode()
        ).decode()

        response = requests.post(
            self.API_URL,
            data=query_string,
            headers={
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Authorization": auth,
            }
        )

        try:
            result = response.json()
        except Exception:
            result = {}

        if response.status_code == 200 and result.get("redirectTO"):
            return {"status": True, "redirect_to": result["redirectTO"]}

        return {"status": False, "message": result.get("message", "Payment failed")}
