import os
import json

read_path = 'G:/Dataset/Object_Detection/COCO_2017/annotaions/annotations_trainval2017/annotations/instances_train2017.json'
assert os.path.exists(read_path), 'json文件不存在'

image_prefix = 'G:/Dataset/Object_Detection/COCO_2017/images/train2017'
assert os.path.exists(image_prefix), 'prefix路径不存在'

write_path = 'G:/Dataset/Object_Detection/COCO_2017/annotaions/annotations_trainval2017/annotations'
assert os.path.exists(write_path), '保存路径不存在'

read_file = open(read_path, 'r', encoding='utf-8')
json_file = json.load(read_file)

# davar格式字典
coco2davar_dict = {}

# 辅助字典
# 图像字典
image_dict = {}

for idx, element in enumerate(json_file['images']):
    image_name = element['file_name']
    image_height = element['height']
    image_width = element['width']
    image_id = element['id']

    image_path = image_prefix + '/' + image_name
    assert os.path.exists(image_path), 'image路径不存在'

    if image_id not in image_dict:
        image_dict[image_id] = image_path
        
    if image_path not in coco2davar_dict:
        coco2davar_dict[image_path] = {'width': image_width, 'height': image_height, 'image_id': image_id, 'content_ann': {'bboxes': [], 'labels':[], 'bbox_ids': []}}

# 辅助字典
# 类别字典
category_dict = {}

for idx, element in enumerate(json_file['categories']):
    category_id = element['id']
    category_name = element['name']

    if category_id not in category_dict:
        category_dict[category_id] = category_name

for idx, element in enumerate(json_file['annotations']):
    image_id = element['image_id']
    bbox = element['bbox']
    category_id = element['category_id']
    bbox_id = element['id']

    # xywh 2 x1y1x2y2
    x = bbox[0]
    y = bbox[1]
    w = bbox[2]
    h = bbox[3]

    x1 = x
    y1 = y
    x2 = x + w
    y2 = y + h

    bbox = [x1, y1, x2, y2]

    assert image_id in image_dict, 'image不存在'
    coco2davar_dict[image_dict[image_id]]['content_ann']['bboxes'].append(bbox)
    coco2davar_dict[image_dict[image_id]]['content_ann']['labels'].append([category_dict[category_id]])
    coco2davar_dict[image_dict[image_id]]['content_ann']['bbox_ids'].append(bbox_id)

with open(write_path + '/' + 'coco_dataset_2017_train_davar_format.json', 'w') as file_point:
    json.dump(coco2davar_dict, file_point)