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

### useful comands

#### get acces token


curl -X POST -H "Accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -H "Cache-Control: no-cache" -H "Postman-Token: db682c85-b005-96f0-bb7a-8a3c29f77e27" -d '=' "https://api.enco.io/token?grant_type=client_credentials&client_id=mKPCKnzKW4j8eVh4WaEmR3qlhwQa&client_secret=uVzpRK57MizQ7aNN_0LL8M3avR4a&scope=openid"

#### build docker image locally

´sudo docker build -t potential001:latest .´
´sudo docker run -d -p 5000:5000 potential001´

access on http://localhost:5000

#### build docker image on AWS
url : https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#Instances:
instance id : i-143002a8

ssh to instance:
´ssh -i ~/Documents/keys/my-ec2-key_pair.pem ec2-user@52.59.230.157´

´docker build -t potential001:latest .´
´docker run -d -p 80:5000 potential001´

access the application at:

http://ec2-52-59-224-105.eu-central-1.compute.amazonaws.com/ (public dns)
http://52.59.224.105 (public ip)
