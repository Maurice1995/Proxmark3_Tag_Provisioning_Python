#********************** TAG provision Script **************************#
#**********************************************************************#
#**** this script was made for Riddle & Code **************************#
#**** in case of questions or emergency contact the authors ***********#
#**** authors: Lucas Schmirl (lucas_schmirl@hotmail.com), *************#
#************* Maurice Pannard (maurice.paannard@riddleandcode.com) ***#
#**********************************************************************#


# **************** This script reads the UID of a TAG with Proxmark3, 
# **************** builds a URL from this UID and writes it to the TAG, 
# **************** aditionally a text file with all written TAGS gets generated.
#  
# steps needed: 1. install proxmark3 for windows following this guide: https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/Windows-Installation-Instructions.md
#               2. copy this ultimate_tool_windows.py script into the folder : /Proxspace
#               3. go threw the --- SETTING SECTION --- (in this script) and specify: paths, url, TAG_specific vars, pm3 commands, http replacement and element positions
#               4. connect the Proxmark3
#               5. run ultimate_tool_windows.py script and follow terminal output
#               6. after provisioning TAGS, look into /Proxspace/written_TAGS.txt (gets generated automatically)

import subprocess
import binascii
from pygame import mixer
mixer.init() # beep init

#--------------------------------- SETTING SECTION---------------------------------------#

# insert absolute path to any .wav or put it in Proxspace folder and use relative path (relative only works with VS Code)
good_sound=mixer.Sound(r"Proxmark3_Tag_Provisioning_Python/beep_sounds/good_beep_2.wav")
bad_sound=mixer.Sound(r"Proxmark3_Tag_Provisioning_Python/beep_sounds/bad_beep.wav")	

#check COM Port of Proxmark in Device Manager
com = 3

# insert path to 'runme64.bat'
programpath = 'runme64.bat'

# insert URL (to be written) # no http://
given_url = "google.com/" 

# TAG_specific vars 
given_url_len = len(given_url)
uid_char_len = 14
uid_hex_len = 7
totalURLchars = given_url_len + uid_char_len # URL +UID

double_blockWidth = 16

# pm3 commands according to reader and needed actions -> see pm3 documentation
test="hf mfu dump"
pre_command = 'hf 14a raw -sc A2'
wincom = "cd proxmark3/"+"\n"+"client/proxmark3 COM"+str(com)+"\n"

# http:// replacement
cmd0= pre_command + "05450331D1"
cmd1= pre_command + "06012D5503"

# element position commands
a= pre_command + "07"
b= pre_command + "08"
c= pre_command + "09"
d= pre_command + "0A"
e= pre_command + "0B"
f= pre_command + "0C"
g= pre_command + "0D"
h= pre_command + "0E"
i= pre_command + "0F"
j= pre_command + "10"
k= pre_command + "11"

#--------------------------------- FUNCTIONS SECTION---------------------------------------#

# -----Functions for parsing -----

# convert string
def ascii_to_hex(ascii_str):
    hex_str = binascii.hexlify(ascii_str.encode())
    return hex_str

# build string
def stringcreator(command, uid_block_START, uid_block_END):
    append=[command]
    append.append("".join(li[uid_block_START : uid_block_END]))
    final="".join(append[0:2])
    return final

# ----- FILE functions -----

# create empty text file
def check_create():
    with open('written_TAGS.txt', 'a+') as TAG_FILE:
        TAG_FILE.write('')

# write UID and finished URL to text file
def write_to_FILE(uid, url):
    with open('written_TAGS.txt', 'a') as TAG_FILE:
        TAG_FILE.write(f'{uid}, {url}\n')

# check the text file for existance of the read UID
def check_FILE(uid):
    with open('written_TAGS.txt', 'r') as TAG_FILE:
        if uid in TAG_FILE.read():
            return False
        else:
            return True


#--------------------------------- MAIN LOOP SECTION---------------------------------------#

