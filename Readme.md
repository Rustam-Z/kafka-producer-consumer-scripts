# Apche Kafka Producers & Consumers in Python 
Learning Apache Kafka Producers and Consumers

1. Created function for generating data
```py
faker = Faker()

def get_registered_user():
    return {
        "name": faker.name(),
        "address": faker.address(),
        "created_at": faker.year()
    }
```
2. Created the KafkaProducer, to write messages to single broker with 1 partition. 
```py
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

producer.send("registered_user", registered_user)  # "registered_user" is the Kafka topic

# Generated data example -> {'name': 'Barry Vargas', 'address': '829 Stephen Glens\nSarahmouth, AZ 55533', 'created_at': '1994'}
```
3. Created KafkaConsumer and consumer group, to read the messages from topic.
```python
consumer = KafkaConsumer(
    "registered_user",  # From which topic consume messages
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",  # Consume from first message
    group_id="consumer-group-a"
)

for msg in consumer:
    print(f"Registered user = {json.loads(msg.value)}")
```
4. Tested that same partition cannot be assigned to multiple consumer in same group. If they belong to different consumer group, then everything is fine. In this case we have only 1 partition with 2 consumers.

<img src="images/2_kafka_consumer_groups.png">
5. If we have 2 partitions and 2 consumers inside the topic, then everything is OK. So, the message from one partition will go to one consumer, and message from another to second consumer.
