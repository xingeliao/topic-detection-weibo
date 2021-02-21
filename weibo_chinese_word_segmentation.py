import jieba
import codecs
from itertools import chain
import re

def chinese_word_segmentation(text):

    text = str(text)
    text = text.replace("\n", "")
    text = text.replace("\r", "")
    text = text.replace(" ", "")

    weibo_stopwords = ['u3000',"u200b","d收起全文","##", "xa0",'ue627','收起全文','真的','这座', '一座', '微博', 'casabatlló','sagradafamilia', 'sagradafam','lia','微博','casamila','链接', '网页', 'casamil', 'casabatll','cia','passeigdegr', 'sagradafami']
    for i in weibo_stopwords:
        text = text.replace(i, "") # special stop words for weibo

    bcnword_dict = ['巴特罗之家','毛不易','易烊千玺','米拉之家','没有完工','未完成','未完工','圣家堂', '聖家堂', '奎尔公园', '巴特罗', '诺坎普', '格拉纳达', '加利西亚','塞维利亚']
    for a in bcnword_dict:
        jieba.suggest_freq(a, True)
    words_list = jieba.lcut(text) # tokenization

    words_without_stopwords = []
    stopwords = [ line.rstrip() for line in codecs.open(r"stopwords-master\hit_stopwords.txt","r", encoding="utf-8") ]
    stopwords2 = [ line.rstrip() for line in codecs.open(r"stopwords-master\cn_stopwords.txt","r", encoding="utf-8") ]
    stopwords3 = [ line.rstrip() for line in codecs.open(r"stopwords-master\baidu_stopwords.txt","r", encoding="utf-8") ]
    stopwords4 = [ line.rstrip() for line in codecs.open(r"stopwords-master\scu_stopwords.txt","r", encoding="utf-8") ]
    for word in words_list:
        if word not in chain(stopwords, stopwords2, stopwords3, stopwords4):
            words_without_stopwords.append(word) #quit stop words
    words_with_spaces = " ".join(words_without_stopwords)

    return words_with_spaces
