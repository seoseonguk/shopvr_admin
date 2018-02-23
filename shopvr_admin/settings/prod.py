from .common import *

DEBUG = False
ALLOWED_HOSTS = ["*"]


import os
import pymysql
pymysql.install_as_MySQLdb()



DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'HOST': os.environ['DB_HOST'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'NAME': os.environ['DB_NAME'],
        'PORT': os.environ['DB_PORT'],
    }
}

INSTALLED_APPS += ['storages']
STATICFILES_STORAGE = 'shopvr_admin.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'shopvr_admin.storages.MediaS3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME'] # 필수 지정
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', 'ap-northeast-2')


