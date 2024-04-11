from src.custom_utils.audio_file_reader import AudioFileReader
from src.processor.spectra_processor import SpectraProcessor


class SoundableML:

  @staticmethod
  def main():
    file_dir = AudioFileReader().read_path("test_samp")
    audio_sample = SpectraProcessor().read_audio(
      file_dir,
      "XC836745-Common-Starling-Sturnus-vulgaris.wav",
      ".wav"
    )
    signal_array = SpectraProcessor().gen_signal_array(audio_sample)








SoundableML().main()
