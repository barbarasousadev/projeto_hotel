import re

class Cliente:
    def __init__(self, id_cliente:int, nome: str, cpf: str, email: str, telefone: str):
        self.id_cliente = id_cliente
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

class Quarto:
    def __init__(self, numero_quarto: int, tipo_de_quarto: str, preco: float):
        self.numero_quarto = numero_quarto
        self.tipo_de_quarto = tipo_de_quarto
        self.preco = preco
        self.disponibilidade = True  

class Reserva:
    def __init__(self, id_reserva ,id_cliente: str, numero_quarto: str, data: str):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.numero_quarto = numero_quarto
        self.data = data

class Hotel:
    def __init__(self, cnpj: str):
        self.lista_de_clientes = []
        self.lista_de_quartos = []
        self.lista_de_reservas = []
        self._senha = "admin123"
        self.cnpj = cnpj
        self.id_cliente = 1
        self.numero_quarto = 1
        self.id_reserva = 1

    def autenticarFuncionario(self):
        senha = input("Digite a senha do funcionário: ")
        return senha == self._senha 

    def adicionarCliente(self):
        nome = input("Digite o nome do cliente: ").strip()

        while True:
            cpf = input("Digite o CPF: ").strip()
            cpf = re.sub(r"\D", "", cpf)  
            if len(cpf) == 11:
                if any(cliente.cpf == cpf for cliente in self.lista_de_clientes):
                    print("Erro: CPF já cadastrado.")
                else:
                    break
            else:
                print("CPF inválido! Digite exatamente 11 números.")

        while True:
            email = input("Digite o e-mail: ").strip()
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
                break
            else:
                print("E-mail inválido! Digite um e-mail válido.")

        telefone = input("Digite o telefone (com DDD): ").strip()

        cliente = Cliente(self.id_cliente, nome, cpf, email, telefone)
        self.lista_de_clientes.append(cliente)
        self.id_cliente += 1
        print(f"Cliente {nome} cadastrado com sucesso!")




    def verTodosClientes(self):
        if not self.lista_de_clientes:
            print("Nenhum cliente cadastrado.")
            return
        for cliente in self.lista_de_clientes:
            print(f"""
            ====================================
            Id: {cliente.id_cliente}
            Nome: {cliente.nome}
            Telefone: {cliente.telefone}
            E-mail: {cliente.email}
            CPF: {cliente.cpf}
            ====================================
            """)

    def editarCliente(self):
        cliente_nome = input("Digite o nome do cliente que deseja editar: ")
        cliente_encontrado = next((c for c in self.lista_de_clientes if c.nome == cliente_nome), None)

        if cliente_encontrado:
            while True:
                menu = input("""
                    Escolha o que quer atualizar:
                    1 - Nome
                    2 - CPF
                    3 - Telefone
                    4 - E-mail
                    0 - Voltar
                    """)
                
                match menu:
                    case "1":
                        cliente_encontrado.nome = input("Novo nome: ")
                    case "2":
                        cliente_encontrado.cpf = input("Novo CPF: ")
                    case "3":
                        cliente_encontrado.telefone = input("Novo telefone: ")
                    case "4":
                        cliente_encontrado.email = input("Novo e-mail: ")
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
        else:
            print("Cliente não encontrado.")

    def excluirCliente(self):
        if not self.autenticarFuncionario():
            print("Senha incorreta. Ação cancelada.")
            return
        cpf = input("Digite o CPF do cliente a ser removido: ")
        self.lista_de_clientes = [c for c in self.lista_de_clientes if c.cpf != cpf]
        print("Cliente removido com sucesso!")
    
    def adicionarQuarto(self):
        tipo_de_quarto = input("Digite o tipo de quarto (Solteiro, Casal, Suite): ")
        preco = float(input("Digite o preço da diária: "))
        quarto = Quarto(self.numero_quarto,tipo_de_quarto, preco)
        self.lista_de_quartos.append(quarto)
        print("Quarto adicionado com sucesso!")

    def verTodosQuartos(self):
        if not self.lista_de_quartos:
            print("Nenhum quarto cadastrado.")
            return
        for quarto in self.lista_de_quartos:
            print(f" Número: {quarto.numero_quarto} | Tipo: {quarto.tipo_de_quarto} | Preço: {quarto.preco} | Disponível: {quarto.disponibilidade}")
    
    def editarQuarto(self):
        numero_quarto = input("Digite o número do quarto que deseja editar: ")
        quarto_encontrado = next((q for q in self.lista_de_quartos if q.numero_quarto == numero_quarto), None)

        if quarto_encontrado:
            print("Quarto encontrado. Informações atuais:")
            print(f"Número: {quarto_encontrado.numero_quarto} | Tipo: {quarto_encontrado.tipo_de_quarto} | Preço: {quarto_encontrado.preco}")

            while True:
                menu = input("""
                    Escolha o que quer atualizar:
                    1 - Número do Quarto
                    2 - Tipo do Quarto (solteiro, casal, suíte)
                    3 - Preço
                    0 - Voltar
                    """)

                match menu:
                    case "1":
                        quarto_encontrado.numero_quarto = int(input("Novo número do quarto: "))
                    case "2":
                        quarto_encontrado.tipo_de_quarto = input("Novo tipo de quarto: ")
                    case "3":
                        quarto_encontrado.preco = float(input("Novo preço da diária: "))
                    case "0":
                        break
                    case _:
                        print("Opção inválida.")
        else:
            print("Quarto não encontrado.")

    def excluirQuarto(self):
        if not self.autenticarFuncionario():
            print("Senha incorreta. Ação cancelada.")
            return
        numero_quarto = int(input("Digite o numero do quarto a ser removido: "))
        self.lista_de_quartos = [q for q in self.lista_de_quartos if q.numero_quarto != numero_quarto]
        print("Quarto removido com sucesso!")

    def realizarReserva(self):
        numero_quarto = int(input("Digite o número do quarto para reservar: ")) 
        quarto = next((q for q in self.lista_de_quartos if q.numero_quarto == numero_quarto), None)

        if quarto and quarto.disponibilidade:
            quarto.disponibilidade = False
            CPF_cliente = input("Digite o CPF do cliente: ")
        
            cliente = next((c for c in self.lista_de_clientes if c.cpf == CPF_cliente), None)
            if not cliente:
                print("Cliente não encontrado.")
                return

            data = input("Digite a data da reserva (DD/MM/AAAA): ")
            reserva = Reserva(self.id_reserva, cliente.id_cliente, numero_quarto, data)
            self.lista_de_reservas.append(reserva)
            self.id_reserva += 1

            print(f"Reserva realizada para o quarto {quarto.numero_quarto}.")
        else:
            print("Quarto não disponível ou não encontrado.")


    def checkoutQuarto(self):
        numero_quarto = input("Digite o ID do quarto para liberar: ")
        quarto = next((q for q in self.lista_de_quartos if q.numero_quarto == numero_quarto), None)

        if quarto and not quarto.disponibilidade:
            quarto.disponibilidade = True
            self.lista_de_reservas = [r for r in self.lista_de_reservas if r.numero_quarto != numero_quarto]
            print(f"O quarto {quarto.numero_quarto} foi liberado.")
        else:
            print("Quarto já está disponível ou não encontrado.")

    def verStatusQuartos(self):
        if not self.lista_de_quartos:
            print("Nenhum quarto cadastrado.")
            return

        disponiveis = [q for q in self.lista_de_quartos if q.disponibilidade]
        ocupados = [q for q in self.lista_de_quartos if not q.disponibilidade]
    
        print("\n--- Quartos Disponíveis ---")
        for quarto in disponiveis:
            print(f"Número: {quarto.numero_quarto} | Tipo: {quarto.tipo_de_quarto} | Preço: R${quarto.preco:.2f}")
    
        print("\n--- Quartos Ocupados ---")
        for quarto in ocupados:
            print(f"Número: {quarto.numero_quarto} | Tipo: {quarto.tipo_de_quarto} | Preço: R${quarto.preco:.2f}")

    def verTodasReservas(self):
        if not self.lista_de_reservas:
            print("Nenhuma reserva cadastrada.")
            return  
        for reserva in self.lista_de_reservas:
            cliente = next((c for c in self.lista_de_clientes if c.id_cliente == reserva.id_cliente), None)
            quarto = next((q for q in self.lista_de_quartos if q.numero_quarto == reserva.numero_quarto), None)
            if cliente and quarto:
                print(f"""
====================================
ID Reserva: {reserva.id_reserva}
Cliente: {cliente.nome} (CPF: {cliente.cpf})
Quarto: {quarto.numero_quarto} - {quarto.tipo_de_quarto}
Data: {reserva.data}
====================================
""")
    def editarReserva(self):
        if not self.autenticarFuncionario():
            print("Senha incorreta. Ação cancelada.")
            return
        
        id_reserva = input("Digite o ID da reserva que deseja editar: ")
        reserva = next((r for r in self.lista_de_reservas if r.id_reserva == id_reserva), None)

        if reserva:
            nova_data = input("Digite a nova data da reserva (DD/MM/AAAA): ")
            reserva.data = nova_data
            print("Reserva atualizada com sucesso!")
        else:
            print("Reserva não encontrada.")

    def excluirReserva(self):
        if not self.autenticarFuncionario():
            print("Senha incorreta. Ação cancelada.")
            return

        id_reserva = input("Digite o ID da reserva que deseja excluir: ")
        reserva_existe = any(r.id_reserva == id_reserva for r in self.lista_de_reservas)

        if reserva_existe:
            self.lista_de_reservas = [r for r in self.lista_de_reservas if r.id_reserva != id_reserva]
            print("Reserva excluída com sucesso!")
        else:
            print("Reserva não encontrada.")
