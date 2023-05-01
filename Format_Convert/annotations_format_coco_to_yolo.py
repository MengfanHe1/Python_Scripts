# Chatgpt Write Python Scripts
import json
import argparse

from pycocotools.coco import COCO
from tqdm import tqdm


def convert_coco_to_yolo(coco_file, image_dir, output_file):
    # 加载COCO数据集
    coco = COCO(coco_file)

    # 加载所有图像ID
    image_ids = coco.getImgIds()

    with open(output_file, 'w') as out_file:
        for image_id in tqdm(image_ids):
            image_data = coco.loadImgs(image_id)[0]
            image_width = image_data['width']
            image_height = image_data['height']

            # 加载图像的所有标注信息
            annotations = coco.loadAnns(coco.getAnnIds(imgIds=image_data['id']))

            for ann in annotations:
                # 获取标注的类别和边界框坐标
                category_id = ann['category_id']
                bbox = ann['bbox']

                # 转换为YOLO格式
                x_center = bbox[0] + bbox[2] / 2
                y_center = bbox[1] + bbox[3] / 2
                w = bbox[2]
                h = bbox[3]

                x_center /= image_width
                y_center /= image_height
                w /= image_width
                h /= image_height

                # 输出YOLO格式的标注信息格式为：class_name x_center y_center width height
                out_file.write(f"{category_id} {x_center} {y_center} {w} {h}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert COCO dataset annotation to YOLOv5 format')
    parser.add_argument('--coco_file', type=str, help='Path to COCO annotation file')
    parser.add_argument('--image_dir', type=str, help='Path to directory containing images')
    parser.add_argument('--output_file', type=str, help='Path to output YOLO annotation file')

    args = parser.parse_args()

    convert_coco_to_yolo(args.coco_file, args.image_dir, args.output_file)