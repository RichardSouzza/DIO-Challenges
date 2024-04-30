"""
DESAFIO: CRIANDO UM SISTEMA BANCÁRIO


OBJETIVO GERAL

Criar um sistema bancário com as operações:
sacar, depositar e visualizar extrato.


DESAFIO

Fomos contratados por um grande banco para desenvolver o seu
novo sistema. Esse banco deseja modernizar suas operações e para
isso escolheu a linguagem Python. Para a primeira versão do sistema
devemos implementar apenas 3 operações: deposito, saque e extrato.


OPERAÇÃO DE DEPÓSITO

Deve ser possível depositar valores positivos para minha conta bancária.
A vl do projeto trabalha apenas com 1 usuário, dessa forma nao precisamos
nos preocupar em identificar qual é número da agência e conta bancária.
Todos os depósitos devem ser armazenados em uma variável e exibidos
na operação de extrato.


OPERAÇÃO DE SAQUE

O sistema deve permitir realizar 3 saques diários com limite máximo
de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema
deve exibir uma mensagem informando que não será possível sacar o dinheiro
por falta de saldo. Todos os saques devem ser armazenados em uma variável
e exibidos na operação de extrato.


OPERAÇÃO DE EXTRATO

Essa operação deve listar todos os depósitos e saques realizados na conta.
No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato
estiver em branco, exibir a mensagem:
"Não foram realizadas movimentações."

Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45
"""


from datetime import date, datetime


class Bank:
    def __init__(self) -> None:
        self.accounts = []
    
    def get_account_by(self, by: str, target: str) -> object | None:
        for account in self.accounts:
            if account.user.__dict__.get(by) == target:
                return account
    
    @staticmethod
    def make_deposit(account: object, value: float) -> None:
        account.balance += value
        account.record_transaction("Depósito", Deposit, value, datetime.now())

    @staticmethod
    def make_withdraw(account: object, value: float) -> None:
        if len(account.withdraws_made_today) >= account.daily_withdraw_limit:
            raise ValueError("Limite de saques diários atingido.")
        if value > account.withdraw_limit_value:
            raise ValueError("O valor solicitado excede o limite de saque.")
        if value > account.balance:
            raise ValueError("O valor solicitado excede o saldo atual da conta.")
        account.balance -= value
        account.record_transaction("Saque", Withdraw, value, datetime.now())

    def open_account(self, user: object) -> object:
        account = Account(user)
        self.accounts.append(account)
        user.set_account(account)
        return account


class Account:
    def __init__(self, user: object) -> None:
        self.user = user
        self.balance = 0
        self.daily_withdraw_limit = 3
        self.withdraw_limit_value = 500
        self.statement = []
    
    def __str__(self) -> str:
        return f"{self.user}'s account"
    
    @property
    def withdraws_made_today(self):
        today = date.today()
        withdraws_made_today = []
        for statement in self.statement:
            if statement.type == Withdraw and statement.date.day == today.day:
                withdraws_made_today.append(statement)
        return withdraws_made_today
    
    def record_transaction(self, title: str, type: object, value: float, date: datetime) -> None:
        transaction = Transaction(title, type, value, date)
        self.update_statement(transaction)
    
    def update_statement(self, transaction) -> None:
        self.statement.insert(0, transaction)

    def show_statement(self, _range: int = 10) -> None:
        if any(self.statement):
            print(f"Extrato de {self.user.username}".upper())
            print("\nTransações:".upper())
            for index in range(_range):
                if index < len(self.statement):
                    print(self.statement[index])
            print(f"\nSaldo: R$ {self.balance:.2f}".upper())
        else:
            print("Não foram realizadas movimentações.")


class Transaction:
    def __init__(self, title: str, type: object, value: float, date: datetime) -> None:
        self.title = title
        self.type = type
        self.value = value
        self.date = date
    
    def __str__(self) -> str:
        return f"{self.title} de R$ {self.value:.2f} em {self.date.strftime("%d/%m/%y às %H:%M:%S")}"


class Deposit:
    pass


class Withdraw:
    pass


class User:
    def __init__(self, username: str) -> None:
        self.username = username
    
    def __str__(self) -> str:
        return self.username

    def set_account(self, account: object) -> None:
        self.account = account


if __name__ == "__main__":
    # Abrir conta
    print("----- Abrir conta -----\n")
    user = User("Richard")
    bank = Bank()
    bank.open_account(user)
    print("Contas abertas:", [account.__str__() for account in bank.accounts])
    print()
    
    # Obter extrato em branco
    print("----- Obter extrato em branco -----\n")
    account = bank.get_account_by("username", "Richard")
    print(account)
    account.show_statement()
    print()
    
    # Realizar depósito
    print("----- Realizar depósito -----\n")
    bank.make_deposit(account, 300)
    assert account.balance == 300
    account.show_statement(1)
    print()
    
    # Realizar saque
    print("----- Realizar saque -----\n")
    bank.make_withdraw(account, 50)
    assert account.balance == 250
    account.show_statement(1)
    print()

    # Testar saque maior que o saldo:
    print("----- Realizar saque maior que o saldo -----\n")
    try:
        bank.make_withdraw(account, account.balance + 1)
    except Exception as error:
        print(error)
    print()

    # Testar limite de valor de saque:
    print("----- Realizar saque acima do limite -----\n")
    try:
        bank.make_withdraw(account, account.withdraw_limit_value + 1)
    except Exception as error:
        print(error)
    print()

    # Testar limite diário de saques:
    print("----- Realizar mais saques que o permitido -----\n")
    print(f"Limite: {account.daily_withdraw_limit}")
    try:
        for withdraw in range(account.daily_withdraw_limit + 1):
            print(f"Realizando {withdraw + 2}º saque...")
            bank.make_withdraw(account, 50)
    except Exception as error:
        print(error)
    print()
    
    # Obter extrato
    print("----- Obter extrato -----\n")
    account.show_statement()