hotel = Hotel("00.000.000/0001-00")

while True:
    menu = input("""
    Escolha uma opção:
    1 - Gerenciar Clientes
    2 - Gerenciar Quartos
    3 - Gerenciar Reservas
    4 - Visualizar Status dos Quartos
    0 - Sair
    """)

    match menu:
        case "1":
            sub_opcao = input("""
            1 - Adicionar Cliente
            2 - Ver todos os Clientes
            3 - Editar Cliente
            4 - Excluir Cliente
            0 - Voltar
            """)
            
            match sub_opcao:
                case "1":
                    hotel.adicionarCliente()
                case "2":
                    hotel.verTodosClientes()
                case "3":
                    hotel.editarCliente()
                case "4":
                    hotel.excluirCliente()
                case "0":
                    continue
                case _:
                    print("Opção inválida.")

        case "2":
            sub_opcao = input("""
            1 - Adicionar Quarto
            2 - Ver todos os Quartos
            3 - Editar Quarto
            4 - Excluir Quarto
            0 - Voltar
            """)
            
            match sub_opcao:
                case "1":
                    hotel.adicionarQuarto()
                case "2":
                    hotel.verTodosQuartos()
                case "3":
                    hotel.editarQuarto()
                case "4":
                    hotel.excluirQuarto()
                case "0":
                    continue
                case _:
                    print("Opção inválida.")

        case "3":
            sub_opcao = input("""
            1 - Fazer uma nova reserva
            2 - Fazer checkout de quarto
            3 - Ver todas as reservas
            4 - Editar reserva
            5 - Excluir reserva
            0 - Voltar
            """)
            
            match sub_opcao:
                case "1":
                    hotel.realizarReserva()
                case "2":
                    hotel.checkoutQuarto()
                case "3":
                    hotel.verTodasReservas()
                case "4":
                    hotel.editarReserva()
                case "5":
                    hotel.excluirReserva()
                case "0":
                    continue
                case _:
                    print("Opção inválida.")

        case "4":
            hotel.verStatusQuartos()
        
        case "0":
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida.")