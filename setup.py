#!/usr/bin/env python

import os

try:
  
  import hashlib
  import uuid
  import datetime
  import pyio
  import matplotlib
  import csv
  print ("Import Libraries All Exist")
  
except ImportError:
  print ("Trying to Install required modules: haslib, csv, time, uuid, matplotlib, and sha3\n")
  
  os.system('python -m pip install hashlib')
  os.system('python -m pip install pyio')
  os.system('python -m pip install uuid')
  os.system('python -m pip install matplotlib')
  os.system('python -m pip install csv')

# -- above lines try to install requests module if not present

# -- if all went well, import required module again ( for global access)
import hashlib
import uuid
import datetime
import pyio
import matplotlib
import csv
