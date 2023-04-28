from cdktf_cdktf_provider_google import (compute_backend_service,
                                         compute_global_address,
                                         compute_global_forwarding_rule,
                                         compute_health_check,
                                         compute_region_network_endpoint_group,
                                         compute_target_http_proxy,
                                         compute_url_map,
                                         compute_managed_ssl_certificate
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
    ):
        super().__init__(scope, id)

        # Create network endpoint group
        self.neg = (
            compute_region_network_endpoint_group.ComputeRegionNetworkEndpointGroup(
                self,
                "function_neg",
                name=name_prefix + "-grafana-lb-neg",
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
        #     name=name_prefix + "-grafana-lb-health-check",
        #     project=project_id,
        #     http_health_check={
        #     "port": 80
        #     },
        # )

        # Create Backend service network endpoint
        self.backend_service = compute_backend_service.ComputeBackendService(
            self,
            "backend_service",
            name=name_prefix + "-grafana-lb-backend",
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
            name=f"{name_prefix}-grafana-ip",
            project=project_id,
        )

        # Create SSL certificate
        # self.certificate = compute_managed_ssl_certificate.ComputeManagedSslCertificate(
        #     self,
        #     "ssl_certificate",
        #     name=name_prefix+"-ssl-certificate",
        #     project=project_id,
        #     type="MANAGED",
        #     managed={
        #     "domains": ["flightcontroller.apacsquadzero.io"]
        #     }
        # )

        # Create URL map
        self.url_map = compute_url_map.ComputeUrlMap(
            self,
            "urlmap",
            name=name_prefix + "-grafana-lb-urlmap",
            default_service=self.backend_service.id,
            project=project_id,
        )

        # self.http_redirect = compute_url_map.ComputeUrlMap(
        #     self,
        #     "http_redirect",
        #     name=name+"-http-redirect",
        #     project=project_id,
        #     default_url_redirect={
        #     "https_redirect": True,
        #     "strip_query": False,
        #     }
        # )

        # # Create target proxy
        # self.targetproxy = compute_target_https_proxy.ComputeTargetHttpsProxy(
        #     self,
        #     "target_proxy",
        #     name=name+"-target",
        #     url_map=self.url_map.id,
        #     project=project_id,
        #     ssl_certificates=[self.certificate.id],
        # )

        # self.redirectproxy = compute_target_http_proxy.ComputeTargetHttpProxy(
        #     self,
        #     "redirect_proxy",
        #     name=name+"http-redirect",
        #     url_map=self.http_redirect.id,
        #     project=project_id,
        # )

        self.redirect_proxy = compute_target_http_proxy.ComputeTargetHttpProxy(
            self,
            "redirect_proxy",
            name=name_prefix + "-grafana-lbhttp-redirect",
            url_map=self.url_map.id,
            project=project_id,
        )

        # Create global forwarding rule
        self.forwarding_rule = (
            compute_global_forwarding_rule.ComputeGlobalForwardingRule(
                self,
                "forwarding_rule",
                name=f"{name_prefix}-grafana-lb",
                target=self.redirect_proxy.id,
                port_range="80",
                project=project_id,
                load_balancing_scheme="EXTERNAL_MANAGED",
                ip_address=self.global_address.address,
            )
        )

        # self.redirect_rule = compute_global_forwarding_rule.ComputeGlobalForwardingRule(
        #     self,
        #     "redirect_rule",
        #     name=name_prefix+"httpredirect",
        #     target=self.redirectproxy.id,
        #     port_range="80",
        #     project=project_id,
        #     ip_address=self.forwarding_rule.ip_address,
        # )
