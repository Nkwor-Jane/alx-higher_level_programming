#!/bin/bash
# Bash script that prints out only status code
curl -sI -o /dev/null -w "%{http_code}" "$1"
