import os, datetime, glob
from posixpath import splitext


#  this will be appended to represent the length of the change log.
length_rep_symbol = ":bread:"
month_start_symbol = ":hammer:"
# getting file length
max_repsize = 2072
block_size = 256

def get_file_profile(fname):
    """This Function to get the length of the text file"""
    size = os.path.getsize(fname)
    return max(min(int(size / block_size), max_repsize), 1)

# Date and times:
now = datetime.datetime.now()
date_str = now.strftime("%Y.%m.%d")
time_str = now.strftime("%H:%M:%S")

# Get Base file dir
logs_dir = os.path.dirname(os.path.dirname(__file__))

# User Name:
admin = "Junru Tao"

str_data = """# :hammer: ChangeLogs
> _Lastest Update on ChangeLogs:_<br>
> __Date stamp: {0}__<br>
> __Time stamp: {1}__<br>
> __Author: {2}__
---
""".format(date_str, time_str, admin)


str_data += "\n<div align=right>\n\n\
( _Note:_ \"%s\" _represent %d bytes_ )\n\n</div> \n\n" % (length_rep_symbol, block_size)

changlog_file = os.path.join(logs_dir, "ChangeLog.md")
subfolders = [f.path for f in os.scandir(logs_dir) if f.is_dir()]
month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


for d in subfolders:
    dirname = os.path.split(d)[-1]
    if not dirname.startswith('2'):
        continue
    
    log_files = []
    for infile in glob.glob(os.path.join(d, "*.md")):
        if os.path.split(infile)[-1].startswith('2'):
            log_files.append(infile)
            
    counter = 0
    
    str_data += "## {0} Change Logs: _{1}, {2}_\n\n".format(month_start_symbol,
                                                                month_list[int(dirname.split("_")[1])-1], 
                                                                dirname.split("_")[0])

    for f in log_files:
        counter += 1
        len = get_file_profile(f)
        title =  os.path.basename(os.path.splitext(f)[0])
        title = str(title).replace("_", "/")
        title = "Change_Log - Date:" + title[:-3]
        file = "./%s/%s" % (dirname, os.path.basename(f))
        str_data += "\n :bookmark_tabs: _{2:03d}_. [{0}]({1}) : ".format(title, file, counter)
        
        for i in range(len):
            str_data += length_rep_symbol
            
        str_data += "\n"
        
    str_data += "\n<br><br>\n\n"


# [ END Wrap Ending and Dump File ]
# 
#
str_data += "\n\n\n<br><br>\n\n> This `Markdown` File is generated by a changLog bot.\
 Please do not change anything in this file. The bot will rewrite this file everytime.\
The size representation is 12 units, which is %s bytes, anything larger will be the same." % max_repsize
str_data += "\n\n--------\n\n"

if changlog_file:
    with open(changlog_file, "w") as file:
        file.write(str_data)
      
# Print to allow VS Code to get it  
print(changlog_file)  
exit(0)