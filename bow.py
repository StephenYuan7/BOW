from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import math
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
word_list_total = word_list
word_list = list(set(word_list))
word_list.sort(key=word_list_total.index)
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
print('my_bow', bow_list)

# sklearn实现
vectorizer = CountVectorizer(max_features=10)
sklearn_bow = vectorizer.fit_transform(corpus)
print("sklearn_bow\n", vectorizer.get_feature_names(), '\n', sklearn_bow.toarray())


# 下面实现tfidf
# 先计算IDF
word_count_dict = {}
for key in word_list_total:
    word_count_dict[key] = word_count_dict.get(key, 0) + 1
print(word_count_dict)
word_count_idf = {}
for key in word_count_dict:
    word_count_idf[key] = math.log((len(corpus) + 1)/(word_count_dict[key] + 1)) + 1
print(word_count_idf)
print('my_tfidf:')

for x in corpus_split:
    count_dict = {}
    for key in x:
        count_dict[key] = count_dict.get(key, 0) + 1
    word_tfidf = {}
    for key in count_dict:
        word_tfidf[key] = count_dict[key] * word_count_idf[key]
    print(word_tfidf)

# 下面用sklearn实现

tf_idf_vectorizer = TfidfVectorizer(norm=None, token_pattern=r"(?u)\b\w+\b", smooth_idf=True)
tf_idf = tf_idf_vectorizer.fit_transform(corpus)
print('sklearn:\n', tf_idf_vectorizer.get_feature_names(), tf_idf.toarray())
