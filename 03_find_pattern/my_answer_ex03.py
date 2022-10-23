# -*- coding: utf-8 -*-
import re

with open("README.md", "r") as f:
  for line in f:
    pattern = re.compile("##+")
    result = pattern.findall(line)
    
    # print(bool(result))

    if bool(result) == True:
      print(line)
