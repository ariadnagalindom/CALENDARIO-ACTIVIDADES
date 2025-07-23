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
    Esta función genera las fechas de asignación D2 para el mes y año dados; 
    2 dias despues de la asignación correctiva.
    """   
    fechas = []
    for flp in flps:
        fecha_correctiva = datetime(anio, mes, flp)
        '''
        lunes: asigna t+1 D2: t+3
        martes: asigna t+1 D2: t+3
        miercoles: asigna t+1 D2: t+5
        jueves: asigna t+1 D2: t+5
        viernes: asigna t+3 D2: t+5
        sabado: asigna t+3 D2: t+5
        domingo: asigna t+2 D2: t+4
        '''
        if fecha_correctiva.strftime("%A") == "Wednesday" or fecha_correctiva.strftime("%A") == 'Thursday' or fecha_correctiva.strftime("%A") == 'Friday' or fecha_correctiva.strftime("%A") == 'Saturday':
            fecha_asignacion = fecha_correctiva + timedelta(days=5)
        elif fecha_correctiva.strftime("%A") == "Monday" or fecha_correctiva.strftime("%A") == 'Tuesday':
            fecha_asignacion = fecha_correctiva + timedelta(days=3)
        else:
            fecha_asignacion = fecha_correctiva + timedelta(days=4)

        # mover un día si es feriado nacional
        if fecha_asignacion.strftime("%Y-%m-%d") in mx_holidays:
            fecha_asignacion = fecha_asignacion + timedelta(days=1)


        fecha_corte = datetime(anio, mes, get_corte(flp))

        fechas.append([get_corte(flp=flp), fecha_asignacion, fecha_corte])
    
    df = pd.DataFrame(fechas, columns=["CORTE", "Fecha Asignación", "Fecha Fin"])
    return df

# print(fechas_D2(1,2025))
# fechas_D2(6,2025).to_csv(r"\\172.16.39.32\recepcion\FECHAS\FECHAS_D2.txt", sep="\t", index=False, header=False)

        