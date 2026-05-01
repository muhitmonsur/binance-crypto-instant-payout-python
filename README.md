# Direct-to-Wallet python Crypto Gateway: Fast Binance payment API (No Merchant account Needed)

Official Python SDK for Binance and Crypto Payment integration.

## Installation

pip install binance-and-crypto-payment


# Accept USDT USDC BTC & ETH in python: 10-Minute Binance Payment Gateway Integration


<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/banner-772x250.png">

## Introduction

The Binance and Crypto Payment Gateway python projects is powered by Payerurl. This package acts as a robust cryptocurrency payment processor, allowing merchants and developers to receive customer payments directly into their crypto wallets without the need for a middleman or intermediary account. We specialize in Binance QR code payments, providing a smooth, integrated experience where users never have to leave your python application to complete a transaction.


### Binance QR Code Payment
<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-5.png">
This package is the ideal solution for developers seeking a secure Binance payment integration for Python and django. Binance payment is a contactless, borderless, and highly secure payment method. By using this projects , you can accept payments via Binance QR codes and process transactions through the Binance personal account API.

The projects serves as a seamless bridge between Binance and your Python application. Customers simply scan the  QR code on your checkout page to finish the transaction. This process is:

* **Fast and Simple**: No complex redirects or external logins for the user.
* **Cost-Effective**: Incurs no network fees or additional hidden costs.
* **Secure**: Enhanced security protocols help avoid scams and ensure transaction safety.

## 📞 Contact US
#### 🌐 Website: <a href="https://payerurl.com" target="_blank" rel="noopener noreferrer">https://payerurl.com</a>
#### 📞 Telegram: <a href="https://t.me/Payerurl" target="_blank" rel="noopener noreferrer">https://t.me/Payerurl (live chat)</a>
#### 📧 Email: support@payerurl.com

### <a href="https://python.payerurl.com/" target="_blank" rel="noopener noreferrer">👉 LIVE DEMO — Click to open in new tab</a>

### How This Package Works

The Binance and Crypto Payment Gateway automatically converts any fiat currency to the selected cryptocurrency using live exchange rates. Once the payment is verified, funds are credited instantly to the merchant's wallet. The package then utilizes a secure API response to update your application's order status (e.g., from "Pending" to "Processing") in real-time.

### Key Features

* **Extensive Network Support**: Supports Binance QR payment, Binance Pay, USDT (TRC20/ERC20), USDC (ERC20), Bitcoin (BTC), and Ethereum (ETH ERC20).
* **Fiat Compatibility**: Supports over 169+ fiat currencies (USD, CAD, GBP, EUR, etc.) with real-time exchange rates powered by payerurl.com.
* **Developer Friendly**: 100% Free Open Source package designed specifically for the Laravel ecosystem.
* **Privacy Focused**: No bank account or mandatory personal identity verification required.
* **Simple Integration**: Streamlined signup process with easy API key integration.
* **Accessibility**: No KYC required for withdrawals on Basic accounts.
* **Dedicated Support**: 24/7 technical assistance for integration via Telegram: https://t.me/Payerurl.

### About Payerurl

Payerurl is a premier payment processor enabling direct cryptocurrency transfers from customers to merchant wallets. Merchants can integrate Binance personal/merchant APIs alongside various receiving wallets including USDT, BTC, ETH, and USDC. We utilize live market rates to ensure accurate conversion from local fiat currencies to the corresponding cryptocurrency amount.


### <a href="https://python.payerurl.com/" target="_blank" rel="noopener noreferrer">🔴 LIVE DEMO</a>

## 🔑 GET API KEY
Get your API key: <a href="https://dash.payerurl.com" target="_blank" rel="noopener noreferrer">https://dash.payerurl.com</a>





## 🚀 How It Works

1. Collect user and order info on your platform.
2. Call the payment() function with required details.
3. User is redirected to PayerURL payment page.
4. After payment:
   * User is redirected to redirect_url.
   * Your backend receives a callback at notify_url with transaction details.
   * On cancellation, user is returned to cancel_url.



## Usage

    from binance_and_crypto_payment import CryptoPaymentClient

    client = CryptoPaymentClient(
        public_key="YOUR_PUBLIC_KEY",
        secret_key="YOUR_SECRET_KEY"
    )

    response = client.payment(
        invoice_id="INV001",
        amount=1.00,
        currency="USD",
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


## Notify Url Callback

    from django.http import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    from django.views.decorators.http import require_POST
    from django.db import transaction
    import logging

    from binance_and_crypto_payment import CryptoPaymentNotify, CryptoPaymentException, StatusCode


    @csrf_exempt
    @require_POST
    def payerurl_notify(request):
        notify = CryptoPaymentNotify(
            public_key="YOUR_PUBLIC_KEY",
            secret_key="YOUR_SECRET_KEY"
        )

        try:
            result = notify.process(request)

            if result["type"] == "cancelled":
                return JsonResponse(
                    {"status": StatusCode.ORDER_CANCELLED, "message": "Order Cancelled"},
                    status=200
                )

            data = result["data"]

            # -------------------------------
            # 🔥 YOUR BUSINESS LOGIC GOES HERE
            # -------------------------------
            # Example pseudo-code:
            # with transaction.atomic():
            # order = Order.objects.select_for_update().get  (invoice_id=data["order_id"])
            #     txn = Transaction.objects.select_for_update().get(order=order)
            #     if order.status == "paid" or txn.status == "success":
            #         return JsonResponse({"status": StatusCode.ALREADY_PROCESSED, "message": "Already processed"}, status=200)
            #     txn.transaction_id = data["transaction_id"]
            #     txn.status = "success"
            #     txn.raw_response = request.POST.dict()
            #     txn.save()
            #     order.status = "paid"
            #     order.invoice_id = data.get("ext_transaction_id", order.invoice_id)
            #     order.save()

            return JsonResponse({"status": StatusCode.SUCCESS, "message": "Payment processed successfully"}, status=200)

        except CryptoPaymentException as e:
            return JsonResponse({"status": e.code, "message": e.message}, status=400)

        except Exception:        
            return JsonResponse({"status": StatusCode.INTERNAL_ERROR, "message": "Internal error"}, status=500)


<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-1.png">
<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-2.png">
<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-4.png">
<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-6.png">
<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-7.png">
<img src="https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-8.png">


## License

This projects is open-sourced software licensed under the [MIT license](LICENSE).

## Support

For support and questions, please contact us via:
- Telegram: https://t.me/Payerurl
- Website: https://payerurl.com

---
