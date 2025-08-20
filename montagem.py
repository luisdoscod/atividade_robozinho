from robo import Robozinho

robos = []

def add_robos(nome, poder, energia):
        r = Robozinho(nome, poder,energia)
        robos.append(r)
        return r 

def listar_robos():
        nova_lista = []
        for i, r in enumerate(robos):
            texto = f"nome: {r.nome}, poder: {r.poder}, energia: {r.energia}"
            nova_lista.append(texto)
        return nova_lista

def excluir_robos(index):
       if 0 <= index < len(robos):
        return robos.pop(index)
       else: 
        return None