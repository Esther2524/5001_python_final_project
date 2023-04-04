import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 添加标签
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# 添加按钮
button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()

# 设置窗口大小
root.geometry("300x200")

# 设置窗口标题
root.title("My GUI")

# 启动事件循环
root.mainloop()



