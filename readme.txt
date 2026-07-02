v2: 2026/06/25 授業後

プロジェクト構成：
nlp_project/
|--- src/
|    |--- main.py
|    |--- preprocess_data.py
|    |--- my_library/
|         |--- load_input_data.py
|         |--- use_dictionary_1.py
|         |--- use_dictionary_2.py
|         |--- predict_polarity.py
|         |--- manage_output.py
|--- data/
|    |--- dictionary1.txt
|    |--- dictionary2.txt
|    |--- data.txt
|    |--- precessed_data.txt
|    |--- output.txt
|--- tests/
|--- logs/
|--- requirements.txt
|--- readme.md

preprocess_data.py:
  "data.txt" から "processed_data.txt" を作成する．
  ライブラリ janome を使って，文を単語ごとに分け，単語の原形も示す．
  単語の間には space ，元の単語とその原形の間には , ．
  出力の形としてーー
    朝,朝 の,の 空,空 が,が きれい,きれい で,だ 、,、 気持ち良く,気持ち良い 一,一 日,日 を,を 始め,始める られ,られる た,た 。,。

load_input_data.py:
  "processed_data.txt" を読み込んで，
  配列 sentence_arrays を返す．
  sentence_arrays[i]: i 番目の文
  sentence_arrays[i][j]: i 番目の文の j 番目の単語
  sentence_arrays[i][j][0/1]: もとの単語とその原形

use_dictionary_1.py:
  dictionary1.txt から一個目の辞書を読み込んで，参照する．
  load(path) -- 辞書を読み込む関数．
    データ構造 dictionary {単語: -1(n)/0(e)/1(p)} を返す．
  count(dic, sentence) -- 辞書を参照する関数
    -1, 0, 1 のみからなら配列を返す．辞書になかった単語はスルーされる．

use_dictionary_2.py:
  dictionary2.txt から二個目の辞書を読み込んで，参照する．
  load(path) -- 辞書を読み込む関数
  count(dic, sentence) -- 辞書を参照する関数
    -1, 0, 1 のみからなら配列を返す．

predict_polarity.py:
  辞書に参照した結果に基づいて，文の極性を推測する．
  配列 results を返す．
  results[i]: i 番目の文の極性結果

manage_output.py:
  出力を管理するモジュール．
  「文」: 極性結果 が並ぶファイル "data/output.txt" を作成する

tests/
