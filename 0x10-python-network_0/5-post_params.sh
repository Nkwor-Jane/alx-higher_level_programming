#!/bin/bash
# Bash script that uses POST methos
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PL" "$1"
