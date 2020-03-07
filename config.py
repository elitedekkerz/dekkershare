import os
import json

class Configuration():
    def __init__(self, path = None):
        self.Config_dir = 'configuration.txt'
        try:
            with open(self.Config_dir,'r') as f:
                self.Share_dir = json.loads(f.read())['Share_dir']
        except:
            self.Share_dir = "share"

    def Set_share_dir(self, path):
        #TODO add share dir to flask app static path
        self.Share_dir = path
    
    def Get_share_dir(self):
        return self.Share_dir

    def Save_config(self):
        with open(self.Config_dir,'w') as f:
            f.write(json.dumps({
                'Share_dir' :self.Share_dir
                })
            )
