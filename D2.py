from datetime import datetime, timedelta
import pandas as pd
import os
import holidays

mx_holidays = holidays.Mexico()

flps = [1, 3, 4, 8, 12, 13, 16, 18, 21]
cortes = [8, 10, 11, 15, 19, 20, 23, 25, 28]


def get_corte(flp):
    """
    Esta función regresa el corte correspondiente al FLP dado.
    """
    condiciones = {1:8, 3:10, 4:11, 8:15, 12:19, 13:20, 16:23, 18:25, 21:28, 26:3, 28:5}
    return condiciones.get(flp, RuntimeWarning)

def fechas_D2(mes, anio):
    """
    Esta función genera las fechas de asignación correctiva para el mes y año dados.
    """   
    fechas = []
    for flp in flps:
        fecha_correctiva = datetime(anio, mes, flp)
        if fecha_correctiva.strftime("%A") == "Sunday":
            fecha_asignacion = fecha_correctiva + timedelta(days=3)
        elif fecha_correctiva.strftime("%A") == "Saturday":
            fecha_asignacion = fecha_correctiva + timedelta(days=4)
        else:
            fecha_asignacion = fecha_correctiva + timedelta(days=2)

        if fecha_asignacion.strftime("%A") == "Sunday":
            fecha_asignacion = fecha_asignacion + timedelta(days=1)
            
        if fecha_asignacion.strftime("%A") == "Saturday":
            fecha_asignacion = fecha_asignacion + timedelta(days=2)

        # mover un día si es feriado nacional
        if fecha_asignacion.strftime("%Y-%m-%d") in mx_holidays:
            fecha_asignacion = fecha_asignacion + timedelta(days=1)


        fecha_corte = datetime(anio, mes, get_corte(flp))

        fechas.append([get_corte(flp=flp), fecha_asignacion, fecha_corte])
    
    df = pd.DataFrame(fechas, columns=["CORTE", "Fecha Asignación", "Fecha Fin"])
    return df

# print(fechas_D2(12,2024))
# fechas_D2(12,2024).to_csv(r"\\172.16.39.32\recepcion\FECHAS\FECHAS_D2.txt", sep="\t", index=False, header=False)

        