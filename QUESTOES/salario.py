#entrada de dados
cargo= input("digite o cargo:")
salario = float(input("digite o salario:"))

#verificaçao do cargo
if cargo == "programador de sistemas":
    novo_salario= salario + (salario + 0.30)
    print(f"o novo salario é: R$ {novo_salario:.2f}")
elif cargo == "analista de sistemas":
    novo_salario= salario + (salario + 0.20)
    print(f"o novo salario é: R$ {novo_salario:.2f}")
elif cargo == "tecnico de informatica":
    novo_salario= salario + (salario + 0.15)
    print(f"o novo salario é: R$ {novo_salario:.2f}")
else:
    print("cargo inválido.")