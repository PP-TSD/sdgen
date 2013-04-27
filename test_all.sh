#!/bin/bash
INPUT=examples/*.json
OUTPUT=examples/output
CONFIG=var/render_config.json
FORMAT=png

mkdir -p $OUTPUT

for f in $INPUT
do
    echo "Processing $f input..."
    python src/test.py $f $OUTPUT --render-config=$CONFIG --format=$FORMAT    
done
