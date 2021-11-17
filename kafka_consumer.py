from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",  # From which topic consume messages
        bootstrap_servers="localhost:9092",
        auto_offset_reset="earliest",  # Consume from first message
        group_id="consumer-group-a"
    )

    print("Starting the consumer ...")

    for msg in consumer:
        print(f"Registered user = {json.loads(msg.value)}")
