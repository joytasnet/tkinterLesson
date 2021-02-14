![sakuma_fortune0](https://user-images.githubusercontent.com/74003343/107876397-2325ca00-6f09-11eb-8205-74ab33379ca9.png)
![sakuma_fortune1](https://user-images.githubusercontent.com/74003343/107876402-2faa2280-6f09-11eb-85c5-6bbc61a32a78.png)
![sakuma_fortune2](https://user-images.githubusercontent.com/74003343/107876411-3fc20200-6f09-11eb-95f0-6edbfca08fd5.png)
上の画像のように誕生日を入力して占うボタンを押すと  
本人の星座とその日の運勢が表示されるプログラムを作ってください。  
運勢は4段階。存在しない日付の処理はお任せします。  
  
運勢の決定は、誕生日を数字化したもの(例えば1月7日なら107)と  
現在の日付を同じく数字化したもの(2月14日に占った場合は214)を  
合計した値を4で割ったときの余り((107+214)%4)によって行われるようにしてください。  
ただし、現在の日付が入力者の星座が含まれる期間だった場合は、上記のロジックよりも  
1段階の運勢が表示されるようにしてください(例えば凶は小吉にアップ。大吉はそのまま大吉)。  
  
なお、日付の取得は下記のようにdatetimeモジュールを用いて行えます。  
import datetime  
today=datetime.date.today().strftime("%m%d")  
このようにすると2月14日の場合は「0214」という文字列が取得されます。
