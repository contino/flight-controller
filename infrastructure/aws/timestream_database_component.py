from cdktf_cdktf_provider_aws import (timestreamwrite_database,
                                      timestreamwrite_table)
from constructs import Construct


class TimeStreamDBcomponent(Construct):
    def __init__(self, scope: Construct, id: str, name: str):
        super().__init__(scope, id)

        timestream_db = timestreamwrite_database.TimestreamwriteDatabase(
            self, "timestreamdb", database_name=name, tags={"deployment": "cdktf"}
        )
        self.timestream_table = timestreamwrite_table.TimestreamwriteTable(
            self,
            "timestreamtable",
            table_name="metrics_table",
            database_name=timestream_db.database_name,
            retention_properties={  # in-memory tier of a week and afterwards data will be moved to read-optimised tier for two years.
                "magnetic_store_retention_period_in_days": 365 * 2,
                "memory_store_retention_period_in_hours": 24 * 2,
            },
        )
