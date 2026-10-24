import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-production")
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024
    TEMP_FOLDER = os.getenv("TEMP_FOLDER", "tmp")
    APP_NAME = "FileSafe"
    APP_DOMAIN = os.getenv("APP_DOMAIN", "https://filesafe.eu")
    PLAUSIBLE_DOMAIN = os.getenv("PLAUSIBLE_DOMAIN", "")
    ADSENSE_CLIENT = os.getenv("ADSENSE_CLIENT", "")
    ADSENSE_SLOT = os.getenv("ADSENSE_SLOT", "")
    GOOGLE_ANALYTICS_ID = os.getenv("GOOGLE_ANALYTICS_ID", "")
