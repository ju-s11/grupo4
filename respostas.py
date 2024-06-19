# dicionário global para armazenar as respostas de avaliação
respostas = []

# exportando funções de acesso
_all_ = [
    "add_resposta",
    "get_resposta",
    "get_resposta_by_aluno",
    "get_resposta_by_avaliacao"
]

# dicionário de avaliações (aqui apenas para testes)
"""
avaliacoes = {
    101: {
        "id": 101,
        "nome": "Prova de História",
        "tipo": 1,
        "gabarito": [1, 2, 3],
        "perguntas": ["Q1", "Q2", "Q3"],
    },
    102: {
        "id": 102,
        "nome": "Prova de Ciências",
        "tipo": 1,
        "gabarito": [4, 5, 6],
        "perguntas": ["Q1", "Q2", "Q3"],
    },
}
"""
# devo criar uma função auxiliar para o usuário (aluno) preencher as respostas de uma resposta? não. módulo principal faz isso.
# def preencher_respostas(id_avaliacao, respostas):retorna lista de inteiros (respostas_aluno)


# função auxiliar (interna) para calcular as notas
def calcular_notas(respostas_aluno, avaliacao):
    # itera sobre cada dicionário na lista de respostas
    for resposta in respostas_aluno:
        # inicializa a nota como 0
        nota = 0
        # itera sobre as respostas do aluno e o gabarito
        for resposta_aluno, resposta_correta in zip(
            resposta["respostas"], avaliacao["gabarito"]
        ):
            # compara a resposta do aluno com o gabarito
            if resposta_aluno == resposta_correta:
                # incrementa a nota se a resposta estiver correta
                nota += 1
        # atualiza a nota no dicionário do aluno
        resposta["nota"] = nota


# função (função de acesso) para adicionar nova resposta de um aluno
def add_resposta(id_aluno, id_avaliacao, respostas_aluno):
    erro = 0
    # gera um novo id para a resposta
    id_resposta = len(respostas) + 1
    # obtém a avaliação correspondente
    avaliacao = avaliacoes.get(id_avaliacao)
    if avaliacao is None:
        # raise ValueError(f"Avaliação com id {id_avaliacao} não encontrada.")
        print("Avaliação com id ", id_avaliacao, " não encontrada.")
        erro = 52
        return (erro, None)
    # cria o dicionário da nova resposta
    nova_resposta = {
        "id": id_resposta,
        "id_aluno": id_aluno,
        "id_avaliacao": id_avaliacao,
        "respostas": respostas_aluno,
        "nota": 0,  # inicializa a nota como 0
    }
    # adiciona a nova resposta ao dicionário
    respostas.append(nova_resposta)
    # atualiza as notas chamando a função calcular_notas
    calcular_notas([nova_resposta], avaliacao)
    return (erro, nova_resposta)


# função (função de acesso) para obter uma resposta apartir do id de um aluno e de uma avaliação
def get_resposta(id_aluno, id_avaliacao):
    # busca a resposta específica pelo id_aluno e id_avaliacao
    erro = 0
    for resposta in respostas:
        if (
            resposta["id_aluno"] == id_aluno
            and resposta["id_avaliacao"] == id_avaliacao
        ):
            return (erro, resposta)
    print(
        "Nenhuma resposta foi achada para estes ids (avaliação com este id e/ou aluno com este id)."
    )
    erro = 13
    return (erro, None)


# função (função de acesso) para obter uma resposta apartir do id de um aluno
def get_respostas_by_aluno(id_aluno):
    # lista para armazenar as respostas do aluno específico
    respostas_aluno = []
    erro = 0
    # itera sobre todas as respostas
    for resposta in respostas:
        # verifica se o id_aluno da resposta é igual ao id_aluno fornecido
        if resposta["id_aluno"] == id_aluno:
            # adiciona a resposta à lista de respostas do aluno
            respostas_aluno.append(resposta)

    if respostas_aluno == []:
        erro = 14
        print("Nenhuma resposta foi achada para este aluno (aluno com este id).")
        return (erro, None)
    else:
        return (erro, respostas_aluno)


# função (função de acesso) para obter uma resposta apartir de uma avaliação
def get_respostas_by_avaliacao(id_avaliacao):
    # lista para armazenar as respostas da avaliação específica
    respostas_avaliacao = []
    erro = 0
    # itera sobre todas as respostas
    for resposta in respostas:
        # verifica se o id_avaliacao da resposta é igual ao id_avaliacao fornecido
        if resposta["id_avaliacao"] == id_avaliacao:
            # adiciona a resposta à lista de respostas da avaliação
            respostas_avaliacao.append(resposta)

    if respostas_avaliacao == []:
        print(
            "Nenhuma resposta foi achada para esta avaliação (avaliação com este id)."
        )
        erro = 15
        return (erro, None)
    else:
        return (erro, respostas_avaliacao)


# exemplos de uso
"""
# adicionando algumas respostas
print("Retorno add_resposta:\n")

print("Resposta de avaliação criada com sucesso:")
print(add_resposta(1, 101, [1, 2, 3]))
print("\n")
print(add_resposta(1, 102, [4, 5, 6]))
print("\n")
print(add_resposta(2, 101, [1, 2, 0]))
print("\n")
print(add_resposta(2, 101, [1, 0, 0]))
print("\n")
print(add_resposta(2, 101, [0, 0, 0]))
print("\n")
print(add_resposta(3, 102, [4, 0, 0]))
print("\n")
print(add_resposta(3, 102, [4, 5, 0]))
print("\n")

print("Avaliação com id que não existe (não encontrado):")
print(add_resposta(3, 103, [4, 5, 0]))
print("\n")

# obtendo uma resposta específica
print("Retorno get_resposta:\n")
print(get_resposta(1, 101))
print(get_resposta(3, 102))
print(get_resposta(3, 101))
print("\n")

# obtendo todas as respostas de um aluno
print("Retorno get_respostas_by_aluno:\n")
print(get_respostas_by_aluno(1))
print("\n")

# obtendo todas as respostas de uma avaliação
print("Retorno get_respostas_by_avaliacao:\n")
print(get_respostas_by_avaliacao(101))
print("\n")
"""
# mensagem subliminar para o flávio :)
print("Oie, Flávio! :), vc viu isso?")
