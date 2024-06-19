import scraper
import json
import boto3

s3 = boto3.client('s3')
bucket_name = 'scraped-data-raw'

for i in range(10, 11):
    for j in range(15):
        try:
            data = scraper.main(i, j)
            data = json.dumps(data)
            print(data)
            # Data to be written to S3
            # S3 parameters

            object_key = f'{i}/{j}.txt'
            # Upload to S3
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)
        except:
            print(f'failed on page: {i} collection: {j}')

