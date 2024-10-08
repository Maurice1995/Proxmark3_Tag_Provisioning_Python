# Proxmark3 Tag Provisioning with Python (on Windows)

This Proxmark3_Tag_Provisioning_Python Script does what it's name suggests.
It is a simple TAG provisioning Script which was made for Riddle & Code Materials Solution.
In case of questions or emergency, contact the authors Lucas Schmirl (lucas_schmirl@hotmail.com) or Maurice Pannard (maurice.paannard@riddleandcode.com)

![Proxmark RDV4](https://user-images.githubusercontent.com/45564963/143783928-d8c88f55-1992-4423-ab88-0adab231d4ea.png)

## Functionalities:

- reads the UID of a TAG with Proxmark3
- appends UID to given URL
- writes the UID specific URL to a TAG
- generates a text file with all written Tag URLs + their corresponding UIDs<br /><br />

## Preliminary steps: <br />

1. &nbsp; Install proxmark3 for windows following this guide: (here's a more detailed guide: [Rfid ResearchGroup Repo](https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Installation_Instructions/Windows-Installation-Instructions.md)) <br />
   - download [ProxSpace.7z](https://github.com/Gator96100/ProxSpace/releases/download/v3.10/ProxSpace.7z) lastest release from [Gater96100 Repo](https://github.com/Gator96100/ProxSpace/releases)
   - extract the file to a location without spaces in the path
   - double click the runme64.bat (this might take up to 10 minutes)
   - after installation you'll get a Bash prompt and your home directory should become the ProxSpace >pm3< sub-directory.
   - type ```git clone https://github.com/RfidResearchGroup/proxmark3.git```
   - ```cd proxmark3```
   - ```make clean && make -j```
   - ```make install``` <br /><br />


2. &nbsp;```git clone https://github.com/Maurice1995/Proxmark3_Tag_Provisioning_Python.git``` **into the Proxspace folder** <br /><br />
3. &nbsp;Open the Proxspace folder with VS Code <br /><br />
4. &nbsp;Go through the --- SETTING SECTION --- (in the python file) and specify the following: <br />
   - paths <br />
   - comport <br />
   - url <br />
   - TAG_specific vars <br />
   - pm3 commands <br />
   - http replacement <br />
   - element positions <br /><br />
5. &nbsp;Connect the Proxmark3 <br /><br />
6. &nbsp;Run ultimate_tool_windows.py script and follow terminal output <br /><br />
7. &nbsp;After provisioning TAGS, look into /Proxspace/written_TAGS.txt (gets generated automatically) <br /><br />

## Important Note
If running this from cmd.exe paths need to be absolute.
VSCode on the other hand is also fine with relative paths.
We suggest running it with VS Code since this will work right off the bat. 

