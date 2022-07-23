class Etaria():

    def __init__(self,idade = 0,perfil = ''):
        self._idade = idade
        self._perfil = perfil

    # metodo get idade
    def get_idade(self):
        return self._idade
      
    # metodo set perfil
    def set_idade(self, x):
        self._idade = x

    #metodo construtor
    def construtor_perfil(self):
        if self._idade >= 0 and self._idade < 12:
            perfil = 'criança'

        elif self._idade >= 12 and self._idade < 19:
            perfil = 'adolescente'

        elif self._idade >= 19 and self._idade < 60:
            perfil = 'adulto'

        elif self._idade >= 60:
            perfil = 'idoso'
        else:
            print('idade fora de contexto')
        
        self._perfil = perfil
        return self._perfil
    

teste = Etaria()

# definindo a idade usando set
idade = int(input('Digite uma idade \n'))
teste.set_idade(idade)

# recuperando a idade usando get
print(teste.get_idade())

# definindo o perfil usando construtor
print(teste.construtor_perfil())
