"""
La asignación por corte se realiza un día después de cada corte y debe tener fecha fin el corte del siguiente mes.
Si el día de la asignación cae en domingo, la fecha de corte se mueve al día lunes siguiente.
"""

from datetime import datetime, timedelta
import pandas as pd
import os
import locale 

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# flps y cortes que tenemos 
flps = [26, 28, 1, 3, 4, 8, 12, 13, 16, 18, 21]
cortes = [3, 5, 8, 10, 11, 15, 19, 20, 23, 25, 28]

# función para detectar 
def mover_dias_corte(dia_asignacion):
    weekday = dia_asignacion.strftime('%A')
    condiciones = {'Sunday': 2}
    return condiciones.get(weekday, 1)

# mover_dias_corte(datetime.now())

# función para obtener la asignación por corte del mes dado
def fechas_corte(mes, anio):
    f_act = datetime(1, mes, anio)
    f_fut = f_act + timedelta(days=31)
    print(datetime(anio, mes, 1).strftime('%B'))

    fi_corte = []
    ff_corte = []
    for corte in cortes:
        fi_corte.append((datetime(anio, mes, corte) + timedelta(days=mover_dias_corte(datetime(anio, mes, corte + 1)))).strftime("%Y-%m-%d"))
        ff_corte.append((datetime(f_fut.year, f_fut.month, corte)).strftime("%Y-%m-%d"))

    df_2PV = pd.concat([pd.Series(cortes), pd.Series(fi_corte), pd.Series(ff_corte)], axis=1)
    print(df_2PV)


fechas_corte(3,2024)