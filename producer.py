import boto3
import json
import random
import time

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='us-east-1')

# Configuration
usernames = ['alice', 'bob', 'charlie']
actions = ['like', 'comment', 'share', 'view', 'follow']

while True:
    for username in usernames:
        num_actions = random.randint(2, 5)  # Each user performs 2 to 5 actions
        for _ in range(num_actions):
            data = {
                'username': username,
                'action': random.choice(actions),
                'timestamp': int(time.time())
            }

            # Send to Kinesis stream
            kinesis.put_record(
                StreamName='SocialMediaStream',
                Data=json.dumps(data),
                PartitionKey=username
            )
            print(f"Sent: {data}")
            time.sleep(0.2)  # Small delay between actions

    time.sleep(3)  # Delay between user batches
