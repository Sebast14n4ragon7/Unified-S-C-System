#INPUT VALORES ENTRADA

from Functions.Input_Values import *
T4,T10,T20,T30,T40,T60,T140,T200,Fondo = Inputs()

#CASAGRANDE
from Functions.Carta_Plasticidad import *


# GRANULOMETRIA
from Functions.Curva_Granulometria import *
tamiz_4, tamiz_200, Cu,Cc,D30,D60,D10 = Valores_Obtenidos_Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)



#ALGORITMO CLASIFICACIÓN USCS
from Functions.Clasificacion import *
Clasificacion_USCS(tamiz_200, tamiz_4, Cu,Cc,cartaPlasticidad,Granulometria,T4,T10,T20,T30,T40,T60,T140,T200,Fondo)

