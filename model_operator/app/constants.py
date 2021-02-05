import os
from pathlib import Path

from jinja2 import Template

POLLER_DELAY = int(os.environ.get("POLLER_DELAY", 5))
MS_CONFIGMAP_TEMPLATE_PATH = Path(os.environ["MODELSERVER_CONFIGMAP_TEMPLATE_PATH"])
assert MS_CONFIGMAP_TEMPLATE_PATH.exists(), MS_CONFIGMAP_TEMPLATE_PATH
MS_CONFIGMAP_TEMPLATE = Template(MS_CONFIGMAP_TEMPLATE_PATH.read_text())

MS_DEPLOYMENT_PATH = Path(os.environ["MODELSERVER_DEPLOYMENT_PATH"])
assert MS_DEPLOYMENT_PATH.exists(), MS_DEPLOYMENT_PATH

K8S_NS = os.environ["K8S_NS"]
MS_CONFIGMAP_NAME = os.environ["MODELSERVER_CONFIGMAP_NAME"]
MS_DEPLOYMENT_NAME = os.environ["MODELSERVER_DEPLOYMENT_NAME"]

MLFLOW_MODEL_NAME = os.environ["MLFLOW_MODEL_NAME"]
MLFLOW_MODEL_STAGE = os.environ.get("MLFLOW_MODEL_STAGE", "Production")
