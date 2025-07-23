from correctiva import fechas_correctiva
from D1 import fechas_D1    
from D2 import fechas_D2
from corte import fechas_corte
from preventiva import fechas_preventiva
from inhabiles import fechas_feriados
import pandas as pd

def all_dates(mes, anio):
    """
    Esta función genera las fechas de corte y asignación correctiva para el mes y año dados.
    """
    try:
        corte = fechas_corte(mes, anio)
        # generamos el archivo 
        corte.to_csv(r"\\172.16.39.32\recepcion\FECHAS\FECHAS_2PV.txt", sep="\t", index=False, header=False)
        print("CORTE\n",corte)
        correctiva = fechas_correctiva(mes, anio)
        print("CORRECTIVA\n",correctiva)
        d1 = fechas_D1(mes, anio)
        # generamos el archivo 
        d1.to_csv(r"\\172.16.39.32\recepcion\FECHAS\FECHAS_D1.txt", sep="\t", index=False, header=False)
        print("D1\n",d1)
        d2 = fechas_D2(mes, anio)
        # generamos el archivo
        d2.to_csv(r"\\172.16.39.32\recepcion\FECHAS\FECHAS_D2.txt", sep="\t", index=False, header=False)
        print("D2\n",d2)
        print("PREVENTIVA\n",fechas_preventiva(mes, anio))
        
        try:
            feriados = fechas_feriados(mes, anio)
            if isinstance(feriados, pd.DataFrame) and not feriados.empty:
                print("INHABILES\n", feriados)
            else:
                print(f"No hay días inhábiles en el mes {mes} de {anio}.")
        except ValueError as e:
            print(f"Error al procesar días inhábiles: {e}")
            
    except Exception as e:
        print(f"Error al procesar las fechas: {e}")

all_dates(7,2025)