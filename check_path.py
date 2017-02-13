import os
path = os.environ['Path']
paths = path.split(';')
for directory in paths:
  if not os.path.exists( directory.strip()):
    print directory





