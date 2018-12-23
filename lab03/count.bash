#!/bin/bash

for f in *; do
if [ -f "$f" ]; then
w=`wc -w $f | cut -f1 -d' '`
l=`wc -l $f | cut -f1 -d' '`
echo "$f $l $w"
fi
done
