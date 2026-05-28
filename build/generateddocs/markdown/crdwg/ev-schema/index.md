
# Essential Variable (Schema)

`ogc.crdwg.ev-schema` *v0.1*

Schema and JSON-LD context for defining a Climate Resilience Essential Variable.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Essential Variable schema

Defines the JSON structure for a single Essential Variable (EV) definition,
together with a JSON-LD context that maps every field to a URI.

A document conforming to this block may be either a single EV object or an
array of EV objects (the `oneOf` at the root of the schema).

### Required fields

| Field | Mapped to | Notes |
|-------|-----------|-------|
| `id` | — (used as `@id`) | Compact URI, e.g. `ev:surface-air-temperature` |
| `name` | `skos:prefLabel` | Human-readable label |
| `code` | `skos:notation` | Authority code, e.g. `T2m` (GCOS) |
| `domain` | `ev:evDomain` | One of the five Earth-system domains |
| `standardAuthority` | `ev:standardAuthority` | Compact URI of the mandating body |

### Optional fields

| Field | Mapped to | Notes |
|-------|-----------|-------|
| `definition` | `skos:definition` | Prose definition |
| `unit` | `qudt:unit` | QUDT unit compact URI, e.g. `qudt-unit:K` |
| `measurementTypes` | `ev:measurementTypes` | Array of `in-situ`, `remote-sensing`, or `reanalysis` |
| `related` | `skos:related` | Compact URIs of related EVs |

### Semantic uplift

The JSON-LD context resolves compact URIs at uplift time:

- `ev:surface-air-temperature` → `https://w3id.org/ogc/crdwg/ev/surface-air-temperature`
- `ev:GCOS` → `https://w3id.org/ogc/crdwg/ev/GCOS`
- `in-situ` (inside `measurementTypes`) → `https://w3id.org/ogc/crdwg/ev/measurementType/in-situ`
- `qudt-unit:K` → `http://qudt.org/vocab/unit/K`

## Examples

### Surface Air Temperature
#### json
```json
{
  "id": "ev:surface-air-temperature",
  "name": "Surface Air Temperature",
  "code": "T2m",
  "definition": "Temperature of the air at 2 m above the surface.",
  "domain": "Atmosphere",
  "standardAuthority": "ev:GCOS",
  "unit": "qudt-unit:K",
  "measurementTypes": ["in-situ", "remote-sensing", "reanalysis"],
  "related": ["ev:precipitation", "ev:soil-moisture", "ev:sea-level"]
}

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-helsinki-crdwg/build/annotated/crdwg/ev-schema/context.jsonld",
  "id": "ev:surface-air-temperature",
  "name": "Surface Air Temperature",
  "code": "T2m",
  "definition": "Temperature of the air at 2 m above the surface.",
  "domain": "Atmosphere",
  "standardAuthority": "ev:GCOS",
  "unit": "qudt-unit:K",
  "measurementTypes": [
    "in-situ",
    "remote-sensing",
    "reanalysis"
  ],
  "related": [
    "ev:precipitation",
    "ev:soil-moisture",
    "ev:sea-level"
  ]
}
```

#### ttl
```ttl
@prefix ev: <https://w3id.org/ogc/crdwg/ev/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudt-unit: <http://qudt.org/vocab/unit/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

[] qudt:unit qudt-unit:K ;
    skos:definition "Temperature of the air at 2 m above the surface." ;
    skos:notation "T2m" ;
    skos:prefLabel "Surface Air Temperature" ;
    skos:related ev:precipitation,
        ev:sea-level,
        ev:soil-moisture ;
    ev:evDomain <https://w3id.org/ogc/crdwg/Atmosphere> ;
    ev:measurementTypes <https://w3id.org/ogc/crdwg/ev/measurementType/in-situ>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/reanalysis>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/remote-sensing> ;
    ev:standardAuthority ev:GCOS .


```


