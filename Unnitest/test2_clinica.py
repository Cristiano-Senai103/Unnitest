import unittest
import sqlite3
from clinica import criar_tabela_funcionarios, criar_tabela_pacientes, inserir_funcionario, cadastrar_paciente
from clinica import Paciente, Funcionario, Medico, Enfermeiro

class TestDatabase(unittest.TestCase):
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

    def test_database_connection(self):
        conexao = sqlite3.connect("clinica.db")
        self.assertIsNotNone(conexao)
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

class TestFuncionario(unittest.TestCase):
    def test_funcionario_cadastro(self):
        funcionario = Funcionario("Joana Costa", "Atendente")
        self.assertIsInstance(funcionario, Funcionario)

    def test_medico_cadastro(self):
        medico = Medico("Dr. João Bento", "Cardiologista", "CRM-123")
        self.assertIsInstance(medico, Medico)

    def test_enfermeiro_cadastro(self):
        enfermeiro = Enfermeiro("Janine Dolores", "Enfermeira Chefe", "COREN-456")
        self.assertIsInstance(enfermeiro, Enfermeiro)

class TestPaciente(unittest.TestCase):
    def test_paciente_cadastro(self):
        paciente = Paciente("Luis Carlos Bispo", " 18/10/1999", "123456789")
        self.assertIsInstance(paciente, Paciente)

class TestCrudOperadores(unittest.TestCase):
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

    def test_cadastrar_paciente(self):
        paciente = Paciente("Luis Carlos Bispo", " 18/10/1999", "123456789")
        paciente_id = cadastrar_paciente(paciente)
        self.assertGreater(paciente_id, 0)

    def test_inserir_funcionario(self):
        medico = Medico("Dr. João Bento", "Cardiologista", "CRM-123")
        funcionario_id = inserir_funcionario(medico)
        self.assertGreater(funcionario_id, 0)

if __name__ == "__main__":
    unittest.main()
