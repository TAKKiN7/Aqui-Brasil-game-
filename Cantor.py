from machine import Pin, PWM
from time import sleep as pause


class Cantor(PWM):
    notes = {  # calclulo das oitavas saindo do oitava 0    (x * 2)(16,35 * 2) = 261,63  com x == 4 (4 oitava)
        # -> x = valor da oitava esperada
        # -> 16,35 = valor de dó na oitava zero

        "do": 262,
        "re": 294,
        "mi": 330,
        "fa": 349,
        "sol": 392,
        "la": 440,
        "si": 494,
        "do2": 523,
        "pause": 0
    }

    """melodia = [
        (notes.get("sol"), 0.8), (notes.get("fa"), 0.3), (notes.get("mi"), 0.3), (notes.get("re"), 0.3),
        (notes.get("mi"), 0.3), (notes.get("fa"), 0.3), (notes.get("sol"), 0.6), (notes.get("pause"), 0.03),
        (notes.get("sol"), 0.5), (notes.get("pause"), 0.03), (notes.get("sol"), 0.5),  # A-ti-rei o pau no ga-to-to
        (notes.get("pause"), 0.1),

        (notes.get("la"), .3), (notes.get("sol"), .3), (notes.get("fa"), .6), (notes.get("pause"), 0.03),
        (notes.get("fa"), .5), (notes.get("pause"), 0.03), (notes.get("fa"), .5)
    ]"""

    beeps = {
        "aprovado": [
            (658, 0.25),
            (878, 0.3)
        ],
        "recusado": [
            (441, 0.4),
            (0, 0.1),
            (441, 0.6)
        ],
        "aproximado": [
            (1046, 0.1)
        ],
        "desligando": [
            (493, 0.2),
            (329, 0.4)
        ],
        "ligando": [
            (523, 0.1),  # Dó (C5)
            (659, 0.1),  # Mi (E5)
            (784, 0.1),  # Sol (G5)
            (1046, 0.2)  # Dó (C6) - Finalização brilhante
        ],
        "tecla": [
            (1046, 0.1)
        ]
    }

    def __init__(self, pin=28):
        super().__init__(Pin(pin))
        self.deinit()

    def tocar_nota(self, frequencia, duracao):
        if frequencia == 0:
            self.duty_u16(0)  # Silêncio
        else:
            self.freq(frequencia)
            self.duty_u16(2500)  # 50% do volume (vibrando)

        pause(duracao)
        self.duty_u16(0)  # Para o som após a nota
        pause(0.05)  # Pequena pausa entre notas

    def tocar(self, beep):
        for nota, tempo in self.beeps.get(beep):
            self.tocar_nota(nota, tempo)

