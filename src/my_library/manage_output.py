def into_str(sentence):
    sen = ""
    for i in sentence:
        sen = sen + i[0]
    return sen

def output_result(sentences_arrays, results):
    # 結果の出力
    with open("data/output.txt", "w", encoding = "utf-8") as f:
        for i in range(len(sentences_arrays)):
            print("「" + into_str(sentences_arrays[i]) + "」:", results[i], file = f)

def output_statistics(sentence, count_statistics):
    # 途中結果の出力
    with open("data/statistics.txt", "a", encoding = "utf-8") as f:
        print("「"+into_str(sentence)+"」:", file = f)
        print("dictionary1:", file = f)
        for sta in count_statistics[0]:
            print(sta, file = f)
        print("dictionary2:", file = f)
        for sta in count_statistics[1]:
            print(sta, file = f)
        print("\n", file = f)