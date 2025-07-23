import holidays
import pandas as pd
from datetime import datetime
import calendar

mx_holidays = holidays.Mexico()

def fechas_feriados(mes, anio):
    """
    Esta función genera las fechas de los feriados para el mes y año dados.
    """
    fechas = []
    _, last_day = calendar.monthrange(anio, mes)
    
    for dia in range(1, last_day + 1):
        fecha = datetime(anio, mes, dia)
        if fecha.strftime("%Y-%m-%d") in mx_holidays:
            fechas.append([dia, fecha])
    
    df = pd.DataFrame(fechas, columns=["DIA", "FECHA"])
    return df

# print(fechas_feriados(1,2025).index >= 0)