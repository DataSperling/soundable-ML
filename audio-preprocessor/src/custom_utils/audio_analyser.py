class AudioAnalyser:

  def get_audio_file_properties(self, audio_sample):
    properties = {}
    properties.update(
      {"number_samples": audio_sample.getnframes(),
       "sample_rate": audio_sample.getframerate(),
       "number_channels": audio_sample.getnchannels(),
       "duration": (audio_sample.getnframes() / audio_sample.getframerate())}
    )
    return properties
