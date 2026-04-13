from conexion_aws import conexion_aws_boto3

dynamodb = conexion_aws_boto3()

def scan_item_tabla(tabla):
    try:
        table = dynamodb.Table(tabla)
        response = table.scan()
        for item in response['Items']:
            print(item)
    except Exception as e:
        print(e)

def scan_item_tabla_ordenada(tabla):
    try:
        table = dynamodb.Table(tabla)
        response = table.scan()
        items = response['Items']
        # ordenar por id
        #items_ordenados = sorted(items, key=lambda x: x['id'])
        items_ordenados = sorted(items, key=lambda x: int(x['id']))
        for item in items_ordenados:
            print(item)
    except Exception as e:
        print(e)

scan_item_tabla_ordenada('Usuarios20')