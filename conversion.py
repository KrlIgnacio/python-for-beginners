import datetime

birth_year = input('Enter your birth year: ')
# pegando a data atual pelo datetime
date = datetime.date.today()
# pegando o ano atual
year = date.year
# calculo idade e convertendo string p/ inteiro
age =  year -  int(birth_year)

print(f'Age: {age}')

# funções integradas para converter tipos
float()
int()
str()
bool()