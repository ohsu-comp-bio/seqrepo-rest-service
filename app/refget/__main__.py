"""start refget webservice

"""

import logging

from pkg_resources import resource_filename

import connexion
from flask import Flask, redirect


if __name__ == "__main__":
    spec_fn = "refget-openapi.yaml"
    cxapp = connexion.App(__name__, debug=True)
    cxapp.add_api(spec_fn,
                  validate_responses=True,
                  strict_validation=True)

    @cxapp.route('/')
    def index():
        return redirect("/refget/1/ui")

    cxapp.run(host="0.0.0.0",
              extra_files=[spec_fn],
              processes=1)
