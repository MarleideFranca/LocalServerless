#Usando a imagem oficial da AWS Lambda

FROM public.ecr.aws/lambda/python:3.11

# Copia o código da função
COPY app.py ${LAMBDA_TASK_ROOT}

# Define o handler (arquivo.função)
CMD ["app.lambda_handler"]
