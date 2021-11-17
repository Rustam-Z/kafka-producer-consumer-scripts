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
2. Created single broker -> 1 partition only, offsets are the same 
```py
def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

producer.send("registered_user", registered_user)  # "registered_user" is the Kafka topic

# Generated data example -> {'name': 'Barry Vargas', 'address': '829 Stephen Glens\nSarahmouth, AZ 55533', 'created_at': '1994'}
```
