
# import boto3
# import time

# ec2 = boto3.client("ec2")
# ec2_resource = boto3.resource("ec2")

# # Common OS names and their AMI mappings (region specific )
# ami_map = {
#     "ubuntu": "ami-080e1f13689e07408",   # Ubuntu Server 22.04 LTS (example)
#     "amazon-linux": "ami-0c2b8ca1dad447f8a",  # Amazon Linux 2
#     "debian": "ami-00a6eeb43b1f9f96b",    # Debian (example)
#     "centos": "ami-0d63de463e6604d0a",    # CentOS 7 (example)
#     "redhat": "ami-052c08d70def0ac62"     # RHEL 8 (example)
# }

# print("Supported OS options:")
# for os_name in ami_map:
#     print(f"- {os_name}")

# chosen_os = input("Enter the OS you want (e.g., ubuntu, amazon-linux): ").strip().lower()
# if chosen_os not in ami_map:
#     print("Unsupported OS. Exiting...")
#     exit(1)

# ami_id = ami_map[chosen_os]

# # Key Pair
# key_pairs = ec2.describe_key_pairs()["KeyPairs"]
# existing_keys = [kp["KeyName"] for kp in key_pairs]

# print("\nAvailable Key Pairs:")
# for i, key in enumerate(existing_keys, 1):
#     print(f"{i}. {key}")

# key_name = input("\nEnter an existing key pair name or a new one to create: ").strip()
# if key_name not in existing_keys:
#     print(f"Creating new key pair '{key_name}'...")
#     key_pair = ec2.create_key_pair(KeyName=key_name)
#     with open(f"{key_name}.pem", "w") as file:
#         file.write(key_pair["KeyMaterial"])
#     print(f"Key pair saved to {key_name}.pem (Make sure to change its permission: chmod 400)")
# else:
#     print(f"Using existing key pair: {key_name}")

# # Security group
# print("\nSecurity Group: Using default security group.")
# print(" To create or modify security groups, go to the 'Networking' section of MCloud.")

# # Instance Type
# instance_types = [
#     "t2.micro", "t3.micro", "t3a.micro",
#     "t2.small", "t3.small", "t2.medium", "t3.medium",
#     "m5.large", "c5.large", "a1.medium"
# ]

# print("\nChoose an instance type:")
# for i, itype in enumerate(instance_types, 1):
#     print(f"{i}. {itype}")

# try:
#     choice = int(input("Your choice: ")) - 1
#     instance_type = instance_types[choice] if 0 <= choice < len(instance_types) else "t2.micro"
# except:
#     print("Invalid choice, using default 't2.micro'")
#     instance_type = "t2.micro"

# # Launch Instance
# print("\nLaunching EC2 instance...")
# response = ec2.run_instances(
#     ImageId=ami_id,
#     InstanceType=instance_type,
#     KeyName=key_name,
#     MinCount=1,
#     MaxCount=1,
#     SecurityGroups=['default']
# )

# instance_id = response["Instances"][0]["InstanceId"]
# print(f" Waiting for instance {instance_id} to enter 'running' state...")

# ec2_resource = boto3.resource("ec2", region_name=region)
# instance = ec2_resource.Instance(instance_id)
# instance.wait_until_running()

# instance.load()
# public_ip = instance.public_ip_address

# print("\n EC2 Instance launched successfully!")
# print(f"Instance ID: {instance_id}")
# print(f"Public IP: {public_ip}")
# print(f"State: {instance.state['Name']}")
# print(f"Launch Time: {instance.launch_time}")
# print(f"Type: {instance.instance_type}")
# print(f"AMI: {instance.image_id}")
# print(f"Key Pair: {instance.key_name}")

# # Asking  about static website hosting
# host_website = input("\n Do you want to host a static website on this instance? (y/n): ").strip().lower()
# if host_website == "y":
#     print(" Redirecting to static website setup...")
# else:
#     print(" Setup complete. You can now SSH into your instance and deploy your applications.")



#Chatgpt ka code (Niche)



# Get default region from config
session = boto3.session.Session()
region = session.region_name

if not region:
    print("❌ No region configured. Please run 'aws configure' first.")
    exit(1)

