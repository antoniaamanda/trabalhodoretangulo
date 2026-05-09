# login 1
usuario1= "procopio"
senha1= 12345
# login 2
usuario2= "paiva"
senha2= 54321

#entrada de dados
usuario= input("digite o nome de usuario: ")
senha= input("digite a senha: ")

#verificacao de login
if (usuario == usuario1 and senha == senha1) or (usuario == usuario2 and senha == senha2):
    print("seja bem vindo!")
else:
    print("usuario ou senha não conferem.")