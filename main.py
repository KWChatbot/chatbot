import tensorflow as tf

### 한국어 자연어 처리를 위한 라이브러리 konlpy사용
### 추후 중국어 및 일본어에 대한 라이브러리 추가 필요
import konlpy

### 단어 임베딩에 사용될 word2vec
from gensim.models import word2vec

### GPU MULTIPROCESSOR COUNT 세팅 
### 좀더 넓은 MULTI GPU 지원용 코드
import os
os.environ["TF_MIN_GPU_MULTIPROCESSOR_COUNT"] = "4"
###

### CUDA의 존재유무 확인 및 없을 경우, 강제 CPU 사용
if tf.test.is_gpu_available():
  print('hello~')
else:
  tf.device('/device:CPU:0')