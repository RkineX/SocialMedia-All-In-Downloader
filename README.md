# Social Media Downloader Toolkit 🎬📥

A cross-platform Python tool to download content from YouTube, Instagram, TikTok, Facebook, and Twitter (Note: Some platforms require API credentials).


## 📋 Table of Contents
- [Disclaimer](#⚠️-disclaimer)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Legal](#-legal-and-ethical-considerations)

## ⚠️ Disclaimer
**Important:** This tool is for educational purposes only. Respect all copyright laws and platform terms of service. Only download content you own or have explicit permission to download.

## 🌟 Features
| Platform  | Videos | Audio | Stories | Posts | Reels |
|-----------|--------|-------|---------|-------|-------|
| YouTube   | ✅     | ✅    | ❌      | ❌    | ❌    |
| Instagram | ✅     | ✅    | ✅      | ✅    | ✅    |
| TikTok    | ✅     | ✅    | ✅      | ✅    | ✅    |
| Facebook  | ✅     | ✅    | ✅      | ✅    | ❌    |
| Twitter   | ✅     | ✅    | ❌      | ✅    | ❌    |

## 🛠 Installation

### Prerequisites
- Python 3.6+
- FFmpeg (for audio conversion)
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# MacOS
brew install ffmpeg

# Windows (via Chocolatey)
choco install ffmpeg
```
## Setup
- Clone repository:
```bash
git clone https://github.com/yourusername/social-media-downloader.git
```
```bash
cd social-media-downloader
```
### Install dependencies:
```bash
pip install -r requirements.txt
```
### 🚀 Usage
- Run the script:
```bash
python social_downloader.py
```
## ⚙ Configuration
- Create `config.ini` for platform authentication:
```bash
[Instagram]
username = your_username
password = your_password

[Twitter]
api_key = xxxxxxxxx
api_secret = xxxxxxxxx
access_token = xxxxxxxxx
access_secret = xxxxxxxxx

[Facebook]
app_id = xxxxxxxxx
app_secret = xxxxxxxxx
page_token = xxxxxxxxx
```
## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue                      | Resolution Steps                                                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Dependency Errors**       | ```bash pip install -r requirements.txt --force-reinstall ```<br>Ensure Python 3.6+ is installed and added to PATH                              |
| **"URL Not Recognized"**    | 1. Verify URL format matches platform requirements<br>2. Check platform selection matches URL source<br>3. Test URL in browser first            |
| **Authentication Failures** | 1. Validate credentials in `config.ini`<br>2. Check API token expiration<br>3. Verify platform API status at [status pages](#platform-status)   |
| **FFmpeg Errors**           | 1. [Install FFmpeg](#ffmpeg-installation)<br>2. Add to system PATH:<br>   ```export PATH="$PATH:/path/to/ffmpeg"``` (Linux/Mac)<br>   Update system environment variables (Windows) |

### Additional Help

🛠 **Common Fixes First:**
```bash
# Clear package cache
pip cache purge

# Update all dependencies
pip install --upgrade -r requirements.txt
```

📝 **Note for Developers:**
```bash
# Enable debug mode (add to script)
import logging
logging.basicConfig(level=logging.DEBUG)
```

⚠️ **Still Having Issues?**  
Open a [GitHub Issue](https://github.com/yourusername/repo/issues) with:
1. Full error output
2. Platform version (Windows/Mac/Linux)
3. Python version (`python --version`)
4. Reproduction steps





