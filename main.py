import os
import xml.etree.ElementTree as ET

'''
<xmin>64-94</xmin>
<ymin>55-3</ymin>
<xmax>87-96</xmax>
<ymax>78-7</ymax>
'''

# 定义要修改的参数值
new_width = 224
new_height = 224
new_xmin = 94
new_ymin = 3
new_xmax = 96
new_ymax = 7

# 遍历处理所有的XML文件
for i in range(1,1501):  # 假设有0.xml到1500.xml
    file_path = f"D:\\Users\\LPY\\Desktop\\毕设相关\\3代码\视觉\\数据集\红绿灯\\train\\train\\xml\\{i}.xml"
    
    # 检查文件是否存在
    if not os.path.exists(file_path):
        continue
    
    # 解析XML文件
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # 修改相应的参数值
    for size in root.iter('size'):
        size.find('width').text = str(new_width)
        size.find('height').text = str(new_height)
    
    for bndbox in root.iter('bndbox'):
        bndbox.find('xmin').text = str(int(bndbox.find('xmin').text) - new_xmin)
        bndbox.find('ymin').text = str(int(bndbox.find('ymin').text) - new_ymin)
        bndbox.find('xmax').text = str(int(bndbox.find('xmax').text) - new_xmin)
        bndbox.find('ymax').text = str(int(bndbox.find('ymax').text) - new_ymin)
    
    # 保存修改后的XML文件
    tree.write(file_path)

print("参数修改完成！")