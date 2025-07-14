# Serverless Social Media Analytics using AWS Kinesis

A real-time data processing and analytics pipeline built on AWS using serverless components.

## 📌 Architecture

- **Amazon Kinesis**: Ingests social media-like data.
- **AWS Lambda**: Processes incoming records from the stream.
- **Amazon S3**: Stores processed data.
- **Amazon QuickSight**: Visualizes and analyzes the output data.
- **IAM**: Manages secure access.

## 🛠️ Technologies

- AWS Lambda (Node.js/Python)
- Amazon Kinesis Data Streams
- Amazon S3
- Amazon QuickSight
- AWS IAM

## 🚀 Setup Instructions

1. Deploy CloudFormation stack to create Kinesis + S3.
2. Upload Lambda function and attach it to the stream.
3. Allow Lambda to write to S3.
4. Ingest mock social media data (via script or AWS CLI).
5. Connect S3 bucket to Amazon QuickSight.
6. Create visualizations and dashboards.



