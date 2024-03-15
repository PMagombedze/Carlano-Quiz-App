"""
flask app configuration
"""

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///items.db'
    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""
    RECAPTCHA_THEME = "dark"
    RECAPTCHA_TYPE = "image"
    RECAPTCHA_SIZE = "compact"
    RECAPTCHA_RTABINDEX = 10
