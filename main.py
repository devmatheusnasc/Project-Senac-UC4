
from tkinter import messagebox

import mysql.connector
from mysql.connector import errorcode

try:
    db_connection = mysql.connector.connect(host='localhost', user='root',
                                                 password='250999', database='projeto_integrador')

    print("Database conectado!")
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database nao existe")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("nome do usuario ou senha invalidos")
    else:
        print(db_connection.close())
cursor = db_connection.cursor()

def CadastrarVendedor():
    print("\nCadastrar Vendedor: ")
    nome = input("Digite o nome do vendedor: ")
    cpf = input("Digite o cpf: ")

    sql = ("INSERT INTO `projeto_integrador`.`Vendedor` (`nome`, `cpf`) VALUES (" + "'" + nome + "','" + cpf + "'" + ");")
    cursor.execute(sql)
    db_connection.commit()

    messagebox.showinfo("Projeto Integrador", "Vendedor cadastrado com Sucesso !")

def CadastrarCliete():
    print("\nCadastrar Cliente: ")

    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone")
    nomeEmpresa = input("Digite o nome da empresa: ")
    cpf = input("Digite o cpf: ")

    sql = ("INSERT INTO `projeto_integrador`.`Cliente` (`nome`, `email`, `telefone`, `nome_empresa`, `cpf`) "
           "VALUES (" + "'" + nome + "','" + email + "','" + telefone + "','" + nomeEmpresa + "','" + cpf + "'" + " );")
    cursor.execute(sql)
    db_connection.commit()

    messagebox.showwarning("Projeto Integrador", "Cliente cadastrado com Sucesso !")

def CadastrarPeca():
    print("\nCadastrar Peças: ")

    nome = input("Digite o nome da peça: ")
    codigo = input("Digite o código peça: ")
    qnt = input("Digite a quantidade de peças: ")

    sql = ("INSERT INTO `projeto_integrador`.`Pecas` (`nome`, `codigo`, `qnt_estoque`) "
           "VALUES (" + "'" + nome + "','" + codigo + "','" + qnt + "'" + " );")
    cursor.execute(sql)
    db_connection.commit()
    messagebox.showinfo("Projeto Integrador", "Peça cadastrada com Sucesso !")

def CadastrarVeiculo():
    print("\nCadastrar Veiculos: ")

    nome = input("Digite o nome do veiculo: ")
    placa = input("Digite a placa do veiculo: ")
    marca = input("Digite a marca do veiculo: ")
    cor = input("Digite a cor do veiculo: ")
    modelo = input("Digite o modelo do veiculo: ")

    sql = ("INSERT INTO `projeto_integrador`.`Veiculos` (`placa`, `nome`, `marca`, `cor`, `modelo`) "
        "VALUES (" + "'" + placa + "','" + nome + "','" + marca + "','" + cor + "','" + modelo +"'" + " );")
    cursor.execute(sql)
    db_connection.commit()

    messagebox.showinfo("Projeto Integrador", "Veiculo cadastrado com Sucesso !")

#Listagem de dados

