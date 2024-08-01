import json
import boto3
import sys
import scraper

page_num = int(sys.argv[1])
s3 = boto3.client('s3')
bucket_name = 'scraped-data-raw'

try:
    page_data = scraper.main(page_num)
    for collection_num, collection_data in enumerate(page_data):
        data = json.dumps(collection_data)
        print('saving to S3:', page_num, collection_num)
        object_key = f'{page_num:03d}/{collection_num+1:03d}.json'
        # Upload to S3
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)
        print(f'succeeded on  page: {page_num:03d} collection: {collection_num + 1:03d}')

except Exception as e:
    print(e)
    print(f'failed on page: {page_num:03d}')
    data = 'failed to scrape'
    object_key = f'failed/{page_num:03d}.text'
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)


