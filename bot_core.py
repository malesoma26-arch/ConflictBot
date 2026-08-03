import time
import random

class AutonomousBotCore:
    def __init__(self, check_interval_minutes=3):
        self.interval = check_interval_minutes * 60  # گۆڕینی بۆ چرکە
        self.is_running = False

    def check_and_balance_army(self):
        """
        پشکنینی خولەیی بۆ دۆزینەوەی کەلێنی سوپا (پیادە، ئاسمان، دەریا)
        """
        print("\n[Bot Core]: 🔄 پشکنینی خولەیی سوپا دەستی پێ کرد...")
        
        units_status = {
            "Ground_Infantry": random.choice(["Normal", "Low", "Critical"]),
            "Air_Forces": random.choice(["Active", "Needs_Repair"]),
            "Naval_Forces": random.choice(["Patrolling", "Under_Risk"])
        }
        
        print(f"[Bot Core]: 📊 ئەنجامی پشکنین: {units_status}")
        
        for unit, status in units_status.items():
            if status in ["Low", "Critical", "Needs_Repair", "Under_Risk"]:
                print(f"[Bot Core]: ⚠️ کەلێن دۆزرایەوە لە ({unit}). فەرمانی دروستکردن و پڕکردنەوەی جێبەجێ کرا!")
            else:
                print(f"[Bot Core]: ✅ یەکەی ({unit}) لە دۆخێکی جێگیردایە.")

    def handle_defense_and_counter_attack(self):
        """
        بەرگریی چڕ و هێرشی پێچەوانەی خۆکار لە کاتی ئۆفڵایندا ئەگەر هێرش کرابێت
        """
        under_attack = random.choice([True, False])
        
        if under_attack:
            print("[Bot Core]: 🚨 ئاگاداری! هێرش لە لایەن دوژمنەوە کراوە سەر هێزەکانمان!")
            print("[Bot Core]: 🛡️ فەرمانی بەرگریی پۆڵایین جێبەجێ کرا...")
            print("[Bot Core]: ⚔️ سوپای دوژمن تێکشکێنرا! دەستبەجێ فەرمانی (هێرشی پێچەوانە - Counter-Attack) دەست پێ کرد!")
        else:
            print("[Bot Core]: 🌐 ناوچەکە ئارامە؛ پاتڕۆڵی ئاسمانی و دەریایی بەردەوامە.")

    def start_24_7_loop(self):
        """
        بەگەڕخستنی بۆتەکە بە شێوەی 24 کاتژمێری لە پاشبنەما (Background)
        """
        self.is_running = True
        print(f"🚀 بۆتە خۆکارەکە بە سەرکەوتوویی کەوتە کار! ماوەی پشکنین: هەر {self.interval // 60} خولەک جارێک.")
        
        try:
            while self.is_running:
                self.check_and_balance_army()
                self.handle_defense_and_counter_attack()
                
                print("تم فەرمانەکانی ئەم خولە تەواو بوون. چاوەڕێی خولی داهاتوو...")
                print("-" * 50)
                
                time.sleep(self.interval)
                
        except KeyboardInterrupt:
            self.is_running = False
            print("\n🛑 بۆتەکە ڕاگیرا.")

if __name__ == "__main__":
    bot = AutonomousBotCore(check_interval_minutes=1)
    bot.start_24_7_loop()