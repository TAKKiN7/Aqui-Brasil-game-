from Display import Display
from Database import Database
from time import sleep as pause
from Leitor import Leitor
from Cantor import Cantor


class Banco:
    def __init__(self, db: Database, display: Display, leitor: Leitor, cantor: Cantor):
        self.leitor = leitor
        self.db = db
        self.dados = db.get()
        self.cantor = cantor
        self.display: Display = display

    def validar_saldo(self, quem_paga, valor):
        conta = self.dados.get(quem_paga)
        saldo = conta.get("saldo")
        res = saldo >= valor
        return res

    def pix(self, quem_paga, quem_recebe, valor):
        conta_paga = self.dados.get(quem_paga)
        conta_recebe = self.dados.get(quem_recebe)
        valor_pix = valor
        if not self.validar_saldo(quem_paga, valor_pix):
            self.display.escrever("Efetuando o Pix", "Aguarde...", True)
            self.display.escrever("Saldo", "Insuficiente")
            self.cantor.tocar("recusado")
            pause(2)
            self.display.escrever("Operacao", "cancelada!")
            pause(1.5)
        else:
            conta_paga["saldo"] -= valor_pix
            conta_recebe["saldo"] += valor_pix

            self.db.commit()

            self.display.escrever("Efetuando o Pix", "Aguarde...", True)
            self.display.escrever("Pagamento", "realizado!")
            self.cantor.tocar("aprovado")
            pause(2)

    def ver_saldo(self, db: dict):
        id = self.leitor.ler_cartao()
        conta = db.get(id)
        if not conta:
            self.display.escrever("Conta", "inexistente")
            pause(2)
            return
        saldo = conta.get("saldo")
        self.display.escrever("Saldo atual:", f"R$ {saldo :.2f}", True)
        
        
    def valida_chave(self, chave):
        chave_ofc = ""
        valido = False
        for dado in self.dados:
            user = self.dados.get(dado)
            dados_chave = user.get("chave")

            if dados_chave == chave:
                nome_card = user.get("nome")
                self.display.escrever("PIX PARA", nome_card)
                chave_ofc = dado
                print(chave_ofc)
                pause(2)
                valido = True
                break

        if not valido:
            self.display.escrever("Chave invalida", "", True)
            return None
        
        return chave_ofc
    