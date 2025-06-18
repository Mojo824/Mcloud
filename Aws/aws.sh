echo "                 ==== MCloud AWS Service ====                "
echo "Starting..."
sleep 2
echo "Configuring  AWS ..."
if ! command -v aws >/dev/null 2>&1; then
    echo "AWS Cli not found !!"
    read -p "Do you want to install AWS CLI? (Y/N): " res
    if [["$res" == "y" || "Y" ]]; then
        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
        unzip awscliv2.zip
        sudo ./aws/install
    

    elif [["$res" == "n" || "N"]]; then 
        echo "Install AWS cli manually \n Exitingg....... "
        exit 1
    else 
        echo "Invalid Input !! \n Exiting....."
        exit 1
    fi
else 
    echo "AWS cli Found"
fi

echo "[*] Checking for boto3 module..."

if ! python3 -c "import boto3" 2>/dev/null; then
    echo "[!] boto3 not found. Attempting installation..."
    
    if command -v pip3 >/dev/null 2>&1; then
        sudo pip3 install boto3
    elif command -v pip >/dev/null 2>&1; then
        sudo pip install boto3
    else
        echo "[✗] pip is not installed. Please install pip to proceed Manually ."
        exit 1
    fi

    echo "[+] boto3 installed successfully."
else
    echo "[✓] boto3 is already installed."
fi


aws configure

echo -e "What you wanna do \n 1.New Deploy "
read -p "Your Response " resD
if [[ "$resD" == "1" ]]; then 
    python3 $BASE_DIR/Aws/ServicesawsD.py
fi