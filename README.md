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

#### build docker image locally

´sudo docker build -t potential001:latest .´
´sudo docker run -d -p 5000:5000 potential001´

access on http://localhost:5000

#### build docker image on AWS
url : https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#Instances:
instance id : i-143002a8

ssh to instance:
cd to ~/Documents/keys
ssh -i my-ec2-key_pair.pem ec2-user@52.59.224.105

´docker build -t potential001:latest .´
´docker run -d -p 80:5000 potential001´

acces the application at:

http://ec2-52-59-224-105.eu-central-1.compute.amazonaws.com/ (public dns)
http://52.59.224.105 (public ip)
