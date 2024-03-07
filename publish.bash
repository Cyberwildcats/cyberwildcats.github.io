#!/bin/bash

# https://docs.getpelican.com/en/3.6.2/tips.html#publishing-to-github

pelican content -o output -s pelicanconf.py
echo "cyberwildcats.net" > output/CNAME
ghp-import output
git push origin gh-pages