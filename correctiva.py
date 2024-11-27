from datetime import datetime, timedelta
import pandas as pd
import os

flps = [26, 28, 1, 3, 4, 8, 12, 13, 16, 18, 21]
cortes = [3, 5, 8, 10, 11, 15, 19, 20, 23, 25, 28]

def fechas_D1(mes, anio):

    fi = []
    ff= []
    ruta_fechas = r"\\172.16.39.32\recepcion\FECHAS"
    for flp in flps:
        if flp != 26 and flp != 28:
            fi.append((datetime(anio, mes, flp) + timedelta(days=mover_dias_corr(datetime(anio, mes, flp).strftime("%A")))).strftime("%Y-%m-%d"))
            ff.append((datetime(anio, mes, get_corte(flp))).strftime("%Y-%m-%d"))
    
    df_d1 = pd.concat([pd.Series(cortes[2:]), pd.Series(fi), pd.Series(ff)], axis=1)
    # df_d1.to_csv(os.path.join(ruta_fechas, "FECHAS_D1.txt"), index=False, header=False, sep="\t")
            
def fechas_D2(mes, anio):

    fi = []
    ff= []
    ruta_fechas = r"\\172.16.39.32\recepcion\FECHAS"
    for flp in flps:
        if flp != 26 and flp != 28:
            fi.append((datetime(anio, mes, flp+1) + timedelta(days=mover_dias_corr(datetime(anio, mes, flp).strftime("%A")))).strftime("%Y-%m-%d"))
            ff.append((datetime(anio, mes, get_corte(flp)) + timedelta(days=1)).strftime("%Y-%m-%d"))
    df_d2 = pd.concat([pd.Series(cortes[2:]), pd.Series(fi), pd.Series(ff)], axis=1)
    # df_d2.to_csv(os.path.join(ruta_fechas, "FECHAS_D2.txt"), index=False, header=False, sep="\t")
