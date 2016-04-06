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
                
                commit()
                
                print "Checkpoint complete. You have been signed up for Eldritch."
                
            else:
                print "There was a problem with one of your inputs."
        
        except:
            print "Christian made a mistake."

def commit():
    subprocess.call("""cd /home/main/notebooks/records;
                     git config --global user.email "ferko7@hotmail.com";
                     git config --global user.name "jttalks";
                     git pull""", shell=True)
    
    my_indices = [int(f) for f in os.listdir('/home/main/notebooks/records/') if '.' not in f]
    new_index = str(max(my_indices)+1)
    
    timestamp = datetime.now().ctime()
    
    my_data = pd.Series([me.real_name,
                         me.character_name,
                         me.email,
                         me.race,
                         me.house,
                         timestamp])
    
    my_data.to_csv("/home/main/notebooks/records/"+new_index,
                   index=False)
                   
    subprocess.call("""cd /home/main/eldritch-signup/records/;
                      git add *;
                      git commit -m "ADD: signup" """, shell=True)
                     
    pexpect.run('git push -u origin master', 
                cwd='/home/main/notebooks/records',
               events={'Username*':'jttalks\n', 'Password*':'jttalks1\n'})    

house_dict = {
    'cadon': 'Bearers of the Mark of Making, the artificers of House Cadon are responsible for creating the Forgelings, Zephyr, and the airships.',
    'donric': 'House Donric is made up of soldiers and bodyguards with the Mark of Sentinel, and its Blade Guild is the only standing army in Caeros.',
    'ghammara': 'Those with the Mark of Hospitality license inns and restaurants throughout Caeros and operate enclaves that offer sanctuary to fugitives and refugees.',
    'jeordo': 'The medics of House Jeordo use the Mark of Healing to mend bones and cure diseases -- for those that can afford it.',
    'kjaldar':'The banker of choice for the wealthy and powerful, House Kjaldar uses the Mark of Warding to guard strongholds and vaults containing great wealth.',
    'larenthil':'The Larenthils are masters of sea and sky, using the Mark of Storm to control the weather and operate elemental airships.',
    'micaeli':'Nothing escapes the notice of House Micaeli, whose members bear the Mark of Detection and are master investigators, researchers, and spy catchers.',
    'oraite':'Oraite carries the Mark of Passage and dominate the business of travel, operating the massive magical train called Zephyr which travels across Caeros.',
    'phaelanmyr':'Those of House Phaelanmyr bear the Mark of Shadow, and carry two faces: they are the house of entertainment, music, and art, and the house of spies and secrecy.',
    'saryn':'Bearing the Mark of Scribing, the Saryns are masters of the written word, working as mediators, translators, and mediators of the law.',
    'thagash':'The youngest house, Thagash consists of reckless prospectors and bounty hunters who use the Mark of Finding to locate deposits of Eldershards and dangerous criminals alike.',
    'vernalis':'Those of House Vernalis bear the Mark of Handling, which gives them a bond to natural creatures; their main business is breeding magical and ordinary animals.'
    }
    
marked_houses = ['Cadon',
                 'Donric',
                 'Ghammara',
                 'Jeordo',
                 'Kjaldar',
                 'Larenthil',
                 'Micaeli',
                 'Oraite',
                 'Phaelanmyr',
                 'Saryn',
                 'Thagash',
                 'Vernalis']
    
def get_info(house):
    try:
        return house_dict[house.lower()]
    except:
        print "The house you entered was not recognized."
        return
        
if __name__ == "__main__":
    ip = get_ipython()
    ip.register_magics(MyMagics)
    
    me = Character()
    
    print "Eldritch setup complete."