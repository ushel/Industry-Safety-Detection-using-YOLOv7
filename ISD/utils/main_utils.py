import os.path
import sys
import yaml
import base64

from ISD.exception import isdException
from ISD.logger import logging

def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            logging.info("Read yaml file sucessfully")
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise isdException(e,sys) from e
    

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open("./data/" + filename, "wb") as f:
        f.write(imgdata)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return basse64.b64encode(f.read())