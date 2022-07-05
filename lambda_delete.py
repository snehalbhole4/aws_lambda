import boto3

def lambda_handler(event, context):
    
    id = event['id']
    name = event['name']

    client = boto3.resource('dynamodb')

    table = client.Table('Pets')

    response = table.delete_item(
        Key={'id': 'd2'
        }
    
      )

    return {

       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

       'body': 'Record ' + event['id'] + ' deleted'

   }
