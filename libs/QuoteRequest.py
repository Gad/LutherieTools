#!/bin/env python

"""This file is part of LuTOOL. LuTOOL is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any later 
version.

LuTOOL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR 
PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with LuTOOL. 
If not, see <https://www.gnu.org/licenses/>. 
    
    Ce fichier fait partie de LuTOOL. LuTOOL est un logiciel libre; vous pouvez le 
redistribuer ou le modifier suivant les termes de la GNU General Public License telle 
que publiée par la Free Software Foundation; soit la version 3 de la licence, soit 
(à votre gré) toute version ultérieure.
LuTOOL est distribué dans l'espoir qu'il sera utile, mais SANS AUCUNE GARANTIE; 
sans même la garantie tacite de QUALITÉ MARCHANDE ou d'ADÉQUATION à UN BUT PARTICULIER. 
Consultez la GNU General Public License pour plus de détails.
Vous devez avoir reçu une copie de la GNU General Public License en même temps que 
LuTOOL; si ce n'est pas le cas, consultez <http://www.gnu.org/licenses>.
"""

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
        
        self.main_logger = logging.getLogger("main_logger")
        self.main_logger.debug('creating quote request')
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
            self.main_logger.error('creating quote request failed with error :{}', format(e))
            raise e
        
        

    
    def send_request(self):
        try:
            r=requests.post(url=self.URL, headers=self.headers, 
                            files=self.files, data=self.form_data)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            self.main_logger.error ("Http Error while sending file:{}".format(errh))
            return False, errh
        except requests.exceptions.ConnectionError as errc:
            self.main_logger.error ("Error Connecting while sending file:{}".format(errc))
            return False, errc
        except requests.exceptions.Timeout as errt:
            self.main_logger.error ("Timeout Error while sending file:{}".format(errt))
            return False, errt
        except requests.exceptions.RequestException as err:
            self.main_logger.error ("unknown error while sending file {}".format(err))
            return False, err
        
        
        else :
            if r.status_code > 299 or r.status_code < 200:
                self.main_logger.error ("Non 2xx code returned while sending file : {}"\
                                                                .format(r.text))
                return False, r.text
            else :
                self.main_logger.debug ("sent file to server with request result :{}"\
                                                                .format(r.text))
                return True, 

def main():
    

    #for testing purposes
    
    r=Quote_request('bigfile.txt', 'Rogér','Ràbit','RR@hole.com','fr_FR').send_request()
    print(r)

if __name__=="__main__": 
    main()
