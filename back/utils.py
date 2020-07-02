# -*- coding: utf-8 -*-
"""Useful functions for Argos backend

This module provides a a few functions used in Argos backend:
    - Saving a base 64 encoded JPEG
    - Setting logging level based on conf file
"""
import base64
import logging
from datetime import datetime


def save_b64_jpeg(img: str, folder_path: str) -> None:
    """Save a b64-encoded picture as jpeg file with the current timestamp as filename.

    Args:
        img: the jpeg picture encoded in base 64, i.e. a string
        folder_path: path to the folder in which to save the picture
    """
    timestamp = datetime.now().isoformat()
    with open(folder_path + f"/{timestamp}.jpg", "wb") as fh:
        fh.write(base64.decodebytes(img.encode()))


def get_logging_level_from_str(level:str):
    level_dic = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }

    return level_dic[level]