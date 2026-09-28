Contador = 50
Excelente = 0 
Bom = 0
Ruim = 0
while Contador >0: 
    Excelente = Excelente 
    Bom = Bom
    Ruim = Ruim
    Nome = input ("Digite seu nome: ")
    Idade = int (input ("Digite sua idade: ")) 
    Opiniao = int (input ("Digite sua opinião sobre nosso atendimento: 1 - Excelente, 2 - Bom, 3 - Ruim: "))
    if Opiniao == 1:
        Excelente = Excelente + 1
    elif Opiniao == 2:
        Bom = Bom + 1
    elif Opiniao == 3:
        Ruim = Ruim + 1
    Contador = Contador - 1
print ("Total de opiniões Excelentes: ", Excelente)
print ("Total de opiniões Bom: ", Bom)
print ("Total de opiniões Ruim: ", Ruim)