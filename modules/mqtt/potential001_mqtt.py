import paho.mqtt.client as mqtt


###############MQTT CONFIGURATION##########################

MQTT_SERVER = "broker.smartliving.io"
MQTT_PORT = "1883"
MQTT_KEEPALIVE = "60"
MQTT_USERNAME = "vclaes1986:vclaes1986"
MQTT_PASSWORD = "ujcpi2ktbyl"
CLIENTID = "2965402703997504261220" 


############### MQTT section ##################
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("5797b306807f240ebc17a515")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	#still need to #TODO
    print(msg.topic+" "+str(msg.payload))
    return msg.payload


client = mqtt.Client()
client.username_pw_set(USERNAME,PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

#connect to smartliving io
client.connect(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()