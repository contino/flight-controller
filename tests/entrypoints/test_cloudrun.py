import base64
from datetime import datetime
import json
import random
import string

from google.cloud import bigquery

import pytest
from src.entrypoints.cloudrun import receive_event


def test_receive_empty_event():
    assert receive_event(None)[1] == 400


def test_receive_no_message_in_event():
    assert receive_event({"thing": "thing"})[1] == 400


def test_receive_data_not_dictionary_in_event():
    assert receive_event(["thing"])[1] == 400


def test_receive_message_not_dictionary_in_event():
    assert receive_event({"message": []})[1] == 400


def test_receive_not_json_in_event():
    assert (
        receive_event({"message": {"data": base64.b64encode("Hi".encode("utf-8"))}})[1]
        == 400
    )


@pytest.mark.integration
def test_receive_correct_data():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    project_number = str(random.randint(100000000000, 999999999999))
    assert (
        receive_event(
            {
                "message": {
                    "data": base64.b64encode(
                        json.dumps(
                            {
                                "project_id": project_id,
                                "project_number": project_number,
                                "created_time": datetime.utcnow().timestamp(),
                                "event_type": "ProjectCreated",
                            }
                        ).encode("utf-8")
                    )
                }
            }
        )[1]
        == 200
    )


@pytest.mark.integration
def test_writes_project_lead_Time():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    project_number = str(random.randint(100000000000, 999999999999))
    receive_event(
        {
            "message": {
                "data": base64.b64encode(
                    json.dumps(
                        {
                            "project_id": project_id,
                            "project_number": project_number,
                            "requested_time": datetime.utcnow().timestamp(),
                            "event_type": "ProjectRequested",
                        }
                    ).encode("utf-8")
                )
            }
        }
    )
    receive_event(
        {
            "message": {
                "data": base64.b64encode(
                    json.dumps(
                        {
                            "project_id": project_id,
                            "project_number": project_number,
                            "created_time": datetime.utcnow().timestamp(),
                            "event_type": "ProjectCreated",
                        }
                    ).encode("utf-8")
                )
            }
        }
    )

    client = bigquery.Client()

    query = f"""
    SELECT lead_time
    FROM `flight_controller.project_lead_times`
    WHERE project_id = '{project_id}'
  """
    got = client.query(query).result()

    count = 0
    for _ in got:
        count += 1

    assert count == 1

@pytest.mark.integration
def test_receive_malformed_data():
    project_id = "".join(random.choices(string.ascii_letters, k=12))
    project_number = str(random.randint(100000000000, 999999999999))
    assert (
        receive_event(
            {
                "message": {
                    "data": base64.b64encode(
                        json.dumps(
                            {
                                "project_id": project_id,
                                "project_number": project_number,
                                "created_time": datetime.utcnow().timestamp(),
                            }
                        ).encode("utf-8")
                    )
                }
            }
        )[1]
        == 200
    )
