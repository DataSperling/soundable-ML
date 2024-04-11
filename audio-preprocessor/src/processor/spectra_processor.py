import errno
import os
import wave

import matplotlib.pyplot as plt
import numpy as np

class SpectraProcessor:

  def __init__(self):
    self.__plot_size = [20, 10]
    self.__plot_freq_range = [5000, 15000]

  def read_audio(
    self,
    file_dir,
    file_name,
    file_type
  ):
    full_path = file_dir + "/" + file_name
    try:
      audio_sample = wave.open(full_path)
      return audio_sample
    except:
      raise PermissionError(
        errno.EACCES, os.strerror(errno.EACCES), file_name)

  def gen_signal_array(self, audio_sample):
    signal_waveform = audio_sample.readframes(audio_sample.getnframes())
    sig_arr = np.frombuffer(signal_waveform, dtype=np.int16)
    if audio_sample.getnchannels != 1:
      sig_arr = sig_arr[1::2]
    return sig_arr

  def compute_mel(self, signal_array):
    time_stamps = self.gen_time_stamps(signal_array)
    plot_figure = plt.figure()
    # TODO add plot params as static iv array
    return plot_figure




  def compute_fft(self, mel_bins, signal_array):
    pass


  def compute_dft(self, mel_bins, signal_array):
    # TODO decide on algo for DFT and language
    pass

  def gen_time_stamps(self, audio_sample):
    return np.linspace(
      0,
      audio_sample.getnframes() / audio_sample.getframerate(),
      num=audio_sample.getnframes()
    )
