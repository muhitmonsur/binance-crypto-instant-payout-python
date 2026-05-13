# 🪙 Binance & Crypto Payment Gateway for Python

> Accept Bitcoin, USDT, USDC, ETH, and BNB payments directly into your wallet — no middleman, no merchant account, no KYC required.

**Powered by [PayerURL](https://payerurl.com)** — the direct-to-wallet crypto payment processor for Python developers.

🔴 **[LIVE DEMO](https://python.payerurl.com/)** | 🔑 **[Get API Key](https://dash.payerurl.com)** | 💬 **[Telegram Support](https://t.me/Payerurl)**

---

## ✅ Why Developers Choose This Package

| Feature | Detail |
|---|---|
| 🏦 **No merchant account needed** | Payments go directly to your crypto wallet |
| 🌍 **169+ fiat currencies** | USD, EUR, GBP, CAD and more — converted at live rates |
| ⚡ **10-minute integration** | Simple API, clear docs, copy-paste code |
| 🔒 **No KYC for withdrawals** | Basic accounts withdraw without identity verification |
| 📱 **Binance QR Code payments** | Customers scan and pay without leaving your app |
| 💸 **Zero hidden fees** | No network surcharges or platform fees |
| 🛠️ **Django & Flask ready** | Works with any Python web framework |

---

## 📦 Installation

```bash
pip install binance-and-crypto-payment
```

---

## 🔑 Get Your API Key (Free)

1. Sign up at **[dash.payerurl.com](https://dash.payerurl.com)**
2. Go to **Dashboard → Get API Credentials**
3. Copy your **Public Key** and **Secret Key**

> 👉 Registration is free and takes under 2 minutes. No credit card required.

---

## 🚀 Quick Start (5 Lines of Code)

```python
from binance_and_crypto_payment import CryptoPaymentClient
import time

client = CryptoPaymentClient(
    public_key="YOUR_PUBLIC_KEY",   # from dash.payerurl.com
    secret_key="YOUR_SECRET_KEY"
)

response = client.payment(
    invoice_id=f"INV-{int(time.time())}",
    amount=10.00,
    currency="USD",
    items=[{"name": "Product", "qty": "1", "price": "10.00"}],
    data={
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
            ##-------------------------------DO NOT CHANGE THE BELOW SECTION-------------------------##
            ##---------------------------------------------------------------------------------------##
            "redirect_url": "https://python.payerurl.com/success",  # After successful payment customer will redirect to this url.
            "notify_url": "https://python.payerurl.com/notify",  # After payment complete our system automatically sent payment detail on this notify_url in few seconds.
            "cancel_url": "https://python.payerurl.com/cancel", # If you user cancel any payment, user will redirect to cancel url
            ##-------------------------------DO NOT CHANGE THE ABOVE SECTION-------------------------##
            ##---------------------------------------------------------------------------------------##
    }
)

print(response)
# {'status': True, 'redirect_to': 'https://api-v2.payerurl.com/web-payment-option/PYP...'}
```

Send the customer to `response['redirect_to']` — they pay with crypto, you receive it instantly in your wallet.

---

## 🌐 Supported Cryptocurrencies & Networks

| Currency | Networks |
|---|---|
| **USDT** | TRC20 (Tron), ERC20 (Ethereum) |
| **USDC** | ERC20 (Ethereum) |
| **Bitcoin (BTC)** | Bitcoin Network |
| **Ethereum (ETH)** | ERC20 |
| **Binance Pay** | Binance QR Code |

---

## 🔗 Django Integration Example

```python
# views.py
from binance_and_crypto_payment import CryptoPaymentClient
from django.http import JsonResponse
import time

def create_payment(request):
    client = CryptoPaymentClient(
        public_key="YOUR_PUBLIC_KEY",
        secret_key="YOUR_SECRET_KEY"
    )

    response = client.payment(
        invoice_id=f"INV-{int(time.time())}",
        amount=float(request.POST.get("amount")),
        currency="USD",
        items=[{"name": request.POST.get("product"), "qty": "1", "price": request.POST.get("amount")}],
        data={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            ##-------------------------------DO NOT CHANGE THE BELOW SECTION-------------------------##
            ##---------------------------------------------------------------------------------------##
            "redirect_url": "https://python.payerurl.com/success",  # After successful payment customer will redirect to this url.
            "notify_url": "https://python.payerurl.com/notify",  # After payment complete our system automatically sent payment detail on this notify_url in few seconds.
            "cancel_url": "https://python.payerurl.com/cancel", # If you user cancel any payment, user will redirect to cancel url
            ##-------------------------------DO NOT CHANGE THE ABOVE SECTION-------------------------##
            ##---------------------------------------------------------------------------------------##
        }
    )

    return JsonResponse(response)
```

---

## 🔗 Flask Integration Example

```python
# app.py
from flask import Flask, request, jsonify, redirect
from binance_and_crypto_payment import CryptoPaymentClient
import time

app = Flask(__name__)

client = CryptoPaymentClient(
    public_key="YOUR_PUBLIC_KEY",
    secret_key="YOUR_SECRET_KEY"
)

@app.route("/pay", methods=["POST"])
def pay():
    response = client.payment(
        invoice_id=f"INV-{int(time.time())}",
        amount=float(request.form["amount"]),
        currency="USD",
        items=[{"name": "Order", "qty": "1", "price": request.form["amount"]}],
        data={
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            ##-------------------------------DO NOT CHANGE THE BELOW SECTION-------------------------##
            ##---------------------------------------------------------------------------------------##
            "redirect_url": "https://python.payerurl.com/success",  # After successful payment customer will redirect to this url.
            "notify_url": "https://python.payerurl.com/notify",  # After payment complete our system automatically sent payment detail on this notify_url in few seconds.
            "cancel_url": "https://python.payerurl.com/cancel", # If you user cancel any payment, user will redirect to cancel url
            ##-------------------------------DO NOT CHANGE THE ABOVE SECTION-------------------------##
            ##---------------------------------------------------------------------------------------##
        }
    )
    return redirect(response["redirect_to"])
```

---

## 📲 How the Binance QR Payment Works

1. Your app calls the API and gets a **payment URL**
2. Customer is redirected to a secure checkout page
3. Customer **scans the QR code** with their Binance app
4. Payment is confirmed and funds land **directly in your wallet**
5. Your `notify_url` receives a webhook with the order status update

No bank accounts. No intermediaries. No waiting.

---

## 🛡️ Security & Privacy

- ✅ Payments go directly to **your** wallet — PayerURL never holds your funds
- ✅ No mandatory KYC for basic accounts
- ✅ No personal identity verification required to get started
- ✅ Secure API with HMAC signature verification
- ✅ MIT licensed — fully open source, audit it yourself

---

## 🌍 Supported Fiat Currencies (169+)

USD, EUR, GBP, CAD, AUD, JPY, SGD, AED, INR, BRL, MXN, NGN, PKR, BDT, and 150+ more.

All fiat amounts are automatically converted to the equivalent crypto amount at live market rates.

---

## 📊 Full Payment Flow Diagram

```
Your App → PayerURL API → Checkout Page → Customer Pays (Binance/Crypto)
                                                    ↓
Your Wallet ← Funds (instant) ← Payment Verified ← Blockchain
                                                    ↓
          Your notify_url ← Webhook (order status update)
```

---

## 🆚 Compared to Other Payment Solutions

| | **PayerURL (This Package)** | Stripe / PayPal | Coinbase Commerce |
|---|---|---|---|
| No merchant account | ✅ | ❌ | ✅ |
| Direct to your wallet | ✅ | ❌ | Partial |
| No KYC required | ✅ (Basic) | ❌ | ❌ |
| Binance QR support | ✅ | ❌ | ❌ |
| Python SDK | ✅ | ✅ | ✅ |
| 169+ fiat currencies | ✅ | Partial | ❌ |
| Zero platform fees | ✅ | ❌ | ❌ |

---

## ❓ FAQ

**Do I need a Binance account?**
Yes, to accept Binance QR payments. For USDT/BTC/ETH/USDC, you just need the corresponding wallet address.

**Is there a transaction fee?**
No network or hidden fees from PayerURL. Standard blockchain network fees may apply depending on the coin.

**Can I use this without KYC?**
Yes. Basic accounts can receive and withdraw crypto without mandatory identity verification.

**Does this work with Django REST Framework / FastAPI?**
Yes — it's a pure Python client that works with any framework.

---

## 📬 Support

| Channel | Link |
|---|---|
| 💬 Telegram | [t.me/Payerurl](https://t.me/Payerurl) |
| 🌐 Website | [payerurl.com](https://payerurl.com) |
| 📊 Dashboard | [dash.payerurl.com](https://dash.payerurl.com) |
| 🔴 Live Demo | [python.payerurl.com](https://python.payerurl.com) |

---

## 📄 License

MIT License — free for personal and commercial use.

---

## 🏷️ Keywords

`crypto payment` `bitcoin payment python` `binance payment gateway` `usdt payment django` `usdc payment flask` `accept crypto python` `crypto checkout` `binance qr code` `trc20 payment` `erc20 payment` `no kyc payment gateway` `direct wallet payment` `crypto invoice python` `binance pay api` `payerurl python sdk`
