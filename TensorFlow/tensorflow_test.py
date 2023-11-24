import tensorflow as tf
import numpy as np

loaded_model = tf.keras.models.load_model("AdditiveTrainingModelTest.h5")
while True:
    try:
        num1 = float(input("请输入第一个数字: "))
        num2 = float(input("请输入第二个数字: "))
        result = loaded_model.predict(np.array([[num1, num2]]))
        print(f"预测和为: {result[0][0]}")
    except ValueError:
        print("输入无效，请输入有效的数字。")
