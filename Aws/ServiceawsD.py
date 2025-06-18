import os
import time 
base_dir = os.path.dirname(os.path.abspath(__file__))
def tamijse_exit():
    print("Invalid Input. EXITING...")
    for i in range(5):
        print(".\n")
        time.sleep(1)
    exit(1)

def fakeload(a):
    print (f" Redirecting to {a} menu \n ")
    for i in range(5):
        print(".", end='', flush=True)
        time.sleep(.3)

print ("                    ++AWS Servises++                    "  )
a=int (input  (" AWS Sevices \n1. Compute Services (Ec2,Lambda etc..) \n2. Storage (S3,Ebs etc..) \n3. Networking (Vpc ,elasticip etc..) \n4. Database (Rds , Dynmodb) \n5. DevOps Tools (Code deploy , github action etc..) \n6. Security & IAM( User creation, role etc.. ) \n [*] Your Response :"))
p1 = "Deployment" 
p2 ="Storage"
p3 = "Networking"
p4= "Database"
p5= "DevOps"
p6= "Security & IAM" 
if a==1 :
    b=int (input("Compute Services:  \n1. Deploy Ec2 \n2. Lmbda  \n Your Response :"))
    if b==1:
        fakeload(p1)
        deployec2_script = os.path.join(base_dir, "Compute", "Deployec2.py")
        os.system(f"python3 {deployec2_script} ")
    elif b==2:
        fakeload(p1)
        deploylambda_script = os.path.join(base_dir, "Compute", "Deployec2.py")
        os.system(f"python3 {deploylambda_script}")
    else :
        tamijse_exit()

elif a==2 :
    b=int (input("Storage Services: \n1. Deploy S3 Bucket \n2. Deploy Ebs volume \n 3. Snapshot \n Your Response : "))
    if b==1 :
        fakeload(p2)
        deployes3_script = os.path.join(base_dir, "Storage", "Deployes3.py")
        os.system(f"python3 {deployes3_script}")
    elif b==2 :
        fakeload(p2)
        deployeebs_script = os.path.join(base_dir, "Storage", "Deployeebs.py")
        os.system(f"python3 {deployeebs_script}")
    elif b==3:
        fakeload(p2)
        Snapshot_script = os.path.join(base_dir, "Storage", "Snapshot.py")
        os.system(f"python3 {Snapshot_script}")
    else:
        tamijse_exit()

elif a==3:
    b=int(input("Network Services \n1. VPC \n2. Elastic IP \n3. Security Groups \nYour Response : "))
    if b==1 :
        fakeload(p3)
        vpc_script = os.path.join(base_dir, "Network", "vpc.py")
        os.system(f"python3 {vpc_script}")
    elif b==2:
        fakeload(p3)
        Elasticip_script = os.path.join(base_dir, "Network", "Elasticip.py")
        os.system("python3 Aws/Network/Elasticip.py")
    elif b==3:
        fakeload(p3)
        Securitygrp_script = os.path.join(base_dir, "Network", "Securitygrp.py")
        os.system(f"python3 {Securitygrp_script}")
    else:
        tamijse_exit()

elif a==4:
    b=int(input("Databases : \n1. Rds \n2. Dynomodb \n Your Response : "))
    if b==1:
        fakeload(p4)
        Rds_script = os.path.join(base_dir, "Database", "Rds.py")
        os.system(f"python3 {Rds_script}")
    elif b==2:
        fakeload(p4)
        Dynmodb_script = os.path.join(base_dir, "Database", "Dynmodb.py")
        os.system(f"python3 {Dynmodb_script}")
    else :
        tamijse_exit()

elif a==5:
    b=int(input("DevOps Tools : \n1. Code Deploy \n2. Github Actions \n Your Response :"))
    if b==1:
        fakeload(p5)
        Codedeploy_script = os.path.join(base_dir, "DevOps", "Codedeploy.py")
        os.system(f"python3 {Codedeploy_script} ")
    elif b==2:
        fakeload(p5)
        Githubaction_script = os.path.join(base_dir, "DevOps", "Githubaction.py")
        os.system(f"python3 {Githubaction_script}")
    else:
        tamijse_exit()

elif a==6:
    b=int(input("Security & IAM : \n1. User Creation  \n2. Role creation  "))
    if b==1:
        fakeload(p6)
        Newuser_script = os.path.join(base_dir, "Security & IAM", "Newuser.py")
        os.system(f"python3 {Newuser_script}")
    elif b==2:
        fakeload(p6)
        Newrole_script = os.path.join(base_dir, "Security & IAM", "Newrole.py")
        os.system(f"python3 {Newrole_script}")
    else:
        tamijse_exit()

        

        


