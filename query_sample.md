[参考(cucmberiumさん)](https://gist.github.com/cucmberium/e687e88565b6a9ca7039)

## twitterの検索術 (`search/tweets` と `search/universal`)

### 注

`search/tweets` では一週間以上前のツイートは検索できないので注意

`search/universal` は公式のConsumerKey/ConsumerSecretでないと使用できない

当方では一切の責任を負いません

#### 使いそうなクエリ群

* `"島風 かわいい"` - `島風 かわいい`が含まれるツイートの検索
* `島風 OR 天津風` - `島風`か`天津風`が含まれるツイートの検索
* `島風 -天津風` - `島風`が含まれ`天津風`が含まれないツイートの検索
* `#島風` - ハッシュタグ`島風`が含まれるツイートの検索
* `from:user` - ユーザー`user`のツイートを検索
* `to:user` - 宛先がユーザー`user`のツイートを検索
* `@user` - リプライ`@user`が含まれるツイートの検索
* `島風 since:2015-02-23` - 2015年2月23日以降の`島風`が含まれるツイートを最新から順に検索(search/tweetsでは1週間以上前のツイートは検索不可)
* `島風 until:2015-02-23` - 2015年2月23日以前の`島風`が含まれるツイートを最新から順に検索(search/tweetsでは1週間以上前のツイートは検索不可)
* `島風 :)` - `島風`が含まれ内容がポジティブなツイートの検索
* `島風 :(` - `島風`が含まれ内容がネガティブなツイートの検索
* `島風 ?` - `島風`が含まれ内容が疑問形なツイートの検索
* `島風 source:flantter` - `島風`が含まれFlantterからつぶやかれたツイートの検索
* `島風 lang:ja` - `島風`が含まれ日本語のツイートを検索(他en等)
* `島風 include:retweets` - `島風`が含まれるリツイートを含むツイートを検索
* `島風 exclude:retweets` - `島風`が含まれるリツイートを含まないツイートを検索
* `島風 exclude:nativeretweets` - `島風`が含まれるリツイートを含まないツイートを検索?
* `島風 list:user/listname` - `user`の`listname`というリスト内で`島風`が含まれるツイートを検索
* `島風 geocode:37.78115,-122.39872,1mi` - `島風`を含み、緯度、経度、範囲を指定して検索(単位はkm,mi等)
* `島風 near:me` - `島風`を含み自分に近いところにいる人間のツイートを検索 (ドキュメントに書いてない)
* `島風 near:新潟` - `島風`を含み新潟付近でつぶやかれたツイートの検索
* `島風 near:新潟 within:10km` - `島風`を含み新潟付近でつぶやかれたツイートの検索(範囲を10kmに指定、単位はkm,mi等)
* `島風 filter:links` - `島風`とリンクが含まれるツイートの検索
* `島風 filter:verified` - `島風`が含まれ認証されたアカウントからつぶやかれたツイートを検索
* `島風 filter:images` - `島風`と画像が含まれるツイートの検索
* `島風 filter:twimg` - `島風`とツイッターの画像が含まれるツイートの検索
* `島風 filter:videos` - `島風`と動画が含まれるツイートの検索
* `島風 filter:media` - `島風`とメディア(画像と動画)が含まれるツイートの検索
* `島風 filter:vine` - `島風`とVineが含まれるツイートの検索 (ドキュメントに書いてない)
* `島風 filter:news` - `島風`が含まれ、ニュースだと思われるツイートの検索 (ドキュメントに書いてない)
* `島風 filter:safe` - `島風`が含まれ、possibly_sensitiveフラグが0のツイートの検索？
* `島風 filter:periscope` - `島風`が含まれ、periscopeで配信しているツイートの検索
* `島風 filter:native_video` - `島風`が含まれ、periscope,vineまたはTwitterにアップロードされた動画の検索
* `島風 card_name:animated_gif` - `島風`が含まれ、GIFが含まれるツイートを検索 (ドキュメントに書いてない)
* `島風 min_retweets:100` - `島風`が含まれリツイートが100以上のツイートを検索 (ドキュメントに書いてない)
* `島風 min_faves:100` - `島風`が含まれお気に入りが100以上のツイートを検索 (ドキュメントに書いてない)
* `島風 min_replies:5` - `島風`が含まれリプライが5以上のツイートを検索 (ドキュメントに書いてない)

###### 備考

filter関連の検索はNOTと併用できる

###### 使用例

* `島風 filter:media exclude:retweets` - `島風`が含まれメディアが含まれるツイートの検索
* `from:user filter:images min_faves:100` - `user`の画像で100ふぁぼ以上のツイートを検索
* `島風 filter:images min_faves:100 exclude:retweets` - `島風`が含まれ100ふぁぼ以上のツイートを検索
* `島風 filter:images -filter:safe` - `島風`が含まれpossibly_sensitiveフラグが1のツイートの検索(おそらくR-18な絵が多いと思われる)

#### search/universalの軽い使い方

###### 重要なパラメータ

* `q` - 検索する文字列 (上記のクエリ使用可)
* `modules` - モジュールを指定(`status`を指定でツイートのみが流れてくる,指定しない場合はユーザーなども含まれる)
* `count` - 取得するツイート数(ツイートのみ,ユーザーなどは別で流れてくる)
* `result_type` - `search/tweets`と同じ?

###### ツイートのさかのぼり方

`since_id`や`max_id`はパラメータで指定せず,検索クエリに含める

例

`search/universal.json?q=島風 max_id:114514&modules=status`

###### CoreTweetによるサンプル

```cs

var param = new Dictionary<string, object>() { { "q", "島風 min_faves:100" }, { "count", 20 }, { "result_type", "recent" }, { "modules", "status"} };
var res = await token.SendRequestAsync(MethodType.Get, "https://api.twitter.com/1.1/search/universal.json", param);
var json = await res.Source.Content.ReadAsStringAsync();
var jsonObject = Newtonsoft.Json.Linq.JObject.Parse(json);
var modules = jsonObject["modules"].Children<Newtonsoft.Json.Linq.JObject>();

var tweets = new List<Status>();
foreach (var status in modules)
{
    foreach (Newtonsoft.Json.Linq.JProperty prop in status.Properties())
    {
        if (prop.Name == "status")
            tweets.Add(CoreBase.Convert<Status>(Newtonsoft.Json.JsonConvert.SerializeObject(status["status"]["data"])));
    }
}

```
