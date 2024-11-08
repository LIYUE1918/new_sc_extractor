from zhipuai import ZhipuAI

def ai_mod(Pending_statements):
    client = ZhipuAI(api_key="")  # 请填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4",  # 请填写您要调用的模型名称
        messages=[
            {"role": "system", "content": '''
             你的任务是检测语句中的各种物品，如果没有则仅输出【无信息】不要输出其他字符
             只检测以下内容：
            名称:代号:
            SEP :re-97: 
            SAT :re-99: 
            LUX :re-96: 
            SOR :re-91: 
            JUM :re-95: 
            BFR :re-94: 
            输出示例：
            #意思：买或买/数量/Q/名称/每升或减壹Q的差价
            【buy_10_Q3_BFR_800k_+/-10k】
            输出示例（假如有的信息有所空缺则输出类似）：
            【buy_10_Q3_BFR_无_+/-10k】
            输出示例（假如有的信息有所空缺则输出类似）：
            【buy_10_Q3_BFR_无_+/-10k】
            【buy_1_Q3_SAT_无_+/-10k】
            输出示例：
            【无信息】
            除了以上给出的输出示例之外不许输出任何内容
             '''},
            {"role": "user", "content": Pending_statements}

    ],
    )
    result = response.choices[0].message
    return result

Pending_statements = '34567890876'
result = ai_mod(Pending_statements)
print(result)

# 输出结果应是，无信息