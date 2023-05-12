ARG GRAFANA_VERSION="latest"

# Download base grafana
FROM grafana/grafana:${GRAFANA_VERSION}

ARG GRAFANA_PASSWORD

USER grafana

# Set the admin password 
ENV GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD}

# Install BigQuery data source plugin
RUN grafana-cli plugins install simpod-json-datasource && \
    grafana-cli plugins install grafana-bigquery-datasource && \
    mkdir -p /var/lib/grafana/plugins/grafana-bigquery-datasource

# Set the default port
ENV GF_SERVER_HTTP_PORT=8080

# Expose Grafana's default port
EXPOSE 8080
