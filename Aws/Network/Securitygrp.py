import boto3
import botocore
import sys
import os
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ServiceawsD import fakeload

base_dir = os.path.dirname(os.path.abspath(__file__))
ec2 = boto3.client("ec2")

def list_vpcs():
    vpcs = ec2.describe_vpcs()["Vpcs"]
    if not vpcs:
        print("❌ No VPCs found.")
        sys.exit(1)

    print("\nAvailable VPCs:")
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

def create_security_group(name, description, vpc_id):
    try:
        response = ec2.create_security_group(
            GroupName=name,
            Description=description,
            VpcId=vpc_id,
            TagSpecifications=[
                {
                    "ResourceType": "security-group",
                    "Tags": [
                        {"Key": "Name", "Value": name},
                        {"Key": "CreatedBy", "Value": "SecurityGroupCreator"}
                    ]
                }
            ]
        )
        return response["GroupId"]
    except botocore.exceptions.ClientError as e:
        print(f"❌ Failed to create security group: {e}")
        sys.exit(1)

def main():
    print("                     ++🔐 AWS Security Group Creator++                       ")

    vpcs = list_vpcs()
    vpc_id = choose_vpc(vpcs)
    print(f"\nSelected VPC: {vpc_id}")

    name = input(" Enter Security Group Name (New): ").strip()
    description = input(" Enter Description: ").strip()

    sg_id = create_security_group(name, description, vpc_id)
    print(f"\nSecurity Group '{name}' created with ID: {sg_id}")

    next_step = input("\n👉 Do you want to add inbound rules now? (y/n): ").strip().lower()
    if next_step == "y":
        
        fakeload("Inbound Rule")
        Inbound_script = os.path.join(base_dir, "Fwrule", "Inbound.py")
        os.system(f"python3 {Inbound_script} {sg_id}")
    else:
        print("⚠️ No rules added. This group blocks all traffic for now.")

if __name__ == "__main__":
    main()
