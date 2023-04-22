import os
import json
import cv2

box_color_dict = {'bottle':(255,182,193), 'dining table':(255,192,203), 'person':(220,20,60), 'knife':(255,240,245), 'bowl':(219,112,147),
                  'oven':(255,105,180), 'cup':(255,20,147), 'broccoli':(199,21,133), 'spoon':(218,112,214), 'carrot':(216,191,216),
                  'sink':(221,160,221), 'potted plant':(238,130,238), 'chair':(255,0,255), 'refrigerator':(139,0,139), 'banana':(128,0,128),
                  'orange':(186,85,211), 'umbrella':(148,0,211), 'handbag':(153,50,204), 'traffic light':(75,0,130), 'bicycle':(138,43,226),
                  'skateboard':(147,112,219), 'car':(123,104,238), 'truck':(106,90,205), 'toilet':(72,61,139), 'motorcycle':(230,230,250),
                  'bird':(248,248,255), 'keyboard':(0,0,255), 'book':(0,0,205), 'tv':(25,25,112), 'vase':(0,0,139),
                  'couch':(0,0,128), 'airplane':(65,105,225), 'suitcase':(100,149,237), 'giraffe':(176,196,222), 'cow':(119,136,153),
                  'boat':(112,128,144), 'bench':(30,144,255), 'sheep':(240,248,255), 'bus':(70,130,180), 'backpack':(135,206,250),
                  'train':(135,206,235), 'stop sign':(0,191,255), 'dog':(173,216,230), 'cat':(176,224,230), 'laptop':(95,158,160),
                  'tie':(240,255,255), 'elephant':(225,255,255), 'clock':(175,238,238), 'frisbee':(0,255,255), 'bear':(0,206,209), 
                  'zebra':(47,79,79), 'horse':(0,139,139), 'skis':(0,128,128), 'sports ball':(72,209,204), 'baseball glove':(32,178,170),
                  'donut':(64,224,208), 'sandwich':(127,255,170), 'cake':(0,250,154), 'surfboard':(245,255,250), 'bed':(0,255,127), 
                  'pizza':(60,179,113), 'tennis racket':(46,139,87), 'toothbrush':(240,255,240), 'remote':(144,238,144), 'apple':(152,251,152), 
                  'snowboard':(143,188,143), 'kite':(50,205,50), 'baseball bat':(0,255,0), 'fire hydrant':(34,139,34), 'mouse':(0,128,0),
                  'teddy bear':(0,100,0), 'cell phone':(127,255,0), 'scissors':(124,252,0), 'wine glass':(173,255,47),  'fork':(85,107,47), 
                  'microwave':(107,142,35), 'hot dog':(250,250,210), 'parking meter':(255,255,240), 'toaster':(255,255,224), 'hair drier':(255,255,0)}


read_path = 'G:/Dataset/Object_Detection/COCO_2017/annotaions/annotations_trainval2017/annotations/coco_dataset_2017_train_davar_format.json'
assert os.path.exists(read_path), 'json文件不存在'

write_path = 'G:/Dataset/Object_Detection/COCO_2017/images/train2017_visual'
assert os.path.exists(write_path), '保存路径不存在'

read_file = open(read_path, 'r', encoding='utf-8')
json_file = json.load(read_file)

for key in json_file:
    # 目标框
    bbox_list = json_file[key]['content_ann']['bboxes']
    # 类别
    label_list = json_file[key]['content_ann']['labels']

    # 图像高
    image_height = json_file[key]['height']
    # 图像宽
    image_width = json_file[key]['width']

    # read_image
    image = cv2.imread(key)

    for num in range(len(bbox_list)):
        box = [int(i) for i in bbox_list[num]]
        label = label_list[num][0]

        # 矩形框绘制
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), color=box_color_dict[label], thickness=2)

        # 计算标签文本的大小
        labelsize = cv2.getTextSize(label + '0', cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]

        # 矩形框上面空间不足
        if box[1] - labelsize[1] -3 < 0:
            # 根据标签文本大小进行矩形填充
            cv2.rectangle(image, (box[0], box[1] + 3), (box[0] + labelsize[0], box[1] + labelsize[1] + 3), color=box_color_dict[label], thickness=-1)

            # 标签文本绘制
            cv2.putText(image, label, (box[0], box[1] + labelsize[1] + 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness=1)
        else:
            cv2.rectangle(image, (box[0], box[1] - labelsize[1] - 3), (box[0] + labelsize[0], box[1] - 3), color=box_color_dict[label], thickness=-1)
            cv2.putText(image, label, (box[0], box[1] - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness=1)
    
    cv2.imwrite(write_path + '/' +key.split('/')[-1], image)
