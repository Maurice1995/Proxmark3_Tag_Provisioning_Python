This Proxmark3_Tag_Provisioning_Python Script does what it's name suggests.
It is a simple TAG provisioning Script which was made for Riddle & Code Materials Solution.
In case of questions or emergency, contact the authors Lucas Schmirl (lucas_schmirl@hotmail.com) or Maurice Pannard (maurice.paannard@riddleandcode.com)


This script:
  * reads the UID of a TAG with Proxmark3
  * builds a URL from this UID
  * writes the URL to a TAG
  * generates a text file with all written Tag URLs + their corresponding UIDs 
 
Preliminary steps:
               1. install proxmark3 for windows following this guide: [Rfid ResearchGroup Repo](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/Windows-Installation-Instructions.md)
               2. copy this ultimate_tool_windows.py script into the folder : /Proxspace
               3. go threw the --- SETTING SECTION --- (in the python file) and specify: paths, url, TAG_specific vars, pm3 commands, http replacement and element positions
               4. connect the Proxmark3
               5. run ultimate_tool_windows.py script and follow terminal output
               6. after provisioning TAGS, look into /Proxspace/written_TAGS.txt (gets generated automatically)
