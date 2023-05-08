import json

from cdktf_cdktf_provider_google import (
    bigquery_dataset, bigquery_table,
    data_google_bigquery_default_service_account, kms_crypto_key,
    kms_crypto_key_iam_binding, kms_key_ring)
from constructs import Construct


class BigQueryComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
        location: str,
        event_table: str,
        metric_table: str,
        flight_controller_key_ring: kms_key_ring.KmsKeyRing,
    ):
        super().__init__(scope, id)

        bigquery_default_service_account = data_google_bigquery_default_service_account.DataGoogleBigqueryDefaultServiceAccount(
            self, "bigquery_default_service_account", project=project_id
        )

        event_dataset_key = kms_crypto_key.KmsCryptoKey(
            self,
            "event_dataset_key",
            name="bigquery_event_dataset_key",
            key_ring=flight_controller_key_ring.id,
            rotation_period="7776000s",

            lifecycle= {
                "prevent_destroy": True
            }
        )

        event_dataset_key_iam = kms_crypto_key_iam_binding.KmsCryptoKeyIamBinding(
            self,
            "event_dataset_key_iam_binding",
            crypto_key_id=event_dataset_key.id,
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            members=[bigquery_default_service_account.member],
        )

        event_table_key = kms_crypto_key.KmsCryptoKey(
            self,
            "event_table_key",
            name="bigquery_event_table_key",
            key_ring=flight_controller_key_ring.id,
            rotation_period="7776000s",

            lifecycle= {
                "prevent_destroy": True
            }
        )

        event_table_key_iam = kms_crypto_key_iam_binding.KmsCryptoKeyIamBinding(
            self,
            "event_table_key_iam_binding",
            crypto_key_id=event_table_key.id,
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            members=[bigquery_default_service_account.member],
        )

        self.event_dataset = bigquery_dataset.BigqueryDataset(
            self,
            "event_dataset",
            dataset_id=event_table,
            location=location,
            project=project_id,
            default_encryption_configuration={"kms_key_name": event_dataset_key.id},
        )

        self.event_table = bigquery_table.BigqueryTable(
            self,
            "event_table",
            dataset_id=self.event_dataset.dataset_id,
            table_id="events_data",
            project=project_id,
            encryption_configuration={"kms_key_name": event_table_key.id},
            schema=json.dumps(
                [
                    {"name": "event_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "event_type", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "aggregate_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "aggregate_type", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "aggregate_version", "type": "INT64", "mode": "REQUIRED"},
                    {"name": "event_version", "type": "INT64", "mode": "REQUIRED"},
                    {"name": "payload", "type": "JSON", "mode": "REQUIRED"},
                    {"name": "timestamp", "type": "TIMESTAMP", "mode": "REQUIRED"},
                ]
            ),
            deletion_protection=False,
        )

        metric_dataset_key = kms_crypto_key.KmsCryptoKey(
            self,
            "metric_dataset_key",
            name="bigquery_metric_dataset_key",
            key_ring=flight_controller_key_ring.id,
            rotation_period="7776000s",

            lifecycle= {
                "prevent_destroy": True
            }
        )

        metric_dataset_key_iam = kms_crypto_key_iam_binding.KmsCryptoKeyIamBinding(
            self,
            "metric_dataset_key_iam_binding",
            crypto_key_id=metric_dataset_key.id,
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            members=[bigquery_default_service_account.member],
        )

        metric_table_key = kms_crypto_key.KmsCryptoKey(
            self,
            "metric_table_key",
            name="bigquery_metric_table_key",
            key_ring=flight_controller_key_ring.id,
            rotation_period="7776000s",

            lifecycle= {
                "prevent_destroy": True
            }
        )

        metric_table_key_iam = kms_crypto_key_iam_binding.KmsCryptoKeyIamBinding(
            self,
            "metric_table_key_iam_binding",
            crypto_key_id=metric_table_key.id,
            role="roles/cloudkms.cryptoKeyEncrypterDecrypter",
            members=[bigquery_default_service_account.member],
        )

        self.metric_dataset = bigquery_dataset.BigqueryDataset(
            self,
            "metric_dataset",
            dataset_id=metric_table,
            location=location,
            project=project_id,
            default_encryption_configuration={"kms_key_name": metric_dataset_key.id},
        )

        self.metric_table = bigquery_table.BigqueryTable(
            self,
            "metric_table",
            dataset_id=self.metric_dataset.dataset_id,
            table_id="metrics_data",
            project=project_id,
            encryption_configuration={"kms_key_name": metric_table_key.id},
            schema=json.dumps(
                [
                    {"name": "aggregate_id", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "guardrail_id", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "container_id", "type": "STRING", "mode": "NULLABLE"},
                    {"name": "measure_name", "type": "STRING", "mode": "REQUIRED"},
                    {"name": "time", "type": "TIMESTAMP", "mode": "REQUIRED"},
                    {"name": "measure_value", "type": "FLOAT64", "mode": "REQUIRED"},
                ]
            ),
            deletion_protection=False,
        )
