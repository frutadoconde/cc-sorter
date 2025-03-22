# **cc-sorter**
*simple python script to automatically organize custom content into category folders based on filename keywords.*

i originally made this for myself, but figured it was good and useful enough to share. the script looks over cc filenames and sorts them into folders based on keywords that correspond to the most common cc categories (for example: a file named "(creator)demi_skirt" will be moved into the "bottoms folder). 

initially there are only categories for cas cc, but you can customize the categories and keywords by editing the config file, so it's pretty flexible and works with most cc folder setups.

this script has been tested on windows and linux, and while i have no way to test it, it should on principle work on mac.
## installation
if [python]( https://www.python.org/downloads/) is not installed yet, get the latest version; be sure to ins/tall pip and add python to path during the installation process.
download the latest version of the script in releases, extract it, then run:
```bash
pip install -r requirements.txt
```
inside the script folder[^1]. open config.yaml with a text editor, add the directory of your unsorted cc and make any other adjustments you want. then just run:
```bash
python cc-sorter.py
```
and it should be automatically done! depending on the size of your unsorted folder it could take a while: keep the command prompt open and wait for it to finish.

[^1]: open command prompt, and type `cd (path to the extracted folder)`

***note**: there is nearly no risk of data loss with this script, but if you want to be completely sure, change the directories into temporary ones and copy some sample files from your cc folder, then do a test run to check the results.*
