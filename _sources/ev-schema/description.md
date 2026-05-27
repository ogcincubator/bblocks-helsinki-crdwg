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
