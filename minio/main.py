import io
import matplotlib.pyplot as plt
from matplotlib.image import imread
from minio import Minio
from PIL import Image

# Connect to MinIO
client = Minio('172.17.0.3:9000',
               access_key='minioadmin',
               secret_key='minioadmin',
               secure=False)


def make_bucket(bucket_name):
    """Creates a new bucket on the MinIO server"""
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)


def list_buckets():
    """Lists all buckets on the MinIO server"""
    buckets = client.list_buckets()
    for bucket in buckets:
        print(bucket.name, bucket.creation_date)


def list_objects(bucket_name):
    """Lists objects in a bucket"""
    objects = client.list_objects(bucket_name)
    for obj in objects:
        print(obj.object_name, obj.size, obj.last_modified)


def upload_file(bucket_name, object_name, file_path):
    """Uploads a file to a bucket"""
    client.fput_object(bucket_name, object_name, file_path)


def download_file(bucket_name, object_name, file_path):
    """Downloads an object and saves it locally"""
    client.fget_object(bucket_name, object_name, file_path)


def download_image(bucket_name, object_name):
    """Downloads an image object and displays it"""
    response = client.get_object(bucket_name, object_name)
    image_bytes = response.read()

    img = Image.open(io.BytesIO(image_bytes))
    plt.imshow(img)
    plt.show()


def remove_bucket(bucket_name):
    """Removes an empty bucket from the MinIO server"""

    # Check if bucket exists
    if client.bucket_exists(bucket_name):

        # Remove bucket
        client.remove_bucket(bucket_name)

    else:
        print(f"Bucket {bucket_name} does not exist")


def remove_object(bucket_name, object_name):
    """Removes an object from a bucket"""

    # Check if object exists
    if client.stat_object(bucket_name, object_name):

        # Remove object
        client.remove_object(bucket_name, object_name)

    else:
        print(f"Object {object_name} does not exist in bucket {bucket_name}")


if __name__ == "__main__":
    bucket_name = 'king'
    # make_bucket(bucket_name)
    #
    # file_path = 'cat.jpg'
    # upload_file(bucket_name, 'cat.jpg', file_path)

    object_name = '2000.jpg'
    download_image(bucket_name, object_name)