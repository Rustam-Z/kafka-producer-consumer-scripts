import time
import json

from kafka import KafkaProducer

from data_generator import get_registered_user

# We need Bootstrap server
# Topic
# Value serializer


def json_serializer(data):
    """
    Method which defines how the values should be serialized
    :param data: message or record
    :return: json representation of message
    """
    return json.dumps(data).encode('utf-8')


def get_partition(key_bytes, all_partition, available_partition):
    return 0


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer,
                         partitioner=get_partition)  # To select to which partition send the message

if __name__ == '__main__':
    while True:
        registered_user = get_registered_user()
        print(registered_user)  # Just to see the result
        producer.send("registered_user", registered_user)  # Here we write "topic" name
        time.sleep(3)
