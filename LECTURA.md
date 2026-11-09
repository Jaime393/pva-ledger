# LECTURA — pva-ledger

Repo: `Jaime393/pva-ledger`, rama `main`.
Leído en vivo: 2026-11-09 ~07:40 -05 (los 7 archivos, íntegros).

## Qué dice el README (citas literales)

Título:

> `# pva-ledger V202 — rho(x)>0`

Descripción:

> `Registro inmutable de contribuciones — Arweave + Zenodo DOI — credito inmediato.`

Uso prometido:

> ```bash
> pip install -r requirements.txt
> python cli.py publish paper.pdf --zenodo
> python cli.py verify <sha256>
> ```

Flujo prometido:

> 1. Calcula SHA256 paper/prueba
> 2. Sube hash a Arweave (testnet gratis, mainnet ~0.01 AR)
> 3. Genera DOI via Zenodo sandbox (gratis)
> 4. Asocia timestamp + hash + autor

Salida prometida:

> `Salida: \`paper.pdf.pva-ledger.json\` con tx Arweave + DOI.`

Cierre:

> `Parte de PVA ecosistema — Bloque 4 memoria inmutable — credito inmediato.`

## Qué dice el código (citas literales de `cli.py`)

Comentario sobre Arweave:

> `# Arweave testnet: simula subida hash (en prod usar arweave-python-client)`

Comentario sobre Zenodo:

> `# Zenodo sandbox DOI (en prod usar zenodo API)`

El comando `verify` no verifica nada; su cuerpo entero es:

> ```python
> print(f"Verificando hash {hash} en Arweave y Zenodo (simulado)")
> print("OK inmutable")
> ```

## Qué dice el workflow (`.github/workflows/pva.yml`, íntegro)

```yaml
name: PVA ledger
on: [push]
jobs:
  pva:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install click requests
      - run: python cli.py publish README.md --zenodo
```

## Qué dice el Makefile (íntegro)

```make
repro:
	python cli.py publish README.md --zenodo

reproduce:
	python cli.py publish README.md --zenodo

dev:
	python cli.py --help
```

## Contradicción entre lo prometido y lo escrito

El README promete subir el hash a Arweave y generar un DOI en Zenodo. El código dice en sus propios comentarios que ambas cosas son simuladas ("en prod usar…"). No hay ninguna llamada de red en todo el repo: ni a Arweave, ni a Zenodo, ni a ninguna otra API.

## NO SÉ

- **NO SÉ** — en qué se basa el coste "mainnet ~0.01 AR" del README: no hay fuente en el repo.
- **NO SÉ** — si el flujo completo (subida real a Arweave + DOI real en Zenodo) existe en algún otro repo: en este repo no existe.
