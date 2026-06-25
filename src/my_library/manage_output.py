def into_str(sentence):
    sen = ""
    for i in sentence:
        sen = sen + i[0]
    return sen

def output(sentences_arrays, results):
    # 結果の出力
    with open("data/output.txt", "w", encoding = "utf-8") as f:
        for i in range(len(sentences_arrays)):
            print("「" + into_str(sentences_arrays[i]) + "」:", results[i], file = f)