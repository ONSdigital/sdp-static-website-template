from json import load

from flask import Flask, render_template, url_for

app = Flask(__name__)
# reads our config file to determine if we load the full website or only the manual/mkdocs pages
with open("config/website_config.json", "r", encoding="utf-8") as read_file:
    config = load(read_file)
content_type = config["content_type"]

# With both trim_blocks and lstrip_blocks enabled, you can put block tags
# on their own lines,and the entire block line will be removed when rendered,
# preserving the whitespace of
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# The MIME type that is assumed when it can not be determined from the filename extension.
app.config["FREEZER_DEFAULT_MIMETYPE"] = "text/html"
# Path to the directory where to put the generated static site.
app.config["FREEZER_DESTINATION"] = "../build"

import static_website_builder.page  # noqa: F401
import static_website_builder.utils  # noqa: F401


@app.route("/")
def index():
    if content_type == "mkdocs_website_only":
        return render_template("index_mkdocs.html")
    return render_template("index.html")


@app.errorhandler(404)
@app.route("/page-not-found")
def page_not_found(e=None):
    return render_template("404.html"), 404 if e else 200


@app.context_processor
def build_type():
    with open(
        "content/website_config/website_type.json", "r", encoding="utf-8"
    ) as read_file:
        build = load(read_file)
        build = build["categories"]
        navigation = {"navigation": {"id": "main-navigation", "itemsList": []}}
        sidebar_navigation = []
        for item in build[content_type]["itemsList"]:
            navigation["navigation"]["itemsList"].append(
                {"url": url_for(item["url"]), "title": item["title"]}
            )
            sidebar_navigation.append(
                {"url": url_for(item["url"]), "text": item["title"]}
            )
    return {"navigation": navigation, "sidebar_navigation": sidebar_navigation}
