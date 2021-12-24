from elites import app, logger
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)


class User(ma.Schema):
    # TODO
    pass
