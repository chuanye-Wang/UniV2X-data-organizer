import os
import gzip
import json

# 源目录（anno 文件夹）
source_dir = '/data/wangchuanye/DriveE2E/data_drivee2e_expert_traj_V1/STR_DriveE2ETown04Opt_Route8_Weather21/anno'

# 目标目录（calib 文件夹）
target_dir_calib = os.path.expanduser('~/V2X-Seq-SPD/vehicle-side/calib')

# 目标目录（label 文件夹）
target_dir_label = os.path.expanduser('~/V2X-Seq-SPD/vehicle-side/label')

# 确保目标目录存在，如果不存在则创建
if not os.path.exists(target_dir_calib):
    os.makedirs(target_dir_calib)
if not os.path.exists(target_dir_label):
    os.makedirs(target_dir_label)

# 遍历 anno 文件夹中的所有 .json.gz 文件
for filename in os.listdir(source_dir):
    if filename.endswith('.json.gz'):
        # 构造源文件路径
        source_file = os.path.join(source_dir, filename)

        # 打开并读取 .json.gz 文件
        with gzip.open(source_file, 'rt', encoding='utf-8') as gz_file:
            data = json.load(gz_file)
        
        # 提取 'sensors' 数据
        sensors_data = data.get('sensors', {})

        # 提取 'bounding_boxes' 数据
        bounding_boxes_data = data.get('bounding_boxes', {})

        # 构造目标文件路径，保存为 .json 文件（不带 .gz）
        target_file_calib = os.path.join(target_dir_calib, filename.replace('.json.gz', '.json'))
        target_file_label = os.path.join(target_dir_label, filename.replace('.json.gz', '.json'))

        # 保存提取的 'sensors' 数据到目标 calib 路径
        with open(target_file_calib, 'w', encoding='utf-8') as json_file_calib:
            json.dump(sensors_data, json_file_calib, ensure_ascii=False, indent=4)

        # 保存提取的 'bounding_boxes' 数据到目标 label 路径
        with open(target_file_label, 'w', encoding='utf-8') as json_file_label:
            json.dump(bounding_boxes_data, json_file_label, ensure_ascii=False, indent=4)

        print(f"已保存: {target_file_calib}")
        print(f"已保存: {target_file_label}")
