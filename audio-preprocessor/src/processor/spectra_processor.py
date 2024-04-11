import errno
import os
import wave
import numpy as np


class SpectraProcessor:


  def gen_signal_array(
    self,
    file_dir,
    file_name,
    file_type
  ):
    full_path = file_dir + file_name
    try:
      audio = wave.open(full_path)
      sig_arr = np.frombuffer(
        audio.readframes(audio.getnframes()), dtype=np.int16)
      if audio.getnchannels() != 1:
        r_chan = sig_arr[1::2]
      else:
        r_chan = sig_arr
    except:
      raise PermissionError(
        errno.EACCES, os.strerror(errno.EACCES), file_name)
    return r_chan




  def compute_mel(self, audio_sample):
    pass


  def compute_fft(self, mel_bins, signal_array):
    pass


  def compute_dft(self, mel_bins, signal_array):
    pass