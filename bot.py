import telebot
import qrcode
from io import BytesIO

# Ganti dengan token bot Telegram kamu
TOKEN = "8133073041:AAE0aqwg2Jbb0XVz2nAHbcmtqNocAR_i0IU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Kirim teks atau link, saya akan buatkan barcode untukmu.")

@bot.message_handler(func=lambda message: True)
def generate_qr(message):
    text = message.text  # Ambil teks yang dikirim pengguna
    
    # Buat QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Simpan ke buffer
    img = qr.make_image(fill="black", back_color="white")
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Kirim gambar QR Code ke pengguna
    bot.send_photo(message.chat.id, img_buffer, caption="Berikut QR Code kamu!")

# Jalankan bot
print("Bot barcode berjalan...")
bot.polling()