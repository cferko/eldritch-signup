import subprocess
import pexpect
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
import os         
from datetime import datetime
import pandas as pd, numpy as np


class Character():
    def __init__(self):
        self.character_name = None
        self.real_name = None
        self.email = None
        self.race = None
        self.house = None

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
                   
    subprocess.call("""cd /home/main/notebooks/records;
                      git add *;
                      git commit -m "ADD: signup" """, shell=True)
                     
    pexpect.run('git push -u origin master', 
                cwd='/home/main/notebooks/records',
               events={'Username*':'jttalks\n', 'Password*':'jttalks1\n'})    

house_dict = {
    'cadon': 'Bearers of the Mark of Making, the artificers of House Cadon are responsible for creating the Forgelings, Zephyr, and the airships.\n',
    'donric': 'House Donric is made up of soldiers and bodyguards with the Mark of Sentinel, and its Blade Guild is the only standing army in Caeros.\n',
    'ghammara': 'Those with the Mark of Hospitality license inns and restaurants throughout Caeros and operate enclaves that offer sanctuary to fugitives and refugees.\n',
    'jeordo': 'The medics of House Jeordo use the Mark of Healing to mend bones and cure diseases -- for those that can afford it.\n',
    'kjaldar':'The banker of choice for the wealthy and powerful, House Kjaldar uses the Mark of Warding to guard strongholds and vaults containing great wealth.\n',
    'larenthil':'The Larenthils are masters of sea and sky, using the Mark of Storm to control the weather and operate elemental airships.\n',
    'micaeli':'Nothing escapes the notice of House Micaeli, whose members bear the Mark of Detection and are master investigators, researchers, and spy catchers.\n',
    'oraite':'Oraite carries the Mark of Passage and dominate the business of travel, operating the massive magical train called Zephyr which travels across Caeros.\n',
    'phaelanmyr':'Those of House Phaelanmyr bear the Mark of Shadow, and carry two faces: they are the house of entertainment, music, and art, and the house of spies and secrecy.\n',
    'saryn':'Bearing the Mark of Scribing, the Saryns are masters of the written word, working as mediators, translators, and mediators of the law.\n',
    'thagash':'The youngest house, Thagash consists of reckless prospectors and bounty hunters who use the Mark of Finding to locate deposits of Eldershards and dangerous criminals alike.\n',
    'vernalis':'Those of House Vernalis bear the Mark of Handling, which gives them a bond to natural creatures; their main business is breeding magical and ordinary animals.\n'
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

def random_name(race, gender):
    global name_frame    
    my_frame = name_frame.copy()    
    
    try:
        if race.lower()=='nantangil':
            this_race = 'Nantangil'
        elif race.lower()=='human':
            this_race = 'Human'
        elif race.lower()=='forgeling':
            this_race = 'Forgeling'
    except:
        this_race = None
        
    try:
        if gender.lower()=="male":
            this_gender="Male"
        elif gender.lower()=='female':
            this_gender = 'Female'
            
    except:
        this_gender = None        
        
    if this_race != None:
        my_frame = my_frame[my_frame["Race"]==this_race]
    if this_gender !=None:
        my_frame = my_frame[my_frame["Gender"]==this_gender]
        
    names = my_frame["Name"].values
    
    return np.random.choice(names)

if __name__ == "__main__":
    ip = get_ipython()
    ip.register_magics(MyMagics)
    
    name_frame = pd.read_csv("names_df.csv")  
    
    me = Character()
    
    print "Eldritch setup complete."