"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo Actualiza la tabla  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""


from config.conexion_aws import conexion_aws_boto3
#llamado a la conexión DynamoDb
dynamodb = conexion_aws_boto3()
#Actualizar tabla generica
def actualizar_tabla(table_name, item):
    try:
        table = dynamodb.Table(table_name)

        response = table.update_item(
            Key={'id': item['id']},
            UpdateExpression="""
                SET nombre = :nombre,
                    edad = :edad,
                    direccion = :direccion,
                    telefonos = :telefonos,
                    activo = :activo
            """,
            ExpressionAttributeValues={
                ':nombre': item['nombre'],
                ':edad': item['edad'],
                ':direccion': item['direccion'],
                ':telefonos': item['telefonos'],
                ':activo': item['activo']
            },
            ReturnValues="UPDATED_NEW"
        )

        print("Usuario actualizado:", response.get("Attributes"))

    except Exception as e:
        print("Error al actualizar usuario")
        print(e)


item = {
            "id": "1",
            "nombre": "Carlos Caceres",
            "edad": 31,
            "direccion": {
                "ciudad": "Santiago",
                "pais": "Chile"
            },
            "telefonos": ["12345633", "9876543"],
             "activo": False
        }


#llamado a la función
actualizar_tabla("Usuarios", item)