# Estudio de Video IA · plan de evolución

Este documento define una evolución incremental del fork `gusrodzu/MoneyPrinterTurbo`
sin romper el proyecto base. «Estudio de Video IA» es un nombre de trabajo;
no cambia todavía el nombre del paquete, los endpoints ni la licencia.

## Arquitectura existente (verificada)

- **Interfaz actual:** Streamlit (`webui/Main.py` y `webui/styles.css`).
- **Motor y servicios:** Python, procesamiento audiovisual y proveedores externos.
- **API:** FastAPI (`main.py`) con documentación disponible en `/docs`.
- **Internacionalización:** `webui/i18n/*.json`; cada idioma usa claves compartidas
  y la interfaz recurre al inglés cuando falta una traducción.
- **Despliegue local:** Python o Docker. El `docker-compose.yml` de desarrollo
  vincula los puertos 8501 (WebUI) y 8080 (API) a `127.0.0.1`.

## Etapa 1 · Iteración inicial (este PR)

- Completar 123 traducciones de español para guiones, estados de generación,
  audio, modelos y avisos.
- Añadir una descripción introductoria localizada al encabezado.
- Mejorar espaciado, tarjetas, botones, formularios, focos de teclado y
  comportamiento móvil, heredando colores de tema.
- Añadir una prueba de regresión para traducciones críticas.

**No se modifica** el contrato de API, la base de datos, la lógica de generación,
las credenciales, la publicación ni el esquema de tareas.

## Etapa 2 · Nuevo frontend desacoplado

- Construir un cliente React + TypeScript + Vite en carpeta independiente.
- Definir un sistema de diseño con tokens, componentes compartidos, claro/oscuro
  y un patrón mobile-first.
- Revisar y documentar los contratos reales de la API antes de conectarse.
- Crear el flujo: idea → guion → materiales → audio → subtítulos →
  vista previa → generación → descarga.
- Mostrar estados de tarea reales; no presentar resultados de ejemplo como reales.
- Mantener Streamlit mientras la nueva interfaz alcanza paridad funcional.

## Etapa 3 · Biblioteca y automatizaciones

- Historial y biblioteca de videos con filtros y reintentos seguros.
- Plantillas por plataforma, duraciones, voces y formatos.
- Lotes y programación con límites, monitoreo y control de costos.
- Publicación únicamente mediante cuentas autorizadas y confirmaciones
  explícitas; contemplar requisitos y restricciones de cada plataforma.

## Etapa 4 · Calidad y despliegue

- QA visual de 360–430 px, tablet y escritorio; navegación con teclado,
  accesibilidad y modos claro/oscuro.
- Pruebas de API, manejo de fallos de servicios externos y seguridad de claves.
- Revisión de costos, derechos de contenido y políticas de las plataformas.
- Proteger la API con autenticación si se expone fuera de localhost;
  no incluir claves privadas en el frontend.

## Cómo revisar esta etapa

1. Abrir el WebUI existente y elegir «Español» en el selector de idiomas.
2. Revisar creación de guion, ajustes de video, narración, subtítulos y
   estados de generación con la nueva presentación responsive.
3. Ejecutar `python -m pytest -q test/test_studio_locale.py`.
4. Confirmar en CI que se mantienen las pruebas originales antes de integrar.

**Pendiente de validar:** renderizado real en navegador y pruebas completas
de video, que requieren un entorno con las dependencias instaladas y las
credenciales de los proveedores que se quieran utilizar.
