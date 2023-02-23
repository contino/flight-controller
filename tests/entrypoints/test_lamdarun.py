from datetime import datetime
import random
import string

import pytest
from src.entrypoints.aws_lambda import lambda_handler


aggregate_id = "".join(random.choices(string.ascii_letters, k=12))
requested_time = int(round(datetime.utcnow().timestamp()))


@pytest.mark.integration
def test_lambda_handles_basic_event():
    lambda_handler(
        {
            "detail": {
                "event_type": "account_requested",
                "aggregate_id": f"{aggregate_id}",
                "time": f"{requested_time}",
            }
        },
        {},
    )


@pytest.mark.integration
def test_lambda_handles_unknown_event_type():
    lambda_handler(
        {
            "detail": {
                "event_type": "not_an_event_type",
                "aggregate_id": f"{aggregate_id}",
                "time": f"{requested_time}",
            }
        },
        {},
    )
