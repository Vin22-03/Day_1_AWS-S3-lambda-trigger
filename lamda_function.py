import json

def lambda_handler(event, context):
    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        filename = record['s3']['object']['key']
        
        print(f"✅ New file uploaded: {filename} to bucket: {bucket}")
        
        return {
            'statusCode': 200,
            'body': json.dumps(f"File {filename} uploaded to bucket {bucket}")
        }
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing upload event')
        }
