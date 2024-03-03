import boto3


# Instantiate a boto3 resource for S3 and name you bucket
s3 = boto3.resource('s3')
bucket_name = 'my-bucket-rd-std'


# Check if bucket exists
# Create the bucket if it does NOT exist
all_my_buckets = [bucket_name for bucket in s3.buckets.all()]
if bucket_name not in all_my_buckets:
    print(f"'{bucket_name}' bucket does not exist. Creating now...")
    s3.create_bucket(Bucket=bucket_name)
    print(f"'{bucket_name}' bucket has been created.")
else:
    print(f"'{bucket_name}' bucket already exist. No need to create new one.")

# Create 'billing_data_meat_june_2023.csv'
csv_file = 'billing_data_meat_june_2023.csv'

# UPLOAD 'file_1' to new bucket
s3.Bucket(bucket_name).upload_file(Filename=csv_file, Key=csv_file)

# READ and print the file from the bucket
obj = s3.Object(bucket_name, csv_file)
body = obj.get()['Body'].read()
print(body)