def ListarVendedorPorId():

    id = input("Digite o ID do Vendedor: ")

    sql = ("SELECT `nome`, `cpf`, `id_vendedor` FROM `projeto_integrador`.`Vendedor` WHERE  `id_vendedor`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:

        messagebox.showinfo("Projeto Integrador", "VENDEDOR INEXISTENTE !")

    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("CPF: ", registro[1])
            print("ID: ", registro[2])

def ListarVendedores():

    sql = ("SELECT `nome`, `cpf`, `id_vendedor` FROM `projeto_integrador`.`Vendedor`;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    for registro in registros:
        print("\nNOME: ", registro[0])
        print("CPF: ", registro[1])
        print("ID: ", registro[2])

def ListarClientePorId():
    id = input("Digite o ID do Cliente: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Cliente` WHERE  `id_cliente`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showwarning("Projeto Integrador", "CLIENTE INEXISTENTE !")

    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("EMAIL: ", registro[1])
            print("Telefone: ", registro[2])
            print("NOME_EMPRESA: ", registro[3])
            if registro[5] is not None:
                print("CPF: ", registro[5])
            if registro[6] is not None:
                print("CNPJ: ", registro[6])
            print("ID: ", registro[4])

def ListarClientes():

    sql = ("SELECT * FROM `projeto_integrador`.`Cliente`;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    for registro in registros:
        print("\nNOME: ", registro[0])
        print("EMAIL: ", registro[1])
        print("Telefone: ", registro[2])
        print("NOME_EMPRESA: ", registro[3])
        if registro[5] is not None:
            print("CPF: ", registro[5])
        if registro[6] is not None:
            print("CNPJ: ", registro[6])
        print("ID: ", registro[4])

def ListarPecaPorId():
    id = input("Digite o ID da Peça: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Pecas` WHERE  `id_peca`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "Não Contém essa Peça ou Está em Falta !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("CÓDIGO: ", registro[2])
            print("QNT_ESTOQUE: ", registro[3])
            print("ID: ", registro[1])

def ListarPecas():

    sql = ("SELECT * FROM `projeto_integrador`.`Pecas`;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    for registro in registros:
        print("\nNOME: ", registro[0])
        print("CÓDIGO: ", registro[2])
        print("QNT_ESTOQUE: ", registro[3])
        print("ID: ", registro[1])

def ListarVeiculoPorId():
    id = input("Digite a Placa do Veiculo: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Veiculos` WHERE  `placa`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "Veículo Não Encontrado !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[1])
            print("MARCA: ", registro[2])
            print("Modelo: ", registro[4])
            print("COR: ", registro[3])
            print("PLACA: ", registro[0])


def ListarVeiculos():

    sql = ("SELECT * FROM `projeto_integrador`.`Veiculos`;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    for registro in registros:
        print("\nNOME: ", registro[1])
        print("MARCA: ", registro[2])
        print("Modelo: ", registro[4])
        print("COR: ", registro[3])
        print("PLACA: ", registro[0])


def AtualizarVendedor():
    id = input("Digite o ID do Vendedor: ")

    sql = ("SELECT `nome`, `cpf`, `id_vendedor` FROM `projeto_integrador`.`Vendedor` WHERE  `id_vendedor`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()
    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "VENDEDOR INEXISTENTE !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("CPF: ", registro[1])
            print("ID: ", registro[2])
        update = input("\nDigite O que deseja atualizar: \n 1 - NOME:  \n 2 - CPF: ")

        if update == "1":
            nome = input("Novo Nome: ")
            sql = ("UPDATE `projeto_integrador`.`Vendedor` SET `nome`='" + nome + "' WHERE  `id_vendedor`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "NOME ATUALIZADO COM SUCESSO !")

        elif update == "2":
            cpf = input("Novo CPF: ")
            sql = ("UPDATE `projeto_integrador`.`Vendedor` SET `cpf`='" + cpf + "' WHERE  `id_vendedor`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "CPF ATUALIZADO COM SUCESSO !")

        else:
            print("Opção Inválida")


def AtualizarCliente():
    id = input("Digite o ID do Cliente: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Cliente` WHERE  `id_cliente`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "CLIENTE INEXISTENTE !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("EMAIL: ", registro[1])
            print("Telefone: ", registro[2])
            print("NOME_EMPRESA: ", registro[3])
            if registro[5] is not None:
                print("CPF: ", registro[5])
            if registro[6] is not None:
                print("CNPJ: ", registro[6])
            print("ID: ", registro[4])

        update = input("\nDigite O que deseja atualizar: \n 1 - NOME:  \n 2 - EMAIL:  \n 3 - TELEFONE:"
                       "  \n 4 - NOME_EMPRESA:  \n 5 - CPF/CNPJ: ")

        if update == "1":
            nome = input("Novo Nome: ")
            sql = ("UPDATE `projeto_integrador`.`Cliente` SET `nome`='" + nome + "' WHERE  `id_cliente`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "NOME ATUALIZADO COM SUCESSO !")
        elif update == "2":
            email = input("Novo Email: ")
            sql = ("UPDATE `projeto_integrador`.`Cliente` SET `email`='" + email + "' WHERE  `id_cliente`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "EMAIL ATUALIZADO COM SUCESSO !")
        elif update == "3":
            telefone = input("Novo Telefone: ")
            sql = ("UPDATE `projeto_integrador`.`Cliente` SET `telefone`='" + telefone + "' WHERE  `id_cliente`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "TELEFONE ATUALIZADO COM SUCESSO !")
        elif update == "4":
            nomeEmpresa = input("Novo Nome_Empresa: ")
            sql = ("UPDATE `projeto_integrador`.`Cliente` SET `nome_empresa`='" + nomeEmpresa + "' WHERE  `id_cliente`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "NOME DA EMPRESA ATUALIZADO COM SUCESSO !")
        elif update == "5":
            if registro[5] is not None:
                cpf = input("Novo Cpf: ")
                sql = ("UPDATE `projeto_integrador`.`Cliente` SET `cpf`='" + cpf + "' WHERE  `id_cliente`= " + id + " ;")
                cursor.execute(sql)
                db_connection.commit()
                messagebox.showinfo("Projeto Integrador", "CPF ATUALIZADO COM SUCESSO !")
            else:
                cnpj = input("Novo Cnpj: ")
                sql = ("UPDATE `projeto_integrador`.`Cliente` SET `cnpj`='" + cnpj + "' WHERE  `id_cliente`= " + id + " ;")
                cursor.execute(sql)
                db_connection.commit()
                messagebox.showinfo("Projeto Integrador", "CNPJ ATUALIZADO COM SUCESSO !")
        else:
            print("Opção Inválida")

def AtualizarPeca():
    id = input("Digite o ID da Peça: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Pecas` WHERE  `id_peca`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "Não Contém essa Peça ou Está em Falta !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("CÓDIGO: ", registro[2])
            print("QNT_ESTOQUE: ", registro[3])
            print("ID: ", registro[1])
        update = input("\nDigite O que deseja atualizar: \n 1 - NOME:  \n 2 - CÓDIGO:  \n 3 - QNT_ESTOQUE: ")

        if update == "1":
            nome = input("Novo Nome: ")
            sql = ("UPDATE `projeto_integrador`.`Pecas` SET `nome`='" + nome + "' WHERE  `id_peca`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "NOME ATUALIZADO COM SUCESSO !")

        elif update == "2":
            codigo = input("Novo Código: ")
            sql = ("UPDATE `projeto_integrador`.`Pecas` SET `codigo`='" + codigo + "' WHERE  `id_peca`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "CÓDIGO ATUALIZADO COM SUCESSO !")
        elif update == "3":
            qntEstoque = input("Nova Quantidade em Estoque: ")
            sql = ("UPDATE `projeto_integrador`.`Pecas` SET `qnt_estoque`='" + qntEstoque + "' WHERE  `id_peca`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "QUANTIDADE DE ESTOQUE ATUALIZADO COM SUCESSO !")
        else:
            print("Opção Inválida")

def AtualizarVeiculo():
    id = input("Digite a Placa do Veiculo: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Veiculos` WHERE  `placa`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "Veículo Não Encontrado !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[1])
            print("MARCA: ", registro[2])
            print("Modelo: ", registro[4])
            print("COR: ", registro[3])
            print("PLACA: ", registro[0])

        update = input("\nDigite O que deseja atualizar: \n 1 - COR: ")

        if update == "1":
            cor = input("\nNova Cor: ")
            sql = ("UPDATE `projeto_integrador`.`Veiculos` SET `cor`='" + cor + "' WHERE  `placa`= " + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "COR ATUALIZADA COM SUCESSO !")

        else:
            print("Opção Inválida")




def DeleteVendedor():
    id = input("Digite o ID do Vendedor: ")

    sql = ("SELECT `nome`, `cpf`, `id_vendedor` FROM `projeto_integrador`.`Vendedor` WHERE  `id_vendedor`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:

        messagebox.showinfo("Projeto Integrador", "VENDEDOR INEXISTENTE !")

    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("CPF: ", registro[1])
            print("ID: ", registro[2])

        idverificador = input("\nConfirme o ID do Vendedor: ")
        if(idverificador == id ):
            sql = ("DELETE FROM `projeto_integrador`.`Vendedor` WHERE `id_vendedor`=" + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "VENDEDOR DELETADO COM SUCESSO!")

def DeleteCliente():
    id = input("Digite o ID do Cliente: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Cliente` WHERE  `id_cliente`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showwarning("Projeto Integrador", "CLIENTE INEXISTENTE !")

    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("EMAIL: ", registro[1])
            print("Telefone: ", registro[2])
            print("NOME_EMPRESA: ", registro[3])
            if registro[5] is not None:
                print("CPF: ", registro[5])
            if registro[6] is not None:
                print("CNPJ: ", registro[6])
            print("ID: ", registro[4])

        idverificador = input("\nConfirme o ID do Cliente: ")
        if(idverificador == id ):
            sql = ("DELETE FROM `projeto_integrador`.`Cliente` WHERE `id_cliente`=" + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "CLIENTE DELETADO COM SUCESSO!")


def DeletePeca():
    id = input("Digite o ID da Peça: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Pecas` WHERE  `id_peca`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "Não Contém essa Peça ou Está em Falta !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[0])
            print("CÓDIGO: ", registro[2])
            print("QNT_ESTOQUE: ", registro[3])
            print("ID: ", registro[1])

        idverificador = input("\nConfirme o ID da Peça: ")
        if(idverificador == id ):
            sql = ("DELETE FROM `projeto_integrador`.`Pecas` WHERE `id_peca`=" + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "PEÇA DELETADA COM SUCESSO!")



def DeleteVeiculo():
    id = input("Digite a Placa do Veiculo: ")

    sql = ("SELECT * FROM `projeto_integrador`.`Veiculos` WHERE  `placa`=" + id + " ;")
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) == 0:
        messagebox.showinfo("Projeto Integrador", "Veículo Não Encontrado !")
    else:
        for registro in registros:
            print("\nNOME: ", registro[1])
            print("MARCA: ", registro[2])
            print("Modelo: ", registro[4])
            print("COR: ", registro[3])
            print("PLACA: ", registro[0])

        idverificador = input("\nConfirme a Placa Do Veículo: ")
        if(idverificador == id ):
            sql = ("DELETE FROM `projeto_integrador`.`Veiculos` WHERE `placa`=" + id + " ;")
            cursor.execute(sql)
            db_connection.commit()
            messagebox.showinfo("Projeto Integrador", "VEÍCULO DELETADO COM SUCESSO!")

cont = 1
while (cont > 0):

    menuOp = input("\n\n\n****** ***  MENU DE OPÇÔES  *** *******\n\n"
               " 1 - Cadastrar Vendedor\n 2 - Cadastrar Cliete\n 3 - Cadastrar Peça \n 4 - Cadastrar Veiculo\n"
               " 5 - Listar Vendedor\n 6 - Listar Todos Vendedores\n 7 - Listar Cliente\n 8 - Listar Todos Clientes\n"
               " 9 - Listar Peça\n 10 - Listar Todas Peças\n 11 - Listar Veiculo\n 12 -  Listar Todos Veiculos\n"
               " 13 - Atualizar Vendedor\n 14 - Atualizar Cliente\n 15 - Atualizar Peça\n 16 - Atualizar Veiculo\n"
               " 17 - Deletar Vendedor\n 18 - Deletar Cliente\n 19 - Deletar Peça\n 20 - Deletar Veículo\n"
               " 0 - Sair\n\n\n")

    if menuOp == "1":
        CadastrarVendedor()

    elif menuOp == "2":
        CadastrarCliete()
    elif menuOp == "3":
        CadastrarPeca()
    elif menuOp == "4":
        CadastrarVeiculo()
    elif menuOp == "5":
        ListarVendedorPorId()
    elif menuOp == "6":
        ListarVendedores()
    elif menuOp == "7":
        ListarClientePorId()
    elif menuOp == "8":
        ListarClientes()
    elif menuOp == "9":
        ListarPecaPorId()
    elif menuOp == "10":
        ListarPecas()
    elif menuOp == "11":
        ListarVeiculoPorId()
    elif menuOp == "12":
        ListarVeiculos()
    elif menuOp == "13":
        AtualizarVendedor()
    elif menuOp == "14":
        AtualizarCliente()
    elif menuOp == "15":
        AtualizarPeca()
    elif menuOp == "16":
        AtualizarVeiculo()
    elif menuOp == "17":
        DeleteVendedor()
    elif menuOp == "18":
        DeleteCliente()
    elif menuOp == "19":
        DeletePeca()
    elif menuOp == "20":
        DeleteVeiculo()
    elif menuOp == "0":
        exit()
else:
    print("Opção Inválida, Encerramento do Sistema !")