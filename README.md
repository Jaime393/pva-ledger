# pva-ledger V202 — rho(x)>0

Registro inmutable de contribuciones — Arweave + Zenodo DOI — credito inmediato.

```bash
pip install -r requirements.txt
python cli.py publish paper.pdf --zenodo
python cli.py verify <sha256>
```

Flujo:
1. Calcula SHA256 paper/prueba
2. Sube hash a Arweave (testnet gratis, mainnet ~0.01 AR)
3. Genera DOI via Zenodo sandbox (gratis)
4. Asocia timestamp + hash + autor

Salida: `paper.pdf.pva-ledger.json` con tx Arweave + DOI.

Parte de PVA ecosistema — Bloque 4 memoria inmutable — credito inmediato.
