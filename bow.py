corpus = ["我 来到 北京 清华大学",
          "他 来到 了 网易 杭研 大厦",
          "小明 硕士 毕业 与 中国 科学院",
          "我 爱 北京 天安门"]

word_list = []
corpus_split = []
# 分割元素
for line in corpus:
    word_list.extend(line.split())
    corpus_split.append(line.split())
# 去重
word_list_temp = word_list
word_list = list(set(word_list))
word_list.sort(key=word_list_temp.index)
print(word_list)
print(corpus_split)

bow_list = [[0 for i in range(len(word_list))] for j in range(len(corpus))]
print(bow_list)

i = 0
for x in word_list:
    j = 0
    for y in corpus_split:
        for z in y:
            if z == x:
                bow_list[j][i] = bow_list[j][i] + 1
        j = j + 1
    i = i + 1
print('final_result', bow_list)
