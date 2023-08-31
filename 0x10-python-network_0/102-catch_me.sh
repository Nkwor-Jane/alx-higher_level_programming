#!/bin/bash
# Get sever to respond with You got me
curl -s -d  "You got me!" "0.0.0.0:5000/catch_me" -X PUT
