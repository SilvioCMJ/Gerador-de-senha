from faker import Faker

#   puxando lib
gerador = Faker()

# gerando e exibindo senha
senha = gerador.password()
print(senha)
