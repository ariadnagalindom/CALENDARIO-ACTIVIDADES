"""
La asignación por corte se realiza un día después de cada corte y debe tener fecha fin el corte del siguiente mes.
Si el día de la asignación cae en domingo, la fecha de corte se mueve al día lunes siguiente.
"""

from datetime import datetime, timedelta
import pandas as pd
import os
import locale 
import holidays

# locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
# feriados México
mx_holidays = holidays.Mexico()

# flps y cortes que tenemos 
flps = [26, 28, 1, 3, 4, 8, 12, 13, 16, 18, 21]
cortes = [3, 5, 8, 10, 11, 15, 19, 20, 23, 25, 28]

def fechas_corte(mes, anio):
    """
    Esta función genera las fechas de corte para   el mes y año dados.
    """
    fechas = []
    for corte in cortes:
        fecha_corte = datetime(anio, mes, corte)
        if fecha_corte.strftime("%A") == "Saturday":
            fecha_asignacion = fecha_corte + timedelta(days=2)
        else:
            fecha_asignacion = fecha_corte + timedelta(days=1)

        if fecha_asignacion.strftime("%Y-%m-%d") in mx_holidays:
            fecha_asignacion = fecha_asignacion + timedelta(days=1)

        siguiente_mes = fecha_corte + timedelta(days=29)
        siguiente_corte = datetime(siguiente_mes.year, siguiente_mes.month, corte)

        fechas.append([corte, fecha_asignacion, siguiente_corte])

    df = pd.DataFrame(fechas, columns=["CORTE", "Fecha Asignación", "Fecha Fin"])

    return df

# print(fechas_corte(2,2025))
# (fechas_corte(4,2025)).to_csv(r"\\172.16.39.32\recepcion\FECHAS\FECHAS_2PV.txt", sep="\t", index=False, header=False)