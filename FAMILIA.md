# FAMILIA — pva-ledger

Repo: `Jaime393/pva-ledger`, rama `main`.
Leído en vivo: 2026-11-09 ~07:40 -05.

## El ecosistema PVA

El README ubica el repo así:

> `Parte de PVA ecosistema — Bloque 4 memoria inmutable — credito inmediato.`

PVA es una familia de 7 repos, todos nacidos el 2026-09-10 con la marca
V202 (salvo `pva-api`, que llegó a V203). Cada uno cubre un bloque:

| Repo | Bloque | Estado |
|---|---|---|
| `pva-lint` | Linter, score 0–1 | Muerto 2026-09-10, 5 commits |
| `pva-docker-template` | Plantilla de reproducibilidad | Minado ola 4 tanda 1, 2026-11-09 |
| `pva-lean-bridge` | Puente LaTeX → Lean 4 | Minado ola 4 tanda 2, en curso |
| `pva-ledger` | Registro inmutable (este repo) | Este archivo |
| `pva-orchestrator` | Orquestador (lee `pva.yml`) | Minado ola 4 tanda 2, en curso |
| `pva-swarm` | Validación adversarial distribuida | Minado ola 4 tanda 2, en curso |
| `pva-api` | API flexible FastAPI / stdlib | En cola, ola 4 tanda 3 |

## Relaciones concretas dentro de la familia

- `pva-docker-template` (minado en la tanda 1) tiene el mismo patrón que
  este repo: README que promete más de lo que el código hace. Su `repro.py`
  escribe un PNG con bytes `dummy` y lo anuncia; su CSV tiene 7 filas
  mientras su `data/README.md` afirma 221.
- `pva-orchestrator` lee un archivo `pva.yml` y ejecuta cada paso. El
  `pva.yml` de este repo es otra cosa: es el workflow de GitHub Actions
  (`.github/workflows/pva.yml`), no la configuración del orquestador. No
  hay evidencia en este repo de que el orquestador lo invoque.
- `pva-lint` es el linter que, según el README de `pva-docker-template`,
  verifica DOI, datos públicos, código abierto y Dockerfile. Este repo no
  pasa su propio listón: su DOI es fabricado y su "tx Arweave" es una
  cadena local.
- El DOI fabricado usa el prefijo `10.5281/zenodo`, el mismo de Zenodo.
  No hay evidencia de que ningún DOI real de esta familia exista.

## Relaciones fuera de PVA

- Ninguna declarada en los archivos: el README, el código y el workflow
  no nombran ningún repo fuera de la familia PVA.
- El autor del commit (`Jaime363`) difiere en un dígito del dueño del
  repo (`Jaime393`); registrado sin interpretar (ver HISTORIAL.md).

## NO SÉ

- **NO SÉ** — si `pva-orchestrator` encadena realmente este repo en algún
  `pva.yml`: en este repo no hay ninguna evidencia de esa integración.
- **NO SÉ** — si los 7 repos PVA se probaron juntos alguna vez: cada uno
  tiene su propio commit inicial del 2026-09-10 y no hay ningún registro
  de integración conjunta en este repo.
- **NO SÉ** — qué significa "Bloque 4" fuera de este README: la numeración
  de bloques no está documentada en este repo.
