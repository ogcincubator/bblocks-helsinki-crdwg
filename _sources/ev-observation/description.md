## Essential Variable Observation

A GeoJSON Feature that records a single observation of a CRDWG Essential
Variable. The block extends `ogc.sosa.features.observation` (from the
[ogcapi-sosa register](https://opengeospatial.github.io/ogcapi-sosa/)) and
constrains the `observedProperty` field to conform to the `ev-schema` block.

Because it inherits from a GeoJSON Feature, the bblocks viewer renders example
instances on an interactive map.

### Structure

```
Feature
└── geometry        — point, polygon, or other geometry for the observation location
└── properties
    ├── observedProperty  — an EV object conforming to ogc.crdwg.ev-schema
    ├── resultTime        — ISO 8601 timestamp of the observation
    ├── hasResult         — the measured value and unit of measure
    └── madeBySensor      — URI of the sensor or platform
```

### Parent block

The SOSA Observation Feature block provides the base structure and JSON-LD
context for all SOSA/SSN terms (`sosa:observedProperty`, `sosa:resultTime`,
`sosa:hasResult`, `sosa:madeBySensor`). This block only adds the constraint
on `observedProperty` — no extra context mappings are needed unless additional
custom fields are introduced.
