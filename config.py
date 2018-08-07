#default config
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\rI\x13\xdc\xb8\x0b\xc3\x1a\xa5a\xdc\x025*"H2\xdea\xf6~\x08\x02\x96'
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<username>:<password>@localhost/<database>'
	SESSION_TYPE = 'memcached'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

#Development config
class DevelopmentConfig(BaseConfig):
	DEBUG = True