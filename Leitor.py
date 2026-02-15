from machine import Pin, I2C
from pn532 import PN532_I2C
from sys import exit
from Display import Display
from Cantor import Cantor


class Leitor:
    leitor_rfid = I2C(1, sda=Pin(26), scl=Pin(27), freq=400000)
    nfc: PN532_I2C
    display: Display

    def __init__(self, display: Display, cantor: Cantor):
        self.display = display
        self.criar_leitor_nfc()
        self.cantor = cantor

    def criar_leitor_nfc(self):
        try:
            self.nfc = PN532_I2C(self.leitor_rfid)
            versiondata = self.nfc.firmware_version

            if versiondata:
                ic, ver, rev, support = versiondata
                print(f'PN532 Conectado! Firmware v{ver}.{rev}')

            self.nfc.SAM_configuration()

        except Exception as e:
            print('Erro ao iniciar o modulo:', e)
            self.display.escrever("Erro Hardware", "Verificar NFC")
            exit()

    def ler_cartao(self):
        self.display.escrever("Aprox. o cartao")
        cartao_lido = False
        while not cartao_lido:
            uid = self.nfc.read_passive_target(timeout=500)

            if uid:
                self.cantor.tocar("aproximado")
                id_hex = "".join("{:02X}".format(b) for b in uid)
                self.display.escrever("Realizando", "leitura...", True)
                return id_hex



