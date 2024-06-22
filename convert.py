import click
from moviepy.editor import *


@click.command()
@click.argument('filepath')
def convert_video_to_mp3(filepath):
  videoclip = VideoFileClip(filepath)
  audioclip = videoclip.audio
  audioclip.write_audiofile("converted_output.mp3")

  audioclip.close()
  videoclip.close()

def main():
  convert_video_to_mp3()

if __name__ == '__main__':
  main()

