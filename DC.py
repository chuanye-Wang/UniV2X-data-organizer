import os
import gzip
import json

source_dir = '/data/wangchuanye/DriveE2E/data_drivee2e_expert_traj_V1/STR_DriveE2ETown04Opt_Route8_Weather21/anno'


target_dir_coop_label = os.path.expanduser('~/V2X-Seq-SPD/cooperative/label')
target_dir_infra_velodyne = os.path.expanduser('~/V2X-Seq-SPD/infrastructure-side/velodyne')
target_dir_infra_image = os.path.expanduser('~/V2X-Seq-SPD/infrastructure-side/image')
target_dir_infra_calib = os.path.expanduser('~/V2X-Seq-SPD/infrastructure-side/calib')
target_dir_infra_label = os.path.expanduser('~/V2X-Seq-SPD/infrastructure-side/label')
target_dir_maps = os.path.expanduser('~/V2X-Seq-SPD/maps')
target_dir_velodyne = os.path.expanduser('~/V2X-Seq-SPD/vehicle-side/velodyne')
target_dir_image = os.path.expanduser('~/V2X-Seq-SPD/vehicle-side/image')
target_dir_calib = os.path.expanduser('~/V2X-Seq-SPD/vehicle-side/calib')
target_dir_label = os.path.expanduser('~/V2X-Seq-SPD/vehicle-side/label')


os.makedirs(target_dir_coop_label, exist_ok=True)
os.makedirs(target_dir_infra_velodyne, exist_ok=True)
os.makedirs(target_dir_infra_image, exist_ok=True)
os.makedirs(target_dir_infra_calib, exist_ok=True)
os.makedirs(target_dir_infra_label, exist_ok=True)
os.makedirs(target_dir_maps, exist_ok=True)
os.makedirs(target_dir_velodyne, exist_ok=True)
os.makedirs(target_dir_image, exist_ok=True)
os.makedirs(target_dir_calib, exist_ok=True)
os.makedirs(target_dir_label, exist_ok=True)


# proc the json in anno dir. 
for filename in os.listdir(source_dir):
    if filename.endswith('.json.gz'):
        source_file = os.path.join(source_dir, filename)
        # open json.gz
        with gzip.open(source_file, 'rt', encoding='utf-8') as gz_file:
            data = json.load(gz_file)
        
        sensors_data = data.get('sensors', {})
        bounding_boxes_data = data.get('bounding_boxes', {})
        filtered_sensors_data = {key: value for key, value in sensors_data.items() if key != 'CAM_RS_NORTH'}
        CAM_RS_NORTH_sensors_data = {key: value for key, value in sensors_data.items() if key == 'CAM_RS_NORTH'}

        # change tails
        target_file_calib = os.path.join(target_dir_calib, filename.replace('.json.gz', '.json'))
        target_file_label = os.path.join(target_dir_label, filename.replace('.json.gz', '.json'))
        target_file_infra_calib = os.path.join(target_dir_infra_calib, filename.replace('.json.gz', '.json'))
        target_file_infra_label = os.path.join(target_dir_infra_label, filename.replace('.json.gz', '.json'))
        target_file_coop_label = os.path.join(target_dir_coop_label, filename.replace('.json.gz', '.json'))

        # write
        with open(target_file_calib, 'w', encoding='utf-8') as json_file_calib:
            json.dump(filtered_sensors_data, json_file_calib, ensure_ascii=False, indent=4)

        with open(target_file_label, 'w', encoding='utf-8') as json_file_label:
            json.dump(bounding_boxes_data, json_file_label, ensure_ascii=False, indent=4)

        with open(target_file_infra_calib, 'w', encoding='utf-8') as json_file_infra_calib:
            json.dump(CAM_RS_NORTH_sensors_data, json_file_infra_calib, ensure_ascii=False, indent=4)

        with open(target_file_infra_label, 'w', encoding='utf-8') as json_file_infra_label:
            json.dump(bounding_boxes_data, json_file_infra_label, ensure_ascii=False, indent=4)

        with open(target_file_coop_label, 'w', encoding='utf-8') as json_file_coop_label:
            json.dump(bounding_boxes_data, json_file_coop_label, ensure_ascii=False, indent=4)


        print(f"\033[32m已保存\033[0m: {target_file_calib}")
        print(f"\033[32m已保存\033[0m: {target_file_label}")
        print(f"\033[32m已保存\033[0m: {target_file_infra_calib}")
        print(f"\033[32m已保存\033[0m: {target_file_infra_label}")
        print(f"\033[32m已保存\033[0m: {target_file_coop_label}")

