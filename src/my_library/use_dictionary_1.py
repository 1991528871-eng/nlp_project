#辞書を読み込んで単語ごとにp/n判定
def load(path):
    dic = {}
    with open(path, "r", encoding = "utf-8")as f:
        lines = f.read()
        for l in lines.split("\n"):
            word = l.split("\t")
            if len(word) > 2:
                key = word[0]
                if word[1] == "p":
                    value = 1
                elif word[1] == "n":
                    value = -1
                elif word[1] == "e":
                    value = 0
                dic[key] = value    
    return dic

def count(dic, sentence):
    result = []
    for i in range(len(sentence)):
        if sentence[i][1] in dic:
            result.append(dic[sentence[i][1]])
    return result

# sentence = [['朝', '朝'], ['の', 'の'], ['空', '空'], ['が', 'が'], ['きれい', 'きれい'], ['で', 'だ'], ['、', '、'], ['気持ち良く', '気持ち良い'], ['一', '一'], ['日', '日'], ['を', 'を'], ['始め', '始める'], ['られ', 'られる'], ['た', 'た'], ['。', '。']]
# dic = {"気持ち良い": 1,.