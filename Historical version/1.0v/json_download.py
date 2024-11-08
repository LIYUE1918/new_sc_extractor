import requests
import json
from datetime import datetime, timezone
import os,time
import urllib3
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def download_and_append_json(session, json_url, prefix):
    if session is None:
        print("Session is None, cannot download JSON.")
        return None

    response = requests.get(json_url, cookies=session, verify=False) 
    #print('Downloading from', json_url)

    # Make the request using the session
    response = requests.get(json_url, cookies=session)  
    if response.status_code == 200:
        new_json_data = response.json()
        #print("JSON data downloaded successfully")

        # Define path for saving file, ensure it ends with a slash
        save_path = ''
        filename = f"{prefix}_data.json"
        file_path = os.path.join(save_path, filename)

        # Load existing data if the file exists
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        # Use a set to track combined keys for uniqueness
        existing_keys = {(entry["sender"]["company"], entry["datetime"]) for entry in existing_data}

        # Add new entries if they are not already in the existing set
        for entry in new_json_data:
            key = (entry["sender"]["company"], entry["datetime"])
            if key not in existing_keys:
                existing_data.append(entry)
                existing_keys.add(key)

        # Write the updated data back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

        #print(f"JSON data appended and saved to {file_path}")
        print(f"{prefix}_已保存")
        print(time.strftime ('%Y-%m-%d %H:%M:%S',time. localtime (time.time ())))
        return existing_data
    else:
        print(f"Download failed, status code: {response.status_code}")
        return None