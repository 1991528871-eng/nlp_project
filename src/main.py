from my_library import load_input_data as input_loader

from my_library import use_dictionary_1 as use_d1
from my_library import use_dictionary_2 as use_d2 

from my_library import predict_polarity as predictor

from my_library import manage_output as output_manager

sentence_arrays = input_loader.load("data/processed_data.txt")
#sentence_arrays = input_loader.load("data/test_data.txt")

d1 = use_d1.load("data/dictionary1.txt")
d2 = use_d2.load("data/dictionary2.txt")

results = []
for i in range(len(sentence_arrays)):
    sentence = sentence_arrays[i]
    count_statistics = [ use_d1.count(d1, sentence), use_d2.count(d2, sentence) ]
    results.append( predictor.predict(count_statistics) )

output_manager.output(sentence_arrays, results)
