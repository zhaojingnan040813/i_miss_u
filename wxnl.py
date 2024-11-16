import tkinter as tk
import random


gs = 120  # 窗口数量


# 创建窗口和标签的函数
def create_window_and_label(window, title, width, height, text, font):
    window.title(title)
    window.configure(bg="pink")
    window.geometry(f"{width}x{height}")
    label = tk.Label(window, text=text, bg="pink", font=font)
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


# 创建主窗口
root = tk.Tk()
create_window_and_label(root, " ", 200, 50, "我想你了！", ("仿宋", 18, "bold"))


# 创建第二个窗口
window2 = tk.Toplevel()
window2.title(" ")
window2.configure(bg="pink")
window2.geometry("190x40")


# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口生成位置为屏幕右上角
window2.geometry(f"+{screen_width - 190}+0")

# 在第二个窗口中创建按钮
button = tk.Button(
    window2, text="点击我关闭所有窗口", bg="lightblue", font=("仿宋", 12, "bold")
)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# 设置窗口置顶
window2.attributes("-topmost", True)


# 添加按钮点击事件
def close_all_windows():
    root.destroy()


button.config(command=close_all_windows)


# 每秒创建一个窗口
def create_windows():
    global count
    if count < gs:
        window = tk.Toplevel()
        window.title(" ")
        window.configure(bg="pink")
        window.geometry("200x50")
        x = random.randint(0, root.winfo_screenwidth() - 200)
        y = random.randint(0, root.winfo_screenheight() - 50)
        window.geometry(f"+{x}+{y}")
        label = tk.Label(
            window, text="我想你了！", bg="pink", font=("仿宋", 18, "bold")
        )
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        count += 1
        root.after(100, create_windows)


count = 0
root.after(200, create_windows)

# 运行主循环
root.mainloop()
