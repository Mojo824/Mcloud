import boto3
import sys

ec2 = boto3.client("ec2")

def create_vpc(cidr_block, name_tag, tenancy):
    try:
        print("🚀 Creating VPC...")

        # Create the VPC
        response = ec2.create_vpc(
            CidrBlock=cidr_block,
            InstanceTenancy=tenancy,
            TagSpecifications=[
                {
                    "ResourceType": "vpc",
                    "Tags": [{"Key": "Name", "Value": name_tag}]
                }
            ]
        )

        vpc_id = response['Vpc']['VpcId']
        print(f" VPC Created with ID: {vpc_id}")

        # Enable DNS settings
        ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
        ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

        print(" DNS support and hostnames enabled.")

        return vpc_id

    except Exception as e:
        print(f"❌ Failed to create VPC: {e}")
        sys.exit(1)

def main():
    print("                         +++VPC Creation Tool+++                         ")

    # Get CIDR input
    cidr = input(" Enter IPv4 CIDR block (e.g., 10.0.0.0/16): ").strip()

    # Get name tag
    name = input(" Enter a name tag for the VPC: ").strip() or "MyVPC"

    # Get tenancy
    print("\n Choose Tenancy:")
    print("1. Default (shared hardware) [Free Tier]")
    print("2. Dedicated (separate hardware) [More Costly]")
    tenancy_choice = input("Enter choice [1 or 2]: ").strip()
    tenancy = "dedicated" if tenancy_choice == "2" else "default"

    vpc_id = create_vpc(cidr, name, tenancy)

    print(f"\n VPC {vpc_id} created successfully with CIDR {cidr} and Name: {name}")


if __name__ == "__main__":
    main()
