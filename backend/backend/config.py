import os 
from backend import TEST

class Config:
    # to handle testing scenarios
    if TEST:
        # generated using 
        # >>> import secrets 
        # 16 bytes key
        # >>> secrets.token_hex(16) 
        # app.config['SECRET_KEY'] = "61f00b99579bcd4c16850a8e46177c3b"
        SECRET_KEY              = "61f00b99579bcd4c16850a8e46177c3b"
    else:
        SECRET_KEY              = os.environ.get("SECRET_KEY")
    
    if TEST:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    else:
        SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    # MAIL_SERVER             = "smtp.googlemail.com"
    # MAIL_PORT               = 587
    # MAIL_USE_TLS            = True
    # # set these environment variables beforehand
    # MAIL_USERNAME           = os.environ.get("EMAIL_USER")
    # MAIL_PASSWORD           = os.environ.get("EMAIL_PASS")