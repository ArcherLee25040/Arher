import matplotlib.pyplot as plt

x = []
y = []

with open('lum(1).dat', 'r') as file:
    for line in file:
        data = line.strip().split()
        x.append(float(data[0]))
        y.append(float(data[1]))

plt.figure(figsize=(16, 6))  # 调整图形大小，进一步延长 x 轴
plt.plot(x, y, linestyle='-', linewidth=1)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot of X and Y')
plt.xlim(min(x) - 20, max(x) + 20)  # 调整 x 坐标轴范围，增加 20 的余量
plt.ylim(min(y), max(y))
plt.savefig('lum_dat.jpg')
plt.show()