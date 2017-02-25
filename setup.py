from setuptools import setup

setup(name='potential001',
      version='0.0.1',
      description='proof of concept for lora protocol integration',
      author='IVI',
      author_email='example@example.com',
      url='http://potential001-iotpotential.rhcloud.com/',
      #scripts=['iotpotential/location.py'],
      install_requires=[
            'Flask==0.10.1',
            'flask-googlemaps==0.2.2',
            'requests',
            'gunicorn',
            'Jinja2',
            'Werkzeug',
            'mock',
            'nose',
            'sqlalchemy',
            'psycopg2',
            'python-dateutil'
      ],
     )
