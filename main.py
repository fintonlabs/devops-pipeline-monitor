import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from typing import Dict, List, Any

app = Flask(__name__)
api = Api(app)

pipelines = {}
alerts = {}


class Pipeline(Resource):
    def get(self, id: int) -> Dict[str, Any]:
        """Retrieve details of a specific pipeline."""
        if id not in pipelines:
            return {"error": "Pipeline not found"}, 404
        return pipelines[id]

    def put(self, id: int) -> Dict[str, Any]:
        """Update the configuration of a specific pipeline."""
        if id not in pipelines:
            return {"error": "Pipeline not found"}, 404
        pipelines[id] = request.json
        return pipelines[id]

    def delete(self, id: int) -> Dict[str, Any]:
        """Stop monitoring a specific pipeline."""
        if id not in pipelines:
            return {"error": "Pipeline not found"}, 404
        del pipelines[id]
        return {"result": "Pipeline deleted"}


class Pipelines(Resource):
    def get(self) -> Dict[str, Any]:
        """Retrieve a list of all monitored pipelines."""
        return pipelines

    def post(self) -> Dict[str, Any]:
        """Add a new pipeline to monitor."""
        id = max(pipelines.keys()) + 1 if pipelines else 1
        pipelines[id] = request.json
        return pipelines[id]


class Alert(Resource):
    def get(self, id: int) -> Dict[str, Any]:
        """Retrieve details of a specific alert."""
        if id not in alerts:
            return {"error": "Alert not found"}, 404
        return alerts[id]

    def put(self, id: int) -> Dict[str, Any]:
        """Update a specific alert."""
        if id not in alerts:
            return {"error": "Alert not found"}, 404
        alerts[id] = request.json
        return alerts[id]

    def delete(self, id: int) -> Dict[str, Any]:
        """Remove a specific alert."""
        if id not in alerts:
            return {"error": "Alert not found"}, 404
        del alerts[id]
        return {"result": "Alert deleted"}


class Alerts(Resource):
    def get(self) -> Dict[str, Any]:
        """Retrieve a list of all alerts."""
        return alerts

    def post(self) -> Dict[str, Any]:
        """Create a new alert."""
        id = max(alerts.keys()) + 1 if alerts else 1
        alerts[id] = request.json
        return alerts[id]


api.add_resource(Pipelines, '/pipelines')
api.add_resource(Pipeline, '/pipelines/<int:id>')
api.add_resource(Alerts, '/alerts')
api.add_resource(Alert, '/alerts/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)