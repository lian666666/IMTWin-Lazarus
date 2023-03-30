import os

# 重命名文件
file_path = r"C:\\IMTWin\\IMTWin.exe"
new_path = os.path.splitext(file_path)[0] + ".txt"
os.rename(file_path, new_path)

# 重新启动系统
os.system("shutdown -r -t 5")
