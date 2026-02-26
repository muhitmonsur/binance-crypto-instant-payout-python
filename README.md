# binance-and-crypto-payment

Official Python SDK for Binance and Crypto Payment integration.

## Installation

pip install binance-and-crypto-payment

## Usage

from binance_and_crypto_payment import CryptoPaymentClient

client = CryptoPaymentClient("PUBLIC_KEY", "SECRET_KEY")

response = client.payment(
    invoice_id="INV001",
    amount=1.00,
    items=[{"name": "Product", "qty": "1", "price": "1.00"}],
    data={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "redirect_url": "https://example.com/success",
        "notify_url": "https://example.com/notify",
        "cancel_url": "https://example.com/cancel",
    }
)

print(response)
