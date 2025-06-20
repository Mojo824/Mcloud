import boto3
import sys

ec2 = boto3.client("ec2")

def add_outbound_rule(sg_id, protocol, port, cidr):
    try:
        ec2.authorize_security_group_egress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    "IpProtocol": protocol,
                    "FromPort": port,
                    "ToPort": port,
                    "IpRanges": [{"CidrIp": cidr}]
                }
            ]
        )
        print(f"Outbound Rule added: {protocol.upper()} on port {port} to {cidr}")
    except Exception as e:
        print(f"❌ Error adding outbound rule: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 add_outbound_rules.py <SECURITY_GROUP_ID>")
        sys.exit(1)

    sg_id = sys.argv[1]
    print(f" Adding Outbound Rules to Security Group: {sg_id}")

    while True:
        protocol = input("Protocol (tcp/udp/all): ").strip().lower()
        if protocol == "all":
            protocol = "-1"
            port = -1
        else:
            try:
                port = int(input("  Port number: ").strip())
            except ValueError:
                print("❌ Invalid port. Try again.")
                continue

        cidr = input(" Destination CIDR (e.g., 0.0.0.0/0): ").strip()

        add_outbound_rule(sg_id, protocol, port, cidr)

        more = input(" Add another Outbound rule? (y/n): ").strip().lower()
        if more != "y":
            break

if __name__ == "__main__":
    main()
