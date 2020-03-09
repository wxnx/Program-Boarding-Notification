#   import library paho
import paho.mqtt.client as mqtt

#   definisi broker/(IP yang digunakan)
broker_address = "localhost"

#   membuat client bernama admin
print("Creating New Instance")
client = mqtt.Client("admin_b")

#   membuat admin terkoneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

#   mulai loop client
client.loop_start()

#   melakukan publish boarding dan lokasi dengan topik "pemberitahuan"
#   perulangan untuk inputan boarding
while True:
    #   inputan boarding
    flight      =   input("Input Flight      :")
    time        =   input("Input Time        :")
    destination =   input("Input Destination :")     
    gate        =   input("Input Gate        :")      
    msg         =   flight +  " " + " " + time +  " " + " " + destination +  " " + " " +  " " + " " +  " " + " " + " " + " " + gate 
    #   melakukan publish 
    client.publish("pemberitahuan_boarding", 'waktu' + " " + msg)
    #   menanyakan apakah ingin menginputkan boarding lagi
    ask         =   input("Apakah ingin menginputkan Boarding Schedule lagi? Ya/Tidak :")
    #   ini kondisinya
    if ask=="Ya" or ask=="y" or ask=="Y" or ask=="ya":
        True
    else:
        break

#   loop client berhenti
client.loop_stop()