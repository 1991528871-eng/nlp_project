from janome.tokenizer import Tokenizer

def load(path):
    dic = {}
    t = Tokenizer()
    with open(path, "r", encoding = "utf-8") as f:
        lines = f.read()
        for l in lines.split("\n"):
            word = l.split("\t")
            if len(word) < 2:
                continue
            value = -1 if word[0].split("（")[0] == "ネガ" else 1
            word[1] = word[1].replace(" ", "")
            word[1] = [ token.base_form for token in t.tokenize(word[1]) ]
            # 活用に影響されないように，すべて原形に直す
            key = word[1][0]
            if not(key in dic):
                dic[key] = []
            dic[key].append([ word[1][1:], value ])
        # 1つ目の単語を key にして，その後続く単語列とその極性を配列にして value として登録する
    return dic

def check(key, words):
    for i in range(len(key)):
        if key[i] != words[i][1]:
            return False
    return True

def search(dic_arr, words):
    for key in dic_arr:  # 辞書にある sentence[i][1] から始まるものをすべて確認する
        if check(key[0], words):  # key[0]: 単語列, key[1]: 極性
            return key
    return None

def count(dic, sentence):
    result = []
    i = 0
    while i < len(sentence):
        if sentence[i][1] in dic:
            tmp = search(dic[sentence[i][1]], sentence[(i+1):])
            # 辞書には sentence[i][1] から始まるもの と 文の続き を比較
            if tmp != None:
                tmp[0] = [sentence[i][1]] + tmp[0]
                result.append(tmp)
                i = i + len(tmp[0])
                # 一度参照された箇所をとばす
        i = i + 1  # 次の単語に行く
    return result

#def count(dic, sentence):
#    count_statistics = []
#    sentence = sentence.split(" ")
#    for word in sentence:
#        tmp1 = 0
#        if word in dic:
#            tmp = dic[word]
#        count_statistics.append(tmp)
#    return count_statistics