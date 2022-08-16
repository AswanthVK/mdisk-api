
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
  
    def upload(self, link:str, silently_fail:bool = False) -> str:
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
            return await self.__error_handler(url=link, silently_fail=silently_fail, exception=LinkInvalid)

        except ConnectionError as e:
            sys.exit(f"ERROR : {e}")

    def __error_handler(self, url:str, silently_fail:bool, exception=Exception, message="Some error occurred during converting: %s"):
        """
        If the URL is valid, return it. If it's not, return it or raise an exception, depending on the value
        of the `silently_fail` parameter
        
        :param url: The URL to be validated
        :type url: str
        :param silently_fail: If True, then if the URL is not valid, return the original URL. If False,
        raise an exception
        :type silently_fail: bool
        :param exception: The exception to raise if the URL is not valid
        :return: The url is being returned.
        """
        if silently_fail:
            return url
        else:
            raise exception(message % url)

