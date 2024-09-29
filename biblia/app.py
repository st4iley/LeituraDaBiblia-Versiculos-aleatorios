import json
import random

# Função para carregar o dicionário do arquivo JSON
def carregar_dicionario(arquivo_json):
    with open(arquivo_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)
        
        # Verifique se os dados são uma lista ou um dicionário
        if isinstance(dados, list):
            print("O JSON contém uma lista, não um dicionário.")
            return random.choice(dados)  # Escolhe um dicionário aleatório na lista
        elif isinstance(dados, dict):
            return dados
        else:
            raise TypeError("O JSON não contém nem uma lista nem um dicionário.")

# Função para pegar uma entrada aleatória do dicionário
def pegar_entrada_aleatoria(dicionario):
    chave = random.choice(list(dicionario.keys()))
    return chave, dicionario[chave]

# Carregar o dicionário do arquivo JSON
dicionario = carregar_dicionario('biblia.json')

# Se 'dicionario' for uma lista, o loop abaixo não faz sentido, então lidaremos com isso
if isinstance(dicionario, dict):
    # Loop contínuo até o usuário sair
    while True:
        chave, valor = pegar_entrada_aleatoria(dicionario)
        print(f"Chave: {chave} -> Valor: {valor}")
        
        # Perguntar ao usuário se deseja continuar
        continuar = input("Deseja ler outra linha aleatória? (s/n): ").strip().lower()
        if continuar != 's':
            print("Saindo...")
            break
else:
    print("Não foi possível encontrar um dicionário no arquivo JSON.")
