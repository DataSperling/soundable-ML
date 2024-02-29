import errno
import os
import yaml
import wave
import numpy as np


class AudioFileReader:
  yml_config = 'config.yml'


# Read appropriate file path from config.yaml
def read_path(audio_set):
  with open('../config.yml', 'r') as stream:
    try:
      data = yaml.safe_load(stream)
      if audio_set in data['paths']:
        path = (data['paths'])[audio_set]
      else:
        print('audio dataset not found...')
    except yaml.YAMLError as exception:
      print(exception)
  return path

# Compute mel
def compute_signal_array(audio_set):
  dir_path = read_path(audio_set)
  right_chan= []
  for audio_file in os.listdir(dir_path):
    if audio_file.endswith(".wav"):
      try:
        audio = wave.open("zzz")
        sig_arr = np.frombuffer(audio.readframes(audio.getnframes()), dtype=np.int16)
        if audio.getnframes() != 1:
          right_chan = sig_arr[1::2]
        else:
          right_chan = sig_arr
      except:
        raise PermissionError(
          errno.ENOENT, os.strerror(errno.ENOENT), dir_path)
  return right_chan

# Compute mel spectra
def compute_mel():
  pass

# Plot random sample of mel spectra
def sample_plot():
  pass