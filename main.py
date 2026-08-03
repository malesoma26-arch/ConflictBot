from telegram_bot import send_telegram_message

def main():
    print("🤖 بۆتی چاودێری Conflict of Nations دەستی بە کار کرد...")

    report_message = (
        "🚨 *ڕاپۆرتی نوێی بۆتی Conflict of Nations*\n\n"
        "🟢 دۆخی ناوچەکە: ئارامە و سەقامگیرە.\n"
        "🏗️ شارەکان ئامادەن بۆ پەرەپێدان.\n"
        "⚔️ هێزەکان لە پاتڕۆڵدان."
    )

    send_telegram_message(report_message)

if __name__ == "__main__":
    main()