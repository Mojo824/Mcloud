import boto3
from botocore.exceptions import ClientError

def get_bucket_region(s3_client, bucket_name):
    try:
        region = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        return region or "us-east-1"
    except ClientError as e:
        return f"Error: {e.response['Error']['Message']}"

def get_bucket_acl(s3_client, bucket_name):
    try:
        acl = s3_client.get_bucket_acl(Bucket=bucket_name)
        grants = acl.get("Grants", [])
        permissions = [f"{g['Grantee'].get('Type')} - {g['Permission']}" for g in grants]
        return permissions
    except ClientError:
        return ["Private"]

def get_bucket_versioning(s3_client, bucket_name):
    try:
        status = s3_client.get_bucket_versioning(Bucket=bucket_name)
        return status.get("Status", "Disabled")
    except ClientError:
        return "Unknown"

def get_public_block_settings(s3_client, bucket_name):
    try:
        settings = s3_client.get_bucket_policy_status(Bucket=bucket_name)
        is_public = settings.get("PolicyStatus", {}).get("IsPublic", False)
        return "Public " if is_public else "Private "
    except ClientError:
        return "Private "

def list_all_buckets():
    s3 = boto3.client("s3")
    response = s3.list_buckets()
    buckets = response.get("Buckets", [])

    if not buckets:
        print("❌ No S3 buckets found in your Account .")
        return

    print(f"\n Total Buckets Found: {len(buckets)}\n" + "=" * 50)

    for b in buckets:
        name = b["Name"]
        created = b["CreationDate"]

        region = get_bucket_region(s3, name)
        acl = get_bucket_acl(s3, name)
        versioning = get_bucket_versioning(s3, name)
        public_status = get_public_block_settings(s3, name)

        print(f"Bucket Name      : {name}")
        print(f"Created On       : {created}")
        print(f"Region           : {region}")
        print(f"ACL Permissions  : {', '.join(acl)}")
        print(f"Versioning       : {versioning}")
        print(f"Public Access    : {public_status}")
        print("-" * 50)

if __name__ == "__main__":
    print ("                    +++S3 List Tool+++")
    list_all_buckets()
