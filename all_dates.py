from correctiva import fechas_correctiva
from D1 import fechas_D1    
from D2 import fechas_D2
from corte import fechas_corte
from preventiva import fechas_preventiva
from inhabiles import fechas_feriados

def all_dates(mes, anio):
    """
    Esta función genera las fechas de corte y asignación correctiva para el mes y año dados.
    """
    corte = fechas_corte(mes, anio)
    print("CORTE\n",corte)
    correctiva = fechas_correctiva(mes, anio)
    print("CORRECTIVA\n",correctiva)
    d1 = fechas_D1(mes, anio)
    print("D1\n",d1)
    d2 = fechas_D2(mes, anio)
    print("D2\n",d2)
    print("PREVENTIVA\n",fechas_preventiva(mes, anio))
    if fechas_feriados(1,2025).index >= 0:
        print("INHABILES\n",fechas_feriados(mes, anio))
all_dates(2,2025)
    