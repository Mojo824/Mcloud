import boto3

def get_all_regions():
    ec2 = boto3.client("ec2")
    return [r["RegionName"] for r in ec2.describe_regions()["Regions"]]

def show_regions_menu(regions):
    print("\n Available AWS Regions:")
    for idx, region in enumerate(regions):
        print(f"{idx + 1}. {region}")
    print("a. All regions")

def get_user_region_selection(regions):  # user selection
    selection = input("\n Enter region index(es) (e.g., 1 or 1,3 or 'a' for all): ").strip().lower()
    if selection == 'a':
        return regions

    try:
        indexes = [int(i.strip()) - 1 for i in selection.split(',')]
        return [regions[i] for i in indexes if 0 <= i < len(regions)]
    except ValueError:
        print("❌ Invalid input.")
        return []

def list_vpcs_in_region(region):
    ec2 = boto3.client("ec2", region_name=region)

    print(f"\n Region: {region}")
    print("-" * 40)

    try:
        vpcs = ec2.describe_vpcs()["Vpcs"]
    except Exception as e:
        print(f" Error fetching VPCs: {e}")
        return

    if not vpcs:
        print("❌ No VPCs found.")
        return

    for vpc in vpcs:
        cidr = vpc.get("CidrBlock", "N/A")
        vpc_id = vpc.get("VpcId")
        state = vpc.get("State")
        is_default = vpc.get("IsDefault")
        tags = {tag["Key"]: tag["Value"] for tag in vpc.get("Tags", [])}
        name = tags.get("Name", "N/A")

        print(f"VPC ID        : {vpc_id}")
        print(f"Name          : {name}")
        print(f"CIDR Block    : {cidr}")
        print(f"State         : {state}")
        print(f"Is Default     : {is_default}")
        print("-" * 40)

def main():
    while True:
        regions = get_all_regions()
        show_regions_menu(regions)

        selected_regions = get_user_region_selection(regions)
        if not selected_regions:
            print("❌ No valid regions selected.")
            return

        for region in selected_regions:
            list_vpcs_in_region(region)
        again = input ("[*] Wanna se more again (Another) ??? (y/n)")
        if again!="y":
            break

if __name__ == "__main__":
    print ("                    ++ Vpc List Tool Mcloud++")
    main()
