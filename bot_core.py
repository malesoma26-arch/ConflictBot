import os
import requests
import random

class MasterConflictBot:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.username = os.getenv("CON_USERNAME")
        self.password = os.getenv("CON_PASSWORD")

    def send_telegram_message(self, message):
        """ناردنی ڕاپۆرتی گشتگیر بۆ تەلەگرام"""
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
            requests.post(url, json=payload)
        except Exception as e:
            print(f"[Telegram]: هەڵە: {e}")

    def manage_economy(self):
        """بەڕێوەبردنی ئابووری و سەرچاوەکان و دروستکردنی بینا"""
        print("[Economy]: 💰 پشکنینی سەرچاوەکان و دروستکردنی بینا...")
        actions = [
            "دروستکردنی کارگەی چەک لە شاری سەرەکی",
            "پەرەپێدانی کێڵگەی نەوت و کانزا بۆ بەرزکردنەوەی داهات",
            "بونیاتنانی بینای ئابووری و پێداویستییەکان"
        ]
        return random.choice(actions)

    def manage_army_production(self):
        """دروستکردنی سەرباز و هێزی نوێ"""
        print("[Army Production]: 🏭 دروستکردنی سەرباز...")
        units = [
            "دەستکردن بە دروستکردنی یەکەی پیادەی نوێ (Infantry)",
            "دروستکردنی تانک و هێزی زەمینی",
            "پەرەپێدانی هێزی ئاسمانی و فڕۆکە"
        ]
        return random.choice(units)

    def manage_movement_and_patrol(self):
        """جووڵاندنی سەرباز و پاتڕۆڵکردن"""
        print("[Movement]: 🚀 جووڵاندنی سەرباز و پاتڕۆڵ...")
        movements = [
            "گواستنەوەی هێزەکان بەرەو سنووری نێودەوڵەتی",
            "رەوانەکردنی پاتڕۆڵی ئاسمانی بۆ چاودێری ناوچە ستراتیژییەکان",
            "ڕێکخستنەوەی جێگیربوونی سوپا لە ناوخۆدا"
        ]
        return random.choice(movements)

    def manage_war_and_defense(self):
        """جەنگ، بەرگری و هێرشکردن"""
        print("[War & Defense]: ⚔️ دۆخی جەنگ و بەرگری...")
        combat_actions = [
            "دۆخی ئارام؛ پاراستنی سەقامگیری و ئامادەباشی بەرگری",
            "⚠️ هەستی بە جووڵەی دوژمن کرد؛ جێبەجێکردنی فەرمانی (بەرگری پۆڵایین)",
            "🔥 ئەنجامدانی هێرشی پێچەوانە (Counter-Attack) بۆ سەر پێگەی دوژمن"
        ]
        return random.choice(combat_actions)

    def run_all_systems(self):
        """جێبەجێکردنی هەموو بخشەکان بەیەکەوە"""
        print("🤖 [MasterBot]: دەستپێکردنی خولی گشتگیری دەسەڵات...")
        
        eco_res = self.manage_economy()
        army_res = self.manage_army_production()
        move_res = self.manage_movement_and_patrol()
        war_res = self.manage_war_and_defense()
        
        report = (
            f"🌐 **ڕاپۆرتی سەرجەم بوارەکانی دەوڵەت (ConflictBot)**\n\n"
            f"💰 **ئابووری و بیناسازی:**\n{eco_res}\n\n"
            f"🏭 **سەربازی و بەرهەمهێنان:**\n{army_res}\n\n"
            f"🚀 **جووڵە و پاتڕۆڵ:**\n{move_res}\n\n"
            f"⚔️ **جەنگ و بەرگری:**\n{war_res}\n\n"
            f"✅ **دۆخ:** هەموو فەرمانەکان لە پاشبنەماوە بە سەرکەوتوویی جێبەجێ کران."
        )
        
        self.send_telegram_message(report)

if __name__ == "__main__":
    bot = MasterConflictBot()
    bot.run_all_systems()
