"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo Crea la tabla  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""

from config.conexion_aws import conexion_aws_boto3

#autor carlos jose caceres ochoa
###########################################################
#              conexion a aws boto3                       #
###########################################################
dynamodb = conexion_aws_boto3()

#crear la tabla
def crear_tabla_dynamodb(table_name):
    print(f"Espere un momento mientra se crea la tabla {table_name} sea paciente...")
    try:        
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
               {'AttributeName': 'id', 'KeyType': 'HASH'}  # Primary Key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
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

#llamado a la funcion
crear_tabla_dynamodb("Usuarios")