# time_price

#此專案為台北市房地產之預測，資料來源為實價登錄網站(https://plvr.land.moi.gov.tw/DownloadOpenData)中下載之108年第一季至110年第2季之房價資料，18萬筆資料。
![image](https://user-images.githubusercontent.com/71545529/152314389-299b144e-5b2e-4889-87fd-71cb176d6c53.png)
![image](https://user-images.githubusercontent.com/71545529/152314525-5ba50b85-4428-4486-ba6e-e11d85083590.png)


#藉由python程式price_predict.py進行資料清洗，運用lasso、決策樹回歸、隨機森林回歸等回歸演算法建模，找出最低誤差值(MAE平均絕對誤差)之演算法，可作為房價預測之用途，具有以下二益處:


#1.藉此幫助房仲業者能夠更精確服務客戶，在確定客戶欲購買之房產配置需求以及坪數、買房預算(此2條件可變相得出適合客戶之「單價元平方公尺」數值)，之後能找到合適之價位之房產，促成台灣房地產景氣適當之活絡與交易效率。


#2.進一步保護買房者，由於政府為打壓房產炒作，房地產買賣稅額近期將更改:不論持有房屋之年限，課稅之比例皆為統一標準。但難保賣房者會將課稅額度加諸於房價，反而加強炒房之不良風氣及經濟傷害之程度，此模型能幫助政府評估日後房價之合理價值。限制個別房屋之房價，保護買房者也保護台灣經濟健康。



#資料處理順序:
1.清除無法使用之欄位。
![image](https://user-images.githubusercontent.com/71545529/152314938-5bb250bb-cd0a-4224-a226-319d67367912.png)


2.空值處理。類別資料之空值，以眾數取代。數值資料之NA，以中位數取代。

![image](https://user-images.githubusercontent.com/71545529/152315320-38125c13-b56e-41b2-aa1e-f5ffb3097eb1.png)


![image](https://user-images.githubusercontent.com/71545529/152314681-545a696e-39eb-4373-b2e7-59b21c20ef55.png)


#建模後比較個別演算法之準確度，以隨機森林回歸(RandomForestRegressor)之誤差值為最小。

![image](https://user-images.githubusercontent.com/71545529/152315610-0061d549-4fb8-44a3-8158-971f8fb762e8.png)


#使用python進行可視化分析:
![image](https://user-images.githubusercontent.com/71545529/152315879-58ca5f59-3dcb-4d8d-be9f-e1efe2938546.png)

高估之數據為「單價元平方公尺」中最高價位者，根據房地產之經濟生態，可能原因為高價位之新建、黃金地段之高集房產賣出利潤高過其他類型之房產。因此房仲或原屋主願意以略低於市場行情之價格售出，在能與買家更輕易達成成交共識之優點下，利潤仍然可觀。 「單價元平方公尺」較低者可能發生於郊外地區大家族間親戚低價轉讓。低估之「單價元平方公尺」數值比較偏向低價位之房產，可能出現在近期地方政府準備開發商場(EX:Outlet、捷運)等郊區、工業區地段。導致以往日之資料訓練之模型低估此地區房價上漲之趨勢。



#使用Power BI進行可視化分析:

![image](https://user-images.githubusercontent.com/71545529/152316271-c5e67685-8723-4671-91da-63019229cfef.png)

![image](https://user-images.githubusercontent.com/71545529/152316492-5137702b-af0e-45f1-b90d-c7e93dec52a4.png)
![image](https://user-images.githubusercontent.com/71545529/152316562-d8da4000-c5ff-4f2e-acb5-3a1333e50b80.png)
![image](https://user-images.githubusercontent.com/71545529/152316630-05bd9758-a246-4f9b-a278-f403ca763670.png)
![image](https://user-images.githubusercontent.com/71545529/152316703-e53c7992-0386-4f37-8fb6-fbc39cbb61c3.png)
![image](https://user-images.githubusercontent.com/71545529/152316729-842721a9-12b0-44e0-a03e-becdb0b8720f.png)
![image](https://user-images.githubusercontent.com/71545529/152316784-6491828d-c6de-4d50-a605-db785a5c25ed.png)
![image](https://user-images.githubusercontent.com/71545529/152316858-3e124fb2-3b62-4d6e-b9b4-a03607be1803.png)
![image](https://user-images.githubusercontent.com/71545529/152316919-12f93950-3a80-4b61-99db-4bf941d2ba4c.png)


