# MCloud

![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**MCloud** is a beginner-friendly, open-source multi-cloud automation utility designed to manage and deploy services across **AWS** and **Azure** directly from your terminal.

> **Currently Under Construction**
> 
>  AWS: EC2, S3, IAM, VPC  
>  Azure: Modules under development  
>  Static website hosting, security, and DevOps integrations incoming!

```bash
$ bash MCloud.sh

````
Choose your Cloud
1. Azure
2. AWS

 Features

     Multi-cloud support (AWS + Azure)

     EC2 deployment with:

        Key pair creation/check

        AMI selection by OS

        Auto-detection of region from AWS CLI config

     S3, EBS volume and snapshot automation

     VPC, Elastic IP, Security Group setup

     IAM (users and roles)

     DevOps tooling (CodeDeploy, GitHub Actions – WIP)

     Clean Bash/Python modular structure

 Requirements

    Python 3.6+

    AWS CLI configured (aws configure)

    Bash terminal (Linux/macOS/WSL)

    boto3 library (pip install boto3)

    unzip, curl, sudo privileges (for auto-install)

 Project Structure

```json 

MCloud/
├── Aws/
│   ├── Compute/
│   ├── Network/
│   ├── Storage/
│   └── ...
├── Azure/
│   └── (coming soon)
├── LICENSE
├── README.md
└── MCloud.sh

<<<<<<< HEAD
```json 

 Setup
=======
```
🛠 Setup
>>>>>>> 94f8017ee34dd78dc7d3a013bf2b76d992615f1d

# Clone the repo
```bash 
git clone https://github.com/Mojo824/MCloud.git
cd MCloud

# Make executable if needed
chmod +x MCloud.sh

# Run the tool
bash MCloud.sh
<<<<<<< HEAD

 License
=======
```
📝 License
>>>>>>> 94f8017ee34dd78dc7d3a013bf2b76d992615f1d

This project is licensed under the MIT License.
Feel free to use, modify, and distribute!
 Contributing

MCloud is in active development, and contributions are highly welcome!
Steps to contribute:

    Fork the repository

    Create your branch: git checkout -b feature-name

    Make changes

    Push changes: git push origin feature-name

    Open a pull request 

    New to open source? No worries — just open an issue or ask for guidance.

Author

Mojo823
Email : [insane.mjoshi@gmail.com]
🔗 GitHub Profile
Contact & Discussion

    Got ideas?

    Want to improve a module?

    Spotted a bug?

Open an issue or pull request — we’d love to collaborate!
