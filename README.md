# Direct-to-Wallet python Crypto Gateway: Fast Binance payment API (No Merchant account Needed)

Official Python SDK for Binance and Crypto Payment integration.

## Installation

pip install binance-and-crypto-payment


## 🔑 GET API KEY
Get your API key: [https://dash.payerurl.com](https://dash.payerurl.com)


## 🚀 How It Works

1. collect  your payerurl api public key and secret key . Get your API key: [https://dash.payerurl.com](https://dash.payerurl.com)->dashboard->get api credencials
2. Create a new file (payment.py)  in your project root directory
3. Paste the below code block


## payment.py

    from binance_and_crypto_payment import CryptoPaymentClient
    import time
    
    invoice_id = f"INV-{int(time.time())}"
    amount=1.00
    currency="USD"
    first_name="customer first name"
    last_name= "customer last name"
    email= "customeremail@email.com"
    
    # item variable
    productItemName= "Product"
    qty= "1"
    price= "1.00"
    
    
    client = CryptoPaymentClient(
        public_key="PAYERURL API PUBLIC KEY",  # your public key from dash.payerurl.com
        secret_key="PAYERURL API SECRET KEY"   # your secret key from dash.payerurl.com
    )
    
    
    response = client.payment(
        invoice_id=invoice_id,
        amount=amount, # default if there has no value
        currency=currency, # default currency, please change accroding to your store currency 
        items=[{"name": productItemName , "qty": qty, "price": price}], # default product item description 
        data={
            "first_name": first_name,  
            "last_name": last_name,    
            "email": email, 
    
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

4. run python .\payment.py
5. you will get response like {'status': True, 'redirect_to': 'https://api-v2.payerurl.com/web-payment-option/PYP19DFD97D5DC'}
6. the payment link is like "https://api-v2.payerurl.com/web-payment-option/PYP19DFD97D5DC"
7. use this link to make a payment for your customer. 




# Accept USDT USDC BTC & ETH in python: 10-Minute Binance Payment Gateway Integration


![banner](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/banner-772x250.png)

## Introduction

The Binance and Crypto Payment Gateway python projects is powered by Payerurl. This package acts as a robust cryptocurrency payment processor, allowing merchants and developers to receive customer payments directly into their crypto wallets without the need for a middleman or intermediary account. We specialize in Binance QR code payments, providing a smooth, integrated experience where users never have to leave your python application to complete a transaction.


### Binance QR Code Payment
![screenshot-5](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-5.png)

This package is the ideal solution for developers seeking a secure Binance payment integration for Python and django. Binance payment is a contactless, borderless, and highly secure payment method. By using this projects , you can accept payments via Binance QR codes and process transactions through the Binance personal account API.

The projects serves as a seamless bridge between Binance and your Python application. Customers simply scan the  QR code on your checkout page to finish the transaction. This process is:

* **Fast and Simple**: No complex redirects or external logins for the user.
* **Cost-Effective**: Incurs no network fees or additional hidden costs.
* **Secure**: Enhanced security protocols help avoid scams and ensure transaction safety.



### [👉 LIVE DEMO — Click to open in new tab](https://python.payerurl.com/)

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


### [🔴 LIVE DEMO](https://python.payerurl.com/)


![screenshot-1](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-1.png)
![screenshot-2](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-2.png)
![screenshot-4](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-4.png)
![screenshot-6](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-6.png)
![screenshot-7](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-7.png)
![screenshot-8](https://raw.githubusercontent.com/muhitmonsur/assets/refs/heads/main/screenshot-8.png)


## License

This projects is open-sourced software licensed under the [MIT license](LICENSE).

## Support

For support and questions, please contact us via:
- Telegram: https://t.me/Payerurl
- Website: https://payerurl.com
