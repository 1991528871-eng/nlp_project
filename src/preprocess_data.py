from janome.tokenizer import Tokenizer
import chardet

def into_str(str_list):
    output = str_list[0][0] + "," + str_list[0][1]
    for i in range(1, len(str_list)):
        output = output + " " + str_list[i][0] + "," + str_list[i][1]
    return output

with open("data/data.txt", "r", encoding = "utf-8") as f:
#with open("data/test_data.txt", "r", encoding = "utf-8") as f:
    lines = f.read()
    t = Tokenizer()
    sentences = []
    for l in lines.split("\n"):
        # print(list(t.tokenize(l, wakati = True)))
        if l != "":
            sentences.append([ [token.surface, token.base_form] for token in t.tokenize(l) ])

with open("data/processed_data.txt", "w", encoding = "utf-8") as f:
#with open("data/processed_test_data.txt", "w", encoding = "utf-8") as f:
    for tokens in sentences:
        print(into_str(tokens), file = f)
