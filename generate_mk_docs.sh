#!/bin/sh

set -e

poetry run mkdocs build

mkdir -p static_website_builder/templates/content/
cp -a ./site/external_content/. ./static_website_builder/templates/content
cp -a ./site/internal_content/. ./static_website_builder/templates/content
cp -R ./site/static ./static_website_builder/