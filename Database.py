import json

class Database:
    arq = open("dados.json").read()
    dados: dict = json.loads(arq)

    def commit(self):
        with open("dados.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.dados, arquivo)

        print("Atualização realizada")


    def get(self):
        return self.dados


