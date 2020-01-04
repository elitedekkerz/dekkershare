import os
import json

class Configuration():
    def __init__(self, path = None):
        #TODO load settings from path
        self.Config_dir = 'configuration.txt'
        self.Share_dir = None

    def Set_share_dir(self, path):
        self.Share_dir = path
    
    def Get_share_dir(self):
        return self.Share_dir

    def Save_config(self):
        with open(self.Config_dir,'w') as f:
            f.write(json.dumps({
                'Share_dir' :self.Share_dir
                })
            )
