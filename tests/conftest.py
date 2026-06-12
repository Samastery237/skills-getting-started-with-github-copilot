import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

initial_activities = copy.deepcopy(activities)


def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(initial_activities))


@pytest.fixture(name="client")
def client_fixture():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_fixture():
    reset_activities()
