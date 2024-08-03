import json
import boto3
import sys
import scraper
from entities import Collection


# todo make summary pages show lots
# todo scrape images
# todo comment code
# todo get category of art
# todo scrape failed pages
# todo

with open('Config/config.json') as file:
    config_data = json.load(file)

s3 = boto3.client('s3')
bucket_name = config_data['AWS']['BUCKET']
page_num = int(sys.argv[1])


def send_to_s3(collection: Collection) -> None:
    data = json.dumps(collection.to_dict())
    print('saving to S3:', collection.page_id, collection.collection_id)
    object_key = f'{collection.page_id:03d}/{collection.collection_id + 1:03d}.json'
    # Upload to S3
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)
    print(f'succeeded on  page: {collection.page_id:03d} collection: {collection.collection_id + 1:03d}')


def main():
    try:
        collections = scraper.main(page_num)
        list(map(lambda collection: send_to_s3(collection), collections))

    except Exception as e:
        print(e)
        print(f'failed on page: {page_num:03d}')
        data = f'{e}'
        object_key = f'failed/{page_num:03d}.text'
        s3.put_object(Bucket=bucket_name, Key=object_key, Body=data)


if __name__ == "__main__":
    main()

