"""aula 04 - propriedades"""

# Forma de controlar acesso aos atributos de uma instancia
# forma personalizada de alterar e obter valores dos atributos


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # getter
    @property
    def base(self):
        return self._base

    # setter
    @base.setter
    def base(self, valor):
        if valor <= 0:
            raise ValueError('A base deve ser maior que zero.')
        self._base = valor

    @property
    def altura(self):
        return self._altura

    # setter
    @altura.setter
    def altura(self, valor):
        if valor <= 0:
            raise ValueError('A altura deve ser maior que zero.')
        self._altura = valor

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


retangulo1 = Retangulo(10.5, 5.0)

print(retangulo1.base)

retangulo1.base = 30.0
print(retangulo1.base)
