import json

def lambda_handler(event, context):
    """
    AWS Lambda function handler.
    This function returns a simple response for demonstration purposes.
    """
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello, world! This is a serverless app!",
            "input": event
        })
    }

