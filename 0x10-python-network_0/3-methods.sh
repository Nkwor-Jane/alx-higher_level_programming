#!/bin/bash
# Bash script that displays all HTTP methods of the server
curl -X GET -sI "$1" | grep "Allow" | cut -d " " -f2-
