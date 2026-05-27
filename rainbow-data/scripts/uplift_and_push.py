"""
Validates, semantically uplifts, and pushes all EV instance files in a
directory to a Fuseki endpoint.

Usage:
    python uplift_and_push.py <data-dir>

Environment variables:
    FUSEKI_URL       (default: http://localhost:3030)
    FUSEKI_DATASET   (default: fuseki)
    FUSEKI_PASSWORD
    GRAPH_URI        (default: https://w3id.org/ogc/crdwg/graphs/ev)
    BASE_URI         (default: https://w3id.org/ogc/crdwg/)
    REGISTER_URL     URL of the bblocks register.json
                     (default: published GitHub Pages URL)
"""
import json
import os
import sys
from pathlib import Path

import requests
from ogc.bblocks.register import load_register
from ogc.bblocks.validate import validate_json
from ogc.bblocks.semantic_uplift import uplift_json

FUSEKI_URL     = os.environ.get("FUSEKI_URL",     "http://localhost:3030")
FUSEKI_DATASET = os.environ.get("FUSEKI_DATASET", "fuseki")
FUSEKI_PASSWORD = os.environ.get("FUSEKI_PASSWORD", "changeme")
GRAPH_URI      = os.environ.get("GRAPH_URI",      "https://w3id.org/ogc/crdwg/graphs/ev")
BASE_URI       = os.environ.get("BASE_URI",       "https://w3id.org/ogc/crdwg/")
REGISTER_URL   = os.environ.get(
    "REGISTER_URL",
    "https://ogcincubator.github.io/bblocks-helsinki-crdwg/build/register.json",
)
BLOCK_ID = "ogc.crdwg.ev-schema"

data_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("rainbow-data/ev")

register = load_register(REGISTER_URL)
bblock   = register.get_item_full(BLOCK_ID)

combined_graph = None

for json_file in sorted(data_dir.glob("**/*.json")):
    print(f"Processing {json_file} …")
    with open(json_file) as f:
        data = json.load(f)

    result = validate_json(bblock, data)
    result.raise_for_invalid()
    print(f"  ✓ validation passed")

    graph = uplift_json(bblock, data, base_uri=BASE_URI)
    if combined_graph is None:
        combined_graph = graph
    else:
        combined_graph += graph

if combined_graph is None:
    print("No files found.")
    sys.exit(0)

turtle = combined_graph.serialize()

response = requests.put(
    f"{FUSEKI_URL}/{FUSEKI_DATASET}/data",
    params={"graph": GRAPH_URI},
    headers={"Content-Type": "text/turtle"},
    data=turtle,
    auth=("admin", FUSEKI_PASSWORD),
)
response.raise_for_status()
print(f"\nPushed to {GRAPH_URI} (HTTP {response.status_code})")
