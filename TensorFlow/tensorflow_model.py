import tensorflow as tf
import numpy as np

data = []
labels = []


# 生成带有权重的自定义数据集
def generate_weighted_dataset(num_samples):
    global data, labels
    for _ in range(num_samples):
        num1 = np.random.randint(-200, 201)
        num2 = np.random.randint(-200, 201)
        data.append([num1, num2])

        # 计算和
        total = num1 + num2
        labels.append(total)
        # 添加和为0的数据集
        data.append((num1, -num1))
        labels.append(0)

    return np.array(data), np.array(labels)


# num_samples = 200
generate_weighted_dataset(200)

"""
# 生成训练数据集
x = np.random.randint(-100, 101, size=(100, 2))  # 生成100组随机的两个数字
y = np.sum(x, axis=1)  # 计算每组数字的和作为目标标签
"""
# 创建神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),  # 输入层，接收两个数字
    tf.keras.layers.Dense(1)  # 输出层，一个神经元
])

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(data, labels, epochs=5000, verbose=0)

# 保存模型
model.save("AdditiveTrainingModelTest.h5")
