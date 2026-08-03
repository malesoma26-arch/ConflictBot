import requests
import json

class WarAdvisor:
    def __init__(self, api_key=None):
        self.api_key = api_key or "YOUR_API_KEY"
        
    def analyze_situation(self, world_news, army_status):
        """
        ئەم فەنکشنە هەواڵەکانی جیهانی یاری و دۆخی سوپا شیکار دەکات
        و وەک فەرماندەیەک ڕاوێژت پێ دەدات.
        """
        print("[AI Advisor]: خەریکی شیکردنەوەی دۆخی جیهان و سوپاکەتم...")
        
        # لێرەدا دەتوانین لۆژیکی پەیوەندیکردن بە API یان مۆدێلی زمانەوانی دابنێین
        # بۆ نموونە لێرەدا وەڵامێکی نموونەیی دەگەڕێنینەوە:
        
        analysis = (
            f"📊 **ڕاپۆرتی هەواڵگریی ڕاوێژکار:**\n"
            f"- **دۆخی هەواڵەکان:** {world_news}\n"
            f"- **دۆخی هێزەکان:** {army_status}\n\n"
            f"💡 **پێشنیازی فەرماندە:** بەپێی ئەم زانیارییانە، دوژمن لەو ناوچەیە لاوازە و هێزی ئاسمانیی تێکشکاوە. "
            f"کاتی گونجاوە ئێستا فەرمانی هێرش ڕادەست بکەین!"
        )
        return analysis

    def chat_response(self, user_message):
        """
        بۆ وەڵامدانی خێرا لە کاتی چاتکردندا لەگەڵ بۆتەکەدا
        """
        return f"فەرماندە: پێشوازی لە فەرمانەکەت دەکەم ('{user_message}'). پلانەکە جێبەجێ دەکەم و چاودێریی بەرەکان دەکەم!"

if __name__ == "__main__":
    advisor = WarAdvisor()
    print(advisor.chat_response("یەڵا برا با دەست بە هێرش بکەین بۆ سەری!"))