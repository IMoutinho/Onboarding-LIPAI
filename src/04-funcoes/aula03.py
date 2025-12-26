#com o *args consigo passar maiores quantidades de argumentos
def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)

#com o **kwargs consigo passar diferentes argumentos, de acordo com o nome dado pra ele. Assim posso realizar ações diferentes de acordo com o argumento escolhido
def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value


world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')

world_cup_titles('Espanha', '2010')

final_price = calculate_price(100.0)
print(final_price)


final_price = calculate_price(100.0, discount=5.0)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)
