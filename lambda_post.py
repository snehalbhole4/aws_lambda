def lambda_handler(event, context):

    client = boto3.resource('dynamodb')

    table = client.Table('Pets')

    response = table.put_item(

       Item={

           'id': event['id'],

           'name': event['name']

         

       }

   )

    return {

       'statusCode': response['ResponseMetadata']['HTTPStatusCode'],

       'body': 'Record ' + event['id'] + ' added'

   }
   
     