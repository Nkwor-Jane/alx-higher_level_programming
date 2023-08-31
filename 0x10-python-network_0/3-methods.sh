#!/bin/bash
# Bash script that displays all HTTP methods of the server
curl -sI "$1" | grep "Allow" | cut -d "" -f2-
