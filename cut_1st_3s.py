import os

def cut_3s_start(in_dir, out_dir):
  for f in os.listdir('in_dir'):
    if f.endswith(".mp4"):
      in_file = in_dir + '/' + f
      out_file = out_dir + '/' + f
      ex = 'ffmpeg -y -ss 00:00:03 -i "{in_file}" -codec copy "{out_file}"'.format(in_file=in_file, out_file=out_file)
      os.system(ex)

cut_3s_start("input_folder", "output_folder")
