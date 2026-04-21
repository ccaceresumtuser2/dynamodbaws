
"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo Elimina Registros(Item) de la tabla  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""

from config.conexion_aws import conexion_aws_boto3
from scan_tabla import scan_filter_expresion_activo_tabla
from boto3.dynamodb.conditions import Attr
#autor carlos jose caceres ochoa
###########################################################
#              conexion a aws boto3                       #
###########################################################
dynamodb = conexion_aws_boto3()

#Elimina si el usuario y el Id esta activo
def eliminar_usuario_si_activo(table_name, user_id,activo):
    try:
        table = dynamodb.Table(table_name)

        response = table.delete_item(
            Key={
                'id': user_id
            },
            ConditionExpression="activo = :val",
            ExpressionAttributeValues={
                ':val': activo
            }
        )

        print(f"Usuario {user_id} eliminado correctamente")

    except Exception as e:
        print(f"No se pudo eliminar el usuario {user_id}")
        print(e)

#elimina todosl os reigstros todos los registros activos

def eliminar_usuario_todos_registros_si_activo(table_name):
    try:
       response = scan_filter_expresion_activo_tabla("Usuarios",True)
       table = dynamodb.Table(table_name)
       with table.batch_writer() as batch:
        while True:
            for item in response['Items']:
                batch.delete_item(Key={'id': item['id']})

            if 'LastEvaluatedKey' not in response:
                break

            response = table.scan(
                FilterExpression=Attr('activo').eq(True),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )    

    except Exception as e:
        print(f"No se pudo eliminar el registros tabla usuarios")
        print(e)

#elimina todosl os reigstros todos los registros con parametros activos True/False

def eliminar_usuario_todos_registros_si_activo(table_name,activo):
    try:
       response = scan_filter_expresion_activo_tabla("Usuarios",activo)
       table = dynamodb.Table(table_name)
       with table.batch_writer() as batch:
        while True:
            for item in response['Items']:
               print(item)
               batch.delete_item(Key={'id': item['id']})

            if 'LastEvaluatedKey' not in response:
                break

            response = table.scan(
                FilterExpression=Attr('activo').eq(activo),
                ExclusiveStartKey=response['LastEvaluatedKey']
            )    

    except Exception as e:
        print(f"No se pudo eliminar el registros tabla usuarios")
        print(e)

#eliminar_usuario_si_activo("Usuarios","1",False)
eliminar_usuario_todos_registros_si_activo("Usuarios",False)