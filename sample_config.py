import os

class Config(object):

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "niii21")

    APP_ID = int(os.environ.get("APP_ID", "16612056"))
    
    API_HASH = os.environ.get("API_HASH", "ae32caf162207865ff93b9b931b2ba54")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 3600
    
    TG_MAX_FILE_SIZE = 2097152000

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://king:139715202Aa@cluster0.4lzzm.mongodb.net/?retryWrites=true&w=majority")

    UPDATE_GROUP = os.environ.get("UPDATE_GROUP", "yop18741564")
    
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "yop18741564")

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    # For private use 
    PRIVATE = bool(os.environ.get("PRIVATE", False))

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", None).split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Generate screenshots for file after uploading
    # Defaults to True
    SCREENSHOTS = os.environ.get("SCREENSHOTS", "False")

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", None)

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    
