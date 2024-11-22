
import mod_sign
import json_download
import time
import logging
import os

# Ensure the logs directory exists
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure the logging
logging.basicConfig(filename='logs/app.log', filemode='a', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

max_count = 10
Repeat_time = 300
session_refresh_time = 168 * 3600  # Refreshing every 168 hours
json_url = {
    "ZH": "https://www.simcompanies.com/api/v2/chatroom/N/",
    "EN": "https://www.simcompanies.com/api/v2/chatroom/G/",
    #"H": "https://www.simcompanies.com/api/chatroom/?chatroom=H&last_id=1000000000",
    "X": "https://www.simcompanies.com/api/v2/chatroom/X/",
}

def get_user_selection():
    # Display API options and allow user selection
    print("请选择要提取数据的API（用逗号分隔多个选项，或输入'all'选择全部）：")
    for key in json_url.keys():
        print(f"{key}: {json_url[key]}")
    user_input = input("输入你的选择: ").strip()
    if user_input.lower() == 'all':
        return list(json_url.keys())
    else:
        return [key.strip() for key in user_input.split(',') if key.strip() in json_url]

def login_with_retry(email, password, retries=3, delay=60):
    """Attempts to log in, retrying on failure."""
    attempt = 0
    while attempt < retries:
        session = mod_sign.login_sim_companies(email, password)
        if session:
            return session
        else:
            logging.warning("Login failed, retrying in %s seconds...", delay)
            time.sleep(delay)
            attempt += 1
    logging.error("Failed to create session after %s retries.", retries)
    return None

def main():
    email = '' # Replace with your email
    password = '' # Replace with your password
    
    # Get initial user selection only once
    selected_api_keys = get_user_selection()
    logging.info("User selected API keys: %s", selected_api_keys)

    session = login_with_retry(email, password)
    logging.debug('Session acquired: %s', session)
    count_number = 0
    start_time = time.time()
    
    if session:
        # while count_number < max_count:
        while True:
            logging.info('开始循环')
            print('开始循环')
            
            # Refresh session if 168 hours have passed
            if time.time() - start_time > session_refresh_time:
                logging.info("Refreshing session after 168 hours.")
                session = login_with_retry(email, password)
                start_time = time.time()
            
            for api_key in selected_api_keys:
                url = json_url[api_key]
                logging.info('Processing API key: %s with URL: %s', api_key, url)

                # Pass the api_key as the prefix to the download_json function
                json_data = json_download.download_and_append_json(session, url, api_key)
                
                # Add logic to process json_data if needed
                if json_data:
                    logging.info("数据检索成功: %s", api_key)
                    print("数据检索成功")
                else:
                    logging.warning("请求失败，1分钟后重试...")
                    print("请求失败，1分钟后重试...")
                    time.sleep(60) # 等待一分钟后重试
            
            count_number += 1
            time.sleep(Repeat_time)
    else:
        logging.error('Session creation failed with provided email and password.')

if __name__ == "__main__":
    main()
