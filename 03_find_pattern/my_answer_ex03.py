# -*- coding: utf-8 -*-
import re
import os

# with open("README.md", "r") as f:
#   for line in f:
#     pattern = re.compile("##+")
#     result = pattern.findall(line)
    
#     # print(bool(result))

#     if bool(result) == True:
#       print(line)

def main(file_path):
    pattern = re.compile("##.*")
    matched = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            m = pattern.match(line.strip())
            if m:
                matched.append(m.group(0))
    
    print(matched)

if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__),"README.md")
    main(file_path)
  