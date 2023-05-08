from cdktf_cdktf_provider_google import (compute_backend_service,
                                         compute_global_address,
                                         compute_global_forwarding_rule,
                                         compute_health_check,
                                         compute_region_network_endpoint_group,
                                         compute_target_http_proxy,
                                         compute_url_map,
                                         compute_managed_ssl_certificate,
                                         compute_target_https_proxy,
                                         )
from constructs import Construct


class LBComponent(Construct):
    def __init__(
        self,
        scope: Construct,
        id: str,
        project_id: str,
        location: str,
        name_prefix: str,
        DOMAIN_NAME: str,
    ):
        super().__init__(scope, id)

        # Create network endpoint group
        self.neg = (
            compute_region_network_endpoint_group.ComputeRegionNetworkEndpointGroup(
                self,
                "function_neg",
                name=name_prefix+"-grafana-lb-neg",
                project=project_id,
                region=location,
                network_endpoint_type="SERVERLESS",
                cloud_run={
                    "service": f"{name_prefix}-grafana",
                },
            )
        )

        # self.health_check = compute_health_check.ComputeHealthCheck(
        #     self,
        #     "health_check",
        #     name=name_prefix+"-grafana-lb-health-check",
        #     project=project_id,
        #     ssl_health_check={
        #     "port": 443
        #     },
        # )

        # Create Backend service network endpoint
        self.backend_service = compute_backend_service.ComputeBackendService(
            self,
            "backend_service",
            name=name_prefix+"-grafana-lb-backend",
            project=project_id,
            timeout_sec=30,
            connection_draining_timeout_sec=300,
            load_balancing_scheme="EXTERNAL_MANAGED",
            # health_checks=[self.health_check.id],
            backend=[{"group": str(self.neg.id)}],
        )

        # Create global address
        self.global_address = compute_global_address.ComputeGlobalAddress(
            self,
            "global_address",
            name=name_prefix+"-grafana-ip",
            project=project_id,
        )

        # Create SSL certificate
        self.certificate = compute_managed_ssl_certificate.ComputeManagedSslCertificate(
            self,
            "ssl_certificate",
            name=name_prefix+"-ssl-certificate",
            project=project_id,
            type="MANAGED",
            managed={
            "domains": [str(DOMAIN_NAME),]
            }
        )

        # Create URL map
        self.default = compute_url_map.ComputeUrlMap(
            self,
            "default-urlmap",
            name=name_prefix+"-grafana-default-urlmap",
            default_service=self.backend_service.self_link,
            project=project_id,
        )

        self.https_redirect = compute_url_map.ComputeUrlMap(
            self,
            "https_redirect",
            name=name_prefix+"-https-redirect",
            project=project_id,
            default_url_redirect={
            "https_redirect": True,
            "strip_query": False,
            "redirect_response_code": "MOVED_PERMANENTLY_DEFAULT"
            }
        )

        # HTTPS proxy when ssl is true
        self.https_proxy = compute_target_https_proxy.ComputeTargetHttpsProxy(
            self,
            "https_proxy",
            name=name_prefix+"-grafana-https-proxy",
            url_map=self.default.self_link,
            project=project_id,
            ssl_certificates=[self.certificate.id],
        )

        # HTTP Proxy when http forwarding is true
        self.http_proxy = compute_target_http_proxy.ComputeTargetHttpProxy(
            self,
            "http_proxy",
            name=name_prefix+"-grafana-http-proxy",
            url_map=self.https_redirect.self_link,
            project=project_id,
        )

        # Create global forwarding rule
        self.http_forwarding = (
            compute_global_forwarding_rule.ComputeGlobalForwardingRule(
                self,
                "http_forwarding",
                name=name_prefix+"-grafana-http",
                target=self.http_proxy.self_link,
                port_range="80",
                project=project_id,
                load_balancing_scheme="EXTERNAL_MANAGED",
                ip_address=self.global_address.address,
            )
        )

        self.https_forwarding = compute_global_forwarding_rule.ComputeGlobalForwardingRule(
            self,
            "https_forwarding",
            name=name_prefix+"-grafana-https",
            target=self.https_proxy.self_link,
            port_range="443",
            project=project_id,
            ip_address=self.global_address.address,
            load_balancing_scheme="EXTERNAL_MANAGED",
        )
