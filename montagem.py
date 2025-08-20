robos = []

def add_robos(nome, poder, energia):
    robos.append({"nome": nome, "poder": poder, "energia": energia})

def listar_robos():
    return robos

def excluir_robos(indice):
    if 0 <= indice < len(robos):
        robos.pop(indice)

def editar_robos(indice, novo_nome=None, novo_poder=None, nova_energia=None):
    if 0 <= indice < len(robos):
        if novo_nome is not None:
            robos[indice]["nome"] = novo_nome
        if novo_poder is not None:
            robos[indice]["poder"] = novo_poder
        if nova_energia is not None:
            robos[indice]["energia"] = nova_energia