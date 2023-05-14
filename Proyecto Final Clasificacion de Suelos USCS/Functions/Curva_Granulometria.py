import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.path as mpath



def Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo):
  #Creando serie de Mallas
  Malla = pd.Series(["N4", 
                    "N10",
                    "N20",
                    "N30",
                    "N40",
                    "N60",
                    "N140",
                    "N200",
                    "Fondo"
                    ]) 

  #Creando serie de Aberturas
  Abertura = pd.Series([4.75, #Diametro en mm malla #4
                        2,    #Diametro en mm malla #10
                        0.850, #Diametro en mm malla #20
                        0.60, #Diametro en mm malla #30
                        0.425, #Diametro en mm malla #40
                        0.250, #Diametro en mm malla #60
                        0.106, #Diametro en mm malla #140
                        0.075, #Diametro en mm malla #200
                        np.nan]) #como esta se va a graficar debe ser numerica porque tambien se va a operar

  #_______________________________________________________________________________
  #Creando serie de Retenido en gramos
  Retenido_en_gramos = pd.Series([T4, #Retenido en malla 4
                        T10, #Retenido en malla 10
                        T20, #Retenido en malla 20
                        T30, #Retenido en malla 30 
                        T40, #Retenido en malla 40 
                        T60, #Retenido en malla 60
                        T140, #Retenido en malla 140
                        T200, #Retenido en malla 200
                        Fondo #Retenido en el fondo
                        ])   

  #Creando un frame que contenga las series creadas anteriormente
  Granulometria = pd.DataFrame({"Malla" : Malla, "Abertura" : Abertura, "Retenido (g)" : Retenido_en_gramos }) 

  #Definiendo la sumatoria de pesos retenidos para posteriores operaciones entre columnas
  Sumatoria_pesos_retenidos = Retenido_en_gramos.sum ()

  #Se crea el primer frame con las 3 series creadas anteriormente (únicamente con propósitos de ver si la info se veía bien, ahora al final es donde aparece la gráfica final)
  Granulometria = pd.DataFrame({"Malla" : Malla, 
                                "Abertura" : Abertura,
                                "Retenido (g)" : Retenido_en_gramos,  
                                }) 

  #Operación que indica que la Serie "%Retenido" del Frame Granulometría se realizará como la división de cada uno de los pesos retenidos por tamiz entre la sumatoria de los pesos *100 para que quede en %, con 2 decimales
  Granulometria["% Retenido"] = round((Granulometria["Retenido (g)"]/Sumatoria_pesos_retenidos)*100,2)
  #Granulometria["% Retenido"]

  Granulometria[" Retenido Acumulado (g)"] = Granulometria["Retenido (g)"].cumsum() #Creando serie que sume los valores retenidos de manera acumulativa mediante el comando cum.sum se logró hacer,
                                                                                                    #había intentado realizarlo por medio de operaciones entre la columna retenido duplicada, pero no daba resultado.

  #Operación que indica que la Serie "%Retenido Acumulado" del Frame Granulometría se realizará como la división de cada uno de los pesos retenidos acumulados por tamiz entre la sumatoria de los pesos *100 para que quede en %, con 2 decimales
  Granulometria["  % Retenido Acumulado"] = round((Granulometria[" Retenido Acumulado (g)"]/Sumatoria_pesos_retenidos)*100,2)

  #Operación que indica que la serie "% Pasa" del frame Granulometría se realiza como la resta entre 100% y el %Retenido acumulado de cada tamiz, con 2 decimales
  Granulometria["  % Pasa"] = round(100-Granulometria["  % Retenido Acumulado"],2)  

  #Aquí se hizo uso del comando append, para añadir un elemento a la columna de Masas retenidas, la cual indique la sumatoria total del valor
  #Python indica que .append será removido en el futuro y que hay que usar .concat. Lo había puesto más arriba, pero generaba problemas con las columnas en las operaciones, por lo que lo puse unicamente al final
  Retenido_en_gramos = Retenido_en_gramos._append (pd.Series(Sumatoria_pesos_retenidos, index=['Sum ']))
  #print (Retenido_en_gramos)

  #Frame Final con toda la información proporcionada
  #Granulometria 

  #Aquí se creó un frame que tuviera únicamente las series que se graficarán, con el fin de revisar si la información estaba correcta
  Curva_Granulometrica= pd.DataFrame({"Abertura" : Abertura, "% Pasa" : Granulometria["  % Pasa"] }) 



  #Comando para PLOTEAR la gráfica, tipo de Gráfico » Línea, Escala Logaritmica, Puntos de los markers » Hexagon 
  Granulometria.plot(kind = 'line', x='Abertura', y='  % Pasa', logx=True,
                    marker="h", markersize=6, markerfacecolor="dodgerblue", markeredgecolor="black", color="black", linewidth=2)



  #Grilla y su color
  plt.grid(color="k", lw=.2, ls='dashed',  which="both")

  #_____________________________________________________________________________ #AQUÍ OCURRE LA INTERPOLACIÓN, SE TOMÓ COMO GUÍA LA EXPLICACIÓN DEL CODIGO REALIZADO EN CLASE CON from scipy.interpolate import interp1d
  f = interp1d(Granulometria["  % Pasa"], Abertura) #Interpola entre %pasa y abertura

  #Aquí esta diciendo las coordenadas x que quiere conocer en y mediante interpolación
  Coordenada_y_D60 = 60 
  Coordenada_y_D30 = 30
  Coordenada_y_D10 = 10

  #Realiza interpolación, está yendo a buscar la coordenada x correspondiente a la y
  D60 = f(Coordenada_y_D60)
  D30 = f(Coordenada_y_D30)
  D10 = f(Coordenada_y_D10)

  # El primer paso es Calcular el Coeficiente de Uniformidad (Cu) y el Coeificiente de Curvatura (Cc) a partir de la interpolación de la curva granulométrica anterior
  tamiz_4 = Curva_Granulometrica.iloc[0]["% Pasa"]
  tamiz_200 = Curva_Granulometrica.iloc[7]["% Pasa"]
  Cu = D60/D10
  Cc = (D30**2)/(D60*D10)


  #Aquí limita a dos decimales las coordenadas obtenidas mediante interpolacion
  D60_2Decimales = '{:.2f}'.format(D60)
  D30_2Decimales = '{:.2f}'.format(D30)
  D10_2Decimales = '{:.2f}'.format(D10)
  

  #Ubicando los puntos en la grafica, tome x1 coord, y1 coord
  plt.scatter(D60, Coordenada_y_D60, marker='s', s=50, color='k', label='D60='+D60_2Decimales)
  plt.scatter(D30, Coordenada_y_D30, marker='<', s=50, color='k', label='D30='+D30_2Decimales)
  plt.scatter(D10, Coordenada_y_D10, marker='>', s=50, color='k', label='D10='+D10_2Decimales)
  plt.legend() 
  #____________________________________________________________________________________________________________

  #Títulos y Labels
  plt.xlabel("Abertura del Tamiz (mm)",fontsize=10)
  plt.ylabel("% Pasa",fontsize=10)
  plt.title("Curva Granulométrica",fontsize=14)

  #Funciones indicadas para invertir el eje X, de tal manera que quede de manera descendente la gráfica granulométrica
  ax = plt.gca()
  ax.invert_xaxis()

  #Límites de los ejes vertical y horizontal para que quede centrada la gráfica
  ax.set_xlim(6,0.07)
  ax.set_ylim(0,100)
  print(Granulometria)
  plt.show()