# 1. read UID form TAG
# 2. build URL from UID
# 3. write built URL to TAG

check_create()
while 1:
#--------------------------------- 1. read UID form TAG ---------------------------------#

    print('place TAG ->')

    # open process_1
    res = subprocess.Popen(programpath,
                        stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        encoding="utf")

    # start communication_1 within process_1 (reading from tag)
    stdout, stderr = res.communicate(input=wincom+"hf mfu info\n")  

    # UID parsing
    mystring = stdout
    parts = mystring.split()

    # catch ERRORS
    if 'card select failed' in stdout:
        continue
    elif 'Failed reading card' in stdout:
        continue
    elif 'Multiple tags detected' in stdout:
        print('Multiple tags detected')
        continue
    elif 'Cmd CRC response error' in stdout:
        print('calm your tits')
        continue

    # if no errors were detected
    else: 
        #print(stdout) ###################### DEBUG: uncomment to print whole pm3 output, see error message and include exception above within another elif
        uid="".join(parts[parts.index("UID:")+1:parts.index("UID:")+1+uid_hex_len])
        print("TAG-UID: "+ uid)



#--------------------------------- 2. build URL from UID ---------------------------------#

    # erase spaces
    uid=uid.replace(" ", "")
    
    # fusion of UID and URL
    ascii_input = given_url + uid 
    print(ascii_input)
    
    # URL+UID(ascii_to_HEX) conversion
    hex_output = ascii_to_hex(ascii_input)
    x=("{0}".format(hex_output))
    x=x.replace("'", "")
    li=list(x)
       
    # create final commands
    y = 1
    z = 9
    finala=stringcreator(a,y,z)
    y = y + double_blockWidth
    finalb=stringcreator(b,z,y)
    z = z + double_blockWidth
    finalc=stringcreator(c,y,z)
    y = y + double_blockWidth
    finald=stringcreator(d,z,y)
    z = z + double_blockWidth
    finale=stringcreator(e,y,z)
    y = y + double_blockWidth
    finalf=stringcreator(f,z,y)
    z = z + double_blockWidth
    finalg=stringcreator(g,y,z)
    y = y + double_blockWidth
    finalh=stringcreator(h,z,y)
    z = z + double_blockWidth
    finali=stringcreator(i,y,z)
    y = y + double_blockWidth
    finalj=stringcreator(j,z,y)
    z = z + double_blockWidth
    finalk=stringcreator(k,y,z)


#--------------------------------- 3. write built URL to TAG ---------------------------------#

    # open process_2 
    res_2 = subprocess.Popen(programpath,
                        stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        encoding="utf")

    # start communication_2 within process_2 (writing to tag)
    # check for URL len
    if len(ascii_input) == totalURLchars:
        stdout, stderr = res_2.communicate(input=wincom+cmd0+"\n"+cmd1+"\n"+finala+"\n"+finalb+"\n"+finalc+"\n"+finald+"\n"+finale+"\n"+finalf+"\n"+finalg+"\n"+finalh+"\n"+finali+"\n"+finalj+"\n"+finalk+"\n")
        
        #check_create()
        
        if check_FILE(uid) and "Can't select card" in stdout:
            # if TAG is new and Card can't be selected
            bad_sound.play()
            print("URL could not be written: " + ascii_input)
        elif check_FILE(uid) and not "Can't select card" in stdout:
            # if TAG is new and successfully written
            good_sound.play()
            write_to_FILE(uid, ascii_input)
            print("URL successfully written: " + ascii_input)
        elif not check_FILE(uid):
            # if TAG is already known
            bad_sound.play()
            print('Tag already written and saved to file!')
        else:
            print('something is wrong with this Tag!!!')
    else:
        # if URL len is invalid
        print('invalid URL length')
    
    #print(stdout)              #### DEBUG


#-------------------------------------- END OF SCRIPT --------------------------------------#

