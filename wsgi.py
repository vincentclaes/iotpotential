#!/usr/bin/python
import os
from threading import Thread

from iotpotential.location import Location

try:
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    execfile(virtualenv, dict(__file__=virtualenv))
except (IOError, KeyError):
    pass
start = False
print 'i am in run'
l = Location()
print 'starting thread'
t = Thread(target=l.continuously_get_current_location)
t.start()
print 'thread started'
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
print 'before import'
print 'after import'


#
# Below for testing only
#
