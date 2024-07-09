import os
from moviepy.editor import *
from pydub import AudioSegment

import click

# https://qiita.com/yukiaprogramming/items/a26836626453d5716767#%E9%96%A2%E6%95%B0%E3%81%AE%E5%AE%9F%E8%A3%85

@click.command()
@click.argument('video_path')
def extract_and_split_audio_from_video(video_path: str):
    """
    動画から音声を抽出し、指定した条件に従って音声を分割する関数

    Parameters:
    - video_path: 入力動画ファイルのパス

    Returns:
    - audio_files: 生成された分割された音声ファイルのパスのリスト
    """

    video = VideoFileClip(video_path)
    video_duration = video.duration

    output_folder = f"outputs/{video_path.split('.')[0]}"
    os.makedirs(output_folder, exist_ok=True)

    audio = video.audio
    output_audio_path = f"{output_folder}/{video_path.split('.')[0]}.wav"
    audio.write_audiofile(output_audio_path)

    audio_files = []
    seconds_to_split = 600

    if video_duration >= 900:  # 900秒 = 15分
        audio_segment = AudioSegment.from_wav(output_audio_path)

        # 切り上げにするため
        n_chunks = int((video_duration + seconds_to_split - 1) // seconds_to_split)
        # n_chunks = int(video_duration // seconds_to_split)

        for i in range(n_chunks):
            start_time = i * seconds_to_split * 1000  # pydubはミリ秒を使用するため、1000をかける
            end_time = (i+1) * seconds_to_split * 1000
            chunk = audio_segment[start_time:end_time]
            chunk_path = f"{output_folder}/{video_path.split('.')[0]}_chunk_{i+1:02d}.wav"
            chunk.export(chunk_path, format="wav")
            audio_files.append(chunk_path)

    audio.close()
    video.close()

if __name__ == '__main__':
    extract_and_split_audio_from_video()


# 使用例:
# video_path = 'path_to_your_video_file.mp4'
# output_audio_path = 'path_for_extracted_audio.wav'
# output_folder = 'path_for_audio_chunks'
# generated_files = extract_and_split_audio_from_video(video_path, output_audio_path, output_folder)
# print(generated_files)