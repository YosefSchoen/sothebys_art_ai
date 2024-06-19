import scraper
import json
import boto3

s3 = boto3.client('s3')
bucket_name = 'scraped-data-raw'

for i in range(50, 51):
    for j in range(5, 15):
        try:
            data = scraper.main(i, j)
            data = json.dumps(data)
            print(data)

            object_key = f'{i}/{j}.txt'
            # Upload to S3
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)

        except:
            print(f'failed on page: {i} collection: {j}')
            data = json.dumps({'page': i, 'collection': j})
            object_key = 'fail.txt'
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)

