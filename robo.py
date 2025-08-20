class Robozinho:
    def __init__(self, nome, poder, energia):
        self.nome = nome
        self.poder = poder
        self.energia = energia

    def robo_pronto(self):
        print(f"o nome do robo é ", {self.nome})
        print(f"meus poderes são ", {self.poder})
        print(f"e minha energia esta ", {self.energia})
        