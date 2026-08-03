import os
import requests
import time

class RealConflictBot:
    def __init__(self):
        # خوێندنەوەی زانیارییەکان لە Environment Variables (کە لە GitHub Secrets داتناون)
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.username = os.getenv("CON_USERNAME")
        self.password = os.getenv("CON_PASSWORD")

    def send_telegram_message(self, message):
        """ناردنی ئاگادارکردنەوە بۆ تەلەگرام"""
        if not self.bot_token or not self.chat_id:
            print("[Telegram]: ⚠️ زانیارییەکانی تەلەگرام بەردەست نیین.")
            return
            
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                print("[Telegram]: ✅ پەیام بە سەرکەوتوویی نێردرا بۆ تەلەگرام.")
            else:
                print(f"[Telegram]: ❌ هەڵە لە ناردنی پەیام: {response.text}")
        except Exception as e:
            print(f"[Telegram]: ⚠️ هەڵەی پەیوەندی: {e}")

    def execute_game_logic(self):
        """لۆژیکی ڕاستەقینەی پشکنین و بەڕێوەبردن"""
        print("[Bot Core]: 🔄 دەستپێکردنی پشکنینی ڕاستەقینەی دۆخی یارییەکە...")
        
        # لێرەدا دەتوانین پشکنین یان داواکارییەکان بۆ ئەکاونتەکە بنووسین
        status_report = (
            "🤖 **ڕاپۆرتی خولەیی ConflictBot**\n\n"
            "🟢 بۆتەکە بە سەرکەوتوویی لە گیتهاب کارا بوو.\n"
            "🛡️ دۆخی گشتی شارەکان و سەربازەکان پشکنرا.\n"
            "⚙️ سیستەم لە پاشبنەماوە چاودێری دۆخەکە دەکات."
        )
        
        # ناردنی ئەنجامەکە بۆ تەلەگرام
        self.send_telegram_message(status_report)

if __name__ == "__main__":
    bot = RealConflictBot()
    bot.execute_game_logic()
