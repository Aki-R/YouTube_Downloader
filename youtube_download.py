from pytube import YouTube
import ffmpeg
from pathlib import Path
from spleeter.separator import Separator

PATH_OUTPUT = "./movie"
URL_YOUTUBE = "https://www.youtube.com/watch?v=da26TN6N7E0"

if __name__ == "__main__":
    yt = YouTube(URL_YOUTUBE)
    yt.streams.filter(file_extension='mp4').get_highest_resolution().download(output_path=PATH_OUTPUT,
                                                                              filename="out.mp4")

    path_out_dir = Path(PATH_OUTPUT)
    path_mp4 = path_out_dir / "out.mp4"
    path_mp3 = path_out_dir / "out.mp3"

    stream = ffmpeg.input(path_mp4)
    stream = ffmpeg.output(stream, str(path_mp3))
    try:
        ffmpeg.run(stream)
    except Exception as e:
        print(e)

    separator = Separator('spleeter:2stems')
    separator.separate_to_file(str(path_mp3), str(path_out_dir), duration=1000)
