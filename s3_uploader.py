# s3_uploader.py
import os
import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError
class S3Uploader:
    def __init__(self, bucket_name: str, region: str | None = None):
        if not bucket_name:
            raise ValueError('S3_BUCKET_NAME required')
        self.bucket = bucket_name
        session = boto3.session.Session()
        self.s3 = session.client('s3', region_name=region or os.getenv('AWS_REGION'))
    def upload_json(self, payload: dict, key: str) -> bool:
        body = json.dumps(payload, default=str)
        try:
            self.s3.put_object(Bucket=self.bucket, Key=key, Body=body, ContentType='application/json')
            return True
        except (BotoCoreError, ClientError) as e:
            print(f"S3 upload failed: {e}")
            return False
 