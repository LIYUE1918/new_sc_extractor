import mod_sign
import json_download
import time
#Maximum number of times
max_count = True
#one round of test
Repeat_time = 300
json_url = {
    "ZH": "https://www.simcompanies.com/api/chatroom/?chatroom=N&last_id=1000000000",
    "EN": "https://www.simcompanies.com/api/chatroom/?chatroom=G&last_id=1000000000",
    #"H": "https://www.simcompanies.com/api/chatroom/?chatroom=H&last_id=1000000000",
    "X": "https://www.simcompanies.com/api/chatroom/?chatroom=X&last_id=1000000000",
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

def main():
    email = ''  # Replace with your email
    password = ''  # Replace with your password

    # Get initial user selection only once
    selected_api_keys = get_user_selection()
    session = mod_sign.login_sim_companies(email, password)
    print(f'session: {session}')
    count_number = 0

    if session:
        #while count_number < max_count:
        while max_count:
            print('开始循环')
            for api_key in selected_api_keys:
                url = json_url[api_key]
                # Pass the api_key as the prefix to the download_json function
                json_data = json_download.download_and_append_json(session, url, api_key)
                # Add logic to process json_data if needed

            count_number += 1
            time.sleep(Repeat_time)

if __name__ == "__main__":
    main()