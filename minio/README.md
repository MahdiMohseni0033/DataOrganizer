# Python MinIO Client Tutorial
This tutorial explains how to install the MinIO Python SDK, connect to a MinIO server, and perform basic object storage operations like creating buckets, uploading and downloading files.

## Installation
Install the minio package using pip:

```
pip install minio
```

## Connect to MinIO Server
Import the Minio client and create an object with your MinIO server endpoint, access key and secret key:


```
from minio import Minio

client = Minio('localhost:9000',
               access_key='minioadmin', 
               secret_key='minioadmin',
               secure=False)             
```

## Create a Bucket
Call make_bucket and pass the name of the bucket you want to create:

```
def make_bucket(bucket_name):
  if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)
```
This will create a new bucket if it doesn't already exist.

## List Buckets
Use list_buckets to print all buckets on the server:

```

def list_buckets():
  buckets = client.list_buckets()
  for bucket in buckets:
    print(bucket.name, bucket.creation_date)
```
## Upload Objects
To upload a file as an object to a bucket:

```
def upload_file(bucket_name, object_name, file_path):
  client.fput_object(bucket_name, object_name, file_path)
```
## Download Objects
Download an object and save to a local file:


```
def download_file(bucket_name, object_name, file_path):
  client.fget_object(bucket_name, object_name, file_path)
```
## Delete Bucket
Remove an empty bucket using:


```
def remove_bucket(bucket_name):
  if client.bucket_exists(bucket_name): 
    client.remove_bucket(bucket_name)
```
## Delete Object
Remove an object from a bucket:

```
def remove_object(bucket_name, object_name):
  if client.stat_object(bucket_name, object_name):
    client.remove_object(bucket_name, object_name)
```
This covers the basic bucket and object operations with MinIO using the Python SDK. Please refer to the MinIO Python Client API Reference for the full list of available methods.