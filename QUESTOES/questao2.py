num1= float(input("Digite o primeiro número: "))
num2= float(input("Digite o segundo número: "))

print("\nMenu:")
print("1 - Média ponderada (pesos 2 e 3)")
print("2 - Quadrado da soma")
print("3 - cubo do menor numero")

opcao = int(input("Escolha a opcao:"))

if opcao == 1:
    media_ponderada = (num1 * 2 + num2 * 3) / 5
    print(f"A média ponderada é: {media_ponderada}")
elif opcao == 2:
    quadrado_da_soma = (num1 + num2) ** 2
    print(f"O quadrado da soma é: {quadrado_da_soma}")
elif opcao == 3:
    cubo_do_menor = min(num1, num2) ** 3
    print(f"O cubo do menor número é: {cubo_do_menor}")
else:
    print("Opção inválida!")