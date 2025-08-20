from montagem import add_robos, listar_robos, excluir_robos, editar_robos

if __name__ == "__main__":
    add_robos ("Paulo", "Super_Força", 100)
    add_robos ("Marcos", "Super_Feiura", -10)
    add_robos ("Vital", "Novo_Hulk", 10000)


    print(listar_robos()) 
    editar_robos(1, novo_nome= "Galvão", novo_poder= "Visao_Noturna", nova_energia= 50)
    excluir_robos(2)
    print(listar_robos())

