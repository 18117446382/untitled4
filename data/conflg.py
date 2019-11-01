import os  # 配置文件

# 该语句表示获取当前文件的上一层文件夹的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
