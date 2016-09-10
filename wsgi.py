#!/usr/bin/python
import os

try:
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError, KeyError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
print 'before import'
from potential001 import app as application

print 'after import'

print 'before run'
application.run()
print 'after run'

#
# Below for testing only
#
