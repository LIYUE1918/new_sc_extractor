import json

def print_json_file(file_path):
    try:
        # 打开JSON文件
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取JSON内容
            data = json.load(file)
            # 打印JSON内容
            print(json.dumps(data, indent=4, ensure_ascii=False))
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except json.JSONDecodeError:
        print(f"文件 {file_path} 不是有效的JSON格式。")
    except Exception as e:
        print(f"发生错误: {e}")

# 使用函数打印JSON文件内容
file_path = ''
print_json_file(file_path)