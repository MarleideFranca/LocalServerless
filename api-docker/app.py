import json

def lambda_handler(event, context):
    pedido = event.get("pedido", {})
    print(f"Processando pedido: {pedido}")
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "ok",
            "pedido": pedido
        })
    }


