from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider, S3Bucket, S3BucketPolicy
import json

class CodeGuruBucketStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # Read the bucket configuration from a JSON file
        with open('cg_bucket_config.json', 'r') as config_file:
            bucket_config = json.load(config_file)

        # Create S3 bucket resource
        s3_bucket = S3Bucket(self, 'MyBucket',
                             bucket=bucket_config['cg-config'],
                             acl=bucket_config['acl'],
                             force_destroy=True)

        # Create S3 bucket policy
        S3BucketPolicy(self, 'MyBucketPolicy',
                       bucket=s3_bucket.bucket,
                       policy=bucket_config['policy'])

app = App()
MyS3BucketStack(app, 's3-bucket-code-guru')
app.synth()
