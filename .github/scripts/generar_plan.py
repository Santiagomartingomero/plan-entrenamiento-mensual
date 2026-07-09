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

    plan = f"""# Plan de Entrenamiento — {mes_cap} {anyo}

> Generado automáticamente. Personaliza los objetivos según tu estado de forma.
> Basado en modelo de periodización 80/20 (Seiler, 2010) y sobrecarga progresiva (ACSM, 2022).

## Objetivos del mes
- [ ] Mantener base aeróbica (ciclismo Z2 ≥ 80% del volumen total)
- [ ] Progresión en fuerza con sobrecarga progresiva (+2.5–5% semanal semanas 1-3)
- [ ] Recuperación activa: sauna 2×/semana
- [ ] Registrar FC, RPE y HRV semanalmente
- [ ] Semana 4: descarga (volumen -40%, intensidad -20%)

## Distribución semanal base

| Día | Modalidad | Duración | Intensidad | Zona FC |
|-----|-----------|----------|------------|---------|
| Lunes | Fuerza tren superior | 60 min | Moderada-Alta | — |
| Martes | Ciclismo commute | 45 min | Baja | Z2 |
| Miércoles | Elíptica + Core | 40 min | Moderada | Z2–Z3 |
| Jueves | Fuerza tren inferior | 60 min | Alta | — |
| Viernes | Ciclismo entrenamiento | 60 min | Moderada | Z2–Z3 |
| Sábado | Actividad larga libre | 90 min | Baja | Z1–Z2 |
| Domingo | Descanso o Sauna | — | Recuperación | — |

> **Zonas FC** (Karvonen): Z1 <60% FCR · Z2 60–70% · Z3 70–80% · Z4 80–90% · Z5 >90%

---

## Semana 1 — Adaptación (volumen base)

| Día | Sesión | Notas | Hecho |
|-----|--------|-------|-------|
| Lunes | Fuerza superior — 3×10 | Peso cómodo, técnica | - [ ] |
| Martes | Ciclismo Z2 — 45 min | FC <145 bpm | - [ ] |
| Miércoles | Elíptica Z2 + Core — 40 min | RPE 5/10 | - [ ] |
| Jueves | Fuerza inferior — 3×10 | Sentadilla, peso muerto | - [ ] |
| Viernes | Ciclismo Z2-Z3 — 60 min | Últimos 15 min Z3 | - [ ] |
| Sábado | Actividad libre — 90 min | Z1-Z2, disfruta | - [ ] |
| Domingo | Descanso / Sauna | Recuperación pasiva | - [ ] |

**RPE objetivo semana 1:** 5–6/10 · **HRV:** registrar valor basal

---

## Semana 2 — Desarrollo (+10% volumen)

| Día | Sesión | Notas | Hecho |
|-----|--------|-------|-------|
| Lunes | Fuerza superior — 3×10 | +2.5 kg respecto S1 | - [ ] |
| Martes | Ciclismo Z2 — 50 min | FC <145 bpm | - [ ] |
| Miércoles | Elíptica Z2 + Core — 45 min | RPE 5-6/10 | - [ ] |
| Jueves | Fuerza inferior — 3×12 | Misma carga S1 | - [ ] |
| Viernes | Ciclismo Z2-Z3 — 65 min | 20 min Z3 | - [ ] |
| Sábado | Actividad libre — 100 min | Z1-Z2 | - [ ] |
| Domingo | Descanso / Sauna | Recuperación | - [ ] |

**RPE objetivo semana 2:** 6–7/10 · **HRV:** comparar con basal

---

## Semana 3 — Pico (+15% volumen acumulado)

| Día | Sesión | Notas | Hecho |
|-----|--------|-------|-------|
| Lunes | Fuerza superior — 4×8 | +5 kg respecto S1 | - [ ] |
| Martes | Ciclismo Z2 — 55 min | FC <150 bpm | - [ ] |
| Miércoles | Elíptica Z3 + Core — 45 min | RPE 6-7/10 | - [ ] |
| Jueves | Fuerza inferior — 4×8 | Carga exigente | - [ ] |
| Viernes | Ciclismo Z3 — 70 min | 30 min Z3 | - [ ] |
| Sábado | Actividad larga — 110 min | Z1-Z2 | - [ ] |
| Domingo | Descanso / Sauna | Recuperación | - [ ] |

**RPE objetivo semana 3:** 7/10 · **HRV:** si baja >10% → reducir intensidad

---

## Semana 4 — Descarga (−40% volumen, −20% intensidad)
> 🔑 La supercompensación ocurre durante la descarga, no durante el estrés. (Issurin, 2010)

| Día | Sesión | Notas | Hecho |
|-----|--------|-------|-------|
| Lunes | Fuerza superior — 2×8 | Carga S1, sin fatiga | - [ ] |
| Martes | Ciclismo Z1 — 30 min | Paseo, FC <130 | - [ ] |
| Miércoles | Movilidad + Core suave — 30 min | Yoga/stretching | - [ ] |
| Jueves | Fuerza inferior — 2×8 | Ligero, técnica | - [ ] |
| Viernes | Ciclismo Z2 — 40 min | Sin esfuerzo | - [ ] |
| Sábado | Actividad libre corta — 60 min | Lo que apetezca | - [ ] |
| Domingo | Sauna + descanso total | Prioridad recuperación | - [ ] |

**RPE objetivo semana 4:** 4–5/10 · **HRV:** debería subir al final de semana

---

## Métricas objetivo del mes

| Métrica | Objetivo | S1 | S2 | S3 | S4 | Fin de mes |
|---------|----------|----|----|----|----|------------|
| Sesiones completadas | ≥ 20/24 | — | — | — | — | — |
| FC media ciclismo | < 145 bpm | — | — | — | — | — |
| RPE medio semanal | 5–7 / 4 (S4) | — | — | — | — | — |
| HRV basal | Estable o ↑ | — | — | — | — | — |
| Sauna sesiones | ≥ 6 | — | — | — | — | — |

## Referencias científicas aplicadas
- Seiler S. (2010). *What is best practice for training intensity distribution in endurance athletes?* IJSPP.
- ACSM Position Stand (2022). *Resistance training progression.*
- Issurin V. (2010). *New horizons for the methodology and physiology of training periodization.* Sports Med.
- Buchheit M. & Laursen P. (2013). *High-intensity interval training.* Sports Med.

## Notas del mes
> Anota aquí ajustes, lesiones, viajes o guardias hospitalarias.
"""

    with open(archivo_plan, 'w', encoding='utf-8') as f:
        f.write(plan)
    print(f'Plan creado: {archivo_plan}')

    if not os.path.exists(archivo_csv):
        with open(archivo_csv, 'w', encoding='utf-8') as f:
            f.write('fecha,semana,modalidad,duracion_min,fc_media,fc_max,rpe,hrv,completada,notas\n')
        print(f'CSV creado: {archivo_csv}')

if __name__ == '__main__':
    main()
