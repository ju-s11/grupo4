import json

# Lista para armazenar as avaliações
avaliacoes = []


# Função para carregar avaliações de um arquivo JSON
def carregar_avaliacoes(nome_arquivo):
    global avaliacoes
    try:
        with open(nome_arquivo, "r") as file:
            avaliacoes = json.load(file)
    except FileNotFoundError:
        avaliacoes = []


# Função para salvar avaliações em um arquivo JSON
def salvar_avaliacoes(nome_arquivo):
    with open(nome_arquivo, "w") as file:
        json.dump(avaliacoes, file, indent=4)


# Função para adicionar uma nova avaliação
def add_avaliacao(id, nome, tipo, gabarito, perguntas):
    for avaliacao in avaliacoes:
        if avaliacao["id"] == id:
            return 1  # Avaliação com este ID já existe
    nova_avaliacao = {
        "id": id,
        "nome": nome,
        "tipo": tipo,
        "gabarito": gabarito,
        "perguntas": perguntas,
    }
    avaliacoes.append(nova_avaliacao)
    return 0  # Sucesso


# Função para obter uma avaliação por ID
def get_avaliacao(id):
    for avaliacao in avaliacoes:
        if avaliacao["id"] == id:
            return avaliacao
    return None  # Avaliação não encontrada


# Função para atualizar uma avaliação existente
def update_avaliacao(id, nome=None, tipo=None, gabarito=None, perguntas=None):
    for avaliacao in avaliacoes:
        if avaliacao["id"] == id:
            if nome:
                avaliacao["nome"] = nome
            if tipo:
                avaliacao["tipo"] = tipo
            if gabarito:
                avaliacao["gabarito"] = gabarito
            if perguntas:
                avaliacao["perguntas"] = perguntas
            return 0  # Sucesso
    return 1  # Avaliação não encontrada


# Função para remover uma avaliação
def delete_avaliacao(id):
    global avaliacoes
    avaliacoes = [avaliacao for avaliacao in avaliacoes if avaliacao["id"] != id]
    return 0  # Sucesso


# Função para listar todas as avaliações
def list_avaliacoes():
    return avaliacoes


# Exemplo de uso do módulo de avaliações
if __name__ == "__main__":
    carregar_avaliacoes("avaliacoes.json")

    print("Adicionando avaliações:")
    print(add_avaliacao(101, "Prova de História", 1, [1, 2, 3], ["Q1", "Q2", "Q3"]))
    print(add_avaliacao(102, "Prova de Ciências", 1, [4, 5, 6], ["Q1", "Q2", "Q3"]))

    print("\nListando todas as avaliações:")
    print(list_avaliacoes())

    print("\nObtendo uma avaliação:")
    print(get_avaliacao(101))

    print("\nAtualizando uma avaliação:")
    print(update_avaliacao(101, nome="Prova de História Atualizada"))

    print("\nListando todas as avaliações após atualização:")
    print(list_avaliacoes())

    print("\nRemovendo uma avaliação:")
    print(delete_avaliacao(101))

    print("\nListando todas as avaliações após remoção:")
    print(list_avaliacoes())

    salvar_avaliacoes("avaliacoes.json")
