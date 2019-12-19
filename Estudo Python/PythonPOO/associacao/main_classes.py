from associacao.classes import Escritor
from associacao.classes import Caneta
from associacao.classes import MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta ('Bic')
maquina = MaquinaDeEscrever()

# associação
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