def Valores_Obtenidos_Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo):
  #Creando serie de Mallas
  Malla = pd.Series(["N4", 
                    "N10",
                    "N20",
                    "N30",
                    "N40",
                    "N60",
                    "N140",
                    "N200",
                    "Fondo"
                    ]) 

  #Creando serie de Aberturas
  Abertura = pd.Series([4.75, #Diametro en mm malla #4
                        2,    #Diametro en mm malla #10
                        0.850, #Diametro en mm malla #20
                        0.60, #Diametro en mm malla #30
                        0.425, #Diametro en mm malla #40
                        0.250, #Diametro en mm malla #60
                        0.106, #Diametro en mm malla #140
                        0.075, #Diametro en mm malla #200
                        np.nan]) #como esta se va a graficar debe ser numerica porque tambien se va a operar

  #_______________________________________________________________________________
  #Creando serie de Retenido en gramos
  Retenido_en_gramos = pd.Series([T4, #Retenido en malla 4
                        T10, #Retenido en malla 10
                        T20, #Retenido en malla 20
                        T30, #Retenido en malla 30 
                        T40, #Retenido en malla 40 
                        T60, #Retenido en malla 60
                        T140, #Retenido en malla 140
                        T200, #Retenido en malla 200
                        Fondo #Retenido en el fondo
                        ])   

  #Creando un frame que contenga las series creadas anteriormente
  Granulometria = pd.DataFrame({"Malla" : Malla, "Abertura" : Abertura, "Retenido (g)" : Retenido_en_gramos }) 

  #Definiendo la sumatoria de pesos retenidos para posteriores operaciones entre columnas
  Sumatoria_pesos_retenidos = Retenido_en_gramos.sum ()

  #Se crea el primer frame con las 3 series creadas anteriormente (únicamente con propósitos de ver si la info se veía bien, ahora al final es donde aparece la gráfica final)
  Granulometria = pd.DataFrame({"Malla" : Malla, 
                                "Abertura" : Abertura,
                                "Retenido (g)" : Retenido_en_gramos,  
                                }) 

  #Operación que indica que la Serie "%Retenido" del Frame Granulometría se realizará como la división de cada uno de los pesos retenidos por tamiz entre la sumatoria de los pesos *100 para que quede en %, con 2 decimales
  Granulometria["% Retenido"] = round((Granulometria["Retenido (g)"]/Sumatoria_pesos_retenidos)*100,2)
  Granulometria["% Retenido"]

  Granulometria[" Retenido Acumulado (g)"] = Granulometria["Retenido (g)"].cumsum() #Creando serie que sume los valores retenidos de manera acumulativa mediante el comando cum.sum se logró hacer,
                                                                                                    #había intentado realizarlo por medio de operaciones entre la columna retenido duplicada, pero no daba resultado.

  #Operación que indica que la Serie "%Retenido Acumulado" del Frame Granulometría se realizará como la división de cada uno de los pesos retenidos acumulados por tamiz entre la sumatoria de los pesos *100 para que quede en %, con 2 decimales
  Granulometria["  % Retenido Acumulado"] = round((Granulometria[" Retenido Acumulado (g)"]/Sumatoria_pesos_retenidos)*100,2)

  #Operación que indica que la serie "% Pasa" del frame Granulometría se realiza como la resta entre 100% y el %Retenido acumulado de cada tamiz, con 2 decimales
  Granulometria["  % Pasa"] = round(100-Granulometria["  % Retenido Acumulado"],2)  

  #Aquí se hizo uso del comando append, para añadir un elemento a la columna de Masas retenidas, la cual indique la sumatoria total del valor
  #Python indica que .append será removido en el futuro y que hay que usar .concat. Lo había puesto más arriba, pero generaba problemas con las columnas en las operaciones, por lo que lo puse unicamente al final
  Retenido_en_gramos = Retenido_en_gramos._append (pd.Series(Sumatoria_pesos_retenidos, index=['Sum ']))
  print (Retenido_en_gramos)


  #Aquí se creó un frame que tuviera únicamente las series que se graficarán, con el fin de revisar si la información estaba correcta
  Curva_Granulometrica= pd.DataFrame({"Abertura" : Abertura, "% Pasa" : Granulometria["  % Pasa"] }) 


  #_____________________________________________________________________________ #AQUÍ OCURRE LA INTERPOLACIÓN, SE TOMÓ COMO GUÍA LA EXPLICACIÓN DEL CODIGO REALIZADO EN CLASE CON from scipy.interpolate import interp1d
  f = interp1d(Granulometria["  % Pasa"], Abertura) #Interpola entre %pasa y abertura

  #Aquí esta diciendo las coordenadas x que quiere conocer en y mediante interpolación
  Coordenada_y_D60 = 60 
  Coordenada_y_D30 = 30
  Coordenada_y_D10 = 10

  #Realiza interpolación, está yendo a buscar la coordenada x correspondiente a la y
  D60 = f(Coordenada_y_D60)
  D30 = f(Coordenada_y_D30)
  D10 = f(Coordenada_y_D10)

  # El primer paso es Calcular el Coeficiente de Uniformidad (Cu) y el Coeificiente de Curvatura (Cc) a partir de la interpolación de la curva granulométrica anterior
  tamiz_4 = Curva_Granulometrica.iloc[0]["% Pasa"]
  tamiz_200 = Curva_Granulometrica.iloc[7]["% Pasa"]
  Cu = D60/D10
  Cc = (D30**2)/(D60*D10)
  
  return tamiz_4, tamiz_200, Cu,Cc,D30,D60,D10








