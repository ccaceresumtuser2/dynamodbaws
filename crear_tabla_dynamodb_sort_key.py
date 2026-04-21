"""
===========================================================
MÓDULO: Gestión de Usuarios en DynamoDB
===========================================================

🧾 DESCRIPCIÓN:
Este archivo Crea la tabla con PA

🛠 TECNOLOGÍA:
- AWS DynamoDB
- boto3 (Python SDK)

AUTOR: Carlos Jose Caceres Ochoa
FECHA: 20-04-2026
VERSIÓN: 1.0
Partition Key (obligatorio)
Sort Key (opcional, pero potente)
o un GSI si necesitas otra forma de búsqueda (combinacion pk y sk)

Tabla: Empleados

Campo	          Tipo	Descripción
departamento_id	   PK	Agrupa empleados
empleado_id	       SK	Identificador único
nombre_apellido       atributo	Nombre
cargo 
correo	           atributo	Para GSI

===========================================================
"""

import boto3

from config.conexion_aws import conexion_aws_boto3

dynamodb = conexion_aws_boto3()
def crear_tabla_empleado():
    print(f"Espere un momento mientra se crea la tabla sea paciente...")
    try:
        table = dynamodb.create_table(
            TableName='Empleados',
            KeySchema=[
                {'AttributeName': 'departamento_id', 'KeyType': 'HASH'},       #Partition Key → agrupa datos
                {'AttributeName': 'empleado_id', 'KeyType': 'RANGE'}          #RANGE = Sort Key → organiza dentro del grupo
            ],
            AttributeDefinitions=[
                {'AttributeName': 'departamento_id', 'AttributeType': 'S'},
                {'AttributeName': 'empleado_id', 'AttributeType': 'S'},
                {'AttributeName': 'correo', 'AttributeType': 'S'},
                {'AttributeName': 'nombre_apellido', 'AttributeType': 'S'},
                {'AttributeName': 'cargo', 'AttributeType': 'S'}
            ],
            GlobalSecondaryIndexes=[

                # 🔍 Buscar por correo
                {
                    'IndexName': 'correo-index',
                    'KeySchema': [
                        {'AttributeName': 'correo', 'KeyType': 'HASH'}
                    ],
                    'Projection': {'ProjectionType': 'ALL'}, #configuración de un GSI (Global Secondary Index) en DynamoDB.
                    'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
                },

                # 🔍 Buscar por nombre + apellido
                {
                    'IndexName': 'nombre-index',
                    'KeySchema': [
                        {'AttributeName': 'nombre_apellido', 'KeyType': 'HASH'}
                    ],
                    'Projection': {'ProjectionType': 'ALL'}, #configuración de un GSI (Global Secondary Index) en DynamoDB.
                    'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
                },

                # 🔍 Buscar por cargo
                {
                    'IndexName': 'cargo-index',
                    'KeySchema': [
                        {'AttributeName': 'cargo', 'KeyType': 'HASH'}
                    ],
                    'Projection': {'ProjectionType': 'ALL'}, #configuración de un GSI (Global Secondary Index) en DynamoDB.
                    'ProvisionedThroughput': {'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        table.wait_until_exists() #espera hasta que se cree la tabla
        print("Tabla creada")
    except Exception as e:
        print(f"Error al crear la tabla en dynamodb")
        print(e)

crear_tabla_empleado()