from flask import abort


def _page_not_found(error):
    print(error)
    abort(404)
