import json

# 定义一个函数来解析文本行
def parse_line(line):
    # 假设链接总是在行的最后
    link_start_index = line.rfind('https')
    link = line[link_start_index:].strip()
    
    # 提取剧集名称
    name = line[:link_start_index].strip()
    
    return {
        "name": name,
        "url": link
    }

# 读取并解析文件
data = []
with open('合集.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip():  # 跳过空行
            data.append(parse_line(line))

# 转换为 JSON 格式
json_data = {"data": data}

# 将 JSON 数据写入到新的文件中
with open('share-data.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print('转换完成，JSON 数据已写入到 share-data.json 文件中。')
