'''ex04 - Classe projeto porem utilizando add'''

from ex01 import Aluno
from ex03 import Participacao


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(sep=',')
        return cls(codigo, titulo, responsavel)

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or valor.strip() == '' or not valor.isdigit():
            raise ValueError('Código não pode ser nulo.')
        self._codigo = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Título não pode ser nulo.')
        self._titulo = valor

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Responsável não pode ser nulo.')
        self._responsavel = valor

    def __eq__(self, value):
        if isinstance(value, Projeto):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f'Projeto(codigo={self.codigo}, titulo={self.titulo}, responsavel={self.responsavel})'


# Criando o projeto
projeto1 = Projeto.from_string(
    "1,Laboratório de Desenvolvimento de Software,Pedro Gomes")

# Criando alunos
aluno1 = Aluno('2021001', 'Maria Silva', 'maria@ufu.br')
aluno2 = Aluno('2021002', 'João Souza', 'joao@ufu.br')

# Adicionando participações
p1 = Participacao("101", "28/12/2025", "28/12/2026", aluno1, projeto1)
projeto1.add_participacao(p1)

p2 = Participacao("102", "28/12/2025", "28/12/2026", aluno2, projeto1)
projeto1.add_participacao(p2)
