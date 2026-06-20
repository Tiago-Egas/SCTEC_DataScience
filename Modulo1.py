# Aula 1
print("Meu primeiro programa em Python")

msg="Ola, mundo!"
print(msg)

# Aula 2
teste1=1
teste2=2
print(teste1+teste2)

teste3 = "Teste 3"
print(len(teste3))

nome = input("Digite seu nome: ")
print("Olá, " + nome + "! Bem-vindo ao Python!")

# Aula 3
idade = int(input("Digite sua idade: "))
anos = 2026 - idade
print("Você nasceu em " + str(anos) + ".")

# Aula 4
telefones = ["1234-5678", "9876-5432", "5555-5555"]
print(telefones[0])
telefones.append("1111-1111") # Adiciona um novo telefone ao final da lista
print(telefones)

telefones.insert(1, "2222-2222") # Insere um novo telefone na posição especificada
print(telefones)

telefones.remove("9876-5432") # Remove o telefone especificado da lista
print(telefones)

telefones.pop(0) # Remove o telefone na posição especificada
print(telefones)

contato = [("João", "1234-5678", "joao@email.com"), ("Maria", "9876-5432", "maria@email.com")] # Lista de contatos, onde cada contato é uma tupla com nome, telefone e email
print(contato[0]) # Acessa o nome do contato
print(contato[0][1]) # Acessa o telefone do primeiro contato
