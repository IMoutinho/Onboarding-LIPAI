'''ex02 - Classe projeto'''


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

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


projeto1 = Projeto.from_string(
    "1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
projeto2 = Projeto("1", "Laboratório de Sistemas Embarcados", "Ana Maria")
projeto3 = Projeto("2", "Laboratório de Redes de Computadores", "Carlos Silva")
print(projeto1 == projeto2)
print(projeto1 == projeto3)

print(projeto1.codigo, projeto1.titulo, projeto1.responsavel)
print(projeto2.codigo, projeto2.titulo, projeto2.responsavel)
print(projeto3.codigo, projeto3.titulo, projeto3.responsavel)
