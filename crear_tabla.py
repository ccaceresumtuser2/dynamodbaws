from config.conexion_aws import conexion_aws_boto3
from botocore.exceptions import ClientError

dynamodb = conexion_aws_boto3()

def tabla_existe(table_name):
    dynamodb_client = dynamodb.meta.client  # 🔥 importante
    try:
        dynamodb_client.describe_table(TableName=table_name)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            return False
        else:
            raise e


#crear la tabla
def crear_tabla_dynamodb(table_name):
    print(f"Espere un momento mientra se crea la tabla {table_name} sea paciente...")
    try:
        if(tabla_existe(table_name)):
            print(f"Tabla {table_name} Existe...")
            return 
        
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
               # {'AttributeName': 'id', 'KeyType': 'HASH'}  # Primary Key
               {'AttributeName': 'codigo', 'KeyType': 'HASH'}  # Primary Key
            ],
            AttributeDefinitions=[
                #{'AttributeName': 'id', 'AttributeType': 'S'}
                {'AttributeName': 'codigo', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists() #espera hasta que se cree la tabla
        print("Tabla creada")
    except Exception as e:
        print(f"Error al crear la tabla {table_name} en dynamodb")
        print(e)

crear_tabla_dynamodb("Usuarios20")