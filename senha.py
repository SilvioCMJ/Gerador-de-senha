from faker import Faker

#   puxando lib
f = Faker()
# gerando e exibindo senha
senha = f.password()
print(senha)
