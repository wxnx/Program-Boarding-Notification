#   import library paho
import paho.mqtt.client as mqtt

#   definisi broker/(IP yang digunakan)
broker_address = "localhost"

#   membuat client bernama admin
print("Creating New Instance")
client = mqtt.Client("admin")

#   membuat admin terkoneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

#   mulai loop client
client.loop_start()

#   melakukan publish boarding dan lokasi dengan topik "pemberitahuan"
msg = "Flight" + " " + "Time " + " " + "Destination" + " " + "Gate" + "\n" + "GA2134" + " " + "07.30" + " " + "Jakarta    " + " " + "F1" 
    
client.publish("pemberitahuan", msg)

#   check publish sending
print("Pemberitahuan Terkirim")

#   loop client berhenti
client.loop_stop()