# drs

一般的な教習所システムの予約空き状況を確認し，LINEで通知するツールです．  
[ノイマン社の自動車教習所システム](https://www.neumann.jp/product/kyosyu-sys)を対象としています．（事前にログインページ下部に`NEUMANN`の表示があるかご確認ください．）

## 詳細

* 7:00~19:00の間に予約に空きが発生した場合にLINEで通知します．
* 情報は2分半毎に更新されます．

## 依存関係のインストール

Chromeをインストール後，以下のコマンドで依存関係をインストールしてください．

```bash
pip install python-dotenv line-bot-sdk selenium chromedriver-binary==Chromeのバージョン
```

## 使い方

1. `.env`ファイルを作成し，以下の環境変数を設定してください．

  * `URL`：対象の教習所予約システムのログインページのURL
  * `ID`：対象の教習所予約システムのログインID
  * `PASS`：対象の教習所予約システムのログインパスワード
  * `LINE_CHANNEL_ACCESS_TOKEN`：LINE Developersのチャンネルアクセストークン

2. `./run.sh`を実行してください（起動可能時刻でない場合は起動できません）．nohupで実行する場合は`./run.sh nohup`とします．ログは`drs.log`に出力されます．
3. 終了する場合は，`./stop.sh`を実行してください．

## 補足

* cronを用いて定期実行することも可能です．定期実行する場合は`crontab -e`でcrontabを開き，以下のように記述してください．（パスはdrsのパスに置き換える）

  ```bash
  0 7 * * * cd /path/to/drs && ./run.sh
  10 19 * * * cd /path/to/drs && ./stop.sh
  ```

* `main.py`内にある`HEADLESS`を`False`に設定すると，Chromeのウィンドウで動作を確認できます．
* スクレイピングやアクセスの間隔を変更する場合は，常識の範囲内で行ってください．（変更によって発生する問題については一切責任を負いません．）

## ライセンス

MIT License