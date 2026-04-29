preco = float(input("Digite o valor total da compra: "))

print("\nFormas de pagamento:")
print("1 - À vista (15% )")
print("2 - Débito (10%)")
print("3 - crédito (5%)")

codigo = int(input("Escolha a forma de pagamento: "))
if codigo == 1:
    desconto = 0.15
elif codigo == 2:
    desconto = 0.10
elif codigo == 3:
    desconto = 0.05
else: 
    print("Código de pagamento inválido!")
    exit()
valor_final = preco - (preco * desconto)
print(f"O valor final da compra é: R$ {valor_final:.2f}")
