def predict(count_statistics):    # 入力形式[[bun1dic1],[bun1dic2]]
    count1 = count_statistics[0]
    count2 = count_statistics[1]
    result = 0
    for i in range (len(count1)):
        result+=count1[i]
    for i in range (len(count2)):
        result+=count2[i]/2
    return result