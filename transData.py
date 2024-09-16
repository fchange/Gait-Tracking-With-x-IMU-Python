import os
import pandas as pd

if __name__ == '__main__':
    # 目录 datasets/TrainData_9_5
    source_dir = 'datasets/TraningData_9_5'
    target_dir = 'datasets/TraningData_9_5_trans'
    # 检查目录是否存在
    if not os.path.exists(source_dir):
        print(f"目录 '{source_dir}' 不存在。")
        exit()

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    # 列出目录中的所有文件
    for file in os.listdir(source_dir):
        print(file)  # 直接打印文件名
        # 按照行读取数据
        data = pd.read_table(os.path.join(source_dir, file), sep=' ', header=None)
        # 头部追加index
        data.insert(0, 'index', range(len(data)))
        # 尾部追加三列0
        data = pd.concat([data, pd.DataFrame([[0, 0, 0] for _ in range(len(data))])], axis=1)
        # 打印最后一行
        print(data.iloc[-1])
        # 转存csv
        data.to_csv(os.path.join(target_dir, file.split('.')[0] + '_CalInertialAndMag.csv'), index=False, header=False)

