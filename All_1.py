import os
import matplotlib.pyplot as plt
import numpy as np
import datetime

# 创建一个保存图片的文件夹
save_folder = "pic"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# 获取文件夹中的所有文件名
file_folder = "file"
file_names = os.listdir(file_folder)

# 初始化空列表用于存储数据
all_x = []
all_y = []

# 遍历数据文件
for filename in file_names:
    # 构建文件路径
    filepath = os.path.join(file_folder, filename)

    # 忽略非文件的项目（比如子文件夹）
    if not os.path.isfile(filepath):
        continue

    # 读取数据文件
    with open(filepath, "r") as file:
        data = file.readlines()
        x = [float(line.split()[0]) for line in data]
        y = [float(line.split()[1]) for line in data]

    # 将数据添加到总列表中
    all_x.append(x)
    all_y.append(y)

# 创建图形和子图
fig, ax = plt.subplots()

# 取对数
for x, y in zip(all_x, all_y):
    x_log = np.log10(x)
    y_log = np.log10(y)

    # 绘制xy图
    ax.plot(x_log, y_log, label=filename)

# 设置坐标轴标签和标题
ax.set_xlabel('Σ [g/cm^2]')
ax.set_ylabel('T (K)')
ax.set_title('Log Plot of X and Y')

# 添加图例
ax.legend()

# 生成唯一的文件名，包含时间信息
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename_with_time = f"combined_plot_{current_time}.jpg"

# 保存图像为jpg格式，放在pic文件夹中
plt.savefig(os.path.join(save_folder, filename_with_time))

# 显示图像
plt.show()
