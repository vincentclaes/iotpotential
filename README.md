# IOT POTENTIAL

### Installation & Run

```bash
git clone git@github.com:Vinnie1986/iotpotential.git
cd Flask-GoogleMaps
python setup.py install
python setup.py develop
cd webapp
python main.py
```

Access: http://localhost:5000/ 

### usefull comands

#### get acces token

curl -i -X POST --basic -u "mKPCKnzKW4j8eVh4WaEmR3qlhwQa:uVzpRK57MizQ7aNN_0LL8M3avR4a" -H "Accept:application/json" -H "Content-Type:application/x-www-form-urlencoded" https://login.enco.io/oauth2/token -d "grant_type=password&username=vclaes1986@gmail.com&password=1saJocVin$

#### deploy to open shift

rhc app-configure potential001 --deployment-branch <branch_name>

rhc deploy <branch_name> -a potential001
# rhc deploy master -a potential001

#### build docker image

´sudo docker build -t potential001:latest .´
´sudo docker run -d -p 5000:5000 potential001´

