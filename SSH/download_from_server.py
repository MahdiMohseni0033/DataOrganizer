import paramiko
from tqdm import tqdm


def download_file(hostname, port, username, password, remote_path, local_path):
    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the remote server
        client.connect(hostname=hostname, port=port, username=username, password=password)

        # Create an SFTP client from the SSH client
        sftp = client.open_sftp()

        # Get the file size
        remote_file = sftp.stat(remote_path)
        total_size = remote_file.st_size

        # Download the file with progress bar
        with tqdm(total=total_size, unit="B", unit_scale=True) as progress_bar:
            sftp.get(remote_path, local_path,
                     callback=lambda transferred, total: progress_bar.update(transferred - progress_bar.n))

        print(f"File downloaded successfully: {local_path}")

    finally:
        # Close the SFTP and SSH connections
        sftp.close()
        client.close()


# Specify the remote server details and file paths
hostname = "209.20.156.195"
port = 22  # Default SSH port is 22
username = "ubuntu"
password = ""
remote_path = "/home/ubuntu/MahdiMohseni/Prjs/StableDiffusion/train/save_results/2023-09-04__08-28-05/accelerator_checkpoints/ckpt2000.zip"
local_path = "/home/mmohseni/Desktop/workload/result_of_inpainting/Lama/ckpt2000.zip"
# Call the function to download the file
download_file(hostname, port, username, password, remote_path, local_path)
