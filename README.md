# Anonymous Discord Bot

## 📌 Overview
This is a **Discord bot** that allows users to send anonymous messages to a designated channel while maintaining a log for moderators. Users must register with a **unique 4-digit code** before they can send anonymous messages.

## 🚀 Features
- **Anonymous Messaging**: Users can send anonymous messages to a specific channel.
- **Secure Registration**: Each user must register with a **unique 4-digit code**.
- **Logging System**: Logs all activities in a separate log channel for moderators.
- **User-friendly Commands**: Easy-to-use commands via **DMs**.

## ⚙️ Installation
### 1. Clone the Repository
```bash
git clone https://github.com/parthxd7/DarkWebBotDiscord.git
cd your-repo-name
```

### 2. Install Dependencies
```bash
pip install discord.py
```

### 3. Configure the Bot
Create a `.env` file and add your **Discord Bot Token**:
```env
TOKEN=YOUR_BOT_TOKEN
```
Or manually replace `TOKEN` in `bot.py` with your **Discord bot token**.

### 4. Run the Bot
```bash
python bot.py
```

## 📜 Usage
### Register a User
- **Step 1**: DM the bot and type:
  ```
  register
  ```
- **Step 2**: Enter a **4-digit numeric code** (must be unique).
- **Step 3**: You will receive a confirmation message.

### Send an Anonymous Message
After registration, send an anonymous message:
```bash
anon Your message here
```
Your message will be posted in the configured channel anonymously.

## 🛠 Configuration
Modify these variables in the script to set up your **log and message channels**:
```python
LOG_CHANNEL_ID = 123456789123789  # Log Channel ID
MESSAGE_CHANNEL_ID = 123456789123789  # Anonymous Message Channel ID
```

## 🛡 Security & Logging
- **Logs user activities** in the log channel for moderation.
- **Prevents duplicate registrations** using a unique 4-digit code.
- **Ensures only registered users can send anonymous messages**.

## 🔗 License
This project is licensed under the **MIT License**.

## 🤝 Contributions
Feel free to **fork**, **submit issues**, or **send pull requests**!

---
Made with ❤️ by [Your Name](https://github.com/parthxd7)

