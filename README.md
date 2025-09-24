# LocalServerless

Protótipo para simular **AWS Lambda Functions** localmente usando **Docker** e **Python**.

---

## Tecnologias
- Python 3.x
- Docker

---


---

## Como rodar

1. **Build da imagem Docker**
```bash
docker build -t localserverless .

## Como rodar o container
docker run -p 9000:8080 localserverless

## Invocando o lambda local
# teste
# usando --% (comando que funcionou no protótipo)
curl.exe --% -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -H "Content-Type: application/json" -d "{\"pedido\": {\"id\": 123, \"produto\": \"Notebook\"}}"
