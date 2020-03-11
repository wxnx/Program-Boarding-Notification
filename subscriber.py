#   import library paho
import paho.mqtt.client as mqtt

#   import library time
import time

# import re (regular expression) untuk filter
import re

#   membuat callback pada saat ada pesan masuk
def on_message(client, userdata, message):
    pesan   =   str(message.payload.decode("utf-8"))
    match   =   re.search('waktu', pesan)

    if match:
        #   Header Boarding
        print("Departures")
        header = " " + " " + " " + " " +  " " + " " +"Time" + " " + " " + "Flight " + " " + " " + "Destination" + " " + " " + "Gate" + "\n"
        print(header)
        print(pesan)
        with open("boarding.txt", "a+") as file:
            file.write(header)
            file.write(pesan + "\n")
    else:
        #   Header Transit
        print("Arrivals")
        header = " " + " " + " " + " " + " " + " " + " " + " " + " " + "Origin" + " " + " " + "Flight" + " " + " " + "Time" + " " + " " + "Terminal" + "\n"
        print(header)
        print(pesan)
        with open("lokasi.txt", "a+") as file:
            file.write(header)
            file.write(pesan + "\n")

#   definisi broker/(IP yang digunakan)
broker_address = "localhost"

#   membuat client bernama penumpang
print("Creating new instance")
client = mqtt.Client("cust")

#   mengaktifkan callback
client.on_message = on_message

#   membuat penumpang terkoneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

#   mulai loop client
client.loop_start()

#   penumpang subscribe ke topik yang ada di publisher
client.subscribe("pemberitahuan_boarding")
client.subscribe("pemberitahuan_transit")

#   melakukan loop forever
while True:
    #   untuk memberikan waktu tunggu 1 detik
    time.sleep(1)

#   loop client berhenti
client.loop_stop()