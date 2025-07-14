import json
import boto3
import time
import uuid
import random

s3 = boto3.client('s3')

def lambda_handler(event, context):
    usernames = ['alice', 'bob', 'charlie']
    actions = ['like', 'comment', 'share', 'view', 'follow']

    social_media_events = []

    for username in usernames:
        num_actions = random.randint(2, 5)  # Each user performs 2 to 5 actions
        for _ in range(num_actions):
            event_data = {
                "username": username,
                "action": random.choice(actions),
                "timestamp": int(time.time())
            }
            social_media_events.append(event_data)

    # Convert events to newline-delimited JSON
    json_lines = "\n".join(json.dumps(event) for event in social_media_events)

    # Unique filename
    filename = f"data/{int(time.time())}_{uuid.uuid4().hex}.json"

    # Upload to S3
    s3.put_object(
        Bucket='bucket-106-data',
        Key=filename,
        Body=json_lines.encode('utf-8')
    )

    return {
        'statusCode': 200,
        'body': f'Uploaded {len(social_media_events)} events to file {filename} in S3'
    }
