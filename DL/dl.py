# -*- coding: utf-8 -*-
"""DL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oUj1v85UhF47jMUybYZffB8KkmiaTf85
"""

#パッケージのインストール
import numpy as np
import librosa
from tensorflow.keras.models import load_model
from PIL import Image
from tensorflow.keras.layers import Reshape
import pickle
import math

def predict(data_pass  : str):
  def get_mfcc(wav_path : str) -> np.ndarray:
    x, fs = librosa.load(wav_path, sr=44100)
    mfccs = librosa.feature.mfcc(x, sr=fs)
    mfccs = mfccs[1:]
    return mfccs

  MAX = 293.0886535644531
  MIN = -256.4121398925781
  def normalize(mfcc : np.ndarray) -> np.ndarray:
    return (mfcc - MIN)/(MAX - MIN)

  def resize(normalized_data : np.ndarray):
    imgdata = Image.fromarray(normalized_data)
    imgdata = imgdata.resize((512,19))
    imgdata = np.array(imgdata)
    imgdata = np.reshape(imgdata, (1, 19, 512))
    return imgdata
  
  def unpickle(file):
    # 保存されたpickleファイルを読み込み
    # 'rb'は｢読み込み専用(r)｣かつ｢バイト列(b)｣を意味する (binaryの略かもしれない)
    with open(file, 'rb') as f:
        return pickle.load(f, encoding='bytes')
  label_dict = unpickle('./label_dict_2.pkl')
  label_dict = {'BUMP OF CHICKEN': 15,
 'DREAMS COME TRUE': 0,
 'ELLEGARDEN': 18,
 'KANA-BOON': 20,
 'LiSA': 4,
 'Mr.Children': 33,
 'Mrs.GREEN APPLE': 22,
 'ONE OK ROCK': 25,
 'Oasis': 34,
 'Official髭男dism_改訂版': 23,
 'RADWIMPS': 28,
 'SEKAI NO OWARI': 3,
 'Superfly': 7,
 'T.M.Revolution': 9,
 'UNISON SQUARE GARDEN': 10,
 'YUI': 12,
 '[Alexandros]': 13,
 'back number': 29,
 'sumika': 6,
 'あいみょん': 30,
 'クリープハイプ': 11,
 'サザンオールスターズ': 17,
 'スピッツ': 5,
 'チャットモンチー': 8,
 '宇多田ヒカル': 14,
 '平井堅': 1,
 '德永英明': 32,
 '松任谷由実': 16,
 '椎名林檎': 19,
 '槇原敬之': 31,
 '水樹奈々': 21,
 '浜崎あゆみ': 24,
 '米津玄師': 26,
 '銀杏BOYZ': 27,
 '長渕剛': 2}

  #modelのファイル名を入力
  #model_name = 'practice_0.h5'
  model = load_model('./practice_0.h5')

  #mfcc変換、標準化、サイズ変換
  mfcc_data = get_mfcc(data_pass)#仮　ここに音声データのパスを入れてください
  normalized_data = normalize(mfcc_data)
  resized_data = resize(normalized_data)

  #予測
  out = model.predict(resized_data)
  
  #辞書を作る
  return_data = {}
  for i in np.argsort(-(out.flatten()))[:5]:
    for k, v in label_dict.items():
      if v == i:
        return_data[k] = math.floor(out.flatten()[i] * 100)
  
  return return_data