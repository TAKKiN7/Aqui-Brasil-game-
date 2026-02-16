from Teclado import Teclado
from Display import Display
from time import sleep as pause
from Banco import Banco
from Leitor import Leitor
from basic_functions import led_error
from _thread import start_new_thread as secundario




class Menu:
    def __init__(self, teclado: Teclado, display: Display, banco: Banco, dados: dict, leitor: Leitor):
        self.teclado: Teclado = teclado
        self.display: Display = display
        self.leitor: Leitor = leitor
        self.banco: Banco = banco
        self.dados: dict = dados
        self.opcoes = ["PIX", "VER SALDO", "CREDITO", "EMPRESTIMO"]


    def contagem(self):
        for c in range(10):
            print(c)
            pause(1)

    def menu_rolagem_um_botao(self, titulo="BANCO DO BRASA"):
        indice: int = 0
        total = len(self.opcoes)
        selecionado = False

        while not selecionado:
            pause(0.5)
            self.display.desligar_backlight()
            # Atualiza o Display
            self.display.limpar()
            self.display.escrever(titulo, "> " + self.opcoes[indice])

            # Aguarda clique ou timeout de confirmação
            confirmando = True

            while True:
                tecla = self.teclado.get_teclas()

                if tecla:
                    self.display.backlight(True)
                    self.display.parar = 1
                    pause(0.5)
                    if tecla == "A":  # equivalente ao btn_move
                        indice = (indice + 1) % total
                        pause(0.3)  # debounce
                        confirmando = False
                        break

                    elif tecla == "B":  # equivalente ao btn_select
                        break
                    else:
                        return 999
                    

            if confirmando:
                selecionado = True

        self.display.limpar()
        self.display.escrever("SELECIONADO:", self.opcoes[indice])
        pause(1)
        return indice  # Retorna o ID da opção escolhida

    def menu(self):
        escolha = self.menu_rolagem_um_botao()
        
        if escolha == 999:
            return
        elif escolha == 0:
            self.display.escrever("Iniciando Pix", "Aguarde...", True)

            while True:
                print("\n--- SISTEMA DE PIX ---")
                self.display.escrever("Digite a chave", "Pix:")

                while True:
                    chave = ""
                    while len(chave) != 8:
                        self.display.escrever("Digite a chave", f"Pix: {chave}")
                        while True:
                            tecla = self.teclado.get_teclas()
                            if tecla:
                                if tecla == "*":
                                    self.display.escrever("Operação", "Cancelada...")
                                    secundario(led_error, ())
                                    pause(1.5)
                                    return
                                elif tecla == "D":
                                    chave = chave[0:-1]
                                break
                        if tecla not in ("A", "B", "C", "D", "#", "*"):
                            chave += tecla

                    self.display.escrever("Confime os dados", f"Chave: {chave}")
                    while True:
                        tecla = self.teclado.get_teclas()
                        if tecla:
                            if tecla == "*":
                                self.display.escrever("Operação", "Cancelada...")
                                secundario(led_error, ())
                                pause(1.5)
                                return
                            elif tecla in ("B", "D"):
                                break
                    if tecla == "B":
                        break
                    else:
                        continue

                while True:
                    valor = ""
                    while len(valor) != 13:
                        self.display.escrever("Digite o valor:", f"R$ {valor}")
                        while True:
                            tecla = self.teclado.get_teclas()
                            if tecla:
                                if tecla == "*":
                                    self.display.escrever("Operação", "Cancelada...")
                                    secundario(led_error, ())
                                    pause(1.5)
                                    return
                                elif tecla == "D":
                                    valor = valor[0:-1]
                                elif tecla == "B":
                                    pass
                                break
                        if tecla not in ("A", "B", "C", "D", "#", "*"):
                            valor += tecla
                        elif tecla == "B":
                            break
                    if tecla == "B":
                        self.display.escrever("Voce confirma:", f"R$ {valor}")
                        while True:
                            tecla = self.teclado.get_teclas()
                            if tecla:
                                if tecla == "*":
                                    self.display.escrever("Operação", "Cancelada...")
                                    secundario(led_error, ())
                                    pause(1.5)
                                    return
                                if tecla in ("B", "D"):
                                    break
                        if tecla == "B":
                            break
                chave_ofc = self.banco.valida_chave(chave)
                if not chave_ofc:
                    continue

                quem_paga = self.leitor.ler_cartao()
                self.banco.pix(quem_paga, chave_ofc, int(valor))
                break




        elif escolha == 1:
            self.banco.ver_saldo(self.dados)
        elif escolha > 1:
            self.display.escrever("Disponivel", "Em breve...", True)
