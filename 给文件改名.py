# 给导出的文件加上'.jpg' 后缀
import os
paths = []
dirs = []
files = []
for i, j, k in os.walk('f:\\Users\\ZhangYF\\Desktop\\win10锁屏壁纸\\新'):        # 需要处理的文件的位置
    paths.append(i)
    dirs.append(j)
    files.append(k)
# print(paths)  测试用
# print(dirs)  测试用
# print(files)  测试用
files_names = files[0]
for i in files_names:
    file_path = paths[0] + '\\' + i                                         # 需要处理的文件完整地址
    file_path_new = file_path + '.jpg'                                      # 新文件名
    os.rename(file_path, file_path_new)
print('Done')


