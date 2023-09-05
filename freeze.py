from flask_frozen import Freezer  # pylint: disable=import-error

from static_website_builder import app

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
