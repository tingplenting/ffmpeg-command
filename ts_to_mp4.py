import os
import re

def ts_to_mp4(DIRECTORY):
  for f in os.listdir(DIRECTORY):
    file, ext = os.path.splitext(f)
    if re.match(r'\.ts', ext, re.I):
      in_file = DIRECTORY+ '/' + f
      out_file = DIRECTORY + '/' + file
      ex = 'ffmpeg -i "{in_file}" -acodec copy -vcodec copy "{out_file}.mp4"'.format(in_file=in_file, out_file=out_file)
      os.system(ex)

ts_to_mp4("ts")
