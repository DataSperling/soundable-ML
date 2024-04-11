from src.custom_utils.audio_file_reader import AudioFileReader
from src.processor.spectra_processor import SpectraProcessor


class SoundableML:

  @staticmethod
  def main():
    file_dir = AudioFileReader().read_path("test_samp")
    file_list = AudioFileReader.list_files(file_dir)
    sig_arr = SpectraProcessor().gen_signal_array(
      file_dir,
    "XC836745-Common-Starling-Sturnus-vulgaris.wav",
    ".wav")



SoundableML().main()