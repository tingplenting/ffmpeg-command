import os

def convertvid(in_dir, out_dir):
  for f in os.listdir(in_dir):
    if f.endswith(".mp4"):
      in_file = in_dir + '/' + f
      out_file = out_dir + '/' + f
      ex = 'ffmpeg -i "{in_file}" -c:v libx264 -preset slow -profile:v high -crf 18 -coder 1 -pix_fmt yuv420p -movflags +faststart -g 30 -bf 2 -c:a aac -b:a 384k -profile:a aac_low "{out_file}"'.format(in_file=in_file, out_file=out_file)
      os.system(ex)

convertvid("input_folder", "output_folder")
