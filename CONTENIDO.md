# CONTENIDO — pva-ledger

Repo: `Jaime393/pva-ledger`, rama `main`.
Leído en vivo 2026-11-09 ~07:40 -05. Todos los números abajo se leyeron
o se calcularon de los archivos del repo, no de memoria.

## Qué hace

Es una herramienta de línea de comandos (`cli.py`, 1.282 B, librería `click`)
con 2 comandos:

1. `publish <archivo> [--zenodo]` — calcula el SHA256 real del archivo,
   escribe `{archivo}.pva-ledger.json` en local e imprime el registro.
2. `verify <hash>` — imprime "OK inmutable" sin comprobar nada.

## Lo real

- El SHA256 sí se calcula de verdad: `hashlib.sha256(p.read_bytes())`.
- El `timestamp` es la hora local del momento (`datetime.now().isoformat()`).
- El `author` es el literal fijo `"Jaime393"`.

## Lo simulado

### La transacción de Arweave no existe

El código construye la "transacción" como una cadena a partir del hash:

```python
arweave_tx = f"arweave_tx_{h[:16]}"
```

No hay subida, no hay cliente, no hay red. El propio comentario lo dice:
"simula subida hash (en prod usar arweave-python-client)".

### El DOI no es un DOI y cambia en cada ejecución

El código construye el "DOI" así (solo con `--zenodo`):

```python
doi = f"10.5281/zenodo.{abs(hash(h)) % 10000000}" if zenodo else None
```

`hash()` de Python, aplicado a un `str`, es aleatorio por proceso
(la sal de `PYTHONHASHSEED` cambia en cada ejecución). Verificado en vivo
2026-11-09 ~07:40 -05: el mismo valor de entrada dio 4553639, 9651531
y 4424841 en tres procesos distintos. El mismo archivo publicado dos veces
recibe dos "DOI" distintos. Ninguno de los dos existe en Zenodo: no hay
ninguna llamada a la API de Zenodo en el código.

### `verify` no verifica

Su cuerpo entero imprime dos líneas y termina. No lee Arweave, no lee
Zenodo, no compara el hash con ningún registro. Cualquier cadena que se le
pase recibe "OK inmutable".

## Dependencia muerta

`requirements.txt` lista `click` y `requests`. `cli.py` importa `hashlib`,
`json`, `pathlib`, `click` y `datetime`: `requests` no se importa en ningún
archivo del repo. El `Dockerfile` y el workflow instalan una dependencia
que el programa no usa.

## El flujo completo, según los archivos

- `make repro` y `make reproduce` publican `README.md` con `--zenodo`
  (no hay ningún `paper.pdf` en el repo; el README hace de sustituto).
- El workflow de GitHub Actions hace lo mismo en cada push: publica
  `README.md` y descarta la salida (no sube ningún artefacto).
- El `.gitignore` excluye `*.pva-ledger.json`, así que las salidas nunca
  entran al repo aunque se generen en local.

## Carencias medidas

- Sin `LICENSE`.
- Sin `tests/`: 0 archivos de pruebas.
- Sin datos: 0 archivos de entrada reales (el único archivo publicable
  en el repo es su propio README).
- 0 llamadas de red en todo el código.

## NO SÉ

- **NO SÉ** — si alguna vez se generó una transacción real de Arweave o un
  DOI real de Zenodo con este código: el código no puede producirlos, y en
  el repo no hay ningún registro de salida.
- **NO SÉ** — si el workflow llegó a correr en CI: no hay registros de
  ejecución en el repo.
