from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext

# Token del bot de Telegram
BOT_TOKEN = "7830359662:AAFk9JW7-Ky5IbtPttfhOE4_wf-ZZ81gzJ8"

# Función para mostrar el menú principal
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("¿Qué es una CCS?", callback_data="opcion1")],
        [InlineKeyboardButton("¿Qué es una tarjeta blanca?", callback_data="opcion2")],
        [InlineKeyboardButton("Recomendaciones para la CCS", callback_data="opcion3")],
        [InlineKeyboardButton("Recomendaciones para la Tarjeta blanca", callback_data="opcion4")],
        [InlineKeyboardButton("¿A qué nos dedicamos?", callback_data="opcion5")],
        [InlineKeyboardButton("Nuestras garantías", callback_data="opcion6")],
        [InlineKeyboardButton("Métodos de pago", callback_data="opcion7")],
        [InlineKeyboardButton("Realizar un pedido", callback_data="opcion8")],
        [InlineKeyboardButton("Canales de difusión", callback_data="opcion9")],
        [InlineKeyboardButton("Referencias", callback_data="opcion10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Selecciona una opción:", reply_markup=reply_markup)

# Función para manejar las opciones del menú
async def handle_menu(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    respuestas = {
        "opcion1": "Son tarjetas de crédito con saldo para comprar en tiendas en línea, al adquirir una puedes sacar ganancias en productos, la preferencia de nuestros clientes se basa en artículos del hogar como: celulares, muebles, escritorios, aparatos electrónicos, componentes para computadoras, consolas de videojuegos y algunos artículos personales.",
        "opcion2": "Para los que no saben que son las tarjetas blancas de este video son las CCs o llamadas también "Tarjetas Blancas" que en realidad son tarjetas clonadas de crédito la mayoría con buenos limites de crédito. Algunos se preguntan que Por qué no nos las quedamos Es sencillo, como sabemos las tarjetas de crédito solo dejan comprar mas no sacar efectivo lo cual no es tan factible para nosotros, es un cierto desgaste comprar y revender, se puede sacar buena ganancia pero el tiempo no nos da. Por lo cual optamos por vender las tarjetas y así tener tiempo para las CCS y venderlas el negocio es redondo y veloz, nuestros clientes ya conocen esto solo es para que los nuevos estén bien informados y no tengas preguntas y dudas de que si esto es un fraude ✅",
        "opcion3": "Siempre es recomendable el uso correcto en cualquier plataforma en la que usted planee sacar sus artículos, el uso correcto es: Verificar el BIN que son los primeros 6 dígitos de la tarjeta, la fecha de expiración. Ante de cada compra se les avisa que tienen un cierto limite para que no lo sobrepasen para que no haya errores al querer usar la CSS. La CSS es de un solo uso y no se pude usar en dos pagos, es único pago y en una sola plataforma. Mejor plateado es en un solo pago. Verificando siempre que en la plataforma que usen este su dirección registrada o el punto de recogida. No se mete en asuntos legales ya que están aseguradas por sus bancos y la plataforma no se hace responsable de estas acciones mas que con rembolsos.",
        "opcion4": "Las tarjetas blancas son utilizadas para sacar únicamente efectivo en cajeros automáticos. En este caso se les indica el banco y el NIP de la tarjeta para que vallan a realizar su retiro de efectivo. Con las precauciones de se cuidadoso y cubrirte con lentes o un cubre bocas sin llamar la atención e intentar recurrir al banco en horarios no tan concurridos con la menor cantidad de personas para no llamar la atención.",
        "opcion5": "Yo me dedico al carding y preguntarán que es eso, pues el Carding es un término general para referirse a la utilización de los datos de las tarjetas de crédito robadas para beneficio personal, que puede consistir en la venta de los datos, en su utilización para comprar artículos. Hay que tener en cuenta que las CCs pueden utilizarse para hacer compras directas. Y ustedes no corren riesgo a nada, así que no se preocupen que nos les va a pasar nada. Como experiencia propia les puedo decir que en todos mis años sacando productos, nunca he tenido ningún problema, diariamente las páginas reciben miles de compras con tarjetas falsas y aún así pasa desapercibido la pregunta es, ¿por qué te buscarían a ti habiendo tanta gente que lo hace? Mi única recomendación es no abusar con las compras y nunca tendrán ningún problema. Después de lo explicado anteriormente, pues para los que se preguntan... ¿Qué hacemos? Pues les vendemos la CC a un precio muy accesible para que ustedes puedan comprar sus productos más baratos en Amazon o en cualquier otra página web con CCs Para las otras páginas web se usa el mismo método con las tarjetas.",
        "opcion6": "🚨 GARANTÍAS AL INVERTIR CONMIGO 🚨✅Experiencia y profesionalismo: Con confianza afirmo que mi gran experiencia y profesionalismo te permitirán alcanzar resultados exitosos al invertir conmigo.✅Honestidad y transparencia: 🔻Doy gran importancia a la honestidad y transparencia en cada una de nuestras referencias y trabajos. Tendrás la oportunidad de hacer el trabajo conmigo paso a paso, contribuyendo a la construcción de relaciones honestas y confiables con ustedes.✅Compromiso y responsabilidad: 🔻Mi reputación juega un papel crucial y estoy lista para escuchar todas sus preguntas. Recuerda que la decisión es completamente tuya, nosotros ni nadie tiene porque insistirte ni obligarte a comprar algo.",
        "opcion7": "Nosotros Solo aceptamos pago por deposito  y trasferencia. Si eres de otro país puedes consultarlo con el  administrador",
        "opcion8": "Para realizar un pedido con el administrador:  @BLEEST_AWS",
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
