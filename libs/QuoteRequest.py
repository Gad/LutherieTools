#!/bin/env python

import requests
import logging
import zlib
from base64 import urlsafe_b64encode as b64e

UPLOAD_SERVER = "devsandbox.damengo.com"
UPLOAD_PORT = "4857"
def obscure(data: bytes) -> bytes:
    return b64e(zlib.compress(data, 9))




class Quote_request():
    def __init__(self, file, sender_fname="", sender_sname="", 
                 sender_email="", sender_lang="")->None:
        
        try:
        
            self.files = {'file': open(file, 'rb'),}
            self.URL = 'http://'+UPLOAD_SERVER+':'+UPLOAD_PORT+"/uploadfile"
            print(self.URL)
            self.headers ={
                'accept' : 'application/json',
            }
            self.form_data={
                'sender_fname':obscure(str.encode(sender_fname, "utf-8")),
                'sender_sname':obscure(str.encode(sender_sname, "utf-8")),
                'sender_email':obscure(str.encode(sender_email, "utf-8")),
                'sender_lang':obscure(str.encode(sender_lang, "utf-8"))
            }
            
        except Exception as e:  
            raise e
        
        

    
    def send_request(self):
        try:
            r=requests.post(url=self.URL, headers=self.headers, 
                            files=self.files, data=self.form_data)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            logging.error ("Http Error while sending file:{}".format(errh))
            return False, errh
        except requests.exceptions.ConnectionError as errc:
            logging.error ("Error Connecting while sending file:{}".format(errc))
            return False, errc
        except requests.exceptions.Timeout as errt:
            logging.error ("Timeout Error while sending file:{}".format(errt))
            return False, errt
        except requests.exceptions.RequestException as err:
            logging.error ("unknown error while sending file {}".format(err))
            return False, err
        
        
        else :
            if r.status_code > 299 or r.status_code < 200:
                logging.error ("Non 2xx code returned while sending file : {}"\
                                                                .format(r.text))
                return False, r.text
            else :
                logging.debug ("sent file to server with request result :{}"\
                                                                .format(r.text))
                return True, 

def main():
    

    #for testing purposes
    
    r=Quote_request('bigfile.txt', 'Rogér','Ràbit','RR@hole.com','fr_FR').send_request()
    print(r)

if __name__=="__main__": 
    main()
