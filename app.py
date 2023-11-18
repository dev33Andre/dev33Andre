import random
from datetime import datetime

class ModuloLogin:
    def __init__(self):
        self.registros = []

    def obter_nome_usuario(self):
        nome = input("Digite o nome do usuário: ")
        return nome

    def obter_idade_usuario(self):
        idade = int(input("Digite a idade do usuário: "))
        return idade

    def gerar_data_registro(self):
        data_registro = datetime.now().strftime("%d/%m/%Y")
        return data_registro

    def sortear_cartao(self):
        cartao_sorteado = random.choice(['R$50,00', 'R$250,00', 'R$120,00'])
        return cartao_sorteado

    def cadastrar_funcionario(self):
        nome = self.obter_nome_usuario()
        idade = self.obter_idade_usuario()
        data_registro = self.gerar_data_registro()
        cartao_sorteado = self.sortear_cartao()

        # Adiciona informações do funcionário ao registro
        self.registros.append({
            'Nome': nome,
            'Idade': idade,
            'Data de Registro': data_registro,
            'Cartão Sorteado': cartao_sorteado
        })

    def obter_aniversario(self):
        aniversario = input("Digite a data de aniversário do funcionário (dd/mm/aaaa): ")
        return aniversario

    def mostrar_mensagem_boas_vindas(self):
        if not self.registros:
            print("Nenhum registro encontrado.")
            return

        ultimo_registro = self.registros[-1]
        nome = ultimo_registro['Nome']
        data_registro = ultimo_registro['Data de Registro']
        cartao_sorteado = ultimo_registro['Cartão Sorteado']

        mensagem = f"Olá {nome}, seu registro foi concluído com sucesso no dia {data_registro}.\n" \
                   f"Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {cartao_sorteado}."
        print(mensagem)

# Exemplo de uso
modulo_login = ModuloLogin()
modulo_login.cadastrar_funcionario()
modulo_login.obter_aniversario()

# Exibindo os registros
print(modulo_login.registros)

# Mostrar a mensagem de boas-vindas
modulo_login.mostrar_mensagem_boas_vindas()
