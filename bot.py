import os
import requests
import time

# الإعدادات من منصة Render
TOKEN = os.getenv("TELEGRAM_TOKEN")
# سنرسل التنبيه للقناة ولحسابك الشخصي
CHAT_IDS = ["1106252748", "-1003760053148"] 

def send_telegram_msg(text):
    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Error sending message: {e}")

def check_visa_slots():
    # هذا الرابط كمثال لموقع المواعيد
    target_url = "https://gatewayinternational.com.tr/" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=20)
        
        # منطق الفحص: إذا وجدنا كلمة تدل على توفر المواعيد
        # سنفترض هنا أننا نبحث عن "Available" أو اختفاء "No Slots"
        if response.status_code == 200:
            # تنبيه بسيط للتشغيل لأول مرة
            print("Site is reachable...")
            # هنا يمكنك إضافة فحص دقيق لمحتوى الصفحة (Scraping)
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    # عند تشغيل الكود بواسطة Cron Job سيقوم بالفحص مرة واحدة ويرسل تقرير
    check_visa_slots()
    send_telegram_msg("🔄 **نظام المراقبة يعمل:** تم فحص موقع مواعيد تركيا الآن.")