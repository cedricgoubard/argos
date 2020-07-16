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
import logging

import yaml
from box import Box
from flask import Flask, request, make_response
from flask_restx import Api, Resource

from utils import save_b64_jpeg, get_logging_level_from_str

with open("config.yaml", "r") as ymlfile:
    cfg = Box(yaml.safe_load(ymlfile))

app = Flask(cfg.name)
api = Api(app)

api.logger.setLevel(get_logging_level_from_str(cfg.logging_level))

@api.route('/webcam')
class ImageUpload(Resource):
    def post(self):
        img = request.json["img"]
        img_without_metadata = img.split(",")[1]
        save_b64_jpeg(img_without_metadata, cfg.upload.folder)

        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response


if __name__ == '__main__':
    host = "localhost"
    if cfg.debug:
        host = "0.0.0.0"
    app.run(debug=cfg.debug, host=host, port=cfg.port)
