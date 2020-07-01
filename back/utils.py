# -*- coding: utf-8 -*-
"""Useful functions for flask restx

This module provides useful functions to process pictures with flask restx (parser to enable API
testing using swagger, checking file extensions, and savig the files).
"""
import os
import werkzeug
from flask_restx import reqparse


def allowed_file(filename, extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in extensions


def save_picture(flask_file, cfg):
    if not allowed_file(flask_file.filename, cfg.upload.extensions):
        extension = flask_file.filename.rsplit('.', 1)[1].lower()
        return f"Extension not allowed; found {extension}, expected {cfg.upload.extensions}", 400

    save_path = os.path.join(cfg.upload.folder, flask_file.filename)
    flask_file.save(save_path)
    return "File saved", 200


def get_file_parser():
    file_upload = reqparse.RequestParser()
    file_upload.add_argument('image',
                            type=werkzeug.datastructures.FileStorage,
                            location='files',
                            required=True,
                            help='User picture')
    return file_upload
