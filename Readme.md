# kafka-producers-consumers
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
