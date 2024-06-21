from pessoa_class import Pessoa
pessoa1 = Pessoa("Zeca", 22)
pessoa2 = Pessoa("Joana", 60)

def salva_pessoa(pessoa:Pessoa):
    with open('atividade_salvar_lista/pessoas.txt', 'a') as file:
        file.write(f'Gato: nome:{pessoa.nome};idade:{pessoa.idade}\n')

def salva_lista_pessoa(list_pessoa:list[Pessoa]):
    with open ("atividade_salvar_lista/pessoas.txt", 'r') as file:
        for pessoa in list_pessoa:
            salva_pessoa(pessoa)
        
list_pessoa = [pessoa1, pessoa2]
salva_lista_pessoa(list_pessoa)