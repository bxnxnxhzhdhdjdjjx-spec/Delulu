<div align="center">

# 🎵 DYNAMIC MULTI-TENANT TELEGRAM MUSIC BOT
### 🚀 100% Dynamic Link & Media Configurable via Environment Variables (`.env`)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pyrogram](https://img.shields.io/badge/Pyrogram-v2.0-orange.svg)](https://docs.pyrogram.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An advanced, high-performance Telegram Music & Management Bot built on **Pyrogram** and **Py-Tgcalls**. Engineered specifically for **Bot Hosting Platforms**, **SaaS Web Panels**, and **Custom Bot Deployment Websites**. Every single link, channel, owner handle, image, and API endpoint in this codebase is dynamically loaded from Environment Variables.

---

</div>

## 📌 WHY THIS CODEBASE IS BEST FOR BOT-MAKING WEBSITES / PANELS

Hindi / Hinglish Summary:
> **इस कोडबेस को ऐसा बनाया गया है कि यदि आप एक वेबसाइट या बॉट मेकर पैनल चलाते हैं, तो आपके यूजर सिर्फ फॉर्म में अपना लिंक्स (Telegram Channel, Support Chat, Images, Owner Name, etc.) डालेंगे और पर्यावरण वेरिएबल्स (Environment Variables) के ज़रिए बॉट का हर एक लिंक (Start image, Help menu links, Repo button, Must Join channel, Owner button) अपने आप यूजर के दिए गए लिंक से बदल जाएगा! कोड में कहीं भी कोई भी लिंक हार्डकोड (Hardcode) नहीं है।**

---

## 🌟 KEY FEATURES

- 🔄 **100% Dynamic Link Replacement**: Change Support Chat, Updates Channel, Repo Link, Owner Profile, and Must-Join Channels dynamically via ENV variables.
- 🖼️ **Dynamic Image & Media Support**: Configure Start Images, Ping Videos, Playlist Thumbnails, Log Banners, and Must-Join Photos using direct URLs in `.env`.
- ⚡ **Multi-Image Randomization**: Supply comma-separated image URLs (e.g. `START_IMG_URL=url1,url2,url3`) to enable random thumbnail cycling!
- 🌐 **Web Panel & SaaS Ready**: Built-in support for Docker, Heroku `app.json`, Pterodactyl Panel, and custom Node.js/Python web deployment backends.
- 🎶 **Multi-Platform Music Playback**: High-quality audio and video streaming from YouTube, JioSaavn, Resso, SoundCloud, and Spotify.
- 🛠️ **Group Management & Tools**: Built-in admin controls, auth users, broadcast, speed test, ChatGPT AI, couples, and fun modules.

---

## ⚙️ COMPLETE ENVIRONMENT VARIABLES REFERENCE

Below is the exhaustive list of environment variables supported by the bot. Any website or deployment panel can generate a `.env` file or inject process environment variables using these keys.

