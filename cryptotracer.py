import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def price_tracker(update, context):

    base_url = "https://indodax.com"
    coin_name = context.args[0]
    api_url = f"{base_url}/api/ticker/{coin_name}idr"
    response = requests.get(api_url)

    print(response.json().get("ticker").get("last"))
    price_data = response.json().get("ticker").get("last")
    price_data = "{:0,}".format(float(price_data))
    update.message.reply_text(f'Harga {coin_name} adalah Rp {price_data}')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def user(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Halo semuanyaa')

updater = Updater('5246435600:AAF3ZtVxf66u9rO_uRmzODkTnieu_odVl_U')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('price', price_tracker))
updater.dispatcher.add_handler(CommandHandler('user', user))

updater.start_polling()
updater.idle()