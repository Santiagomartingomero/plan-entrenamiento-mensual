import sys
import os
from datetime import date

def main():
    mes = sys.argv[1].lower()
    anyo = sys.argv[2]
    mes_cap = mes.capitalize()

    os.makedirs('planes', exist_ok=True)
    os.makedirs('metricas', exist_ok=True)

    archivo_plan = f'planes/{mes}_{anyo}.md'
    archivo_csv = f'metricas/metricas_{mes}_{anyo}.csv'

    plan = f"""# Plan de Entrenamiento - {mes_cap} {anyo}

> Generado automaticamente. Personaliza los objetivos segun tu estado de forma.

## Objetivos del mes
- [ ] Mantener base aerobica (ciclismo Z2)
- [ ] Progresion en fuerza (sobrecarga progresiva)
- [ ] Recuperacion activa: sauna 2x/semana
- [ ] Registrar FC, RPE y HRV semanalmente

## Distribucion semanal

| Dia | Modalidad | Duracion | Intensidad | Zona FC |
|-----|-----------|----------|------------|---------|
| Lunes | Fuerza tren superior | 60 min | Moderada | - |
| Martes | Ciclismo | 45 min | Baja | Z2 |
| Miercoles | Eliptica + Core | 40 min | Moderada | Z2-Z3 |
| Jueves | Fuerza tren inferior | 60 min | Alta | - |
| Viernes | Ciclismo | 60 min | Moderada | Z2-Z3 |
| Sabado | Actividad larga libre | 90 min | Baja | Z1-Z2 |
| Domingo | Descanso o Sauna | - | Recuperacion | - |

## Semana 1
- [ ] Lunes - Fuerza superior
- [ ] Martes - Ciclismo
- [ ] Miercoles - Eliptica
- [ ] Jueves - Fuerza inferior
- [ ] Viernes - Ciclismo
- [ ] Sabado - Actividad libre

## Semana 2
- [ ] Lunes - Fuerza superior
- [ ] Martes - Ciclismo
- [ ] Miercoles - Eliptica
- [ ] Jueves - Fuerza inferior
- [ ] Viernes - Ciclismo
- [ ] Sabado - Actividad libre

## Semana 3
- [ ] Lunes - Fuerza superior
- [ ] Martes - Ciclismo
- [ ] Miercoles - Eliptica
- [ ] Jueves - Fuerza inferior
- [ ] Viernes - Ciclismo
- [ ] Sabado - Actividad libre

## Semana 4
- [ ] Lunes - Fuerza superior
- [ ] Martes - Ciclismo
- [ ] Miercoles - Eliptica
- [ ] Jueves - Fuerza inferior
- [ ] Viernes - Ciclismo
- [ ] Sabado - Actividad libre

## Metricas objetivo

| Metrica | Objetivo | Real (fin de mes) |
|---------|----------|-------------------|
| Sesiones completadas | >= 20/24 | - |
| FC media ciclismo | < 145 bpm | - |
| RPE medio | 5-6/10 | - |
| HRV | Estable o subiendo | - |

## Notas del mes
> Anota aqui ajustes, lesiones, viajes o congresos.
"""

    with open(archivo_plan, 'w') as f:
        f.write(plan)
    print(f'Plan creado: {archivo_plan}')

    if not os.path.exists(archivo_csv):
        with open(archivo_csv, 'w') as f:
            f.write('fecha,modalidad,duracion_min,fc_media,fc_max,rpe,hrv,notas\n')
        print(f'CSV creado: {archivo_csv}')

if __name__ == '__main__':
    main()
