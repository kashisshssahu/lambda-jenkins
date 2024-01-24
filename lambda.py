import json
import boto3
def lambda_handler(event, context):
    client = boto3.client('ec2', region_name= 'us-east-1')
    response = client.run_instances(
           ImageId='ami-0a3c3a20c09d6f377',
           InstanceType='t2.micro',
           KeyName='boto3',
           MaxCount=1,
           MinCount=1
           )

