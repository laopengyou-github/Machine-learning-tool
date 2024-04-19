import os  
import re  
  
def rename_images(directory):  
    # 获取目录中的文件列表  
    files = os.listdir(directory)  
    # 初始化序号  
    count = 1  
    # 用于生成唯一文件名的前缀  
    prefix = 'other_'  
    # 用于存储已存在的文件名，以便检查新文件名是否唯一  
    existing_names = set(files)  
  
    # 遍历目录中的文件  
    for filename in files:  
        # 使用正则表达式匹配图片文件的扩展名  
        if re.search(r'\.(jpg|jpeg|png|gif|bmp|tiff|webp)$', filename, re.IGNORECASE):  
            # 构建新的文件名基础部分（不包含扩展名）  
            base_new_name = f'{prefix}{count:03d}'  # 使用格式化字符串和补零来生成序号  
            # 获取文件的扩展名  
            extension = os.path.splitext(filename)[1]  
            # 构建完整的新文件名  
            new_name = base_new_name + extension  
              
            # 检查新文件名是否已经存在  
            while new_name in existing_names:  
                count += 1  # 递增序号  
                base_new_name = f'{prefix}{count:03d}'  # 重新生成基础部分  
                new_name = base_new_name + extension  # 重新构建完整的新文件名  
              
            # 构建文件的完整路径  
            old_path = os.path.join(directory, filename)  
            new_path = os.path.join(directory, new_name)  
            # 重命名文件  
            os.rename(old_path, new_path)  
            print(f'Renamed {filename} to {new_name}')  
            # 更新已存在的文件名集合  
            existing_names.remove(filename)  
            existing_names.add(new_name)  
  
# 使用示例  
directory = 'D:\\Users\\LPY\\Desktop\\毕设相关\\3代码\\视觉\\数据集\\其他'  # 修改为你的图片目录路径  
rename_images(directory)

# directory = 'D:\\Users\\LPY\\Desktop\\毕设相关\\3代码\\视觉\\数据集\\其他'  # 修改为你的图片目录路径  
# rename_images(directory)