import configparser
from utils import create_input_files

config = configparser.ConfigParser()
config.read('config.ini')
currentCfg = config[config['common']['current']]

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset=currentCfg['dataset'],
                       karpathy_json_path=currentCfg['karpathy_json_path'],
                       image_folder=currentCfg['image_folder'],
                       output_folder=currentCfg['data_folder'],
                       captions_per_image=5,
                       min_word_freq=5,
                       max_len=50)
