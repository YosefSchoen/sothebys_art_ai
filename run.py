import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')


for page_num in range(10, 13):
    print(f'page: {page_num}')
    for collection_num in range(5):
        print('\t', f'collection: {collection_num}')
        instances = ec2.create_instances(
            ImageId='ami-04e75d33c0dea8a97',  # Replace with your AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',  # Replace with your instance type
            KeyName='Web-Scraper-Key',  # Replace with your key pair name
            IamInstanceProfile={
                'Name': 'ec2-admin'  # Replace with your IAM role name
            },
            UserData=f'''#!/bin/bash
                        cd sothebys_art_ai/ && && git pull && python3 main.py {page_num} {collection_num}
                        '''
        )