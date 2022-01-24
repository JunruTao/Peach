#!/usr/bin/python

import sys
import os, datetime

msg = sys.argv[1]


# Get Base file dir
logs_dir = os.path.dirname(os.path.dirname(__file__))

# Date and times:
now = datetime.datetime.now()
filename = now.strftime("%Y_%m_%d") + "_cl.md"
subdir = now.strftime("%Y_%m")
date_str = now.strftime("%Y.%m.%d")
time_str = now.strftime("%H:%M:%S")
logs_dir = os.path.join(logs_dir, subdir)
file_dir = os.path.join(logs_dir, filename)

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# User Name:
admin = "Junru Tao"

str_init = """# :hammer: ChangeLog
> __Date: {0}__<br>
> __Author: {1}__<br>
---
\n""".format(date_str, admin)

append = """### :electric_plug: `Commit` : {3}
> Time: {2} | Author: {1}
---
""".format(date_str, admin, time_str, msg)


# Running: Either Append
if os.path.exists(file_dir):
    with open(file_dir, "a+") as file:
        file.write(append)
# OR create a new file
else:
    with open(file_dir, "w+") as file:
        file.write(str_init + append)
        
print(file_dir)  
exit(0)