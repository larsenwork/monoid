#!/bin/bash
echo Total Nodes: $CIRCLE_NODE_TOTAL
echo Current Node: $CIRCLE_NODE_INDEX

docker run -v `pwd`:/data colman/py-fontforge ./Scripts/build.py $CIRCLE_NODE_TOTAL $CIRCLE_NODE_INDEX $1
