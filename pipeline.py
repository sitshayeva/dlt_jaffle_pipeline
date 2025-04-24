import os
import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import HeaderLinkPaginator

# Environment configuration for performance
os.environ["RUNTIME__WORKERS"] = "4"
os.environ["RUNTIME__BUFFER_MAX_ITEMS"] = "1000"
os.environ["RUNTIME__MAX_PARALLEL_ITEMS"] = "1000"

# Define the data source
@dlt.source
def jaffle_shop_source():
    client = RESTClient(
        base_url="https://jaffle-shop.scalevector.ai/api/v1",
        paginator=HeaderLinkPaginator()
    )

    @dlt.resource(
        table_name="orders",
        write_disposition="append",
        primary_key="id",
        columns={"order_total": {"data_type": "decimal"}}
    )
    def orders(cursor=dlt.sources.incremental("ordered_at", initial_value="2017-08-01T00:00:00Z")):
        params = {
            "start_date": cursor.last_value,
            "page_size": 100
        }
        for page in client.paginate("orders", params=params):
            for row in page:
                try:
                    if float(row.get("order_total", 0)) <= 500:
                        yield row
                except:
                    continue
    return orders

# Define the pipeline
pipeline = dlt.pipeline(
    pipeline_name="jaffle_shop_pipeline",
    destination="duckdb",
    dataset_name="jaffle_data",
    progress="log"
)

# Run the pipeline
if __name__ == "__main__":
    load_info = pipeline.run(jaffle_shop_source())
    print("✅ Pipeline run completed.")
    print(load_info)
