import os
import os.path
import jieba

cache_path = os.path.join(os.getcwd(), "cache")
# jieba.Tokenizer.tmp_dir = cache_path
jieba.dt.tmp_dir = cache_path

sentence = "李小福是创新办主任也是云计算方面的专家"
# jieba.load_userdict("dict.txt")

seg_list = jieba.cut(sentence, cut_all=False)
print("/ ".join(seg_list))


