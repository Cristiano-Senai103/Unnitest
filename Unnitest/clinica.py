import sqlite3
from datetime import datetime

def criar_tabela_funcionarios(): 
    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especialidade TEXT NOT NULL,
        crm TEXT,
        coren TEXT
    )
    """)
    conexao.commit()
    conexao.close()

def criar_tabela_pacientes():
    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        telefone TEXT
    )
    """)
    conexao.commit()
    conexao.close()

def cadastrar_paciente(paciente):
    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO pacientes (nome, data_nascimento, telefone) VALUES (?, ?, ?)
    """, (paciente.nome, paciente.data_nascimento, paciente.telefone))
    conexao.commit()
    conexao.close()
    return cursor.lastrowid

def inserir_funcionario(funcionario):
    conexao = sqlite3.connect("clinica.db")
    cursor = conexao.cursor()
    if isinstance(funcionario, Medico):
        cursor.execute("""
        INSERT INTO funcionarios (nome, especialidade, crm) VALUES (?, ?, ?)
        """, (funcionario.nome, funcionario.especialidade, funcionario.crm))
    elif isinstance(funcionario, Enfermeiro):
        cursor.execute("""
        INSERT INTO funcionarios (nome, especialidade, coren) VALUES (?, ?, ?)
        """, (funcionario.nome, funcionario.especialidade, funcionario.coren))
    
    conexao.commit()
    conexao.close()
    return cursor.lastrowid

class Funcionario():
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def consulta_especialidade(self):
        print(f"{self.nome} e um medico")

class Paciente():
    def __init__(self, nome, data_nascimento, telefone):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

class Medico(Funcionario):
    def __init__(self, nome, especialidade, crm):
        super().__init__(nome, especialidade)
        self.crm = crm

    def realizar_exame(self, paciente):
        print(f"{self.nome} realizou um exame para {paciente}")

    def prescrever_medicamento(self, paciente, medicamento):
        print(f"{self.nome} prescreveu {medicamento} para {paciente}")

class Enfermeiro(Funcionario):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def aplicar_injecao(self, paciente, medicamento):
        print(f"{self.nome} aplicou {medicamento} no paciente {paciente}")

        

criar_tabela_funcionarios()
criar_tabela_pacientes()

paciente = Paciente("Pedro", "25/04/2001", "555 0987")
paciente2 = Paciente("Pedra", "24/05/2001", "555 1234")
cadastrar_paciente(paciente)
cadastrar_paciente(paciente2)

medico = Medico("Isabel", "Cardiologista", "CRM-965874")
medico2 = Medico("Isabelo", "Cardiologista", "CRM-475869")
inserir_funcionario(medico)
inserir_funcionario(medico2)

enfermeiro = Enfermeiro("Maria", "Enfermeira Chefe", "COREN-67890")
enfermeiro2 = Enfermeiro("Mario", "Enfermeiro Plantonista", "COREN-251463")
inserir_funcionario(enfermeiro)
inserir_funcionario(enfermeiro2)
    
administrativo = Funcionario("Tânia", "Atendente")
inserir_funcionario(administrativo)