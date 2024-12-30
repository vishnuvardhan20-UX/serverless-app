

# Serverless App

A **serverless application** built using AWS Lambda, API Gateway, and DynamoDB. This project demonstrates how to build a fully serverless backend with API integration and scalable data storage.

---

## Features

- **Serverless Backend**: Hosted entirely on AWS Lambda for a scalable and cost-effective solution.
- **API Integration**: Uses AWS API Gateway to expose RESTful endpoints.
- **Database Storage**: DynamoDB for fast and scalable NoSQL storage.
- **Easy Deployment**: Deployment instructions are included to help you get started quickly.

---

## Prerequisites

Before you begin, ensure you have the following:
- **AWS Account**: To deploy and test the app.
- **AWS CLI**: Installed and configured.
- **Python 3.x**: For Lambda function development and testing.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/vishnuvardhan20-UX/serverless-app.git

2. Navigate to the project directory:
   ```bash
   cd serverless-app

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Edit the user_handler.py file to add your logic or test the default Lambda function
   
---

#### **5. Deployment Guide**
Include the deployment steps (as mentioned earlier). Use formatting for better readability.

```markdown
## Deployment Guide

### Prerequisites
- AWS account
- AWS CLI installed and configured
- Python 3.x installed

### Steps to Deploy

1. **Zip the Lambda function**:

   zip function.zip lambda/user_handler.py

2. **Deploy the Lambda function**:
   aws lambda create-function \
    --function-name serverless-app \
    --runtime python3.x \
    --role <IAM_ROLE_ARN> \
    --handler user_handler.lambda_handler \
    --zip-file fileb://function.zip

