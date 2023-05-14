import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import matplotlib.path as mpath


def Clasificacion_USCS(tamiz_200, tamiz_4, Cu,Cc,cartaPlasticidad,Granulometria,T4,T10,T20,T30,T40,T60,T140,T200,Fondo):
  #CONDICIÓN A. Carta de Plasticidad
  if 50 <= tamiz_200 <= 100: #SUELOS FINOS
  #___________________________________________________
  #INPUT LL y IP, Con esto se garantiza que pida el Input únicamente cuando sea necesario en el código
    Limite_liquido_valido = False
    while not Limite_liquido_valido:
        try:
            Limite_liquido = float(input("Ingresa el Límite Liquido: "))
            if 8 <= Limite_liquido <= 100:
                Limite_liquido_valido = True
            else:
                print("El Límite Liquido debe ser un valor entre 8% y 100%. Inténtalo de nuevo.")
        except ValueError:
            print("Ingresar un valor numérico valido")

    Indice_plasticidad_valido = False
    while not Indice_plasticidad_valido:
        try:
            Indice_plasticidad = float(input("Ingresa el Indice de Plasticidad: "))
            if 0 <= Indice_plasticidad <= 100:
                Indice_plasticidad_valido = True
            else:
                print("El Indice de Plasticidad debe ser un valor entre 1% y 100%. Inténtalo de nuevo.")
        except ValueError:
            print("Ingresar un valor numérico valido")

  #___________________________________________________
    if 8 <=Limite_liquido < 50: #Suelo baja plasticidad 
      if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
        print("El Suelo es de Tipo CL")
        cartaPlasticidad(Limite_liquido,Indice_plasticidad)
        Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
      elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
        print("El Suelo es de Tipo CL-ML")
        cartaPlasticidad(Limite_liquido,Indice_plasticidad)
        Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
      elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
        print("El Suelo es de Tipo ML")
        cartaPlasticidad(Limite_liquido,Indice_plasticidad)
        Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
      else:
        print("EL SUELO NO PUDO SER CLASIFICADO")
    elif 50 <=Limite_liquido <= 100:
      if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
        print("El Suelo es de Tipo CH")
        cartaPlasticidad(Limite_liquido,Indice_plasticidad)
        Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
      elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
        print("El Suelo es de Tipo MH")
        cartaPlasticidad(Limite_liquido,Indice_plasticidad)
        Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
      else:
        print("EL SUELO NO PUDO SER CLASIFICADO") 
    else:
      print("EL SUELO NO PUDO SER CLASIFICADO")

                                                                                    #SUELOS GRUESOS#

  elif 0 <= tamiz_200 < 50: 
                                                                                        #GRAVAS
    if tamiz_4 < 50: 
  #CONDICIÓN A. Granulometría 
      if tamiz_200 < 5: 
        if Cu >= 4 and 1 <= Cc <= 3: 
          print("El Suelo es de Tipo GW")
          Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
        elif Cu < 4 or 1 > Cc > 3:
          print("El Suelo es de Tipo GP")
          Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
        else:
          print("EL SUELO NO PUDO SER CLASIFICADO")

  #CONDICIÓN B. Granulometría + Carta de Plasticidad
      elif 5 <= tamiz_200 <= 12:
  #___________________________________________________
  #INPUT LL y IP, Con esto se garantiza que pida el Input únicamente cuando sea necesario en el código
        Limite_liquido_valido = False
        while not Limite_liquido_valido:
            try:
                Limite_liquido = float(input("Ingresa el Límite Liquido: "))
                if 8 <= Limite_liquido <= 100:
                    Limite_liquido_valido = True
                else:
                    print("El Límite Liquido debe ser un valor entre 8% y 100%. Inténtalo de nuevo.")
            except ValueError:
                print("Ingresar un valor numérico valido")

        Indice_plasticidad_valido = False
        while not Indice_plasticidad_valido:
            try:
                Indice_plasticidad = float(input("Ingresa el Indice de Plasticidad: "))
                if 0 <= Indice_plasticidad <= 100:
                    Indice_plasticidad_valido = True
                else:
                    print("El Indice de Plasticidad debe ser un valor entre 1% y 100%. Inténtalo de nuevo.")
            except ValueError:
                print("Ingresar un valor numérico valido")
  #___________________________________________________ 
        if Cu >= 4 and 1 <= Cc <=3:
          if 8 <=Limite_liquido < 50:
            if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo GW-GC") #GW-GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
              print("El Suelo es de Tipo GW-GC") #GW-GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo GW-GM") #GW-GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO")
          elif 50 <=Limite_liquido <= 100:
            if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo GW-GC") #GW-GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo GW-GM") #GW-GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO") 
          else:
            print("EL SUELO NO PUDO SER CLASIFICADO")
        elif Cu < 4 or 1 > Cc > 3: 
          if 8 <=Limite_liquido < 50: 
            if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo GP-GC") #GP-GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
              print("El Suelo es de Tipo GP-GC") #GP-GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo GP-GM") #GP-GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO")
          elif 50 <=Limite_liquido <= 100:
            if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo GP-GC") #GP-GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo GP-GM") #GP-GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO") 
          else:
            print("EL SUELO NO PUDO SER CLASIFICADO")

  #CONDICIÓN C. Carta de Plasticidad
      elif 12 < tamiz_200: 
  #___________________________________________________
  #INPUT LL y IP, Con esto se garantiza que pida el Input únicamente cuando sea necesario en el código
          Limite_liquido_valido = False
          while not Limite_liquido_valido:
              try:
                  Limite_liquido = float(input("Ingresa el Límite Liquido: "))
                  if 8 <= Limite_liquido <= 100:
                      Limite_liquido_valido = True
                  else:
                      print("El Límite Liquido debe ser un valor entre 8% y 100%. Inténtalo de nuevo.")
              except ValueError:
                  print("Ingresar un valor numérico valido")

          Indice_plasticidad_valido = False
          while not Indice_plasticidad_valido:
              try:
                  Indice_plasticidad = float(input("Ingresa el Indice de Plasticidad: "))
                  if 0 <= Indice_plasticidad <= 100:
                      Indice_plasticidad_valido = True
                  else:
                      print("El Indice de Plasticidad debe ser un valor entre 1% y 100%. Inténtalo de nuevo.")
              except ValueError:
                  print("Ingresar un valor numérico valido")
  #___________________________________________________ 

          if 8 <=Limite_liquido < 50: 
            if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo GC") #GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)
            elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
              print("El Suelo es de Tipo GC-GM") #GC-GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo GM") #GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO")
          elif 50 <=Limite_liquido <= 100:
            if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo GC") #GC
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo GM") #GM
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)             
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO") 
          else:
            print("EL SUELO NO PUDO SER CLASIFICADO")       

                                                                                        #ARENAS
    elif tamiz_4 >= 50: 
  #CONDICIÓN A. Granulometría 
      if tamiz_200 < 5: 
        if Cu >= 6 and 1 <= Cc <= 3: 
          print("El Suelo es de Tipo SW")
          Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)          
        elif Cu < 6 or 1 > Cc > 3:
          print("El Suelo es de Tipo SP")
          Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)    
        else:
          print("EL SUELO NO PUDO SER CLASIFICADO")

  #CONDICIÓN B. Granulometría + Carta de Plasticidad
      elif 5 <= tamiz_200 <= 12:
  #___________________________________________________
  #INPUT LL y IP, Con esto se garantiza que pida el Input únicamente cuando sea necesario en el código
        Limite_liquido_valido = False
        while not Limite_liquido_valido:
            try:
                Limite_liquido = float(input("Ingresa el Límite Liquido: "))
                if 8 <= Limite_liquido <= 100:
                    Limite_liquido_valido = True
                else:
                    print("El Límite Liquido debe ser un valor entre 8% y 100%. Inténtalo de nuevo.")
            except ValueError:
                print("Ingresar un valor numérico valido")

        Indice_plasticidad_valido = False
        while not Indice_plasticidad_valido:
            try:
                Indice_plasticidad = float(input("Ingresa el Indice de Plasticidad: "))
                if 0 <= Indice_plasticidad <= 100:
                    Indice_plasticidad_valido = True
                else:
                    print("El Indice de Plasticidad debe ser un valor entre 1% y 100%. Inténtalo de nuevo.")
            except ValueError:
                print("Ingresar un valor numérico valido")
  #___________________________________________________  
        if Cu >= 6 and 1 <= Cc <=3:
          if 8 <=Limite_liquido < 50:
            if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo SW-SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
              print("El Suelo es de Tipo SW-SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo SW-SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO")
          elif 50 <=Limite_liquido <= 100:
            if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo SW-SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo SW-SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO") 
          else:
            print("EL SUELO NO PUDO SER CLASIFICADO")
        elif Cu < 6 or 1 > Cc > 3: 
          if 8 <=Limite_liquido < 50: 
            if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo SP-SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
              print("El Suelo es de Tipo SP-SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo SP-SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO")
          elif 50 <=Limite_liquido <= 100:
            if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo SP-SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo SP-SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO") 
          else:
            print("EL SUELO NO PUDO SER CLASIFICADO")       

  #CONDICIÓN C. Carta de Plasticidad
      elif 12 < tamiz_200: 
  #___________________________________________________
  #INPUT LL y IP, Con esto se garantiza que pida el Input únicamente cuando sea necesario en el código
          Limite_liquido_valido = False
          while not Limite_liquido_valido:
              try:
                  Limite_liquido = float(input("Ingresa el Límite Liquido: "))
                  if 8 <= Limite_liquido <= 100:
                      Limite_liquido_valido = True
                  else:
                      print("El Límite Liquido debe ser un valor entre 8% y 100%. Inténtalo de nuevo.")
              except ValueError:
                  print("Ingresar un valor numérico valido")

          Indice_plasticidad_valido = False
          while not Indice_plasticidad_valido:
              try:
                  Indice_plasticidad = float(input("Ingresa el Indice de Plasticidad: "))
                  if 0 <= Indice_plasticidad <= 100:
                      Indice_plasticidad_valido = True
                  else:
                      print("El Indice de Plasticidad debe ser un valor entre 1% y 100%. Inténtalo de nuevo.")
              except ValueError:
                  print("Ingresar un valor numérico valido")
  #___________________________________________________ 
          if 8 <=Limite_liquido < 50: 
            if Indice_plasticidad > 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo SC") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif 4 <= Indice_plasticidad <= 7 and Indice_plasticidad >= 0.73*(Limite_liquido - 20): 
              print("El Suelo es de Tipo SC-SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 4 or Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO")
          elif 50 <=Limite_liquido <= 100:
            if Indice_plasticidad >= 0.73*(Limite_liquido - 20) and Indice_plasticidad < 0.9*(Limite_liquido - 8):
              print("El Suelo es de Tipo SC")
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)              
            elif Indice_plasticidad < 0.73*(Limite_liquido - 20):
              print("El Suelo es de Tipo SM") 
              cartaPlasticidad(Limite_liquido,Indice_plasticidad)
              Granulometria(T4,T10,T20,T30,T40,T60,T140,T200,Fondo)             
            else:
              print("EL SUELO NO PUDO SER CLASIFICADO") 
          else:
            print("EL SUELO NO PUDO SER CLASIFICADO")                
                  
  else: 
    print("Error en % Pasa Tamiz 200, No se pudo clasificar el suelo ")