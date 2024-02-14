import yaml


class audio_file_reader:
  yml_config = 'config.yml'


# Read appropriate file path from config
def read_resource(yml_config, audio_dataset):
  with open(yml_config, 'r') as stream:
    try:
      data = yaml.safe_load(stream)
      if audio_dataset in data['paths']:
        path = (data['paths'])[audio_dataset]
      else:
        print('audio dataset not found...')
    except yaml.YAMLError as exception:
      print(exception)
  return path


# Load appropriate audio dataset
def load_resource(path):
  read_resource('config.yml', 'test_audio')
