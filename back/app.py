# -*- coding: utf-8 -*-
"""Argos backend application

This Flask application receives images from the front end, and transfer them to the processing
microservices.

Attributes:
    cfg (box.Box): configuration object based on the box module, which reads the config.yaml file
        and make the key / values accessible as attributes of this object.

    app (flask.Flask): the core Flask application

    api (flask_restx.Api): the Flask restx api, which is an overlay of the Flask app providing an
        integrated swagger
"""
import yaml
from box import Box
from flask import Flask
from flask_restx import Api, Resource

from utils import get_file_parser, save_picture

with open("config.yaml", "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))

app = Flask(cfg.name)
api = Api(app)

@api.route('/webcam')
class ArgosBack(Resource):
    @api.expect(get_file_parser())
    def post(self):
        args = get_file_parser().parse_args()
        return save_picture(args["image"], cfg)


if __name__ == '__main__':
    app.run(debug=cfg.debug, port=cfg.port)
