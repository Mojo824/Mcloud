import boto3

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

    indexes = []
    try:
        indexes = [int(i) - 1 for i in selection.split(',') if i.strip().isdigit()]
    except ValueError:
        print("❌ Invalid input.")
        return []

    return [regions[i] for i in indexes if 0 <= i < len(regions)]

def list_instances_in_region(region):
    ec2 = boto3.resource("ec2", region_name=region)
    instances = ec2.instances.all()
    print(f"\n Region: {region}")
    print("-" * 40)

    found = False
    for instance in instances:
        found = True
        name_tag = next((tag['Value'] for tag in instance.tags or [] if tag['Key'] == 'Name'), 'N/A')
        print(f"Name            : {name_tag}")
        print(f"Instance ID     : {instance.id}")
        print(f"State           : {instance.state['Name']}")
        print(f"Instance Type   : {instance.instance_type}")
        print(f"AMI ID          : {instance.image_id}")
        print(f"Public IP       : {instance.public_ip_address}")
        print(f"Launch Time     : {instance.launch_time}")
        print("Security Groups :")
        for sg in instance.security_groups:
            print(f"  🛡️ {sg['GroupName']} (ID: {sg['GroupId']})")
    print("-" * 40)

    if not found:
        print("❌ No EC2 instances found in this region.")

def main():
    regions = get_all_regions()
    show_regions_menu(regions)

    selected_regions = get_user_region_selection(regions)
    if not selected_regions:
        print("❌ No valid regions selected.")
        return

    for region in selected_regions:
        list_instances_in_region(region)

if __name__ == "__main__":
    print ("                    ++Ec2 list Tool MCloud ++")
    main()
