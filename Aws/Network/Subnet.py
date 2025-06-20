import boto3
import os
import sys

ec2 = boto3.client("ec2")

def list_vpcs():
    vpcs = ec2.describe_vpcs()["Vpcs"]
    if not vpcs:
        print("❌ No VPCs found.")
        print(" Please create one first.")
        res = input("wanna create one ?? (y/n)").strip().lower()
        if res =="y":
            os.system("python3 Vpc.py")
            sys.exit(1)
    else :
        exit(1)

    print("\n Available VPCs:")
    for idx, vpc in enumerate(vpcs):
        vpc_id = vpc["VpcId"]
        cidr = vpc["CidrBlock"]
        is_default = vpc.get("IsDefault", False)
        print(f"{idx+1}. {vpc_id} | CIDR: {cidr} {'[Default]' if is_default else ''}")
    return vpcs

def choose_vpc(vpcs):
    try:
        choice = int(input("\nChoose a VPC by number: ")) - 1
        if 0 <= choice < len(vpcs):
            return vpcs[choice]["VpcId"]
        else:
            print("❌ Invalid choice.")
            sys.exit(1)
    except ValueError:
        print("❌ Please enter a valid number.")
        sys.exit(1)

def get_availability_zone():
    zones = ec2.describe_availability_zones()["AvailabilityZones"]
    print("\n Available Zones:")
    for i, zone in enumerate(zones):
        print(f"{i+1}. {zone['ZoneName']}")

    choice = input("Choose zone number (press Enter to auto-select): ").strip()
    if choice == "":
        return zones[0]['ZoneName']
    try:
        index = int(choice) - 1
        return zones[index]["ZoneName"]
    except:
        print("❌ Invalid zone choice.")
        sys.exit(1)

def create_subnet(vpc_id, cidr_block, zone, name):
    try:
        response = ec2.create_subnet(
            VpcId=vpc_id,
            CidrBlock=cidr_block,
            AvailabilityZone=zone,
            TagSpecifications=[
                {
                    "ResourceType": "subnet",
                    "Tags": [
                        {"Key": "Name", "Value": name}
                    ]
                }
            ]
        )
        subnet_id = response["Subnet"]["SubnetId"]
        print(f"\n [*] Subnet created!")
        print(f"   Subnet ID: {subnet_id}")
        print(f"   CIDR: {cidr_block}")
        print(f"   AZ: {zone}")
        return subnet_id
    except Exception as e:
        print(f"❌ Failed to create subnet: {e}")
        sys.exit(1)

def main():
    print("                      +++AWS Subnet Creator+++                           ")

    vpcs = list_vpcs()
    vpc_id = choose_vpc(vpcs)

    cidr_block = input(" Enter Subnet CIDR (e.g., 10.0.1.0/24): ").strip()
    name = input(" Enter Subnet Name (tag): ").strip()
    zone = get_availability_zone()

    create_subnet(vpc_id, cidr_block, zone, name)

if __name__ == "__main__":
    main()
