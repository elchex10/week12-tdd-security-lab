"""Data importer using formats that do not execute arbitrary code."""
import ast
import json


def load_session(blob: bytes):
    return json.loads(blob)


def compute_discount(expression: str):
    return ast.literal_eval(expression)
