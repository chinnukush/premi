from bot import Bot
import pyrogram.utils
from plugins.verify_server import app
import threading

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

def run_web():
    app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    
    # Start Flask server
    threading.Thread(target=run_web).start()

    # Start Telegram bot
    Bot().run()





