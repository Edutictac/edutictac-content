# EduTicTac Content

Catálogo versionado de contenidos públicos para EduTicTac Commons.

La publicación `releases/2026.09.0/` es la primera fotografía del catálogo público actual:

- `resources/catalog.json`: índice público de Recursos EduTicTac.
- `eduhoot/quizzes.json`: actividades públicas de EduHoot con sus preguntas.
- `manifest.json`: versión, canales, metadatos y hashes SHA-256.

Esta primera publicación usa paquetes por canal. Las instalaciones Commons validan el manifiesto y descargan el paquete elegido; los importadores específicos de Recursos y EduHoot convertirán después esos paquetes en datos locales.
