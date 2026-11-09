# INVENTARIO — pva-ledger

Repo: `Jaime393/pva-ledger`, rama `main`.
Leído en vivo: 2026-11-09 ~07:40 -05 (todos los archivos, íntegros).
Commits: 1. Último commit: 2026-09-10T17:02:57Z. Muerto desde entonces.

## Archivos (7 archivos, 2.346 B en total)

| Archivo | Tamaño | Qué es |
|---|---|---|
| `README.md` | 545 B | Descripción del registro inmutable (Arweave + Zenodo DOI) y su flujo en 4 pasos. |
| `cli.py` | 1.282 B | El programa: 2 comandos (`publish`, `verify`), librería `click`. |
| `Dockerfile` | 139 B | Imagen `python:3.11-slim`, instala dependencias, `CMD ["python", "cli.py", "--help"]`. |
| `Makefile` | 131 B | Objetivos `repro`, `reproduce` (publican README.md con --zenodo) y `dev` (--help). |
| `requirements.txt` | 15 B | Dos dependencias: `click`, `requests`. |
| `.gitignore` | 27 B | Ignora `*.tar.gz` y `*.pva-ledger.json` (las salidas del programa). |
| `.github/workflows/pva.yml` | 207 B | Workflow de GitHub Actions: en cada push, instala click+requests y publica README.md con --zenodo. |

## Directorios

- `.github/workflows/` — contiene solo `pva.yml` (207 B).

## Lo que NO hay

- Sin `LICENSE`.
- Sin directorio `tests/` ni ningún archivo de pruebas.
- Sin archivos de datos: no hay ningún `paper.pdf` ni ningún `.pva-ledger.json` en el repo (el `.gitignore` los excluiría si existieran en local, pero en el repo no hay ninguno).
- Sin archivo de configuración propio: no hay `pva.yml` en la raíz (el `pva.yml` que existe es el workflow de GitHub Actions, no la configuración del orquestador PVA).

## NO SÉ

- **NO SÉ** — si el workflow `pva.yml` llegó a ejecutarse alguna vez con éxito: los registros de ejecuciones de GitHub Actions no están en el repo.
- **NO SÉ** — si alguna salida `.pva-ledger.json` existe fuera del repo (en local de alguien o en CI): el `.gitignore` las excluye y en el repo no hay ninguna.
