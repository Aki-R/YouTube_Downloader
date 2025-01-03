# YouTube ダウンロードスクリプト
このスクリプトは、YouTubeの動画をダウンロードし、以下の処理を行います：

- 動画を最高画質でダウンロード
- 動画をMP4形式に変換
- 音声を分離してMP3形式で保存

## 必要条件
このスクリプトを実行するためには、以下のソフトウェアとライブラリが必要です：

- Python 3.7以上
- yt-dlp
- ffmpeg

## 必要なPythonライブラリのインストール
以下のコマンドを使用して必要なライブラリをインストールしてください：

```bash
pip install yt-dlp ffmpeg-python
```
また、ffmpegがシステムにインストールされている必要があります。

インストール方法は[こちら](https://ffmpeg.org/download.html)を参照してください。

## 使い方
以下のコマンドでスクリプトを実行します：

```bash
python youtube_download.py --url <YouTubeの動画URL> --output-dir <出力先ディレクトリ>
```
## 引数
- --url または -i

ダウンロードしたいYouTube動画のURLを指定します。

**必須**

- --output-dir または -o

ダウンロードしたファイルの保存先ディレクトリを指定します。デフォルトは./movieです。

**任意**

## 例
動画を指定したディレクトリにダウンロード：

```bash
python youtube_download.py --url https://www.youtube.com/watch?v=example --output-dir ./downloads
```

デフォルトディレクトリにダウンロード：

```bash
python youtube_download.py --url https://www.youtube.com/watch?v=example
```

## 動作概要
yt-dlpを使用して、指定されたURLの動画を最高画質でダウンロードします（out.webmとして保存）。

ffmpegを使用して、動画をMP4形式（out.mp4）に変換します。

MP4動画から音声を分離し、MP3形式（out.mp3）で保存します。

## 注意事項
本スクリプトは、個人利用の目的でのみ使用してください。著作権を侵害する行為は法律で禁止されています。

yt-dlpやffmpegの動作に関する問題が発生した場合は、それぞれの公式ドキュメントを参照してください。

## ライセンス
このプロジェクトはMITライセンスの下で公開されています。

