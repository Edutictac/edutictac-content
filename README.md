# EduTicTac Content

Catàleg de continguts educatius oberts per a EduTicTac Commons.

El repositori publica un `manifest.json` i els fitxers d'activitat associats.
Commons descarrega el catàleg per canals i verifica el hash SHA-256 abans
d'activar una còpia local.

## Publicació local

```bash
python3 scripts/build-manifest.py
python3 scripts/validate-manifest.py manifest.json --check-files
```

El catàleg està pensat per servir-se com a fitxers estàtics. La URL base ha
de contenir `manifest.json` i les rutes relatives que hi apareixen.

## Llicència

Els fitxers d'aquest repositori es publiquen sota CC BY-SA 4.0, excepte quan
una fitxa indique una llicència més específica compatible.