ec2 = session.client("ec2")
ec2_resource = session.resource("ec2")

# AMI map based on region
ami_map_by_region = {
    "us-east-1": {
        "ubuntu": "ami-080e1f13689e07408",
        "amazon-linux": "ami-0c2b8ca1dad447f8a",
        "debian": "ami-00a6eeb43b1f9f96b",
        "centos": "ami-0d63de463e6604d0a",
        "redhat": "ami-052c08d70def0ac62"
    },
    "us-west-2": {
        "ubuntu": "ami-09ebacdc178ae23c1",
        "amazon-linux": "ami-0b2f6494ff0b07a0e",
        "debian": "ami-0dc2d3e4c0f9ebd18",
        "centos": "ami-05e79b4c0c8e8f1b0",
        "redhat": "ami-077e31c4939f6a2f3"
    }
    # Add more regions and AMIs if needed
}

if region not in ami_map_by_region:
    print(f"❌ Region '{region}' not supported in AMI map.")
    exit(1)

print(f"\n Using region: {region}")
print("\nSupported OS options for your region:")
ami_map = ami_map_by_region[region]
for os_name, ami_id in ami_map.items():
    print(f"- {os_name}: {ami_id}")

chosen_os = input("\nEnter the OS you want (e.g., ubuntu, amazon-linux): ").strip().lower()
if chosen_os not in ami_map:
    print("Unsupported OS. Exiting...")
    exit(1)

ami_id = ami_map[chosen_os]

# Key Pair
key_pairs = ec2.describe_key_pairs()["KeyPairs"]
existing_keys = [kp["KeyName"] for kp in key_pairs]

print("\nAvailable Key Pairs:")
for i, key in enumerate(existing_keys, 1):
    print(f"{i}. {key}")

key_name = input("\nEnter an existing key pair name or a new one to create: ").strip()
if key_name not in existing_keys:
    print(f"Creating new key pair '{key_name}'...")
    key_pair = ec2.create_key_pair(KeyName=key_name)
    with open(f"{key_name}.pem", "w") as file:
        file.write(key_pair["KeyMaterial"])
    print(f"Key pair saved to {key_name}.pem (chmod 400 recommended)")
else:
    print(f"Using existing key pair: {key_name}")

# Security group
print("\nSecurity Group: Using default security group.")
print("💡 To create or modify security groups, go to the 'Networking' section of MCloud.")

# Instance Type
instance_types = [
    "t2.micro", "t3.micro", "t3a.micro",
    "t2.small", "t3.small", "t2.medium", "t3.medium",
    "m5.large", "c5.large", "a1.medium"
]

print("\nChoose an instance type:")
for i, itype in enumerate(instance_types, 1):
    print(f"{i}. {itype}")

try:
    choice = int(input("Your choice: ")) - 1
    instance_type = instance_types[choice] if 0 <= choice < len(instance_types) else "t2.micro"
except:
    print("Invalid choice, using default 't2.micro'")
    instance_type = "t2.micro"

# Launch Instance
print("\n🚀 Launching EC2 instance...")
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    MinCount=1,
    MaxCount=1,
    SecurityGroups=['default']
)

instance_id = response["Instances"][0]["InstanceId"]
print(f"⏳ Waiting for instance {instance_id} to enter 'running' state...")

instance = ec2_resource.Instance(instance_id)
instance.wait_until_running()
instance.load()

public_ip = instance.public_ip_address

print("\n✅ EC2 Instance launched successfully!")
print(f"Instance ID: {instance_id}")
print(f"Public IP: {public_ip}")
print(f"State: {instance.state['Name']}")
print(f"Launch Time: {instance.launch_time}")
print(f"Type: {instance.instance_type}")
print(f"AMI: {instance.image_id}")
print(f"Key Pair: {instance.key_name}")

# Ask about static website hosting
host_website = input("\n🌐 Do you want to host a static website on this instance? (y/n): ").strip().lower()
if host_website == "y":
    print("🚀 Redirecting to static website setup...")
else:
    print("🎉 Setup complete. You can now SSH into your instance and deploy your applications.")
