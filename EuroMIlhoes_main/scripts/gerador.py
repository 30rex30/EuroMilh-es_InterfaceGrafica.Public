import random

# Primeiro crias as variáveis vazias
numeros_bot = []
estrelas_bot = []

def key_gerador():
    global numeros_bot, estrelas_bot
    numeros_bot = sorted(random.sample(range(1, 51), 5))
    estrelas_bot = sorted(random.sample(range(1, 13), 2))
    return numeros_bot, estrelas_bot

# Gera a primeira chave logo ao iniciar o script
key_gerador()