

import tkinter as tk

# 建立主視窗
root = tk.Tk()
root.title("顯示學號")
root.geometry("200x100")

# 建立 Label 元件來顯示學號
label = tk.Label(root, text="學號：u127", font=("Arial", 16))
label.pack(pady=20)

# 啟動主迴圈
root.mainloop()
