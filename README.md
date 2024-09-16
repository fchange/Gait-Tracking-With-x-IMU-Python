# 原项目地址 https://github.com/daehwa/Gait-Tracking-With-x-IMU-Python

# 该脚本

主要做了两件事：

## transData.py
解析目录并转换成csv
from datasets/TraningData_9_5/*.txt
to datasets/TraningData_9_5_trans/*_CalInertialAndMag.csv

## calc.py
输入csv文件，计算并打印对应的数据到图片
from datasets/TraningData_9_5_trans/*_CalInertialAndMag.csv
to 
 - calc/*_magFile.png
 - calc/*_position.png
 - calc/*_trajectory.png
 - calc/*_velocity.png



