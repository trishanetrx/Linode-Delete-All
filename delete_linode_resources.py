import os
import requests

# Linode API endpoint
API_URL = 'https://api.linode.com/v4/'

# Get the Linode API key from environment variable
API_KEY = os.getenv('LINODE_API_KEY')

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def delete_linode_instances():
    # List Linodes
    response = requests.get(API_URL + 'linode/instances', headers=headers)
    if response.status_code != 200:
        print(f"Error fetching Linodes: {response.text}")
        return

    linodes = response.json().get('data', [])
    for linode in linodes:
        linode_id = linode['id']
        print(f"Deleting Linode instance {linode_id}...")
        delete_response = requests.delete(API_URL + f'linode/instances/{linode_id}', headers=headers)
        if delete_response.status_code == 204:
            print(f"Linode {linode_id} deleted successfully.")
        else:
            print(f"Error deleting Linode {linode_id}: {delete_response.text}")

def delete_volumes():
    # List Volumes
    response = requests.get(API_URL + 'volumes', headers=headers)
    if response.status_code != 200:
        print(f"Error fetching Volumes: {response.text}")
        return

    volumes = response.json().get('data', [])
    for volume in volumes:
        volume_id = volume['id']
        print(f"Deleting Volume {volume_id}...")
        delete_response = requests.delete(API_URL + f'volumes/{volume_id}', headers=headers)
        if delete_response.status_code == 204:
            print(f"Volume {volume_id} deleted successfully.")
        else:
            print(f"Error deleting Volume {volume_id}: {delete_response.text}")

def main():
    print("Deleting Linode resources...")
    delete_linode_instances()
    delete_volumes()

if __name__ == '__main__':
    main()
