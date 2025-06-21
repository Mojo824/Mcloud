import boto3
import time
def get_all_regions():
    ec2 = boto3.client("ec2")
    return [r["RegionName"] for r in ec2.describe_regions()["Regions"]]

def show_regions_menu(regions):
    print("\n Available AWS Regions:")
    for idx, region in enumerate(regions):
        print(f"{idx + 1}. {region}")
    print("a. All regions")

def get_user_region_selection(regions):
    selection = input("\n Enter region index(es) (e.g., 1 or 1,3 or 'a' for all): ").strip().lower()
    if selection == 'a':
        return regions

    try:
        indexes = [int(i.strip()) - 1 for i in selection.split(',')]
        return [regions[i] for i in indexes if 0 <= i < len(regions)]
    except ValueError:
        print("❌ Invalid input.")
        return []

def get_vpc_name(tags):
    if not tags:
        return "N/A"
    for tag in tags:
        if tag["Key"].lower() == "name":
            return tag["Value"]
    return "N/A"

def is_subnet_public(ec2_client, subnet_id, route_table_map):
    for route_table in route_table_map:
        for assoc in route_table.get("Associations", []):
            if assoc.get("SubnetId") == subnet_id:
                for route in route_table.get("Routes", []):
                    if route.get("GatewayId", "").startswith("igw-"):
                        return True
    return False

def list_subnets_in_region(region):
    print(f"\n Region: {region}")
    print("-" * 50)

    ec2 = boto3.client("ec2", region_name=region)

    try:
        subnets = ec2.describe_subnets()["Subnets"]
        vpcs = {vpc["VpcId"]: vpc for vpc in ec2.describe_vpcs()["Vpcs"]}
        route_tables = ec2.describe_route_tables()["RouteTables"]
    except Exception as e:
        print(f" Error: {e}")
        return

    if not subnets:
        print("❌ No subnets found.")
        return

    for subnet in subnets:
        subnet_id = subnet["SubnetId"]
        cidr = subnet["CidrBlock"]
        az = subnet["AvailabilityZone"]
        vpc_id = subnet["VpcId"]
        is_default = subnet.get("DefaultForAz", False)
        name = get_vpc_name(subnet.get("Tags"))
        vpc_name = get_vpc_name(vpcs[vpc_id].get("Tags"))

        public = is_subnet_public(ec2, subnet_id, route_tables)

        print(f"Subnet Name     : {name}")
        print(f"Subnet ID       : {subnet_id}")
        print(f"CIDR Block      : {cidr}")
        print(f"AZ              : {az}")
        print(f"Default Subnet   : {'Yes' if is_default else 'No'}")
        print(f"Public/Private  : {'Public ' if public else 'Private '}")
        print(f"VPC             : {vpc_id} ({vpc_name})")
        print("-" * 50)

def main():
    regions = get_all_regions()
    show_regions_menu(regions)

    selected_regions = get_user_region_selection(regions)
    if not selected_regions:
        print("❌ No valid regions selected.")
        return

    for region in selected_regions:
        list_subnets_in_region(region)

if __name__ == "__main__":
    print ("                     +++Subnet List Tool MCloud+++")
    time.sleep(1)
    while True:
        main()
        again=input ("\n Wanna see Others or Again (y/n): ").strip().lower()
        if again!="y":
            break 