### 🔑 1. Required Telegram Credentials
| Environment Variable | Required | Description | Example / Default |
| :--- | :---: | :--- | :--- |
| `API_ID` | **Yes** | Telegram API ID from [my.telegram.org](https://my.telegram.org) | `12345678` |
| `API_HASH` | **Yes** | Telegram API Hash from [my.telegram.org](https://my.telegram.org) | `a1b2c3d4e5f6...` |
| `BOT_TOKEN` | **Yes** | Telegram Bot Token from [@BotFather](https://t.me/BotFather) | `123456:ABC-DEF...` |
| `OWNER_ID` | **Yes** | Telegram User ID of the Bot Owner | `7915069238` |
| `LOGGER_ID` | **Yes** | Telegram Group ID for Bot Logs & Alerts | `-1001234567890` |
| `MONGO_DB_URI` | **Yes** | MongoDB Connection String from [MongoDB Cloud](https://cloud.mongodb.com) | `mongodb+srv://...` |
| `STRING_SESSION` | **Yes** | Pyrogram v2 Userbot String Session | `BQB123...` |

---

### 🏷️ 2. Bot Branding & Owner Details
| Environment Variable | Required | Description | Default Value |
| :--- | :---: | :--- | :--- |
| `BOT_NAME` | No | Custom display name of the music bot | `sejal 𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕` |
| `BOT_USERNAME` | No | Telegram Username of the Bot (without `@`) | `MAHI_MUSICSBOT` |
| `OWNER_USERNAME` | No | Telegram Username of the Bot Owner (without `@`) | `II_ALONE_BOY_Il` |
| `ASSUSERNAME` | No | Telegram Username of the Assistant Account | `II_ALONE_BOY_Il` |

---

### 🔗 3. Custom Links & Channels
| Environment Variable | Required | Description | Default Value |
| :--- | :---: | :--- | :--- |
| `SUPPORT_CHANNEL` | No | Updates / Network Channel Link | `https://t.me/II_SHAYRI_KI_DUNIYA_II` |
| `SUPPORT_CHAT` | No | Support Group / Chat Link | `https://t.me/+8u7DHj1SZi9mYjll` |
| `MUST_JOIN` | No | Force Join Channel Username or Invite Link | `kriti_bot_update` |
| `UPSTREAM_REPO` | No | Source Code Repository URL | `https://github.com/spicycodez/DeluluMusic` |
| `PRIVACY_LINK` | No | Privacy Policy URL | `""` |

---

### 🖼️ 4. Dynamic Media & Image URLs
*Note: You can pass a single URL or multiple comma-separated URLs for random cycling.*

| Environment Variable | Required | Description | Default Value |
| :--- | :---: | :--- | :--- |
| `START_IMG_URL` | No | Banner image(s) for `/start` command | `https://litter.catbox.moe/xr9jf82b2umeke7j.jpg` |
| `PING_IMG_URL` | No | Video/Image URL for `/ping` command | `https://litter.catbox.moe/xyedznhk80hmial2.mp4` |
| `MUST_JOIN_IMG` | No | Image banner for Force Join prompt | `https://files.catbox.moe/fu6jk3.jpg` |
| `LOG_IMG_URL` | No | Notification photo for log group | `https://files.catbox.moe/tdj8he.jpg` |
| `REPO_IMG_URL` | No | Banner photo for `/repo` command | `https://litter.catbox.moe/xr9jf82b2umeke7j.jpg` |
| `PLAYLIST_IMG_URL` | No | Thumbnail for Playlist command | `https://graph.org/...` |
| `STATS_IMG_URL` | No | Thumbnail for Stats command | `https://graph.org/...` |
| `STREAM_IMG_URL` | No | Default stream thumbnail | `https://graph.org/...` |
| `SOUNCLOUD_IMG_URL` | No | SoundCloud track thumbnail | `https://graph.org/...` |
| `YOUTUBE_IMG_URL` | No | YouTube fallback thumbnail | `https://graph.org/...` |
| `SPOTIFY_PLAYLIST_IMG_URL` | No | Spotify playlist thumbnail | `https://graph.org/...` |

---

### 🌐 5. API Endpoints
| Environment Variable | Description | Default Value |
| :--- | :--- | :--- |
| `SAAVN_API_URL` | JioSaavn song search API | `https://jiosaavn-a.kvinit6421.workers.dev/api/search/songs` |
| `JIOSAAVN_API_URL` | Secondary JioSaavn search endpoint | `https://jiosaavn-a.kvinit6421.workers.dev/api/search/songs` |
| `API_URL` | Pytdbot API Endpoint | `https://pytdbotapi.thequickearn.xyz` |
| `VIDEO_API_URL` | Video search API Endpoint | `https://api.video.thequickearn.xyz` |
| `SHRUTI_API_URL` | Shruti Bots API Endpoint | `https://api.shrutibots.site` |

---

## 🌐 WEBSITE & BOT MAKER PANEL INTEGRATION GUIDE

If you are building a **Bot Deployment Website**, **Telegram Bot Creation Service**, or **SaaS Web Panel**:

### 1. Web Form Inputs for Users
Create a web form where users enter their bot details:
- Bot Token (`BOT_TOKEN`)
- Owner Username (`OWNER_USERNAME`)
- Support Group Link (`SUPPORT_CHAT`)
- Channel Link (`SUPPORT_CHANNEL`)
- Force Join Channel Username (`MUST_JOIN`)
- Start Photo URL (`START_IMG_URL`)

### 2. Backend Deployment Workflow
When a user submits the form on your website:
1. Generate a custom `.env` file for the user's container or process.
2. Spawn a Docker container, VPS process, or Heroku dyno passing these environment variables.
3. The bot automatically starts using the user's custom links, channel buttons, start images, and owner profile without modifying a single line of code!

### 3. Heroku One-Click Deploy Button Integration
You can integrate Heroku deploy button on your website using:
```html
<a href="https://dashboard.heroku.com/new?template=YOUR_GITHUB_REPO_URL">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku">
</a>
```
All fields defined in `app.json` will automatically appear in Heroku's web form!

---

## 💻 LOCAL / VPS DEPLOYMENT GUIDE

### 1. Clone Repo & Install Requirements
```bash
git clone https://github.com/spicycodez/DeluluMusic
cd DeluluMusic
pip install -r requirements.txt
```

### 2. Create `.env` File
Copy `sample.env` to `.env` and fill in your details:
```bash
cp sample.env .env
nano .env
```

### 3. Start the Bot
```bash
python3 -m SONALI_MUSIC
```

---

## 🐳 DOCKER DEPLOYMENT GUIDE

```bash
# Build the docker image
docker build -t musicbot .

# Run container with environment variables
docker run -d --name musicbot \
  --env-file .env \
  musicbot
```

---

## 🤝 CREDITS & CONTRIBUTIONS

- **Pyrogram** by [Dan](https://github.com/pyrogram/pyrogram)
- **Py-Tgcalls** by [Telegram-Music](https://github.com/pytgcalls/pytgcalls)
- Developed & Maintained with ❤️ for the Telegram Bot Community.

---
