# ---------------------------------------------------
# File Name: Config.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import os

# Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Port for Web Server
PORT = int(os.environ.get("PORT", "8080"))

# Your API ID & Hash
API_ID = int(os.environ.get("API_ID", "28578880"))
API_HASH = os.environ.get("API_HASH", "5f8c87efde57e01d12c0ce98ffdf5928")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6814614245"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URL"," ")
DB_NAME = os.environ.get("DB_NAME", "SaveRestricted")

# Log Channel to Track New Users 
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003759762110"))

# Dump Channel for File Tracking (ADDED)
DUMP_CHANNEL = int(os.environ.get("DUMP_CHANNEL", "-1003759762110"))

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then False
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Keep-Alive URL
KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "")

# Start pic on /start 
START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/krxuel.jpg")

# -------------------
# VERIFICATION CONFIG
# -------------------
VERIFY = bool(os.environ.get('VERIFY', True)) # Set True to enable
VERIFY_SHORTLINK_URL = os.environ.get('VERIFY_SHORTLINK_URL', 'ShrinkMe.io') # Your Shortener Domain
VERIFY_SHORTLINK_API = os.environ.get('VERIFY_SHORTLINK_API', '') # Your Shortener API Key
VERIFY_TUTORIAL = os.environ.get('VERIFY_TUTORIAL', 'https://t.me/your_tutorial_link') # Tutorial Link


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
