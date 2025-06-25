import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 请将 'YOUR_TELEGRAM_BOT_TOKEN' 替换为你的实际 Bot Token
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

WELCOME_MESSAGE = (
    "🇰🇭柬埔寨游艇Cambodia Yacht Rental\n\n"
    "业务咨询✈️ : @Boatbabes\n"
    "Business Inquiry: @Boatbabes\n\n"
    "🚤 柬埔寨游艇服务\n"
    "Cambodia Yacht Services\n\n"
    "🎉 海上派对\n"
    "Sea Parties\n\n"
    "💃 游艇宝贝气氛组\n"
    "Yacht Babes Team\n\n"
    "✨ 护照签证、劳工证、驾照、VIP接机\n"
    "Passport/Visa, Work Permit, Driver’s License, VIP Airport Pickup\n\n"
    "🏝 高龙岛、撒冷岛、情人岛、天堂岛、当岛酒店预定\n"
    "Hotel Booking: Koh Rong, Koh Rong Samloem, Lover’s Island, Paradise Island, Dang Island\n"
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("请点击 /start 获取服务介绍。For service info, please use /start.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 可以自定义自动回复逻辑，这里简单回复欢迎信息
    await update.message.reply_text(WELCOME_MESSAGE)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))

    print("KHYachtBot is running...")
    app.run_polling()
