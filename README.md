# 🧠 Aqui Brasil Game

> Uma **maquininha de cartão simulada** feita com **Raspberry Pi** e **MicroPython**, usando módulos como **Display LCD I2C** e **Leitor RFID**.

Essa aplicação simula operações de pagamento (como PIX e ver saldo) usando um leitor de cartão RFID + display e teclado. Ela roda em dispositivos como Raspberry Pi com suporte a MicroPython.

---

## 📌 Visão geral

O projeto inclui:

- Funções de **leitura de cartão (RFID)**
- Operações de **PIX**
- Visualização de saldo da conta
- Interface com display e teclado
- Estrutura modular em Python

📌 Linguagem: Python (MicroPython)

---

## 🧩 Estrutura do projeto

Principais arquivos:

| Arquivo | Descrição |
|---------|-----------|
| `main.py` | Arquivo principal que inicializa tudo e executa o menu |
| `Banco.py` | Lógica de operações financeiras (PIX, validar saldo, etc.) |
| `Display.py` | Interface com o display LCD |
| `Leitor.py` | Leitor de cartões RFID |
| `Database.py` | Banco de dados simples para contas |
| `Teclado.py` | Captura entrada do usuário |
| `Menu.py` | Sistema de menu principal |
| `basic_functions.py` | Funções auxiliares usadas pelo sistema |
| `Cantor.py` | Controle de sons/feedback |

---

## 🛠️ Pré-requisitos

Antes de rodar o projeto, você precisa de:

✔️ **Raspberry Pi** com MicroPython instalado  
✔️ Módulos conectados corretamente:  
- Display LCD I2C  
- Leitor RFID (como PN532)  
- Teclado de entrada

✔️ Biblioteca para PN532 e suporte a I2C no MicroPython

---

## 🚀 Como usar

1. **Clone o repositório**

```bash
git clone https://github.com/TAKKiN7/Aqui-Brasil-game-.git
cd Aqui-Brasil-game-