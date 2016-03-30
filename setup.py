import subprocess
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
import os         
from datetime import datetime
import pandas as pd
import pexpect

class Character():
    def __init__(self):
        self.character_name = None
        self.real_name = None
        self.email = None
        self.race = None
        self.house = None
        
def get_info(house):
    pass

@magics_class
class MyMagics(Magics):

    @line_magic
    def checkpoint(self, line):
        """For signup, just save name if it exists
        """
        try:
            if (me.character_name != None and
                me.real_name != None and
                me.email != None and
                me.race != None and
                me.house != None):
                
                commit(me)
                
                print "Checkpoint complete. You have been signed up for Eldritch."
                
            else:
                print "There was a problem with one of your inputs."
        
        except:
            print "Christian made a mistake."

def commit():
    subprocess.call(["""cd /home/main/notebooks/records;
                     git config --global user.email "ferko7@hotmail.com";
                     git config --global user.name   "jttalks";
                     git pull"""], shell=True)
    my_indices = [int(f) for f in os.listdir('/home/main/notebooks/records')]
    new_index = str(max(my_indices)+1)
    
    timestamp = datetime.now().ctime()
    
    my_data = pd.Series([me.real_name,
                         me.character_name,
                         me.email,
                         me.race,
                         me.house,
                         timestamp])
    
    my_data.to_csv("/home/main/eldritch-signup/records/"+new_index,
                   index=False)
                   
    subprocess.call(["cd /home/main/eldritch-signup/records/",
                     "git add "+new_index,
                     'git commit -m "ADD: signup #'+new_index+'"'], shell=True)
                     
    pexpect.run('git push -u origin master', 
                cwd='/home/main/notebooks/records',
               events={'Username*':'jttalks\n', 'Password*':'jttalks1\n'})    

if __name__ == "__main__":
    ip = get_ipython()
    ip.register_magics(MyMagics)
    
    me = Character()
    
    print "Eldritch setup complete."