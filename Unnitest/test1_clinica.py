import unittest
import sqlite3
from datetime import datetime
from clinica import Paciente, Medico, Enfermeiro
from clinica import criar_tabela_funcionarios, criar_tabela_pacientes, cadastrar_paciente, inserir_funcionario

class TestClinica(unittest.TestCase):

    def setUp(self):
        criar_tabela_funcionarios()
        criar_tabela_pacientes()

    def tearDown(self):
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        cursor.execute("DROP TABLE IF EXISTS funcionarios")
        cursor.execute("DROP TABLE IF EXISTS pacientes")
        conexao.commit()
        conexao.close()

    def test_criar_tabela_funcionarios(self):
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='funcionarios'")
        result = cursor.fetchone()
        conexao.close()
        self.assertEqual(result, ('funcionarios',))

    def test_criar_tabela_pacientes(self):
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='pacientes'")
        result = cursor.fetchone()
        conexao.close()
        self.assertEqual(result, ('pacientes',))

    def test_cadastrar_paciente(self):
        paciente = Paciente("Pedro", "18/12/2001", "555 0987")
        cadastrar_paciente(paciente)
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM pacientes WHERE id=1")
        result = cursor.fetchone()
        conexao.close()
        self.assertEqual(result, ('Pedro',))

    def test_inserir_funcionario(self):
        medico = Medico("Isabel", "Cardiologista", "555 0123")
        inserir_funcionario(medico)
        conexao = sqlite3.connect("clinica.db")
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM funcionarios WHERE id=1")
        result = cursor.fetchone()
        conexao.close()
        self.assertEqual(result, ('Isabel',))

    def test_funcionario_consulta_especialidade(self):
        medico = Medico("Isabel", "Cardiologista", "555 0123")
        medico.consulta_especialidade()
        self.assertTrue(True)

    def test_medico_realizar_exame(self):
        paciente = Paciente("Pedro", "6/01/1966", "555 0987")
        medico = Medico("Isabel", "Cardiologista", "555 0123")
        medico.realizar_exame(paciente.nome)
        self.assertTrue(True)

    def test_medico_prescrever_medicamento(self):
        paciente = Paciente("Pedro", "13/04/1996", "555 0987")
        medico = Medico("Isabel", "Cardiologista", "555 0123")
        medico.prescrever_medicamento(paciente.nome, "Aspirina")
        self.assertTrue(True)

    def test_enfermeiro_aplicar_injecao(self):
        paciente = Paciente("Pedro", "25/04/2001", "555 0987")
        enfermeiro = Enfermeiro("Maria", "Enfermeira Chefe", "67890")
        enfermeiro.aplicar_injecao(paciente.nome, "soro")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()