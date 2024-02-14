import errno
import os
import yaml
import wave
import numpy as np
import matplotlib.pyplot as plt


class audio_file_reader:
  yml_config = 'config.yml'


# Read appropriate file path from config
def read_resource(yml_config, training_audio):
  with open(yml_config, 'r') as stream:
    try:
      data = yaml.safe_load(stream)
      if training_audio in data['paths']:
        path = (data['paths'])[training_audio]
      else:
        print('audio dataset not found...')
    except yaml.YAMLError as exception:
      print(exception)
  return path


# Load appropriate audio dataset
def load_resource(path):
  right_chan = []
  try:
    audio = wave.open(path)
    sig_arr = np.frombuffer(audio.readframes(audio.getnframes()), dtype=np.int16)
    if audio.getnchannels() != 1:
      right_chan = sig_arr[1::2]
    else:
      right_cha = sig_arr
  except:
    raise FileNotFoundError(
      errno.ENOENT, os.strerror(errno.ENOENT), path)
  return right_chan



load_resource(read_resource('config.yml', 'test_audio'))
