# 💬 Telegram Notification Setup for LinkedIn Scraper

Send instant push notifications to your phone every time your LinkedIn scraper runs — using the free and secure **Telegram Bot API**. No email, no SMS, no credit card required.

---

## ✅ Step 1: Create Your Telegram Bot
1. Open Telegram
2. Search for **`@BotFather`** and start a chat
3. Send the command: `/newbot`
4. Follow the prompts:
   - Choose a name
   - Choose a unique username (must end in `bot`)
5. You will receive a **Bot Token** — copy and save it

---

## ✅ Step 2: Get Your Chat ID
1. Start a chat with your new bot (send it any message)
2. Visit this URL in your browser (replace `YOUR_BOT_TOKEN`):
```
https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```
3. Look for your `chat_id` in the response (you’ll see it under `message.chat.id`)

---

## ✅ Step 3: Add Telegram Notification to Your Script

### 🔧 Python Code:
```python
import requests

def send_telegram(text):
    token = 'YOUR_BOT_TOKEN'
    chat_id = 'YOUR_CHAT_ID'
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

# Example usage:
send_telegram("✅ LinkedIn scraper completed successfully!")
```

---

## ✅ Add to Your Scraper
Call the `send_telegram()` function at the end of your `scraper.py` to receive a push notification every time it runs.

---

## 📌 Security Tip
- You don’t need to share your phone number with anyone
- You can store the bot token and chat ID in environment variables or GitHub Secrets for safety

---

## ✨ Bonus Tip
Use emoji in the message to make it pop:
```python
send_telegram("✅ Scraper done! 📊 Your CSV is ready.")
```

Let me know if you'd like to send a full report, CSV summary, or use Telegram for error notifications as well!
