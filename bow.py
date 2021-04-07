corpus = ["我 来到 北京 清华大学",
          "他 来到 了 网易 杭研 大厦",
          "小明 硕士 毕业 与 中国 科学院",
          "我 爱 北京 天安门"]

word_list = []
# 分割元素
for line in corpus:
    word_list.extend(line.split())
# 去重
word_list_temp = word_list
word_list = list(set(word_list))
word_list.sort(key=word_list_temp.index)
print(word_list)
