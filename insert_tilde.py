import os
import re

dir = "tex"
pattern = r' \w \w*'

texfiles = filter(lambda x: x.endswith(".tex"), os.listdir(dir))

for path in texfiles:
    with open(dir + "/" + path, "r") as file:
        content = file.read()
    for match in re.finditer(pattern, content):
        content = content[:match.start()+2] + "~" + content[match.start()+3:]
    with open(dir + "/" + path, "w") as file:
        file.write(content)