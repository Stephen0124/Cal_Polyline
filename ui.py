import tkinter as tk
from cal import main

def clear_entries():
    entry.delete(0, tk.END)

def start_cal():
    data = entry.get()
    k = main(data)
    output.delete('1.0', tk.END)
    output.insert('1.0', k)
    # output.config(state='normal')

root = tk.Tk()
root.title("折线长度计算器")
root.resizable(width=False, height=False)

# a部分: 界面标题
frame_a = tk.Frame(root)
frame_a.pack(pady=15)

label_title = tk.Label(frame_a, text="折线长度计算器", font=("等线", 24))
label_title.pack()

tk.Canvas(frame_a, height=2, bg="black", width=1)

# b部分: 输入框
frame_b = tk.Frame(root)
frame_b.pack(pady=15, padx=10)

# 坐标数据
coord = tk.Label(frame_b, text="坐标数据")
coord.grid(row=0, column=0, sticky=tk.W)
entry = tk.Entry(frame_b, width=50)
entry.grid(row=0, column=1)

# 输出框
a = tk.Label(frame_b, text="输出结果")
a.grid(row=1, column=0, sticky=tk.W)
output = tk.Text(frame_b, width=50, height=2, font=('Times New Roman', 10, 'bold'))
output.grid(row=1, column=1, sticky=tk.W)

# c部分: 按钮
frame_c = tk.Frame(root)
frame_c.pack(pady=15)

button_start = tk.Button(frame_c, text="开始计算", command=start_cal)
button_start.pack(side=tk.LEFT, padx=10)

button_clear = tk.Button(frame_c, text="清空输入", command=clear_entries)
button_clear.pack(side=tk.RIGHT, padx=10)

root.mainloop()