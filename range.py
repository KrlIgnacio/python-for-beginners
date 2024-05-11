# sequencia de numeros ate o num 5 -> [0 < 5]
numbers = range(5)
for numb in numbers:
    print(numb)
    
print("\n")    

# dois parametros
x = range(6, 12)
for n in x:
    print(n)
    
print("\n")  
    
# tres parametros - intervalo e qtd de numeros para pular no intervalo
z = range(5, 10, 2) # pule 2 numeros na sequencia de [5 < 10]
for num in z:
    print(num)

print("\n") 

# range dentro do loop
for number in range(48, 53):
    print(number)