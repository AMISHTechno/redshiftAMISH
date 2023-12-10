'''
Create a shell script or cronjob until integrated into our Github actions etc

Backs up to Google Drive by Default, otherwise ext location, or local.

Auth included in .env

'''

import os
import shutil
from datetime import datetime
from dotenv import load_dotenv
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
from tqdm import tqdm

# Load environment variables
load_dotenv()

# Environment variables
EXT_SOURCE = os.getenv('EXT_SOURCE')
LOG_DIR = os.getenv('BACKUP_LOG_DIR', './omni_logs/backup_logs')

def authenticate_google_drive():
    """Authenticate and return a Google Drive service."""
    gauth = GoogleAuth()
    # Load credentials from gAuth.env
    gauth.LoadCredentialsFile("gAuth.env")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile("gAuth.env")
    return GoogleDrive(gauth)

def create_drive_folder(drive, folder_name, parent_id=None):
    """Create a folder in Google Drive."""
    folder_metadata = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        folder_metadata['parents'] = [{'id': parent_id}]
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    return folder['id']

def find_or_create_drive_folder(drive, folder_name, parent_id=None):
    """Find a folder in Google Drive or create it if it doesn't exist."""
    query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    file_list = drive.ListFile({'q': query}).GetList()
    if file_list:
        return file_list[0]['id']
    else:
        return create_drive_folder(drive, folder_name, parent_id)

def backup_to_google_drive(drive, folder_path):
    """Backup files to Google Drive with folder hierarchy."""
    root_folder_id = find_or_create_drive_folder(drive, os.path.basename(folder_path))
    for root, dirs, files in tqdm(os.walk(folder_path), desc="Backing up to Google Drive"):
        parent_folder_id = root_folder_id
        sub_path = root[len(folder_path)+1:]
        for folder in sub_path.split(os.sep):
            if folder:
                parent_folder_id = find_or_create_drive_folder(drive, folder, parent_folder_id)
        for file in files:
            file_path = os.path.join(root, file)
            gfile = drive.CreateFile({'title': file, 'parents': [{'id': parent_folder_id}]})
            gfile.SetContentFile(file_path)
            gfile.Upload()

def backup_to_external_source(folder_path, url):
    """Backup files to an external source."""
    for root, dirs, files in tqdm(os.walk(folder_path), desc="Backing up to External Source"):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                requests.post(url, files={'file': f})

def backup_to_local_storage(folder_path):
    """Backup files to local storage."""
    base_folder_name = os.path.basename(os.path.normpath(folder_path))
    backup_folder = os.path.expanduser(f'~/backup/{base_folder_name}_backup')
    os.makedirs(backup_folder, exist_ok=True)

    for root, dirs, files in tqdm(os.walk(folder_path), desc="Backing up to Local Storage"):
        rel_path = os.path.relpath(root, folder_path)
        dest_dir = os.path.join(backup_folder, rel_path)
        os.makedirs(dest_dir, exist_ok=True)
        for file in files:
            shutil.copy2(os.path.join(root, file), dest_dir)

def log_backup_details():
    """Log backup details."""
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(os.path.join(LOG_DIR, 'backup_log.txt'), 'a') as log_file:
        log_file.write(f'Backup completed at {datetime.now()}\n')

def main():
    folder_path = input("Enter the folder path to backup: ")
    confirmation = input("Are you sure you want to backup this folder? (yes/no): ")

    if confirmation.lower() != 'yes':
        print("Backup cancelled.")
        return

    if EXT_SOURCE:
        print(f"Backing up to external source: {EXT_SOURCE}")
        backup_to_external_source(folder_path, EXT_SOURCE)
    else:
        print("Backing up to Google Drive")
        drive = authenticate_google_drive()
        backup_to_google_drive(drive, folder_path)

    log_backup_details()
    print("Backup completed.")
    

def backup_to_external_source(folder_path, url):
    """Backup files to an external source."""
    for root, dirs, files in tqdm(os.walk(folder_path), desc="Backing up to External Source"):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                requests.post(url, files={'file': f})

def backup_to_local_storage(folder_path):
    """Backup files to local storage."""
    base_folder_name = os.path.basename(os.path.normpath(folder_path))
    backup_folder = os.path.expanduser(f'~/backup/{base_folder_name}_backup')
    os.makedirs(backup_folder, exist_ok=True)

    for root, dirs, files in tqdm(os.walk(folder_path), desc="Backing up to Local Storage"):
        rel_path = os.path.relpath(root, folder_path)
        dest_dir = os.path.join(backup_folder, rel_path)
        os.makedirs(dest_dir, exist_ok=True)
        for file in files:
            shutil.copy2(os.path.join(root, file), dest_dir)

def log_backup_details():
    """Log backup details."""
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(os.path.join(LOG_DIR, 'backup_log.txt'), 'a') as log_file:
        log_file.write(f'Backup completed at {datetime.now()}\n')

def main():
    folder_path = input("Enter the folder path to backup: ")
    confirmation = input("Are you sure you want to backup this folder? (yes/no): ")

    if confirmation.lower() != 'yes':
        print("Backup cancelled.")
        return

    if EXT_SOURCE:
        print(f"Backing up to external source: {EXT_SOURCE}")
        backup_to_external_source(folder_path, EXT_SOURCE)
    else:
        print("Backing up to Google Drive")
        drive = authenticate_google_drive()
        backup_to_google_drive(drive, folder_path)

    log_backup_details()
    print("Backup completed.")

if __name__ == "__main__":

