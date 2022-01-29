# AWS-ListAll
Project to list all resources in an AWS account with tags. 
This script works on any system 


## Get started:

Install python3 and pip3 along with AWS CLI (for your os)
then, 
```sh
git clone https://github.com/connorv001/AWS-ListAll.git
cd AWS-ListAll
pip3 install pandas
pip3 install boto3
```
to run this script, given that you've either ran `aws configure` with an IAM user for programmatic access or configured enviromental variables for enterprise accounts. It should work out of the box after running 
```sh
python3 main.py
```
It will generate an Output.csv with all the resources [which are tagged] 
