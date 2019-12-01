import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
   SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess'
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   MAIL_SERVER = os.environ.get('smtp.googlemail.com')
   MAIL_PORT = int(os.environ.get('587') or 25)
   MAIL_USE_TLS = os.environ.get('1') is not None
   MAIL_USERNAME = os.environ.get('sjg2001')
   MAIL_PASSWORD = os.environ.get('wes#1C@t')
   ADMINS = ['stjagu@whiskeytango.us']
   POSTS_PER_PAGE = 25