# pip install librosa
import librosa


y1,sr1 = librosa.load('C:/Users/stu/Desktop/sing/I_Love_How_You_Loved_Me.wav')
y2,sr2 = librosa.load('C:/Users/stu/Desktop/sing/Ain_t_Another_Girl.wav')
y3,sr3 = librosa.load('C:/Users/stu/Desktop/sing/After_All_I_ve_Done.wav')

y1
sr1
#sr = 22050 샘플링 주파수
#mono = True 스테레오 스타일을 모노로 변환
#offset,duration = 특정 구간만 사용하고 싶을 때

mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)
mfcc3 = librosa.feature.mfcc(y=y3, sr=sr3)

# n_mfcc=20 vector가 20차원이라고 생각하면 된다. 기본값은 20 대부분 20~50정도로 두고 쓴다.

print(mfcc1.shape) # (20,number_of_frame)
print(mfcc2.shape) # (20,number_of_frame)
print(mfcc3.shape) # (20,number_of_frame)


# 분류기 Classifier
# Logistic regression, SVM, decision tree, random forest, neural networks

#pip install sklearn

from sklearn import linear_model 

logreg = linear_model.LogisticRegression()
logreg.fit(X_train, y_train)
y_test_estimated = logreg.predict(X_test)










