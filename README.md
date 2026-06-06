# ERPNext Mexico Compliance

Aplicación de ERPNext para cumplir con las reglas y regulaciones de México.

## Introducción

ERPNext Mexico Compliance adapta la lógica de negocio de ERPNext para cumplir con las reglas y regulaciones de las autoridades mexicanas.

Está construida sobre [ERPNext][erpnext_github] y [Frappe Framework][frappe_github].

Para más detalles, consulta [la documentación](https://tisinproblemas.com/mexico-compliance/introduccion).

## Instalación

Los pasos de instalación asumen que ya tienes instalados [Frappe Framework][frappe_github] y [ERPNext][erpnext_github].

### Frappe Cloud

Regístrate en [Frappe Cloud][frappe_cloud] y consulta la documentación de [instalación de una app][frappe_cloud_app_install].

### Auto hospedado

```bash
# Descargar la app
bench get-app https://github.com/TI-Sin-Problemas/erpnext_mexico_compliance.git --branch version-16

# Instalar la app
bench --site site_name install-app erpnext_mexico_compliance
```

### Configuración de timbrado CFDI

Para habilitar el timbrado CFDI necesitas:

- Un paquete de timbres. Para adquirirlo, escríbenos a info@tisinproblemas.com
- Una API Key y API Secret, incluidas con tu paquete de timbres
- Un Certificado de Sello Digital (CSD) válido emitido por el SAT

Una vez que tengas todo, en tu instancia de ERPNext sigue estos pasos:

1. Ve a Escritorio → Mexico Compliance → Digital Signing Certificate
2. Agrega un Certificado de Sello Digital:

   1. Haz clic en _Add Digital Signing Certificate_
   2. Selecciona tu Empresa
   3. Adjunta tu archivo de certificado (.cer)
   4. Adjunta tu archivo de llave (.key)
   5. Ingresa la contraseña de la llave
   6. Haz clic en _Save_

3. Ve a Escritorio → Mexico Compliance → CFDI Stamping Settings:
   1. Ingresa tu API Key y API Secret
   2. Desmarca el modo de prueba en tu entorno de producción
   3. Haz clic en _Save_

Puedes consultar los timbres disponibles en CFDI Stamping Settings con el botón _Available Credits_.

## Funcionalidades

### Timbrado CFDI

El timbrado CFDI permite crear y timbrar documentos CFDI para **Facturas de Venta** y **Entradas de Pago**, según lo requieren las autoridades mexicanas.

#### Timbrado de facturas de venta

Para timbrar una factura de venta correctamente, deben cumplirse estos requisitos:

- Debe existir al menos un Certificado de Sello Digital para la empresa que emite la factura
- Debes tener timbres disponibles
- La dirección de la empresa debe tener código postal
- El cliente debe tener un RFC válido
- El cliente debe tener un régimen fiscal
- La dirección del cliente debe tener código postal
- Los artículos de la factura deben tener una Clave de producto/servicio SAT
- La UOM de los artículos debe tener una Clave de unidad de medida SAT
- La forma de pago de la factura debe tener una Forma de pago SAT
- La factura debe tener un Método de pago SAT

Una vez enviada la factura, aparecerá el botón **Stamp CFDI** en el formulario de **Sales Invoice**.

#### Timbrado de entradas de pago

Para timbrar una entrada de pago correctamente, deben cumplirse estos requisitos:

- Debe existir al menos un Certificado de Sello Digital para la empresa que emite el pago
- Debes tener timbres disponibles
- La dirección de la empresa debe tener código postal
- Todos los documentos de referencia deben estar timbrados

### Catálogos de autoridades mexicanas

Algunos catálogos de las autoridades mexicanas se agregan como DocTypes:

| DocType                    | Catálogo SAT                   |
| -------------------------- | ------------------------------ |
| Cancellation reason        | Motivo de cancelación SAT      |
| SAT CFDI Use               | Uso de CFDI SAT                |
| SAT Payment Method         | Forma de pago SAT              |
| SAT Payment Option         | Método de pago SAT             |
| SAT Product Or Service Key | Clave de producto/servicio SAT |
| SAT Tax Regime             | Régimen fiscal SAT             |
| SAT UOM Key                | Clave de unidad de medida SAT  |

### Campos de cumplimiento

Se crean campos adicionales en los siguientes DocTypes:

#### Account

| Campo    | Descripción                                      |
| -------- | ------------------------------------------------ |
| Tax Type | Tipo de impuesto para cuentas fiscales (IVA, ISR, IEPS) |

#### Bank Account

| Campo | Descripción                                           |
| ----- | ----------------------------------------------------- |
| CLABE | CLABE (Clave Bancaria Estandarizada) para cuentas bancarias |

#### Company

| Campo          | Descripción                    |
| -------------- | ------------------------------ |
| SAT Tax Regime | Régimen fiscal SAT de la empresa |

#### Customer

| Campo          | Descripción                                                              |
| -------------- | ------------------------------------------------------------------------ |
| SAT Tax Regime | Régimen fiscal SAT del cliente                                           |
| CFDI Use       | Uso de CFDI predeterminado para las facturas del cliente                 |
| Addenda        | Contenido personalizado en la sección Addenda del XML de facturas del cliente |

#### Item

| Campo                      | Descripción                              |
| -------------------------- | ---------------------------------------- |
| SAT Product or Service Key | Clave de producto/servicio SAT del artículo |

#### Mode of Payment

| Campo              | Descripción                                                        |
| ------------------ | ------------------------------------------------------------------ |
| SAT Payment Method | Vincula facturas y entradas de pago con la forma de pago SAT       |

#### Payment Entry

| Campo                        | Descripción                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| Cancellation reason          | Motivo de cancelación requerido si la entrada de pago timbrada debe cancelarse               |
| Substitute payment entry     | Entrada de pago sustituta, si el motivo de cancelación lo requiere                           |
| Stamped XML                  | XML generado por el proceso de timbrado CFDI                                                 |
| Cancellation acknowledgement | XML de acuse generado por el proceso de cancelación CFDI                                     |

#### Sales Invoice

| Campo                        | Descripción                                                                                  |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| Mode of Payment              | Forma de pago de la factura de venta                                                         |
| SAT Payment Option           | Método de pago SAT de la factura                                                             |
| SAT CFDI Use                 | Uso de CFDI de la factura                                                                    |
| SAT Payment Method           | Forma de pago SAT de la factura                                                              |
| Stamped XML                  | XML generado por el proceso de timbrado CFDI                                                 |
| Cancellation reason          | Motivo de cancelación requerido si la factura timbrada debe cancelarse                       |
| Substitute invoice           | Factura sustituta, si el motivo de cancelación lo requiere                                  |
| Cancellation acknowledgement | XML de acuse generado por el proceso de cancelación CFDI                                     |
| Addenda                      | Contenido personalizado en la sección Addenda del XML de la factura                          |

#### Sales Invoice Item

| Campo                      | Descripción                                        |
| -------------------------- | -------------------------------------------------- |
| SAT Product or Service Key | Clave de producto/servicio SAT del artículo de factura |

#### Sales Order Item

| Campo                      | Descripción                                      |
| -------------------------- | ------------------------------------------------ |
| SAT Product or Service Key | Clave de producto/servicio SAT del artículo de pedido |

#### Subscription

| Campo              | Descripción                        |
| ------------------ | ---------------------------------- |
| Mode of Payment    | Forma de pago para facturas de venta |
| SAT Payment Option | Método de pago SAT para facturas   |

#### UOM

| Campo       | Descripción                                              |
| ----------- | -------------------------------------------------------- |
| SAT UOM Key | Vincula artículos de factura con una clave de unidad SAT |

### Hooks

Se implementan los siguientes hooks de eventos de documento:

| Hook                  | Descripción                                                      |
| --------------------- | ---------------------------------------------------------------- |
| `before_stamp_cfdi`   | Método ejecutado antes de timbrar un documento CFDI              |
| `after_stamp_cfdi`    | Método ejecutado después de timbrar un documento CFDI            |
| `before_attach_files` | Método ejecutado antes de adjuntar los archivos CFDI al documento |
| `after_attach_files`  | Método ejecutado después de adjuntar los archivos CFDI al documento |
| `before_attach_pdf`   | Método ejecutado antes de adjuntar el PDF al documento           |
| `after_attach_pdf`    | Método ejecutado después de adjuntar el PDF al documento         |
| `before_attach_xml`   | Método ejecutado antes de adjuntar el XML al documento           |
| `after_attach_xml`    | Método ejecutado después de adjuntar el XML al documento         |

### Tareas programadas

| Tarea programada            | Descripción                                                              | Frecuencia |
| --------------------------- | ------------------------------------------------------------------------ | ---------- |
| `check_cancellation_status` | Consulta el estado de cancelación CFDI de facturas y entradas de pago    | Cada hora  |

## Historial de cambios

Cada commit que modifica comportamiento, herramientas o estructura del proyecto se registra aquí.

### 2026-06-06 — `fix: corregir service_duration_display en Sales Invoice Item`

- Corregida asignación de `service_end_date` a `end_date` en lugar de sobrescribir `start_date`
- Agregados tests en `erpnext_mexico_compliance/tests/test_sales_invoice_item.py` con expectativas basadas en `_()`

### 2026-06-05 — `docs: traducir README al español`

- Traducción completa del README al español
- Se mantienen nombres técnicos de DocTypes, campos y hooks como en ERPNext

### 2026-06-05 — `chore: clean up project structure and tooling`

- Eliminado empaquetado Docker (`docker/`, `.dockerignore`, `docker-ci.yml`) no usado en desarrollo local
- Eliminado `setup.py` legacy y actualizado `MANIFEST.in` al layout actual de la app
- Simplificado `hooks.py` removiendo configuración comentada sin uso
- Eliminado código muerto: `utils/permissions.py`, tests vacíos de DocTypes y hacks temporales de `sys.path`
- Corregido CI eliminando el paso roto de restauración `partial-database.sql.gz`
- Actualizado `.pre-commit-config.yaml` y `.eslintrc` para quitar referencias de otros proyectos
- Movido el logo a `public/img/logo.svg` y corregida la referencia del ícono de escritorio
- Alineada la documentación de instalación con Frappe/ERPNext `version-16`
- Agregados tests reales de validadores en `erpnext_mexico_compliance/tests/test_validators.py`

## Contribuir

¡Los PRs son bienvenidos!

Si quieres ayudar con la traducción de esta app, únete al proyecto en [Crowdin](https://crwd.in/erpnext-mexico-compliance/35a28fa170d6652eeedc5b7dbd064a7a2457550).

## Licencia

MIT

[erpnext_github]: https://github.com/frappe/erpnext
[frappe_github]: https://github.com/frappe/frappe
[frappe_cloud]: https://frappecloud.com/
[frappe_cloud_app_install]: https://frappecloud.com/docs/installing-an-app
