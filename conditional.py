temperature = 22

# condicional
if temperature > 30:
    print("It's a hot day!")
    print("Drink plenty of water")
elif temperature > 20: # intervalo -> [20,30]
    print("It's a nice day!")
elif temperature > 10: # intervalo -> [10,20]
    print("It's a bit cold")
else: # intervalo <= 10
    print("It's cold")


# linha de códico fora do bloco condicional
print(f"Temp: {temperature}")

