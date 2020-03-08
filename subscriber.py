#   import library paho
import paho.mqtt.client as mqtt

#   import library time
import time

#   membuat callback pada saat ada pesan masuk
def on_message(client, userdata, message):
    print(message.payload.decode("utf-8"))

#   definisi broker/(IP yang digunakan)
broker_address = "localhost"

#   membuat client bernama penumpang
print("Creating new instance")
client = mqtt.Client("penumpang")

#   mengaktifkan callback
client.on_message = on_message

#   membuat penumpang terkoneksi ke broker
print("Connecting to broker")
client.connect(broker_address, port=1883)

#   mulai loop client
client.loop_start()

#   penumpang subscribe ke topik yang ada di publisher
client.subscribe("pemberitahuan")

#   melakukan loop forever
while True:
    #   untuk memberikan waktu tunggu 1 detik
    time.sleep(1)

#   loop client berhenti
client.loop_stop()