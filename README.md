# Proxmark3 Tag Provisioning with Python (on Windows)

This Proxmark3_Tag_Provisioning_Python Script does what it's name suggests.
It is a simple TAG provisioning Script which was made for Riddle & Code Materials Solution.
In case of questions or emergency, contact the authors Lucas Schmirl (lucas_schmirl@hotmail.com) or Maurice Pannard (maurice.paannard@riddleandcode.com)

![Proxmark RDV4](https://user-images.githubusercontent.com/45564963/143783928-d8c88f55-1992-4423-ab88-0adab231d4ea.png)

## What the script does:

- reads the UID of a TAG with Proxmark3
- builds a URL from this UID
- writes the URL to a TAG
- generates a text file with all written Tag URLs + their corresponding UIDs

## Preliminary steps: <br />

1. install proxmark3 for windows following this guide: [Rfid ResearchGroup Repo](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/Windows-Installation-Instructions.md) <br />
2. copy this ultimate_tool_windows.py script into the folder : /Proxspace <br />
3. go threw the --- SETTING SECTION --- (in the python file) and specify the following: <br />
   - paths <br />
   - url <br />
   - TAG_specific vars <br />
   - pm3 commands <br />
   - http replacement <br />
   - element positions <br />
4. connect the Proxmark3 <br />
5. run ultimate_tool_windows.py script and follow terminal output <br />
6. after provisioning TAGS, look into /Proxspace/written_TAGS.txt (gets generated automatically) <br />
