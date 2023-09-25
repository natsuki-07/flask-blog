import os

class Config(object):
  DYNAMODB_REGION = 'ap-northeast-1'
  SESSION_TYPE='dynamodb'
  SESSION_DYNAMODB_TABLE = 'serverless_blog_sessions'
  SESSION_DYNAMODB_REGION = DYNAMODB_REGION
  USERNAME = 'john'


class DevelopmentConfig(object):
  DEBUG = True
  AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
  AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
  DYNAMODB_ENDPOINT_URL = 'http://localhost:8000'
  SECRET_KEY = 'secret key'
  PASSWORD = 'due123'
  SESSION_DYNAMODB_KEY_ID = AWS_ACCESS_KEY_ID
  SESSION_DYNAMODB_SECRET = AWS_SECRET_ACCESS_KEY
  SESSION_DYNAMODB_ENDPOINT_URL = DYNAMODB_ENDPOINT_URL

class ProductionConfig(object):
  DEBUG = False
  AWS_ACCESS_KEY_ID = os.environ.get('SERVERLESS_AWS_ACCESS_KEY_ID')
  AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
  DYNAMODB_ENDPOINT_URL = Nine
  SECRET_KEY = os.environ.get('SERVERLESS_SECRET_KEY')
  PASSWORD = os.environ.get('SERVERLESS_USER_PW')
  SESSION_DYNAMODB_KEY_ID = AWS_ACCESS_KEY_ID
  SESSION_DYNAMODB_SECRET = AWS_SECRET_ACCESS_KEY
  SESSION_DYNAMODB_ENDPOINT_URL = DYNAMODB_ENDPOINT_URL