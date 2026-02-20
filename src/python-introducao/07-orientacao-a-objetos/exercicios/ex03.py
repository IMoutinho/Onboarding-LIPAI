'''ex 03 - classe participação'''
from ex01 import Aluno
from ex02 import Projeto


class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if valor is None or valor.strip() == '' or not valor.isdigit():
            raise ValueError('Código não pode ser nulo.')
        self._codigo = valor

    @property
    def data_inicio(self):
        return self._data_inicio

    @data_inicio.setter
    def data_inicio(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Data de início não pode ser nulo.')
        self._data_inicio = valor

    @property
    def data_fim(self):
        return self._data_fim

    @data_fim.setter
    def data_fim(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Data de fim não pode ser nulo.')
        self._data_fim = valor

    @property
    def aluno(self):
        return self._aluno

    @aluno.setter
    def aluno(self, valor):
        if not valor:
            raise ValueError('Aluno não pode ser nulo.')
        self._aluno = valor

    @property
    def projeto(self):
        return self._projeto

    @projeto.setter
    def projeto(self, valor):
        if not valor:
            raise ValueError('Projeto não pode ser nulo.')
        self._projeto = valor

    def __repr__(self):
        return f'Participacao(codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto})'


projeto1 = Projeto.from_string(
    "1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
aluno1 = Aluno.from_string("2021001234,Gabriel Moutinho,gabriel@email.com")

projeto2 = Projeto("2", "Laboratório de Redes de Computadores", "Carlos Silva")
aluno2 = Aluno("2021005678", "Gabriel Carneiro", "carneiro@email.com")

participacao1 = Participacao("1", "2023-01-15", "2023-06-15", aluno1, projeto1)
participacao2 = Participacao("2", "2023-01-15", "2023-06-15", aluno2, projeto2)

print(
    f'Participação 1: Aluno(a): {participacao1.aluno.nome}, Projeto: {participacao1.projeto.titulo}')
print(
    f'Participação 2: Aluno(a): {participacao2.aluno.nome}, Projeto: {participacao2.projeto.titulo}')
