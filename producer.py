# Start Kafka instance locally, so app can connect to Kafka by sending and consuming events. We run Kafka as a Docker Image
# Use Python to build small app
from kafka import KafkaProducer
import time
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

for i in range(10):

    data = {
        "event": "order_created",
        "order_id": i,
        "amount": 100 + i
    }

    producer.send("orders", data)

    print("Sent:", data)

    time.sleep(2)