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

# Compute signal array for given sample
def compute_signal_array(audio_file):
  right_chan = []
  if audio_file.endswith(".wav"):
    try:
      audio = wave.open(audio_file)
      sig_arr = np.frombuffer(audio.readframes(audio.getnframes()), dtype=np.int16)
      if audio.getnchannels() != 1:
        right_chan = sig_arr[1::2]
      else:
        right_chan = sig_arr
    except:
      raise PermissionError(
        errno.EACCES, os.strerror(errno.EACCES), audio_file)
  return right_chan

# Compute time stamp array
def compute_time_stamps(audio_sample):
  return np.linspace(
    0,
    audio_sample.getnframes() / audio_sample.getframerate(),
    num=audio_sample.getnframes())

# Compute mel spectra
def compute_mel(audio_sample):
  pass

def compute_fft():
  pass

def compute_dft():
  pass

# Plot random sample of mel spectra
def sample_plot():
  pass