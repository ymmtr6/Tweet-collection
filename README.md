# tweet-scraping

Twitter APIを利用して情報を取得するためのプログラム

無料で利用できるStandard search APIは、ツイート収集速度、取集可能期間に制限があるため[^1]、参考文献で用いられているツイートIDを元にした降順収集を行う。同文献によると、この手法によりNTTデータが公開しているデータとの差約15％未満で収集することができる。

## ENV

* Python3
* requests
* requests-oauthlib

## INSTALL

TwitterDeveloper登録のち、アクセストークンなどをsecret.envに記載
```
cp secret.sample.env secret.env
nano secret.env
```

* pip利用の場合
```
pip install -r requirements.txt
```

* docker利用の場合(作成中)
```
docker pull hogehoge
```

## RUN
bashで実行する場合
```
export $(cat secret.env | grep -v ^# | xargs); python3 main.py "from:kinkidaigakuPR" test.csv
```

Dockerで実行する場合(作成中)
```
docker run hogehoge "query" output.csv
```


[^1]: [大量ツイートの収集・分析を個人で手軽に実現可能にする方法の提案](https://www.ipsj.or.jp/dp/contents/publication/41/S1101-R1802.html)
[^2]: [TwitterAPIを用いたクローラー作成](https://datumstudio.jp/blog/twitterapi%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%A9%E3%83%BC%E4%BD%9C%E6%88%90)
