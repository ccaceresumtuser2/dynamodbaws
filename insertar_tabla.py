from conexion_aws import conexion_aws_boto3

dynamodb = conexion_aws_boto3()

def insertar_item_tabla(item,tabla):
    try:
        table = dynamodb.Table(tabla)
        table.put_item(
            Item=item
        )
    except Exception as e:
        print(e)

item = {
            "id": 1,
            "nombre": "Carlos",
            "edad": 30,
            "direccion": {
                "ciudad": "Cartagena",
                "pais": "Colombia"
            },
            "telefonos": ["123456", "987654"],
            "activo": True
        }

insertar_item_tabla(item,"Usuarios20")

