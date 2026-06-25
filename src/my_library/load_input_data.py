def load(path):
    sentence_arrays = []
    with open(path, "r", encoding = "utf-8") as f:
        lines = f.read()
        for l in lines.split("\n"):
            if l != "":
                sentence_arrays.append([ word_set.split(",") for word_set in l.split(" ") ])
    return sentence_arrays

# path = "data/test_data.txt"
# sentence_arrays = load("data/test_data.txt")
# print(sentence_arrays)
