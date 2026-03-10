# my-flashdeal-star/main/star_security_core.py

import datetime
import json

class FlashDealStar:
    def __init__(self):
        # إعدادات المنتج
        self.product = {
            "title": "My FlashDeal Star",
            "image": "./assets/headphones_small.png",
            "price": "99.99 €",
            "rating": 4.5,  # تقييم النجوم
        }

        # إعدادات الترجمة (عربي/فرنسي/إنجليزي)
        self.translations = {
            "en": {
                "title": "My FlashDeal Star",
                "price": "Price",
                "countdown": "Countdown",
                "date": "Date",
                "deal_done": "Deal Completed! 🎉✨",
            },
            "ar": {
                "title": "ماي فلاش ديل ستار",
                "price": "السعر",
                "countdown": "المؤقت",
                "date": "التاريخ",
                "deal_done": "تمت الصفقة! 🎈⭐",
            },
            "fr": {
                "title": "Mon FlashDeal Star",
                "price": "Prix",
                "countdown": "Compte à rebours",
                "date": "Date",
                "deal_done": "Transaction terminée ! 🎈⭐",
            },
        }

        # اللغة الافتراضية
        self.language = "en"

        # مؤقت الصفقة (ساعة واحدة)
        self.time_left = 3600

    def change_language(self, lang):
        if lang in self.translations:
            self.language = lang

    def get_translation(self, key):
        return self.translations[self.language].get(key, key)

    def format_time(self):
        m, s = divmod(self.time_left, 60)
        return f"{m}:{s:02d}"

    def tick(self):
        if self.time_left > 0:
            self.time_left -= 1

    def get_date(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")

    def get_rating_stars(self):
        full_stars = int(self.product["rating"])
        half_star = 1 if self.product["rating"] % 1 >= 0.5 else 0
        empty_stars = 5 - full_stars - half_star
        return "⭐" * full_stars + ("☆" if half_star else "") + "☆" * empty_stars

    def complete_deal(self):
        # عند إتمام الصفقة: بالونات + نجوم ذهبية
        return self.get_translation("deal_done")

    def render(self):
        # إخراج منسق للعرض (يمكن ربطه بواجهة React Native أو Web)
        return {
            "title": self.get_translation("title"),
            "image": self.product["image"],
            "price": f"{self.get_translation('price')}: {self.product['price']}",
            "countdown": f"{self.get_translation('countdown')}: {self.format_time()}",
            "date": f"{self.get_translation('date')}: {self.get_date()}",
            "rating": self.get_rating_stars(),
        }


# مثال تشغيل
if __name__ == "__main__":
    app = FlashDealStar()
    app.change_language("ar")  # تغيير اللغة إلى العربية
    print(json.dumps(app.render(), ensure_ascii=False, indent=2))
    print(app.complete_deal())
