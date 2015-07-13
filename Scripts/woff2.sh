#!/bin/bash
git clone https://github.com/google/woff2.git woff2
cd woff2 && git submodule init && git submodule update && make all
