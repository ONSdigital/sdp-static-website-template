from flask import render_template
from markupsafe import escape, Markup
import markdown
from static_website_builder import app
from .utils import _page_not_found


@app.route("/page-1")
def page_1():
    try:
        with open(
            "./content/page_1.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("page_1.html", page_body=body)


@app.route("/page-2")
def page_2():
    try:
        with open(
            "./content/page_2.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("page_2.html", page_body=body)


@app.route("/page-3")
def page_3():
    try:
        with open(
            "./content/page_3.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("page_3.html", page_body=body)


@app.route("/about")
def about_page():
    try:
        with open(
            "./content/about.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("about.html", page_body=body)


@app.route("/accessibility-statement")
def accessibility_page():
    try:
        with open(
            "./content/accessibility.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("accessibility_statement.html", page_body=body)


@app.route("/cookies")
def cookies_page():
    return render_template("cookies.html")


@app.route("/privacy-and-data-protection")
def privacy_data_page():
    try:
        with open(
            "./content/privacy_data.md", "r", encoding="utf-8"
        ) as input_file:
            text = input_file.read()
            escaped_text = escape(text)
            body = Markup(markdown.markdown(escaped_text))
    except OSError as e:
        _page_not_found(e)
    return render_template("privacy_data.html", page_body=body)


@app.route("/.well-known/security.txt")
def security_text_page():
    return render_template("security.html")
