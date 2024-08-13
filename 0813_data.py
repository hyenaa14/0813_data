import pandas as pd
data=pd.read_csv(filepath_or)

data=pd.read_csv("./data/pima-indians-diabetes.data.csv", names=header)

#데이터 전처리:Min-Max 스케일링
array=data.values
X=array[:,0:8]
Y=array[:,8]
scaler=MinMaxScaler(feature_range=(0,1))
rescaled_X=scaler.fit_transform(X)

#모델 선택 및 학습
model=LinearRegression()
model.fit(X_train, Y_train
y_pred=model.predict(X_test)


#데이터 분할
X_train, X_test, Y_train, Y_test=train_test_split(rescaled_X,Y,test=0.3)

#Y test 값 저장 및 Y 예측값 저장
df_Y_test= pd.DataFrame(Y_test)