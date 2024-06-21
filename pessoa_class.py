class Pessoa:
    def __init__(self,_nome,_idade):
        self.nome = _nome
        self.idade = _idade
    def __repr__(self):
        return f"Pessoa: Nome: {self.nome} ; Idade: {self.idade}"