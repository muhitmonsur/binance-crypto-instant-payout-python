from .constants import StatusCode

class CryptoPaymentException(Exception):
    def __init__(self, message, code, http_status=400):
        self.message = message
        self.code = code
        self.http_status = http_status
        super().__init__(message)