# EduTicTac Content

Catàleg versionat de continguts educatius oberts per a EduTicTac Commons.

El repositori publica un `manifest.json` i els fitxers d'activitat associats.
La publicació existent `releases/2026.09.0/` conté el primer índex públic
importat de Recursos i EduHoot. Les activitats noves es preparen en
`activities/` i es publiquen després d'una revisió de llicència i de generar
el manifest corresponent.

## Publicació i validació local

```bash
python3 scripts/build-manifest.py
python3 scripts/validate-manifest.py manifest.json --check-files
```

El catàleg està pensat per servir-se com a fitxers estàtics. La URL base ha
de contenir `manifest.json` i les rutes relatives que hi apareixen. El
servidor públic actual serveix `releases/latest/manifest.json`; el pas de
promoció d'una nova versió ha d'actualitzar eixe punter després de validar
els fitxers.

## Llicència

Els fitxers d'aquest repositori es publiquen sota CC BY-SA 4.0, excepte quan
una fitxa indique una llicència més específica compatible.
