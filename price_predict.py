#列出所需套件
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNetCV
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error as MSE
from sklearn.metrics import mean_absolute_error as MAE

#組合資料
s1_108 = pd.read_csv('108s1.csv', encoding='utf-8')
s1_108['年'] = 108
s1_108['季'] = 1
s1_108 = s1_108.drop(0)

s2_108 = pd.read_csv('108s2.csv', encoding='utf-8')
s2_108['年'] = 108
s2_108['季'] = 2
s2_108 = s2_108.drop(0)

s3_108 = pd.read_csv('108s3.csv', encoding='utf-8')
s3_108['年'] = 108
s3_108['季'] = 3
s3_108 = s3_108.drop(0)

s4_108 = pd.read_csv('108s4.csv', encoding='utf-8')
s4_108['年'] = 108
s4_108['季'] = 4
s4_108 = s4_108.drop(0)

s1_109 = pd.read_csv('109s1.csv', encoding='utf-8')
s1_109['年'] = 109
s1_109['季'] = 1
s1_109 = s1_109.drop(0)

s2_109 = pd.read_csv('109s2.csv', encoding='utf-8')
s2_109['年'] = 109
s2_109['季'] = 2
s2_109 = s2_109.drop(0)

s3_109 = pd.read_csv('109s3.csv', encoding='utf-8')
s3_109['年'] = 109
s3_109['季'] = 3
s3_109 = s3_109.drop(0)

s4_109 = pd.read_csv('109s4.csv', encoding='utf-8')
s4_109['年'] = 109
s4_109['季'] = 4
s4_109 = s4_109.drop(0)

s1_110 = pd.read_csv('110s1.csv', encoding='utf-8')
s1_110['年'] = 110
s1_110['季'] = 1
s1_110 = s1_110.drop(0)

s2_110 = pd.read_csv('110s2.csv', encoding='utf-8')
s2_110['年'] = 110
s2_110['季'] = 2
s2_110 = s2_110.drop(0)


data = pd.concat([s1_108, s2_108, s3_108, s4_108, s1_109, s2_109, s3_109, s4_109, s1_110, s2_110], axis=0)
data.to_csv('time_price3_2.csv', encoding='utf-8')

#讀取資料
data = pd.read_csv('time_price3_2.csv', encoding='utf-8')




#資料清洗


#清除無法使用之欄位

data = data.drop(['Unnamed: 0'], axis=1)
data = data.drop(['土地位置建物門牌'], axis=1)
data = data.drop(['非都市土地使用分區'], axis=1)
data = data.drop(['非都市土地使用編定'], axis=1)
data = data.drop(['編號'], axis=1)
data = data.drop(['備註'], axis=1)
data = data.drop(['移轉編號'], axis=1)
data = data.drop(['交易筆棟數'], axis=1)
data = data.drop(['移轉層次'], axis=1)
data = data.drop(['總樓層數'], axis=1)
data = data.drop(['主要建材'], axis=1)
data = data.drop(['建物型態'], axis=1)
data = data.drop(['主要用途'], axis=1)
data = data.drop(['車位類別'], axis=1)
data = data.drop(['總價元'], axis=1)
data = data.drop(['年'], axis=1)
data = data.drop(['季'], axis=1)
data.drop(data.loc[data['交易標的'] == '車位'].index, inplace=True)
data.drop(data.loc[data['交易標的'] == '土地'].index, inplace=True)
data = data.drop(['交易標的'], axis=1)
data['電梯'] = data['電梯'].fillna('無')

data = data.drop(['建築完成年月'], axis=1)
data = data.drop(['交易年月日'], axis=1)

# print(data)

#將剩下有少數NA之欄位組成一個list，方便處理
null = data.columns[data.isna().any()].tolist()





#製造2個空list，以便分類數值資料以及類別資料
catgory = []

number = []


#dtypes若為float64 或 int64，就是數值欄位，就併入number，否則併入catgory
for y in data.columns:
    if data[y].dtype == np.float64 or data[y].dtype == np.int64:
        number.append(y)

    else:
        catgory.append(y)



#進一步找出數值和類別兩種資料類型中，有NA之欄位
cat_null = [i for i in catgory if i in null]
number_null = [i for i in number if i in null]





