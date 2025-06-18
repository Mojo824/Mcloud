import os
import time 

def tamijse_exit():
    print("Invalid Input. EXITING...")
    for i in range(5):
        print(".\n")
        time.sleep(1)
    exit(1)

print ("                    ++AWS Servises++                    "  )
a=int (input  (" AWS Sevices \n1. Compute Services (Ec2,Lambda etc..) \n2. Storage (S3,Ebs etc..) \n3. Networking (Vpc ,elasticip etc..) \n4. Database (Rds , Dynmodb) \n5. DevOps Tools (Code deploy , github action etc..) \n6. Security & IAM( User creation, role etc.. ) \n [*] Your Response :"))
if a==1 :
    b=int (input("Compute Services:  \n1. Deploy Ec2 \n2. Lmbda  \n Your Response :"))
    if b==1:
        os.system("python3 Aws/Compute/Deployec2.py ")
    elif b==2:
        os.system("python3 Aws/Compute/Deploylambda.py")
    else :
        tamijse_exit()

elif a==2 :
    b=int (input("Storage Services: \n1. Deploy S3 Bucket \n2. Deploy Ebs volume \n 3. Snapshot \n Your Response : "))
    if b==1 :
        os.system("python3 Aws/Storage/Deploys3.py")
    elif b==2 :
        os.system("python3 Aws/Storage/Deployebs.py")
    elif b==3:
        os.system("python3 Aws/Storage/Snapshot.py ")
    else:
        tamijse_exit()

elif a==3:
    b=int(input("Network Services \n1. VPC \n2. Elastic IP \n3. Security Groups \nYour Response : "))
    if b==1 :
        os.system("python3 Aws/Network/Vpc.py")
    elif b==2:
        os.system("python3 Aws/Network/Elasticip.py")
    elif b==3:
        os.system("python3 Aws/Network/Securitygrp.py")
    else:
        tamijse_exit()

elif a==4:
    b=int(input("Databases : \n1. Rds \n2. Dynomodb \n Your Response : "))
    if b==1:
        os.system("python3 Aws/Databases/Rds.py")
    elif b==2:
        os.system("python3 Aws/Databases/Dynmodb.py")
    else :
        tamijse_exit()

elif a==5:
    b=int(input("DevOps Tools : \n1. Code Deploy \n2. Github Actions \ Your Response :"))
    if b==1:
        os.system("python3 Aws/DevOps/Codedeploy.py ")
    elif b==2:
        os.system("python3 Aws/DevOps/Githubaction.py")
    else:
        tamijse_exit()

elif a==6:
    b=int(input("Security & IAM : \n1. User Creation  \n2. Role creation  "))
    if b==1:
        os.system("python3 Usernew.py")
    elif b==2:
        os.system("python3 role.py")
    else:
        tamijse_exit()

        

        


