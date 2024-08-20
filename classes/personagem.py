class Personagem():
    nome = ""
    aceleracao = 0.0
    forca = 0.0
    destreza = 0.0
    agachado = False
    posicao =[0,0]

    def agachar(self):
        #instruções de agachamento
        if not self.agachado:
            self.agachado = True
    
    def mover(self, aceleracao):
        #instruções de correr
        self.posicao[0] =self.posicao[0] + aceleracao[0]
        self.posicao[1] = self.posicao[1] + aceleracao[1]

    
    def pular(self, aceleracao):
        #instruções de pular
        self.posicao[1] = self.posicao[1] + aceleracao[1] + 1.0


p1 = Personagem()
print(p1.posicao)
p1.mover([1,0])
p1.mover([1,0])
p1.mover([1,0])
print(p1.posicao)