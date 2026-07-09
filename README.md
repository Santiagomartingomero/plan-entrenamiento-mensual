# 🚴 Plan de Entrenamiento Mensual

Repositorio para gestionar y automatizar el plan de entrenamiento mensual basado en evidencia científica.
Diseñado para un cardiólogo en formación con modalidades combinadas: ciclismo, fuerza y recuperación activa.

## Estructura

```
📁 planes/              → Planes mensuales generados automáticamente (Markdown)
📁 registros/           → Registro diario de sesiones
📁 metricas/            → CSVs con métricas de rendimiento (FC, RPE, HRV)
📁 .github/workflows/   → Automatizaciones GitHub Actions
📁 .github/scripts/     → Scripts Python generadores
```

## Modalidades
- 🚴 Ciclismo (commute + entrenamiento estructurado)
- 💪 Fuerza / Gym (tren superior e inferior alternos)
- 🏃 Elíptica / Cardio complementario
- 🧖 Sauna (recuperación activa, ≥2×/semana)

## Modelo de periodización

Cada mes sigue un ciclo de 4 semanas basado en evidencia:

| Semana | Fase | Volumen | RPE objetivo |
|--------|------|---------|---------------|
| 1 | Adaptación | Base | 5–6/10 |
| 2 | Desarrollo | +10% | 6–7/10 |
| 3 | Pico | +15% | 7/10 |
| 4 | **Descarga** | **−40%** | **4–5/10** |

> La supercompensación ocurre durante la descarga, no durante el estrés (Issurin, 2010).

## Métricas registradas

El CSV de métricas (`metricas/metricas_mes_año.csv`) incluye:
`fecha, semana, modalidad, duracion_min, fc_media, fc_max, rpe, hrv, completada, notas`

**Criterio HRV:** si el HRV basal cae >10% respecto a la media semanal → reducir intensidad ese día.

## Automatizaciones activas

| Workflow | Frecuencia | Qué hace |
|----------|------------|----------|
| `recordatorio_semanal.yml` | Cada lunes 6:00 UTC | Issue con checklist semanal + alerta semana descarga |
| `plan_mensual_automatico.yml` | Último día del mes 19:00 UTC | Genera plan del mes siguiente + issue de revisión |

## Uso manual

Para generar un plan manualmente:
1. Ve a **Actions → Plan Mensual Automatico → Run workflow**
2. Introduce el mes (ej: `septiembre`) y el año (ej: `2026`)
3. El plan aparecerá en `planes/septiembre_2026.md`

## Referencias científicas
- Seiler S. (2010). *What is best practice for training intensity distribution?* IJSPP.
- ACSM Position Stand (2022). *Resistance training progression.*
- Issurin V. (2010). *New horizons for training periodization.* Sports Med.
- Buchheit M. & Laursen P. (2013). *High-intensity interval training.* Sports Med.
