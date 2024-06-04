"""
Desafio
Vamos agora, adicionar uma funcionalidade à classe `UsuarioTelefone`, que realizar chamadas para
outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do
usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai
permitir que o usuário faça a chamada, ele vai receber o destinatário e duração como parâmetros.
Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar
o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem
adequada como mostra no exemplo a baixo.

Entrada
Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

Saída
Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	          Saída

Rodrigo
(00) 90000-0000   Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00
10.00
(33) 93333-3333
60

Yule              Chamada para (00) 90000-0000 realizada com sucesso. Saldo: $6.00
(11) 91111-1111
30.00
(00) 90000-0000
240

Amelia            Saldo insuficiente para fazer a chamada.
(33) 93333-3333
10.00
(11) 91111-1111
120
"""

# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def plano(self):
        return self.__plano

    # TODO: Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, numero, duracao):
        # TODO: Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
        custo_chamada = self.plano.custo_chamada(duracao)
        # TODO: Verifique se o saldo do plano é suficiente para a chamada.
        if self.plano.saldo > custo_chamada:
            # TODO: Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
            saldo_restante = self.plano.deduzir_saldo(custo_chamada)
            # TODO: E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
            return f"Chamada para {numero} realizada com sucesso. Saldo: ${saldo_restante:.2f}"
        return "Saldo insuficiente para fazer a chamada."


# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo
    
    # TODO: Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo
    
    # TODO: Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, duracao):
        return duracao * 0.1

    # TODO: Crie um método deduzir_saldo para deduzir o valor do saldo do plano:
    def deduzir_saldo(self, custo_chamada):
        return self.saldo - custo_chamada


# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
