
# Essential Variable Ontology (Model)

`ogc.crdwg.ev-ontology` *v0.1*

OWL ontology defining vocabulary terms for Essential Variable descriptions that are not covered by standard vocabularies.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Essential Variable Ontology

This ontology defines the OWL properties and SKOS code list used to describe
Essential Variables (EVs) in the CRDWG registry. It covers only terms that
have no adequate equivalent in widely-adopted standard vocabularies.

### Why a custom ontology?

Standard vocabularies cover most needs:

- `skos:prefLabel` / `skos:definition` / `skos:notation` — human-readable
  labels, definitions, and authority codes.
- `skos:related` — links between related EVs.
- `qudt:unit` — physical units of measurement.
- `dct:*` — provenance and bibliographic metadata.

However, three concepts specific to the EV registry have no standard home:

| Term | Why not standard |
|------|-----------------|
| `ev:standardAuthority` | The body mandating a variable (GCOS, GOOS, GEO BON) has no direct equivalent in SKOS, PROV, or DublinCore that captures the "mandating body" relationship rather than a general creator/publisher. |
| `ev:evDomain` | The Earth-system domain partition (Atmosphere, Land, Ocean, Cryosphere, Biosphere) is specific to the EV community and not covered by CF conventions or existing environmental ontologies at the required granularity. |
| `ev:measurementTypes` | The classification of measurement approaches (in-situ, remote sensing, reanalysis) as a controlled code list is unique to the EV community. |

### Measurement Type code list

`ev:MeasurementTypeScheme` is a `skos:ConceptScheme` with three concepts:

- `ev-mt:InSitu` — ground-based or in-water direct measurements.
- `ev-mt:RemoteSensing` — satellite or airborne observations.
- `ev-mt:Reanalysis` — model-based reconstructions blending observations
  with numerical weather prediction.

## Sources

* [GCOS Essential Climate Variables](https://gcos.wmo.int/en/essential-climate-variables)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/bblocks-helsinki-crdwg](https://github.com/ogcincubator/bblocks-helsinki-crdwg)
* Path: `_sources/ev-ontology`

