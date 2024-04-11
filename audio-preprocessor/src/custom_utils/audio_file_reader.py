import os
import yaml
import glob

class AudioFileReader:

  def __init__(self):
    '''
    @instance variable: available_set: data sets available for use
    '''
    self.__config_path = "src/resources/config.yml"
    self.available_set = ("test_samp", "train_samp", "val_samp")

  def read_path(self, required_set):
    '''
    @param required_set: data set required:
      test_samp = test data,
      train_samp = training data,
      val_samp = validation data
    @return: directory path to required audio set
    '''
    if not required_set in self.available_set:
      raise ValueError(f"{required_set} not in {self.available_set}")
    else:
      with open(self.__config_path, "r") as stream:
        try:
          yaml_paths = yaml.safe_load(stream)
          if required_set in yaml_paths["paths"]:
            return (yaml_paths["paths"])[required_set]
        except yaml.YAMLError as exception:
          return exception

  def list_files(self, file_dir):
    '''
    @param file_dir: source directory
    @return: list of files in file_dir
    '''
    return os.listdir(file_dir)
