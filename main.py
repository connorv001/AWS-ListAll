from pprint import pprint
import pandas as pd
import boto3
from botocore.exceptions import ClientError

client = boto3.client('resourcegroupstaggingapi', )
regions = boto3.session.Session().get_available_regions('ec2')
df=pd.DataFrame({'ResourceARN':[],'Key':[],'Value':[]})

for region in regions:
    try:
        client = boto3.client('resourcegroupstaggingapi', region_name=region)
        for x in client.get_resources().get('ResourceTagMappingList'):
            arn=x.get('ResourceARN')
            for i,tags in enumerate(x.get('Tags')):
                if i==0:
                    df.loc[len(df.index)]=[arn,tags['Key'],tags['Value']]
                else:
                    df.loc[len(df.index)]=['',tags['Key'],tags['Value']]
                
    except ClientError as e:
        print(f'Could not connect to region with error: {e}')
        
df.to_csv('Output.csv')
