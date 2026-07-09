# 🏋️ Agente de Entrenamiento Deportivo Basado en Evidencia

## ¿Qué hace?
Gestiona y automatiza el plan de entrenamiento mensual personal aplicando **periodización científica** (modelo 80/20 + ciclo de 4 semanas). Genera planes personalizados, envía recordatorios semanales y registra métricas de rendimiento.

## Modalidades cubiertas
- 🚴 Ciclismo (commute + entrenamiento estructurado por zonas FC)
- 💪 Fuerza / Gym (tren superior e inferior, sobrecarga progresiva)
- 🏃 Elíptica / Cardio complementario
- 🧖 Sauna (recuperación activa ≥2×/semana)

## Modelo de periodización
Ciclo mensual de 4 semanas basado en evidencia:

| Semana | Fase | Volumen | RPE objetivo |
|--------|------|---------|--------------|
| 1 | Adaptación | Base | 5–6/10 |
| 2 | Desarrollo | +10% | 6–7/10 |
| 3 | Pico | +15% | 7/10 |
| 4 | **Descarga** | **−40%** | **4–5/10** |

## Automatizaciones activas

| Workflow | Cuándo | Qué hace |
|----------|--------|----------|
| `recordatorio_semanal.yml` | Lunes 6:00 UTC | Issue con checklist + alerta semana de descarga |
| `plan_mensual_automatico.yml` | Último día del mes 19:00 UTC | Genera plan del mes siguiente + issue de revisión |

## Stack tecnológico
- **GitHub Actions** — automatización 100% gratuita
- **Python** — generación de planes y CSVs
- **GitHub Issues** — recordatorios y seguimiento

## Métricas registradas
`fecha · semana · modalidad · duracion_min · fc_media · fc_max · rpe · hrv · completada · notas`

**Criterio HRV:** si cae >10% respecto al basal → reducir intensidad ese día.

## Repositorio
🔗 https://github.com/Santiagomartingomero/plan-entrenamiento-mensual

## Coste
**€0/mes** — 100% gratuito con GitHub Actions

## Referencias científicas
- Seiler S. (2010). *What is best practice for training intensity distribution?* IJSPP.
- ACSM Position Stand (2022). *Resistance training progression.*
- Issurin V. (2010). *New horizons for training periodization.* Sports Med.
- Buchheit M. & Laursen P. (2013). *High-intensity interval training.* Sports Med.
