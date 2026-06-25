# 🏆 Caso de Estudio: Análisis de Datos de las Plantillas del Mundial 2026
**Certificación Google Data Analytics**

Este proyecto aplica el ciclo completo de análisis de datos para extraer, limpiar, almacenar y analizar la información demográfica de los 1,248 jugadores convocados para la Copa del Mundo 2026 a partir de fuentes públicas (Wikipedia).

## 🛠️ Stack Tecnológico Utilizado
* **Extracción (Prepare):** Python (Requests, BeautifulSoup4) corriendo en Jupyter Notebooks.
* **Procesamiento y Limpieza (Process):** Pandas y Expresiones Regulares (Regex) para estandarización de strings y segmentación de datos.
* **Análisis (Analyze):** Base de datos relacional con SQLite y consultas complejas (Funciones de agregación, agrupaciones condicionales con `HAVING`).
* **Visualización (Share):** Power BI (En desarrollo).

## 📁 Estructura del Repositorio
* `1_extraccion_datos.ipynb`: Script de Web Scraping automatizado que maneja bloqueos de servidor.
* `2_limpieza_datos.ipynb`: Pipeline de transformación con Pandas (separación de fechas, edades y limpieza de roles).
* `3_analisis_sql.ipynb`: Entorno de base de datos relacional con las queries técnicas y el **Resumen Ejecutivo**.
* `datos_crudos_mundial.csv` & `plantillas_limpias_mundial2026.csv`: Los datasets antes y después del procesamiento.


## 📊 Dashboard Interactivo en Power BI
Aquí una vista previa del reporte ejecutivo con los principales insights demográficos y de concentración de clubes para el torneo:
![Dashboard Ejecutivo Mundial 2026](<img width="1341" height="747" alt="image" src="https://github.com/user-attachments/assets/a1387ea6-a2f0-4ec7-b586-db29cb4ad4b6" />)
