import os
import re

def convert_mp3(infolder, outfolder):
  for f in os.listdir(infolder):
    filename, ext = os.path.splitext(f)
    infile = f"{infolder}"
    outfolder = f'output'
    if re.match(r'\.mp3', ext, re.I):
      if not os.path.exists(outfolder):
        os.makedirs(outfolder)
      outfile = f"{outfolder}/{filename}.mp3"
      ex = f'ffmpeg -i "{infile}" -vn -c:a libmp3lame -y "{outfile}"'
      os.system(ex)

convert_mp3('input_folder', 'output_folder')