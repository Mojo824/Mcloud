import boto3

s3 = boto3.client("s3")

s3_usage_options = [
    "Free Tier Storage [5 GB, basic use, no public access]",
    "Standard Storage [General Use, Versioning Enabled]",
    "Backup Bucket [Infrequent Access, Lifecycle Rules]",
    "Static Website Hosting [Public, Index/404 Pages]",
    "Logging Bucket [Used to store access logs from other buckets]"
]

acl_options = [
    "private [ Recommended: safest for personal/internal use]",
    "public-read [ Anyone can read — for static websites]",
    "authenticated-read [ AWS users only]",
    "log-delivery-write [ For logging buckets]",
]

print(" Choose S3 bucket type to deploy:")
for i, opt in enumerate(s3_usage_options, 1):
    print(f"{i}. {opt}")

bucket_type = s3_usage_options[int(input("\n Your choice: ")) - 1]

# Bucket name and region
bucket_name = input(" Enter a unique bucket name: ").strip()
region = input(" Region (default: us-east-1): ").strip() or "us-east-1"

# Choose ACL
print("\n Choose ACL (Access Control):")
for i, acl in enumerate(acl_options, 1):
    print(f"{i}. {acl}")
acl_choice = acl_options[int(input("\n ACL choice: ")) - 1].split()[0]  # just "private", etc.

# versioning
enable_versioning = input(" Enable versioning? (y/n): ").strip().lower() == "y"

# Ask for static site setup if selected
static_site = "Static Website" in bucket_type
if static_site:
    print(" You selected static site — will enable website hosting & public read access.")

# Create the bucket
def create_bucket(name, region, acl):
    try:
        if region == "us-east-1":
            s3.create_bucket(Bucket=name, ACL=acl)
        else:
            s3.create_bucket(
                Bucket=name,
                ACL=acl,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f" Bucket '{name}' created in region {region} with ACL '{acl}'")
        return True
    except Exception as e:
        print(f"❌ Bucket creation failed: {e}")
        return False

def configure_bucket(name):
    if enable_versioning:
        try:
            s3.put_bucket_versioning(
                Bucket=name,
                VersioningConfiguration={'Status': 'Enabled'}
            )
            print(" Versioning enabled.")
        except Exception as e:
            print(f" Versioning error: {e}")

    if static_site:
        try:
            s3.put_bucket_website(
                Bucket=name,
                WebsiteConfiguration={
                    'IndexDocument': {'Suffix': 'index.html'},
                    'ErrorDocument': {'Key': 'error.html'}
                }
            )
            print(" Static website hosting enabled.")
        except Exception as e:
            print(f" Website config error: {e}")
def set_public_access(bucket_name):
    print("\n Public Access Settings:")
    print("1. Keep Fully Private (Recommended)")
    print("2. Allow Public ACLs (for static hosting)")
    print("3. Remove All Blocks (fully public - risky)")

    choice = input("Your choice: ").strip()

    if choice == "1":
        config = {
            "BlockPublicAcls": True,
            "IgnorePublicAcls": True,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": True
        }
    elif choice == "2":
        config = {
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": True,
            "RestrictPublicBuckets": False
        }
    elif choice == "3":
        config = {
            "BlockPublicAcls": False,
            "IgnorePublicAcls": False,
            "BlockPublicPolicy": False,
            "RestrictPublicBuckets": False
        }
    else:
        print("❌ Invalid choice, keeping defaults.")
        return

    try:
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration=config
        )
        print("Public access configuration applied.")
    except Exception as e:
        print(f"Failed to set public access: {e}")

# Run
if create_bucket(bucket_name, region, acl_choice):
    set_public_access(bucket_name)
    configure_bucket(bucket_name)
