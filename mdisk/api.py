
# Author: heimanpictures (Akkil)
# Project: Mdisk Unofficial API
# Copyrights (c) by heimanpictures (Akkil)


import requests
import re
import sys
from .exception import LinkInvalid
    
class Mdisk:
    '''
    Python mdisk api wrapper from official bot (@)
    
    all method below return dict that contain info
    '''
    
    url = "https://diskuploader.mypowerdisk.com/v1/tp/cp"
    
    def __init__(self, api_key:str):
        '''
        init mdisk
        
        Args:
            api_key (str): api key from mdisk
        '''
        self.api_key = api_key
        self.base_url = 'https://diskuploader.mypowerdisk.com/v1/tp/cp'
  
    def upload(self, link:str):
        '''
        Upload files using direct links
        
        Args:
            link (str): link from site to get streaming link
        '''
        try:
            param = {'token':self.api_key, 'link':link} 
            r = requests.post(base_url, json = param) 
            mdisk = r.json()["sharelink"]
            #response = r.json()
            #data = dict(response)
            #mdisk = data["sharelink"]
            return mdisk

        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")

    
