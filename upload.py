import boto3

# Create S3 client
s3 = boto3.client("s3")

# Your local CSV file path
local_file = r"C:\Users\user\Downloads\Flexi Cap Shortlist.xlsx"

# Your S3 bucket name
bucket_name = "demo-pradyumna-s3-bucket"

# File name in S3
s3_file_name = "data.csv"

# Upload
s3.upload_file(local_file, bucket_name, s3_file_name)

print("File uploaded successfully!")