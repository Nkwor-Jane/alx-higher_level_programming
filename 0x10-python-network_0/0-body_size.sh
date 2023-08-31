#!/bin/bash
# Bash script that displays size of body of response, content-length
curl -sI "$1" | grep "Content-Length" | cut -d '' -f2
