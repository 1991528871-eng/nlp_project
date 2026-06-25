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
            word[1] = word[1].replace(" ", "")
            word[1] = [token.base_form for token in t.tokenize(word[1])]
            value = -1 if word[0].split("（")[0] == "ネガ" else 1
            key = ""
            i = 0
            while not(key in dic) and i < len(word[1]):
                key = key + word[1][i]
                i += 1
            dic[key] = [value]
    return dic

def count(dic, sentence):
    result = []
    for i in range(len(sentence)):
        if sentence[i][1] in dic:
            result.append(dic[sentence[i][1]][0])
    return result

#def count(dic, sentence):
    count_statistics = []
    sentence = sentence.split(" ")
    for word in sentence:
        tmp1 = 0
        if word in dic:
            tmp = dic[word]
        count_statistics.append(tmp)
    return count_statistics