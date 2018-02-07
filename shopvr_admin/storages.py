from shopvr_admin.storages import S3Boto3Storage

class StaticS3Boto3Storage(S3Boto3Storage):
    location = 'static'

class MediaS3Boto3Storage(S3Boto3Storage):
    location = 'media'
