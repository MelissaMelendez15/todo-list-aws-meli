FROM python:3.10-slim

# Evitamos problemas de permisos, y usamos solo lo necesario
RUN pip install --no-cache-dir flake8==7.3.0 bandit==1.8.5
