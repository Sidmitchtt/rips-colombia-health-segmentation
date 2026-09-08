"""
Configuracion central del proyecto RIPS Colombia.
Todas las rutas y constantes van aqui.
"""
from pathlib import Path

# Rutas base
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
EXTERNAL_DIR = DATA_DIR / "external"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"
REPORTS_DIR = PROJECT_ROOT / "reports"
MODELS_DIR = PROJECT_ROOT / "models"

# Columnas originales del dataset
COLS_RIPS = [
    "Departamento",
    "Municipio", 
    "Anio",
    "TipoAtencion",
    "Diagnostico",
    "NumeroAtenciones"
]

# Codigos de "NO DEFINIDO"
COD_NO_DEFINIDO = "1 - NO DEFINIDO"

# Tipos de atencion validos
TIPOS_ATENCION = [
    "CONSULTAS",
    "PROCEDIMIENTOS DE SALUD",
    "URGENCIAS", 
    "HOSPITALIZACIONES"
]

# Periodo de analisis
ANIO_INICIO = 2009
ANIO_FIN = 2021
ANIO_COVID = 2020