from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Token del bot de Telegram
BOT_TOKEN = "7830359662:AAFk9JW7-Ky5IbtPttfhOE4_wf-ZZ81gzJ8"

# Función para mostrar el menú principal
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("1️⃣ ¿Qué es una CCS?", callback_data="opcion1")],
        [InlineKeyboardButton("2️⃣ ¿Qué es una tarjeta blanca?", callback_data="opcion2")],
        [InlineKeyboardButton("3️⃣ Recomendaciones para la CCS", callback_data="opcion3")],
        [InlineKeyboardButton("4️⃣ Recomendaciones para la Tarjeta blanca", callback_data="opcion4")],
        [InlineKeyboardButton("5️⃣ ¿A qué nos dedicamos?", callback_data="opcion5")],
        [InlineKeyboardButton("6️⃣ Nuestras garantías", callback_data="opcion6")],
        [InlineKeyboardButton("7️⃣ Métodos de pago", callback_data="opcion7")],
        [InlineKeyboardButton("8️⃣ Realizar un pedido", callback_data="opcion8")],
        [InlineKeyboardButton("9️⃣ Canales de difusión", callback_data="opcion9")],
        [InlineKeyboardButton("🔟 Referencias", callback_data="opcion10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selecciona una opción:", reply_markup=reply_markup)

# Función para manejar las opciones del menú
async def handle_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    respuestas = {
        "opcion1": "1️⃣ Son tarjetas de crédito con saldo para comprar en tiendas en línea...",
        "opcion2": "2️⃣ Para los que no saben que son las tarjetas blancas...",
        "opcion3": "3️⃣ Siempre es recomendable el uso correcto en cualquier plataforma...",
        "opcion4": "4️⃣ Las tarjetas blancas son utilizadas para sacar únicamente efectivo...",
        "opcion5": "5️⃣ Yo me dedico al carding, que consiste en la utilización de tarjetas...",
        "opcion6": "6️⃣ 🚨 GARANTÍAS AL INVERTIR CONMIGO 🚨✅ Experiencia y profesionalismo...",
        "opcion7": "7️⃣ Nosotros solo aceptamos pago por depósito y transferencia...",
        "opcion8": "8️⃣ Para realizar un pedido, contacta al administrador: @BLEEST_AWS",
        "opcion9": "9️⃣ Canales de difusión:\nTelegram: https://t.me/metodo_aws\nWhatsApp: https://whatsapp.com/channel/0029VatuFfp9MF8se1jl5o0v",
        "opcion10": "🔟 Puedes checar nuestras referencias en nuestro canal de Telegram: https://t.me/Referencias_m3todo_AWS"
    }

    # Responde según la opción seleccionada
    await query.edit_message_text(respuestas[query.data])

# Configurar y ejecutar el bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Comando /start para mostrar el menú
    app.add_handler(CommandHandler("start", start))

    # Manejar las opciones del menú
    app.add_handler(CallbackQueryHandler(handle_menu))

    # Ejecutar el bot
    app.run_polling()

if __name__ == "__main__":
    main()