### All four EVs (array form)
#### json
```json
[
  {
    "id": "ev:surface-air-temperature",
    "name": "Surface Air Temperature",
    "code": "T2m",
    "domain": "Atmosphere",
    "standardAuthority": "ev:GCOS",
    "unit": "qudt-unit:K",
    "measurementTypes": ["in-situ", "remote-sensing", "reanalysis"],
    "related": ["ev:precipitation", "ev:soil-moisture", "ev:sea-level"]
  },
  {
    "id": "ev:precipitation",
    "name": "Precipitation",
    "code": "P",
    "domain": "Atmosphere",
    "standardAuthority": "ev:GCOS",
    "unit": "qudt-unit:MilliM",
    "measurementTypes": ["in-situ", "remote-sensing", "reanalysis"],
    "related": ["ev:surface-air-temperature", "ev:soil-moisture"]
  },
  {
    "id": "ev:soil-moisture",
    "name": "Soil Moisture",
    "code": "SM",
    "domain": "Land",
    "standardAuthority": "ev:GCOS",
    "measurementTypes": ["in-situ", "remote-sensing"],
    "related": ["ev:precipitation", "ev:surface-air-temperature"]
  },
  {
    "id": "ev:sea-level",
    "name": "Sea Level",
    "code": "SL",
    "domain": "Ocean",
    "standardAuthority": "ev:GCOS",
    "unit": "qudt-unit:M",
    "measurementTypes": ["in-situ", "remote-sensing"],
    "related": ["ev:surface-air-temperature"]
  }
]

```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/bblocks-helsinki-crdwg/build/annotated/crdwg/ev-schema/context.jsonld",
  "@graph": [
    {
      "id": "ev:surface-air-temperature",
      "name": "Surface Air Temperature",
      "code": "T2m",
      "domain": "Atmosphere",
      "standardAuthority": "ev:GCOS",
      "unit": "qudt-unit:K",
      "measurementTypes": [
        "in-situ",
        "remote-sensing",
        "reanalysis"
      ],
      "related": [
        "ev:precipitation",
        "ev:soil-moisture",
        "ev:sea-level"
      ]
    },
    {
      "id": "ev:precipitation",
      "name": "Precipitation",
      "code": "P",
      "domain": "Atmosphere",
      "standardAuthority": "ev:GCOS",
      "unit": "qudt-unit:MilliM",
      "measurementTypes": [
        "in-situ",
        "remote-sensing",
        "reanalysis"
      ],
      "related": [
        "ev:surface-air-temperature",
        "ev:soil-moisture"
      ]
    },
    {
      "id": "ev:soil-moisture",
      "name": "Soil Moisture",
      "code": "SM",
      "domain": "Land",
      "standardAuthority": "ev:GCOS",
      "measurementTypes": [
        "in-situ",
        "remote-sensing"
      ],
      "related": [
        "ev:precipitation",
        "ev:surface-air-temperature"
      ]
    },
    {
      "id": "ev:sea-level",
      "name": "Sea Level",
      "code": "SL",
      "domain": "Ocean",
      "standardAuthority": "ev:GCOS",
      "unit": "qudt-unit:M",
      "measurementTypes": [
        "in-situ",
        "remote-sensing"
      ],
      "related": [
        "ev:surface-air-temperature"
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix ev: <https://w3id.org/ogc/crdwg/ev/> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix qudt-unit: <http://qudt.org/vocab/unit/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

[] skos:notation "SM" ;
    skos:prefLabel "Soil Moisture" ;
    skos:related ev:precipitation,
        ev:surface-air-temperature ;
    ev:evDomain <https://w3id.org/ogc/crdwg/Land> ;
    ev:measurementTypes <https://w3id.org/ogc/crdwg/ev/measurementType/in-situ>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/remote-sensing> ;
    ev:standardAuthority ev:GCOS .

[] qudt:unit qudt-unit:K ;
    skos:notation "T2m" ;
    skos:prefLabel "Surface Air Temperature" ;
    skos:related ev:precipitation,
        ev:sea-level,
        ev:soil-moisture ;
    ev:evDomain <https://w3id.org/ogc/crdwg/Atmosphere> ;
    ev:measurementTypes <https://w3id.org/ogc/crdwg/ev/measurementType/in-situ>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/reanalysis>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/remote-sensing> ;
    ev:standardAuthority ev:GCOS .

[] qudt:unit qudt-unit:MilliM ;
    skos:notation "P" ;
    skos:prefLabel "Precipitation" ;
    skos:related ev:soil-moisture,
        ev:surface-air-temperature ;
    ev:evDomain <https://w3id.org/ogc/crdwg/Atmosphere> ;
    ev:measurementTypes <https://w3id.org/ogc/crdwg/ev/measurementType/in-situ>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/reanalysis>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/remote-sensing> ;
    ev:standardAuthority ev:GCOS .

[] qudt:unit qudt-unit:M ;
    skos:notation "SL" ;
    skos:prefLabel "Sea Level" ;
    skos:related ev:surface-air-temperature ;
    ev:evDomain <https://w3id.org/ogc/crdwg/Ocean> ;
    ev:measurementTypes <https://w3id.org/ogc/crdwg/ev/measurementType/in-situ>,
        <https://w3id.org/ogc/crdwg/ev/measurementType/remote-sensing> ;
    ev:standardAuthority ev:GCOS .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: Essential Variable definition
$defs:
  EssentialVariable:
    type: object
    required:
    - id
    - name
    - code
    - domain
    - standardAuthority
    properties:
      id:
        type: string
        description: Compact URI for this variable, e.g. ev:surface-air-temperature
      name:
        type: string
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
      code:
        type: string
        description: Authority code, e.g. T2m (GCOS)
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#notation
      definition:
        type: string
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
      domain:
        type: string
        enum:
        - Atmosphere
        - Land
        - Ocean
        - Cryosphere
        - Biosphere
        x-jsonld-id: https://w3id.org/ogc/crdwg/ev/evDomain
        x-jsonld-type: '@id'
      standardAuthority:
        type: string
        description: Compact URI of the body mandating this variable, e.g. ev:GCOS
        x-jsonld-id: https://w3id.org/ogc/crdwg/ev/standardAuthority
        x-jsonld-type: '@id'
      unit:
        type: string
        description: QUDT unit compact URI, e.g. qudt-unit:K
        x-jsonld-id: http://qudt.org/schema/qudt/unit
        x-jsonld-type: '@id'
      measurementTypes:
        type: array
        items:
          type: string
          enum:
          - in-situ
          - remote-sensing
          - reanalysis
        x-jsonld-id: https://w3id.org/ogc/crdwg/ev/measurementTypes
        x-jsonld-type: '@id'
        x-jsonld-base: https://w3id.org/ogc/crdwg/ev/measurementType/
      related:
        type: array
        items:
          type: string
          description: Compact URIs of related EVs
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#related
        x-jsonld-type: '@id'
oneOf:
- $ref: '#/$defs/EssentialVariable'
- type: array
  items:
    $ref: '#/$defs/EssentialVariable'
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  qudt: http://qudt.org/schema/qudt/
  ev: https://w3id.org/ogc/crdwg/ev/
  qudt-unit: http://qudt.org/vocab/unit/
  dct: http://purl.org/dc/terms/

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/bblocks-helsinki-crdwg/build/annotated/crdwg/ev-schema/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/bblocks-helsinki-crdwg/build/annotated/crdwg/ev-schema/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "name": "skos:prefLabel",
    "code": "skos:notation",
    "definition": "skos:definition",
    "domain": {
      "@id": "ev:evDomain",
      "@type": "@id"
    },
    "standardAuthority": {
      "@id": "ev:standardAuthority",
      "@type": "@id"
    },
    "unit": {
      "@id": "qudt:unit",
      "@type": "@id"
    },
    "measurementTypes": {
      "@context": {
        "@base": "https://w3id.org/ogc/crdwg/ev/measurementType/"
      },
      "@id": "ev:measurementTypes",
      "@type": "@id"
    },
    "related": {
      "@id": "skos:related",
      "@type": "@id"
    },
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "qudt": "http://qudt.org/schema/qudt/",
    "ev": "https://w3id.org/ogc/crdwg/ev/",
    "qudt-unit": "http://qudt.org/vocab/unit/",
    "dct": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/bblocks-helsinki-crdwg/build/annotated/crdwg/ev-schema/context.jsonld)

## Sources

* [GCOS Essential Climate Variables](https://gcos.wmo.int/en/essential-climate-variables)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-helsinki-crdwg](https://github.com/ogcincubator/bblocks-helsinki-crdwg)
* Path: `_sources/ev-schema`

