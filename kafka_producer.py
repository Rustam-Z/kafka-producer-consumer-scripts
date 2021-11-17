import time
import json

from kafka import KafkaProducer

from data_generator import get_registered_user

# We need Bootstrap server
# Topic
# Value serializer


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)


if __name__ == '__main__':
    while True:
        registered_user = get_registered_user()
        print(registered_user)  # Just to see the result
        producer.send("registered_user", registered_user)  # Here we write "topic" name
        time.sleep(3)
