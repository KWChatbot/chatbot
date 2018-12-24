# chatbot
chatbot with deep-learning

## 1. 시작하기
`django`와 `djangorestframework`, `chatterbot`의 설치가 필요합니다.(`tensorflow`, `konlpy`, `gensim` 고려 중)  
(`tensorflow`사용 시, `CUDA`가 사용가능하다면 [CUDA](https://www.tensorflow.org/install/gpu)와 `tensorflow-gpu`를 설치해도 상관없습니다.)

```
git clone https://github.com/KWChatbot/chatbot.git  
cd chatbot  
pip install django djangorestframework chatterbot
python manage.py migrate django_chatterbot
python manage.py train
python manage.py runserver  
...
```
  
## 2. 뭐하지...
Python으로 백 구현(Tensorflow)  
  
## 3. 해야함
12월까지 개발  
12월말 까지 제안서 작성  
  
## 4. 참고
[travis ci python](https://github.com/travis-ci/travis-ci/issues/9815)  
[python tf(Apache 2.0 License)](https://www.slideshare.net/healess/python-tensorflow-ai-chatbot)  
[gensim(GPL License)](https://radimrehurek.com/gensim/)  
[konlpy(LGPL License)](http://konlpy.org/ko/latest/)  
[DjangoRestFramework](https://www.django-rest-framework.org/tutorial/quickstart/)  
[Chatterbot](https://chatterbot.readthedocs.io/en/stable/)  