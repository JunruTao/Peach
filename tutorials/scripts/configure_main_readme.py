import os, glob


# Header:
data = "# Tutorials\n"

data += """
> This section is purposed for local tutorial backup. \
Tutorials divides into several section. find the links to
those sections.

### Topic:
"""

for dir in glob.glob(".././tutorials/*"):
    name = os.path.basename(dir)
    data += "- [%s](./tutorials/%s/README.md)\n" % (name, name)


with open(".././README.md", "w+") as f:
    f.write(data)
    f.close()
    
    