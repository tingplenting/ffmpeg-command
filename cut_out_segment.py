import os
import time

'''
Cut out segments in the middle of video such as commercial or theme song

segments = [('segement start', 'segment end')]
'''


start = time.time()

filename = "INPUT_FILE_NAME"
input_file = f"{filename}.mp4"
output_file = f"{filename}--output.mp4"

segments = [
    ('00:08:45', '00:13:07'),
    ('00:39:06', '00:43:55'),
    ('01:06:47', '01:11:57'),
  ]

def get_sec(time_str):
  """Get Seconds from time."""
  h, m, s = time_str.split(':')
  return int(h) * 3600 + int(m) * 60 + int(s)

def v_name(part):
  return "v" + str(int(part))

def a_name(part):
  return "a" + str(int(part))

def fc_ffmpeg_command(segments):
  sl = len(segments)

  fc = ""
  part = 0
  for seg in range(sl):
    part += 1
    seg_start = get_sec(segments[seg][0])
    seg_end = get_sec(segments[seg][1])

    seg_v = "v" + str(part)
    seg_a = "a" + str(part)

    if part == 1:
      fc += f"[0:v]trim=duration={seg_start}[{seg_v}]; [0:a]atrim=duration={seg_start}[{seg_a}];"
    else:
      fc += f"[0:v]trim=start={get_sec(segments[seg - 1][1])}:end={seg_start},setpts=PTS-STARTPTS[{seg_v}]; [0:a]atrim=start={get_sec(segments[seg - 1][1])}:end={seg_start},asetpts=PTS-STARTPTS[{seg_a}];"
      if part == 2:
        fc += f"[{v_name(int(part - 1))}][{seg_v}]concat[{seg_v + str(part)}]; [{a_name(int(part - 1))}][{seg_a}]concat=v=0:a=1[{seg_a + str(part)}];"
      else:
        fc += f"[{v_name(int(part - 1))}{int(part - 1)}]" f"[{seg_v}]concat[{seg_v + str(part)}]; [{a_name(int(part - 1))}{int(part - 1)}][{seg_a}]concat=v=0:a=1[{seg_a + str(part)}];"

    if part == sl:
      fc += f"[0:v]trim=start={seg_end},setpts=PTS-STARTPTS[{seg_v}]; [0:a]atrim=start={seg_end},asetpts=PTS-STARTPTS[{seg_a}]; [{seg_v}{part}][{seg_v}]concat[outv];[{seg_a}{part}][{seg_a}]concat=v=0:a=1[outa]"

  return fc

exf = f'ffmpeg -i {input_file} -filter_complex "{fc_ffmpeg_command(segments)}" -map [outv] -map [outa] {output_file}'

os.system(exf)

end = time.time()
print(end - start)
