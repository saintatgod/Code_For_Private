# encoding = utf-8
# 题目的开始都是小写数字,如 1、XXX 等
# 填空题里面的括号需要修改为英文括号
# 答案格式
# 填空题目答案写在括号里, 选择题和判断题写在题目结尾的括号里, 问答题另起一行

import docx
import os
import re


def handle(q_file):
    if os.path.isfile(q_file) == False:
        print('{} 路径不正确!!'.format(q_file))
        return False

    # 提取答案
    docxObj = docx.Document(q_file)
    results = {}
    key = ''
    index = 1
    for row in docxObj.paragraphs:
        text = row.text
        if len(text) == 0:
            continue

        # 判断是题目类型还是答案编号.题目类型用中文开头, 答案编号用阿拉伯数字编号.
        # 答案字典的eg: {题目类型:{1:AA, 2:BB CC}}
        if re.match(r"[一二三四五六七八九十]{1,}、", text) == None:
            answer_list = re.split(r"[0-9]+、", text)
            answer = re.split(r"[\s]+", answer_list[1].strip())
            results[index] = answer
            index += 1

    return results


def complide_doc(a_file, results):
    docxObj = docx.Document(a_file)
    title = ''
    answer_num = 1  # 答案的编号
    for row in docxObj.paragraphs:
        # 默认文章的头是文件名, 这里记录文件名字
        # if title == '':
        #     title = row.text
        #     continue

        # 如果题目是大写的数字开头, 则是确定题目类型的, 根据题目类型要做出不同的判断
        # if re.match(r"[一二三四五六七八九十]{1,}、", row.text) != None:
        #     print(row.text)

        # 每个具体题目的命名方式是小写数字做序号开始, 这里用正则检查每一行数字, 确认是不是问题.
        if re.match(r"[0-9]{1,}、", row.text) != None:
            replace_index = 0
            answer = results[answer_num]
            answer_num += 1
            text = row.text

            answer_len = len(answer)
            while replace_index < answer_len:
                replace_str = "( {0[" + str(replace_index) + "]} )"
                text = re.sub(r"\(\s+\)", replace_str, text, count=1)
                replace_index += 1

            # print(answer)
            row.text = text.format(answer)

        docxObj.save("C:/Users/liuke_m/Downloads/demo/卷111答案.docx")


if __name__ == '__main__':
    a_file = 'C:/Users/liuke_m/Downloads/demo/卷1.docx'
    q_file = 'C:/Users/liuke_m/Downloads/demo/卷1答案.docx'
    results = handle(q_file)
    complide_doc(a_file, results)
