import argparse
from pytube import YouTube
from pathlib import Path
from spleeter.separator import Separator
import ffmpeg


def download_and_separate(url, output_dir):
    yt = YouTube(url)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download(output_path=output_dir, filename="out.mp4")

    path_out_dir = Path(output_dir)
    path_mp4 = path_out_dir / "out.mp4"
    path_mp3 = path_out_dir / "out.mp3"

    ffmpeg.input(str(path_mp4)).output(str(path_mp3)).run()

    separator = Separator('spleeter:2stems')
    separator.separate_to_file(str(path_mp3), str(path_out_dir), duration=1000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YouTubeの動画をダウンロードし、音声を分離します。')
    parser.add_argument('--url', '-i', type=str, help='YouTubeの動画URL')
    parser.add_argument('--output-dir', '-o', type=str, default='.', help='出力先ディレクトリ')

    args = parser.parse_args()

    download_and_separate(args.url, args.output_dir)
