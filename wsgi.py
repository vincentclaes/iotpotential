#!/usr/bin/python
import os
try:

    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    execfile(virtualenv, dict(__file__=virtualenv))

except KeyError:
    print 'cannot find open shift python dir on PATH'
    pass
except IOError:
    pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
import potential001

potential001.run()


#
# Below for testing only
#
