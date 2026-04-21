"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo para Insertar Registros  con AWS DynamoDb con boto3

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 13-04-2026
VERSIÓN: 1.0

===========================================================
"""
from config.conexion_aws import conexion_aws_boto3

dynamodb = conexion_aws_boto3()

#insertar un Item
def insertar_item_tabla(item,tabla):
    try:
        table = dynamodb.Table(tabla)
        table.put_item(
            Item=item
        )
    except Exception as e:
        print(e)

#Insertar Multiples Item
def insertar_items_tabla(items,table_name):
    table = dynamodb.Table(table_name)

    try:
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(Item=item)

        print("Usuarios guardados correctamente")

    except Exception as e:
        print("Error al guardar usuarios")
        print(e)


#item de la tabla Usuarios
item = {
            "id": "4",
            "nombre": "Carlos1z",
            "edad": 30,
            "direccion": {
                "ciudad": "Cartagena",
                "pais": "Colombia"
            },
            "telefonos": ["123456", "987654"],
             "activo": False,
             "habilitado":True
        }

items=[
    {
            "id": "2",
            "nombre": "Carlos1z",
            "edad": 30,
            "direccion": {
                "ciudad": "Cartagena",
                "pais": "Colombia"
            },
            "telefonos": ["123456", "987654"],
             "activo": False
    },
    {
            "id": "3",
            "nombre": "Carlos1z",
            "edad": 30,
            "direccion": {
                "ciudad": "Cartagena",
                "pais": "Colombia"
            },
            "telefonos": ["123456", "987654"],
             "activo": False
    }
]


insertar_item_tabla(item,"Usuarios")
#insertar_items_tabla(items,"Usuarios")

