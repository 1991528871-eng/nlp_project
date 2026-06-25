v2: 2026/06/25 授業中

ok preprocess_data.py:
  "data.txt" から "processed_data.txt" を作成する．
  文を単語ごとに分けて，原形に戻す（ライブラリ janome を使う）．

load_input_data.py:
  "processed_data.txt" を読み込んで，
  配列 sentence_arrays を返す．

ok use_dictionary_1.py:

ok use_dictionary_2.py: 

ok predict_polarity.py:
  count_statistics.py の結果を参照して，文の極性を参照する．
  （辞書1の結果 + 0.5 * 辞書2の結果）

manage_output.py:
  出力を管理するモジュール．

（load_input_data.py と manage_output.py は1人で担当した方がいいかもしれません．）

ユニットテストに関してまだ話し合う必要あります．

test_messege : 変更したファイルをコミットしてみる