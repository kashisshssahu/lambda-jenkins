import boto3
lambda_Client = boto3.client('lambda', region_name='us-east-1')
response =lambda_Client.create_function(
          Code={
                'S3Bucket': 'kashisshlambda',
                'S3Key': 'lambda.zip', #how can i create or fetch this S3Key
          },
          Description='Process image objects from Amazon S3.',
          FunctionName="check",
          Handler='lambda.lambda_handler',
          Publish=True,
          Role='arn:aws:iam::260723280636:role/jenkins_lambda',
          Runtime='python3.12'
          )
