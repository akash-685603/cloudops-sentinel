"""s3_backup.py

Small helper to upload a file to S3 using boto3.
"""
import os, logging
_logger = logging.getLogger(__name__)

def upload_file(local_path: str, bucket: str = None, key: str | None = None):
    try:
        import boto3
    except Exception:
        raise RuntimeError('boto3 not installed; install requirements.txt')

    bucket = bucket or os.getenv('S3_BUCKET')
    if not bucket:
        raise ValueError('S3 bucket not specified via argument or S3_BUCKET env')
    key = key or os.path.basename(local_path)
    s3 = boto3.client('s3', region_name=os.getenv('AWS_REGION'))
    _logger.info('Uploading %s to s3://%s/%s', local_path, bucket, key)
    s3.upload_file(local_path, bucket, key)
    _logger.info('Upload complete')