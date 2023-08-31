#!/bin/bash
# Bash script that uses POST methods
curl -sX POST "$1" -H "Content-type: application/json" -d "@$2"
