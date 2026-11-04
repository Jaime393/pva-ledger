# pva-ledger

Recibos locales de contenido con SHA-256 y comprobación de bytes. Esta revisión elimina las transacciones Arweave simuladas, DOIs inventados mediante `hash()` y el “OK inmutable” sin verificación.

```bash
python3 cli.py record README.md --output receipt.json
python3 cli.py verify receipt.json --file README.md
python3 -m unittest discover -s tests -v
```

Solo biblioteca estándar, sin red ni credenciales. El recibo declara `external_publication=not_performed`; un checksum no prueba autoría, timestamp confiable ni almacenamiento inmutable.

La salida existente no se sobrescribe. `--timestamp` permite un recibo reproducible y debe ser UTC; `--producer` es una declaración, no una identidad autenticada.

El comando histórico `publish --zenodo` ya no fabrica publicaciones. Para publicar externamente se necesita un conector autorizado y lectura de retorno con un identificador real, fuera de este contrato.
