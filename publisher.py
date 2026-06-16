import serial
import paho.mqtt.client as mqtt
import time

SERIAL_PORT = "COM9"   # change if needed
BAUD = 9600

BROKER = "broker.benax.rw"   # or HiveMQ / VPS
TOPIC = "anitha/temperature"

ser = serial.Serial(SERIAL_PORT, BAUD)
time.sleep(2)

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

print("Connected")

while True:
    line = ser.readline().decode().strip()
    print("Received:", line)

    if "Temperature:" in line:
        temp = line.split(":")[1].replace("C", "").strip()

        client.publish(TOPIC, temp)
        print("Published:", temp)