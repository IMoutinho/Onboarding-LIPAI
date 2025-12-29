'''ex01 - Classe Aluno com construtor alternativo e validação de atributos.'''


class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @classmethod
    def from_string(cls, rep_aluno):
        prontuario, nome, email = rep_aluno.split(sep=',')
        return cls(prontuario, nome, email)

    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Prontuário não pode ser nulo.')
        self._prontuario = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Nome não pode ser nulo.')
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor is None or valor.strip() == '':
            raise ValueError('Email não pode ser nulo.')
        self._email = valor

    def __eq__(self, value):
        if isinstance(value, Aluno):
            return self.prontuario == value.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)


aluno1 = Aluno.from_string("2021001234,Gabriel Moutinho,moutinho@email.com")
aluno2 = Aluno("2021001234", "Gabriel Antonio", "antonio@email.com")
aluno3 = Aluno("2021005678", "Gabriel Carneiro", "carneiro@email.com")
print(aluno1 == aluno2)

print(aluno1 == aluno3)

print(aluno1.nome, aluno1.prontuario, aluno1.email)
print(aluno2.nome, aluno2.prontuario, aluno2.email)
print(aluno3.nome, aluno3.prontuario, aluno3.email)
