# encoding=utf-8
# 保存 windows 10 的锁屏图片. [windows 聚焦]
import os
import shutil
import datetime
import time

# 存放 windows 10 锁屏图片的目录, 一般在这个目录下
path = "C:/Users/计算机名字/AppData/Local/Packages/Microsoft.Windows." \
       "ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"

# 将图片另存的位置.默认是图片目录下,以日期命名, 这里可以自定义
save_path = "C:/Users/计算机名字/Pictures/" + str(datetime.date.today())
if os.path.isdir(save_path) == False:
    os.mkdir(save_path)

while True:
	# 如果选择 N, 则只复制当天创建的
    select = input("是否复制全部的图片?[Y/N]")
    select = select.upper()
    if select not in ['Y', 'N']:
        print("params is error!!")
    else:
        break

if select == 'Y':
    today_start_time = 0
else:
    today_start_date = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_start_time = int(time.mktime(time.strptime(str(today_start_date), "%Y-%m-%d %H:%M:%S")))

if os.path.isdir(path) == False:
    print("File is not exits:\n {}", path)
    exit(0)

for file_name in os.listdir(path):
    file_path = path + "/" + file_name
    save_file_path = save_path +"/" + file_name + ".jpg"

    ctime = int(os.path.getctime(file_path))
    if(ctime < today_start_time):
        continue

    size = round(os.path.getsize(file_path) / 1024)
    if size < 100:
        continue

    shutil.copy(file_path, save_file_path)
    print('>', end="")

print("\nCopy File is successful")