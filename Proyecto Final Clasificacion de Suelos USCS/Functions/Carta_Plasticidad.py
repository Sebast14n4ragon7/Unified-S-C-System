import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.path as mpath

def cartaPlasticidad(Limite_liquido,Indice_plasticidad):
  LL= [] #Listas vacías para guardar los valores
  IP= []

  for x in range(101):
      LL.append(x) # Agregar el valor de i a la lista LL
      IP.append(x) # Agregar el valor de i a la lista IP

  # Crear los arrays de LL (Límite Liquido) e IP (Indice de Plasticidad)
  LL = np.array(LL)
  IP = np.array(IP)


  LL, IP = np.meshgrid(LL, IP) # Mediante este comando se crea la matriz de coordenadas

  #CREACIÓN DE FUNCIONES QUE DEFINEN LINEAS U, A
  def linea_A(LL):
      return 0.72*(LL-20) #Función de la Línea A

  def linea_U(LL):
      return 0.9*(LL-8) #Función de la Línea U


  # Obteniendo los valores de las líneas A y U
  A = IP-linea_A(LL)
  U = IP-linea_U(LL)

  # Crear la figura y el eje, y el tamaño de la gráfica
  fig, ax = plt.subplots(figsize=(15, 13)) #Aquí de una vez se pone el tamaño de la grafica que se desea

  # Gráfica de las lineas A y U
  ax.contour(LL, IP, A, levels=[0], colors='indigo') #Al graficar la función con ax.contour el Levels=[0] significa que solo quiero dibujar las líneas de contorno donde los valores de Z son iguales a 0 (2D)
  ax.contour(LL, IP, U, levels=[0], colors='midnightblue')
  plt.axvline(x = 50, color = 'orangered', label = 'Línea B') # Se crea la línea B, que separa los suelos de la siguiente forma: 
                                                                  #A la izquierda de la línea están los suelos de baja plasticidad (L) ➢ A la derecha de la línea están los suelos alta plasticidad (H)



  #_________________________________________
  #Superglow up visto en clase para optimizar el Código
  region_MH = np.array([[50,0], [50,22], [100,58], [100,0]])
  region_ML = np.array([[25.5,4], [12.4,4], [8,0], [20,0], [50,0], [50,22]])
  region_CH = np.array([[50,22], [100,58], [100,60], [75,60], [50,38]])
  region_CL_ML = np.array([[29.5,7], [15.7,7], [12.4,4], [25.5,4]])
  region_CL = np.array([[15.7,7], [29.5,7], [50,22], [50,38]])

  #Aqui se usa la funcion mpath.path, para poderla importar hay la libreria mpath, para que
  #esas coordenadas se conviertan en una región

  path_MH = mpath.Path(region_MH)
  path_CH = mpath.Path(region_CH)
  path_CL = mpath.Path(region_CL)
  path_CL_ML = mpath.Path(region_CL_ML)
  path_ML = mpath.Path(region_ML)

  point = np.array([Limite_liquido,Indice_plasticidad]) #Colocar el punto que viene como variable
  #Esta verificando en que zona está ubicado, si arriba si abajo y demás
  if path_MH.contains_point(point):
      print('El punto se encuentra en la zona MH')
  elif path_CH.contains_point(point):
      print('El punto se encuentra en la zona CH')
  elif path_CL.contains_point(point):
      print('El punto se encuentra en la zona CL')
  elif path_CL_ML.contains_point(point):
      print('El punto se encuentra en la zona CL-ML')
  elif path_ML.contains_point(point):
      print('El punto se encuentra en la zona ML')
  else:
      print('El punto no se encuentra en la carta de plasticidad')

  d=[50,50,100,100]
  e=[0,22,58,0]
  plt.fill(d,e,'thistle')

  f=[25.5,12.4,8,20,50,50]
  g=[4,4,0,0,0,22]
  plt.fill(f,g,'paleturquoise')

  h=[50,100,100,50]
  i=[22,58,83,38]
  plt.fill(h,i,'lightgreen')

  j=[29.5,15.7,12.4,25.5]
  k=[7,7,4,4]
  plt.fill(j,k,'salmon')

  l=[15.7,29.5,50,50]
  m=[7,7,22,38]
  plt.fill(l,m,'bisque')
  #_________________________________________

  # APARTADO ESTÉTICO, GRILLA Y LEYENDAS

  plt.xlabel("Límite Líquido LL (%)",fontsize=15)
  plt.ylabel("Índice de Plasticidad IP (%)",fontsize=15)
  plt.title("Carta de Plasticidad de Casagrande",fontsize=15)
  plt.grid(color='k',lw=.2, ls='dashed')
  # plt.legend() NO VOY A PONER LEYENDAS, SINO SOLAMENTE TEXTO EN EL GRAFICO FIJO


  # APARTADO DONDE SE GRAFICA LA ESPECIFICAMENTE LA COORDENADA INPUT DEL USUARIO (LL,LP)
  plt.plot(Limite_liquido,Indice_plasticidad,'db') #db= diamond+blue
  plt.vlines(Limite_liquido,0,100,'darkgray','-.')
  plt.annotate(' LL ',(Limite_liquido,55))
  plt.annotate(' IP ', (20,Indice_plasticidad + 2))
  plt.hlines(Indice_plasticidad,0,100,'darkgray','--')


  # DIBUJANDO LÍNEAS DE LA ZONA CL-ML
            #LINEA INFERIOR
  x1 = 11.2/0.9 # Obtenido de despejar en que momento la línea U IP=0.9(LL-8) es 4, ya que la línea inferior de CL-ML está en IP=4
  x2 = 18.4/0.72 # Obtenido de despejar en que momento la línea A IP=0.72(LL-20) es 4, ya que la línea inferior de CL-ML está en IP=4
  y = 4 # El valor de y de la línea horizontal

  plt.plot([x1, x2], [y, y], color="purple", linestyle="--")
            #LINEA SUPERIOR
  x3 = 14.2/0.9 # Obtenido de despejar en que momento la línea U IP=0.9(LL-8) es 7, ya que la línea superior de CL-ML está en IP=7
  x4 = 21.4/0.72 # Obtenido de despejar en que momento la línea A IP=0.72(LL-20) es 4, ya que la línea superior de CL-ML está en IP=7
  y = 7 # El valor de y de la línea horizontal
  plt.plot([x3, x4], [y, y], color="purple", linestyle="--")

  # Voy a poner el texto del nombre de cada Zona, fue demasiado más tedioso hacerlo así, pero era la única forma que encontre para poner el texto en ubicación requerida
  plt.text(43, 95, 'LÍNEA B', fontsize=13, color='black')
  plt.text(44, 93, 'LL=50', fontsize=13, color='black')
  plt.text(70, 45, 'CH', fontsize=13, color='black')
  plt.text(75, 25, 'MH', fontsize=13, color='black')
  plt.text(18, 5, 'CL - ML', fontsize=13, color='black')
  plt.text(85, 45, 'LÍNEA A', fontsize=13, color='black')
  plt.text(83, 43, 'IP=0.72(LL-20)', fontsize=13, color='black')
  plt.text(39, 20, 'CL', fontsize=13, color='black')
  plt.text(37, 6, 'ML', fontsize=13, color='black')
  plt.text(36, 35, 'LÍNEA U', fontsize=13, color='black')
  plt.text(35, 33, 'IP=0.9(LL-8)', fontsize=13, color='black')
  plt.text(20, 60, 'NO EXISTE', fontsize=13, color='black')

  plt.show()