#類別資料之NA，以眾數取代
for i in cat_null:
    data[i] = data[i].fillna(data[i].mode())


#數值資料之NA，以中位數取代
for i in number_null:
    data[i] = data[i].fillna(data[i].median())

#類別資料資料進行dummy處理
for i in catgory:
    dummy = pd.get_dummies(data[i])   #產生dummy的dataframe
    data = pd.concat([data, dummy], axis=1)  #將產生dummy的dataframe合併到原本的dataframe
    data = data.drop([i], axis=1)    #砍掉原本類別欄位



#製造相關係數dataframe

corr = data.corr()

print(corr)

#建模
x = data.drop(['單價元平方公尺'], axis=1)
y = data['單價元平方公尺']


# split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)



#列出多種回歸演算法，用MAE(平均絕對誤差)檢驗演算法之準確度，越小越準

algorithum = ['Ridge(alpha=1)', 'Lasso()', 'ElasticNetCV()', 'LinearRegression()', 'DecisionTreeRegressor()', 'RandomForestRegressor()']
train_MAE = []
test_MAE = []


#Ridge建模與測試
model = Ridge(alpha=1)
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
train_MAE.append(MAE(y_train, pred_train))
pred_test = model.predict(x_test)
test_MAE.append(MAE(y_test, pred_test))


#Lasso建模與測試
model = Lasso()
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
train_MAE.append(MAE(y_train, pred_train))
pred_test = model.predict(x_test)
test_MAE.append(MAE(y_test, pred_test))

#ElasticNetCV建模與測試
model = ElasticNetCV()
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
train_MAE.append(MAE(y_train, pred_train))
pred_test = model.predict(x_test)
test_MAE.append(MAE(y_test, pred_test))


#LinearRegression建模與測試
model = LinearRegression()
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
train_MAE.append(MAE(y_train, pred_train))
pred_test = model.predict(x_test)
test_MAE.append(MAE(y_test, pred_test))


#DecisionTreeRegressor建模與測試
model = DecisionTreeRegressor()
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
train_MAE.append(MAE(y_train, pred_train))
pred_test = model.predict(x_test)
test_MAE.append(MAE(y_test, pred_test))


#RandomForestRegressor建模與測試
model = RandomForestRegressor()
model.fit(x_train, y_train)

pred_train = model.predict(x_train)
train_MAE.append(MAE(y_train, pred_train))
pred_test = model.predict(x_test)
test_MAE.append(MAE(y_test, pred_test))



#將所有演算法之準確度集中成一個dataframe比較
accuracy =  pd.DataFrame({'algorithum': algorithum, 'train_MAE': train_MAE, 'test_MAE': test_MAE})
print(accuracy)


###########可見得RandomForestRegressor為MAE最小之演算法，準確度最高##################


#將test之資料集變成list
data1 = y_test.to_list()

#將test所預測之資料集變成list
data2 = pred_test
data2 = list(data2)


#合併預測與實際資料

df = pd.DataFrame({'實際之單價元平方公尺': data1,'預測之單價元平方公尺' : data2})

#以前50筆資料作圖

df = df[:50]


#繪製折線圖
plt.style.use("ggplot")               # 使用ggplot主題樣式


#畫第一條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料及線顏色 = 紅色
plt.plot(df.index, df['預測之單價元平方公尺'],c = "r")
#畫第二條線，plt.plot(x, y, c)參數分別為x軸資料、y軸資料、線顏色 = 綠色及線型式 = -.
plt.plot(df.index, df['實際之單價元平方公尺'], "g-.")

# 設定圖例，參數為標籤、位置
plt.legend(labels=["預測之單價元平方公尺", "實際之單價元平方公尺"], loc = 'best')
plt.xlabel("", fontweight = "bold")                # 設定x軸標題及粗體
plt.ylabel("元", fontweight = "bold")    # 設定y軸標題及粗體
plt.title("預測與實際單價元平方公尺", fontsize = 15, fontweight = "bold", y = 1.1)   # 設定標題、文字大小、粗體及位置
plt.xticks(rotation=45)   # 將x軸數字旋轉45度，避免文字重疊
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()





