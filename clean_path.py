import os
path = os.environ['Path']
paths = path.split(';')
print 'Directories to remove from path:'
for directory in paths:
  if not os.path.exists( directory.strip()):
    print directory





