# 导入需要使用的库
import os
import PIL.Image as Image

# 这里写的是数据的10种类型，后续将基于这些类型名保存转换后的结果
dirs_name = ['agricultural', 'airplane', 'baseballdiamond', 'beach', 'buildings', 'chaparral', 'denseresidential',
             'forest', 'freeway', 'golfcourse', 'harbor', 'intersection', 'mediumresidential', 'mobilehomepark',
             'overpass', 'parkinglot', 'river', 'runway', 'sparseresidential', 'storagetanks', 'tenniscourt']

# 创建保存结果的文件夹
for a in dirs_name:
    savepath = 'G:/Dataset/Scene_Classfication/UC_Merced_Land_Use_png/Images/{}'.format(a)
    if not os.path.exists(savepath):
        os.mkdir(savepath)

# tif格式文件所在的路径
dir = "G:/Dataset/Scene_Classfication/UC_Merced_Land_Use/Images"

# 遍历读取的所有文件
for root, dirs, files in os.walk(dir):
    for name in files:
        #判断遍历到的文件是否为tif格式，如果是tif，才进行转换操作
        if os.path.splitext(name)[1] == ".tif":
            print(name)
            #获取当前文件的文件名，例如当前文件为E458.shp，则获取的basename为E458
            basename = os.path.splitext(name)[0]
            #读取当前文件
            image = Image.open(root + '\\' + name)
            
            image_class = root.strip().split('\\')[-1]
            #把结果按照类型保存在对应的文件夹内
            image.save('G:/Dataset/Scene_Classfication/UC_Merced_Land_Use_png/Images/{}/{}.png'.format(image_class, basename))    