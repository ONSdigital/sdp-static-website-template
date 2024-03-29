#!/bin/sh

set -e

website_type=$(jq -r '.content_type' ./config/website_config.json)
if [ "$website_type" != "full_website" ] && [ "$website_type" != "mkdocs_website" ] && [ "$website_type" != "manual_website" ]; then
  echo website_type in ./config/website_config.json it not a valid type, please amend the files value to equal one of full_website, manual_website or mkdocs_website
  exit 1
fi;
echo Building content for type $website_type
poetry run mkdocs build

mkdir -p static_website_builder/templates/content/
cp -a ./site/external_content/. ./static_website_builder/templates/content
cp -a ./site/internal_content/. ./static_website_builder/templates/content
cp -R ./site/static ./static_website_builder/