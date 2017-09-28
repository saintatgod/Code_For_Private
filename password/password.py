# conding=utf-8

import tkinter

app = tkinter.Tk()
app.title("pa")
app.geometry("600x400")
app.resizable(width=True, height=True)
font_cfg = ("Arial", 14)

tkinter.Label(app, text="测试显示", bg="green", font=font_cfg).pack()

frame = tkinter.Frame(app)

input_dic = {"网址": "uri", "用户名": "name", "备注": "desc"}
row_num = 0
for text_val, var_name in input_dic.items():
    tkinter.Label(frame, text=text_val, font=font_cfg).grid(row=row_num, column=0)
    locals()[var_name] = tkinter.StringVar
    tkinter.Entry(frame, textvariable=locals()[var_name], font=font_cfg).grid(row=row_num, column=1)
    row_num += 1

tkinter.Label(frame, text="选择生成规则:", font=font_cfg).grid(row=row_num, column=0, pady=5)
row_num += 1

check_dic = {"字母": "char_check", "数字": "num_check", "符号": "orther_check"}
for text_val, var_name in check_dic.items():
    locals()[var_name] = tkinter.IntVar
    tkinter.Checkbutton(frame, text=text_val, font=font_cfg, textvariable=locals()[var_name]).grid(row=row_num)
    row_num += 1

frame.pack(anchor='w')


def create():
    all_dict = dict(input_dic, **check_dic)
    for text_val, item_name in all_dict.items():
        locals()[item_name] = locals()[item_name].get()
        print("{}\'values is {}".format(item_name, locals()[item_name]))


tkinter.Button(app, text="create", command=create).pack()

app.mainloop()
