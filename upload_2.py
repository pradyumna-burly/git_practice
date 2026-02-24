import boto3
from botocore.exceptions import ClientError
import os
import shutil
from pathlib import Path 

vendor_folder = Path(r"C:\Users\user\Downloads\s3_vendor_folder")
# Your S3 bucket name
bucket_name = "demo-pradyumna-s3-bucket"

# Create S3 client
s3 = boto3.client("s3")

def s3_exists(bucket,key):
    try:
        s3.head_object(Bucket=bucket,Key=key)
        return True
    except ClientError:
        return False

def upload_if_needed(src, bucket, key):
    if not s3_exists(bucket, key):
        s3.upload_file(str(src),bucket,key)
        print("Uploaded: ",key)
    else:
        print("Already exists: ",key)

def process_files():
    for root,_,files in os.walk(vendor_folder):
        for file in files:

            parts = file.split("_",3)
            dataset = parts[0]
            freq = parts[1]
            period = parts[2]

            #build S3 key
            key = f"{dataset}/{freq}/{period}/{file}"

            src_file = Path(root)/file
            upload_if_needed(src_file, bucket_name, key)

    print("\nAll files uploaded")


if __name__ == "__main__":
    process_files()