import scraper
import json
import boto3

s3 = boto3.client('s3')
bucket_name = 'scraped-data-raw'

for i in range():
    for j in range(5, 15):
        try:
            data = scraper.main(i, j)
            data = json.dumps(data)

            object_key = f'{i:03d}/{j:03d}.json'
            # Upload to S3
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)
            print(f'succeeded on  page: {i:03d} collection: {j:03d}')
        except:
            print(f'failed on page: {i:03d} collection: {j:03d}')
            data = 'failed to scrape'
            object_key = f'{i:03d}/{j:03d}.text'
            s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)


