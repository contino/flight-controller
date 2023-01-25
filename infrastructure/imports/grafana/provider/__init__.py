'''
# `provider`

Refer to the Terraform Registory for docs: [`grafana`](https://www.terraform.io/docs/providers/grafana).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class GrafanaProvider(
    _cdktf_9a9027ec.TerraformProvider,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.provider.GrafanaProvider",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana grafana}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: typing.Optional[builtins.str] = None,
        auth: typing.Optional[builtins.str] = None,
        ca_cert: typing.Optional[builtins.str] = None,
        cloud_api_key: typing.Optional[builtins.str] = None,
        cloud_api_url: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        oncall_access_token: typing.Optional[builtins.str] = None,
        oncall_url: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[jsii.Number] = None,
        retries: typing.Optional[jsii.Number] = None,
        sm_access_token: typing.Optional[builtins.str] = None,
        sm_url: typing.Optional[builtins.str] = None,
        store_dashboard_sha256: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_cert: typing.Optional[builtins.str] = None,
        tls_key: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana grafana} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#alias GrafanaProvider#alias}
        :param auth: API token or basic auth ``username:password``. May alternatively be set via the ``GRAFANA_AUTH`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#auth GrafanaProvider#auth}
        :param ca_cert: Certificate CA bundle to use to verify the Grafana server's certificate. May alternatively be set via the ``GRAFANA_CA_CERT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#ca_cert GrafanaProvider#ca_cert}
        :param cloud_api_key: API key for Grafana Cloud. May alternatively be set via the ``GRAFANA_CLOUD_API_KEY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#cloud_api_key GrafanaProvider#cloud_api_key}
        :param cloud_api_url: Grafana Cloud's API URL. May alternatively be set via the ``GRAFANA_CLOUD_API_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#cloud_api_url GrafanaProvider#cloud_api_url}
        :param http_headers: Optional. HTTP headers mapping keys to values used for accessing the Grafana API. May alternatively be set via the ``GRAFANA_HTTP_HEADERS`` environment variable in JSON format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#http_headers GrafanaProvider#http_headers}
        :param insecure_skip_verify: Skip TLS certificate verification. May alternatively be set via the ``GRAFANA_INSECURE_SKIP_VERIFY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#insecure_skip_verify GrafanaProvider#insecure_skip_verify}
        :param oncall_access_token: A Grafana OnCall access token. May alternatively be set via the ``GRAFANA_ONCALL_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#oncall_access_token GrafanaProvider#oncall_access_token}
        :param oncall_url: An Grafana OnCall backend address. May alternatively be set via the ``GRAFANA_ONCALL_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#oncall_url GrafanaProvider#oncall_url}
        :param org_id: The default organization id to operate on within grafana. For resources that have an ``org_id`` attribute, the resource-level attribute has priority. May alternatively be set via the ``GRAFANA_ORG_ID`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#org_id GrafanaProvider#org_id}
        :param retries: The amount of retries to use for Grafana API calls. May alternatively be set via the ``GRAFANA_RETRIES`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#retries GrafanaProvider#retries}
        :param sm_access_token: A Synthetic Monitoring access token. May alternatively be set via the ``GRAFANA_SM_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#sm_access_token GrafanaProvider#sm_access_token}
        :param sm_url: Synthetic monitoring backend address. May alternatively be set via the ``GRAFANA_SM_URL`` environment variable. The correct value for each service region is cited in the `Synthetic Monitoring documentation <https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url>`_. Note the ``sm_url`` value is optional, but it must correspond with the value specified as the ``region_slug`` in the ``grafana_cloud_stack`` resource. Also note that when a Terraform configuration contains multiple provider instances managing SM resources associated with the same Grafana stack, specifying an explicit ``sm_url`` set to the same value for each provider ensures all providers interact with the same SM API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#sm_url GrafanaProvider#sm_url}
        :param store_dashboard_sha256: Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#store_dashboard_sha256 GrafanaProvider#store_dashboard_sha256}
        :param tls_cert: Client TLS certificate file to use to authenticate to the Grafana server. May alternatively be set via the ``GRAFANA_TLS_CERT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#tls_cert GrafanaProvider#tls_cert}
        :param tls_key: Client TLS key file to use to authenticate to the Grafana server. May alternatively be set via the ``GRAFANA_TLS_KEY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#tls_key GrafanaProvider#tls_key}
        :param url: The root URL of a Grafana server. May alternatively be set via the ``GRAFANA_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#url GrafanaProvider#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea14647038b77710b971782d7cedd3a8ad188dc45445ca2d7cf2ef91b2071ace)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = GrafanaProviderConfig(
            alias=alias,
            auth=auth,
            ca_cert=ca_cert,
            cloud_api_key=cloud_api_key,
            cloud_api_url=cloud_api_url,
            http_headers=http_headers,
            insecure_skip_verify=insecure_skip_verify,
            oncall_access_token=oncall_access_token,
            oncall_url=oncall_url,
            org_id=org_id,
            retries=retries,
            sm_access_token=sm_access_token,
            sm_url=sm_url,
            store_dashboard_sha256=store_dashboard_sha256,
            tls_cert=tls_cert,
            tls_key=tls_key,
            url=url,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAuth")
    def reset_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuth", []))

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetCloudApiKey")
    def reset_cloud_api_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudApiKey", []))

    @jsii.member(jsii_name="resetCloudApiUrl")
    def reset_cloud_api_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudApiUrl", []))

    @jsii.member(jsii_name="resetHttpHeaders")
    def reset_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaders", []))

    @jsii.member(jsii_name="resetInsecureSkipVerify")
    def reset_insecure_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipVerify", []))

    @jsii.member(jsii_name="resetOncallAccessToken")
    def reset_oncall_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOncallAccessToken", []))

    @jsii.member(jsii_name="resetOncallUrl")
    def reset_oncall_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOncallUrl", []))

    @jsii.member(jsii_name="resetOrgId")
    def reset_org_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgId", []))

    @jsii.member(jsii_name="resetRetries")
    def reset_retries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetries", []))

    @jsii.member(jsii_name="resetSmAccessToken")
    def reset_sm_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmAccessToken", []))

    @jsii.member(jsii_name="resetSmUrl")
    def reset_sm_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSmUrl", []))

    @jsii.member(jsii_name="resetStoreDashboardSha256")
    def reset_store_dashboard_sha256(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoreDashboardSha256", []))

    @jsii.member(jsii_name="resetTlsCert")
    def reset_tls_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCert", []))

    @jsii.member(jsii_name="resetTlsKey")
    def reset_tls_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsKey", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="authInput")
    def auth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authInput"))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudApiKeyInput")
    def cloud_api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudApiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudApiUrlInput")
    def cloud_api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudApiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeadersInput")
    def http_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerifyInput")
    def insecure_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="oncallAccessTokenInput")
    def oncall_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oncallAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="oncallUrlInput")
    def oncall_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oncallUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="orgIdInput")
    def org_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orgIdInput"))

    @builtins.property
    @jsii.member(jsii_name="retriesInput")
    def retries_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retriesInput"))

    @builtins.property
    @jsii.member(jsii_name="smAccessTokenInput")
    def sm_access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smAccessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="smUrlInput")
    def sm_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="storeDashboardSha256Input")
    def store_dashboard_sha256_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "storeDashboardSha256Input"))

    @builtins.property
    @jsii.member(jsii_name="tlsCertInput")
    def tls_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCertInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsKeyInput")
    def tls_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e1c316442f4830b77ad66b2525ad3d63315664ad4b75e68422078bbac1fb23e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value)

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "auth"))

    @auth.setter
    def auth(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e58243389516b83c222afe3738cb1b1798673278a9c48fd23fd5059f64c08cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auth", value)

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc7b6741b7522708e85e05e18d0e24c28570487f0ed8921fc8314ecc267913ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="cloudApiKey")
    def cloud_api_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudApiKey"))

    @cloud_api_key.setter
    def cloud_api_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e66a0cb66ca2175b31766752add3d125e7f9ada8610a732b09b441c73b091bef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudApiKey", value)

    @builtins.property
    @jsii.member(jsii_name="cloudApiUrl")
    def cloud_api_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudApiUrl"))

    @cloud_api_url.setter
    def cloud_api_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__129a094769e09872489cc92a15fc38eff678c28471cbd41fcf7046bb7585c64c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudApiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpHeaders"))

    @http_headers.setter
    def http_headers(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d1961b8e95d0279a2303028f28646cf1236d565f5ba9566c327ac7de76ea57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerify")
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSkipVerify"))

    @insecure_skip_verify.setter
    def insecure_skip_verify(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1c0c043439eef92fa56c664b6200b50e12ff07afc50f72c0d23189ddc1276c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="oncallAccessToken")
    def oncall_access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oncallAccessToken"))

    @oncall_access_token.setter
    def oncall_access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74b5554c0b61b57c5d1e99f5c14d065ad399026782ee7cf7c2f8604e6c083f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oncallAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="oncallUrl")
    def oncall_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oncallUrl"))

    @oncall_url.setter
    def oncall_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b76c1f264fdb594275c532268e31623bcb4ac5cceaf036fef4bfe0170cd5384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oncallUrl", value)

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orgId"))

    @org_id.setter
    def org_id(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac2fe786ada8f25f342a27ec9cb8afbb15086f3a0cf0d863d6c3b2a4ff6236d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgId", value)

    @builtins.property
    @jsii.member(jsii_name="retries")
    def retries(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retries"))

    @retries.setter
    def retries(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7b39c5ad04e45aaa0a626e29e8f846ecd752a83521132974ddd89f5e8c4af79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retries", value)

    @builtins.property
    @jsii.member(jsii_name="smAccessToken")
    def sm_access_token(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smAccessToken"))

    @sm_access_token.setter
    def sm_access_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1cfad457438fd8f3c5ad019f69fcac46c47ddfbbac8b48ddbefdf2b6fbdffcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smAccessToken", value)

    @builtins.property
    @jsii.member(jsii_name="smUrl")
    def sm_url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "smUrl"))

    @sm_url.setter
    def sm_url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3edb0c618396e9d81ebb70635f8345dfddbd010eda0fcdaea6529354fba67cfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smUrl", value)

    @builtins.property
    @jsii.member(jsii_name="storeDashboardSha256")
    def store_dashboard_sha256(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "storeDashboardSha256"))

    @store_dashboard_sha256.setter
    def store_dashboard_sha256(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__760ed9178c6d3b02d85418c18bdb63e87745fb114dd02f83bd54e4eec60b1daf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeDashboardSha256", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCert")
    def tls_cert(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCert"))

    @tls_cert.setter
    def tls_cert(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbbc1462ef79030b36c34587b41b1afc6939b26a46ff56455460b2ab28968825)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCert", value)

    @builtins.property
    @jsii.member(jsii_name="tlsKey")
    def tls_key(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsKey"))

    @tls_key.setter
    def tls_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b7bfee309b7147bebb4da6031bc3a614e84bb196722f8fd24f467805f0a71a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsKey", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "url"))

    @url.setter
    def url(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cd86739f295b1a4dcc3a3b07167d2af12bb9123b95fb1d2b5f4080b17a64ef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)


@jsii.data_type(
    jsii_type="grafana.provider.GrafanaProviderConfig",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "auth": "auth",
        "ca_cert": "caCert",
        "cloud_api_key": "cloudApiKey",
        "cloud_api_url": "cloudApiUrl",
        "http_headers": "httpHeaders",
        "insecure_skip_verify": "insecureSkipVerify",
        "oncall_access_token": "oncallAccessToken",
        "oncall_url": "oncallUrl",
        "org_id": "orgId",
        "retries": "retries",
        "sm_access_token": "smAccessToken",
        "sm_url": "smUrl",
        "store_dashboard_sha256": "storeDashboardSha256",
        "tls_cert": "tlsCert",
        "tls_key": "tlsKey",
        "url": "url",
    },
)
class GrafanaProviderConfig:
    def __init__(
        self,
        *,
        alias: typing.Optional[builtins.str] = None,
        auth: typing.Optional[builtins.str] = None,
        ca_cert: typing.Optional[builtins.str] = None,
        cloud_api_key: typing.Optional[builtins.str] = None,
        cloud_api_url: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        oncall_access_token: typing.Optional[builtins.str] = None,
        oncall_url: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[jsii.Number] = None,
        retries: typing.Optional[jsii.Number] = None,
        sm_access_token: typing.Optional[builtins.str] = None,
        sm_url: typing.Optional[builtins.str] = None,
        store_dashboard_sha256: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_cert: typing.Optional[builtins.str] = None,
        tls_key: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param alias: Alias name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#alias GrafanaProvider#alias}
        :param auth: API token or basic auth ``username:password``. May alternatively be set via the ``GRAFANA_AUTH`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#auth GrafanaProvider#auth}
        :param ca_cert: Certificate CA bundle to use to verify the Grafana server's certificate. May alternatively be set via the ``GRAFANA_CA_CERT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#ca_cert GrafanaProvider#ca_cert}
        :param cloud_api_key: API key for Grafana Cloud. May alternatively be set via the ``GRAFANA_CLOUD_API_KEY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#cloud_api_key GrafanaProvider#cloud_api_key}
        :param cloud_api_url: Grafana Cloud's API URL. May alternatively be set via the ``GRAFANA_CLOUD_API_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#cloud_api_url GrafanaProvider#cloud_api_url}
        :param http_headers: Optional. HTTP headers mapping keys to values used for accessing the Grafana API. May alternatively be set via the ``GRAFANA_HTTP_HEADERS`` environment variable in JSON format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#http_headers GrafanaProvider#http_headers}
        :param insecure_skip_verify: Skip TLS certificate verification. May alternatively be set via the ``GRAFANA_INSECURE_SKIP_VERIFY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#insecure_skip_verify GrafanaProvider#insecure_skip_verify}
        :param oncall_access_token: A Grafana OnCall access token. May alternatively be set via the ``GRAFANA_ONCALL_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#oncall_access_token GrafanaProvider#oncall_access_token}
        :param oncall_url: An Grafana OnCall backend address. May alternatively be set via the ``GRAFANA_ONCALL_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#oncall_url GrafanaProvider#oncall_url}
        :param org_id: The default organization id to operate on within grafana. For resources that have an ``org_id`` attribute, the resource-level attribute has priority. May alternatively be set via the ``GRAFANA_ORG_ID`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#org_id GrafanaProvider#org_id}
        :param retries: The amount of retries to use for Grafana API calls. May alternatively be set via the ``GRAFANA_RETRIES`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#retries GrafanaProvider#retries}
        :param sm_access_token: A Synthetic Monitoring access token. May alternatively be set via the ``GRAFANA_SM_ACCESS_TOKEN`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#sm_access_token GrafanaProvider#sm_access_token}
        :param sm_url: Synthetic monitoring backend address. May alternatively be set via the ``GRAFANA_SM_URL`` environment variable. The correct value for each service region is cited in the `Synthetic Monitoring documentation <https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url>`_. Note the ``sm_url`` value is optional, but it must correspond with the value specified as the ``region_slug`` in the ``grafana_cloud_stack`` resource. Also note that when a Terraform configuration contains multiple provider instances managing SM resources associated with the same Grafana stack, specifying an explicit ``sm_url`` set to the same value for each provider ensures all providers interact with the same SM API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#sm_url GrafanaProvider#sm_url}
        :param store_dashboard_sha256: Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#store_dashboard_sha256 GrafanaProvider#store_dashboard_sha256}
        :param tls_cert: Client TLS certificate file to use to authenticate to the Grafana server. May alternatively be set via the ``GRAFANA_TLS_CERT`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#tls_cert GrafanaProvider#tls_cert}
        :param tls_key: Client TLS key file to use to authenticate to the Grafana server. May alternatively be set via the ``GRAFANA_TLS_KEY`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#tls_key GrafanaProvider#tls_key}
        :param url: The root URL of a Grafana server. May alternatively be set via the ``GRAFANA_URL`` environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#url GrafanaProvider#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__879ff60525ac5ce5d7787e0e2dd1b8189d403c412b55946137cf484f5c056271)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument cloud_api_key", value=cloud_api_key, expected_type=type_hints["cloud_api_key"])
            check_type(argname="argument cloud_api_url", value=cloud_api_url, expected_type=type_hints["cloud_api_url"])
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
            check_type(argname="argument insecure_skip_verify", value=insecure_skip_verify, expected_type=type_hints["insecure_skip_verify"])
            check_type(argname="argument oncall_access_token", value=oncall_access_token, expected_type=type_hints["oncall_access_token"])
            check_type(argname="argument oncall_url", value=oncall_url, expected_type=type_hints["oncall_url"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
            check_type(argname="argument sm_access_token", value=sm_access_token, expected_type=type_hints["sm_access_token"])
            check_type(argname="argument sm_url", value=sm_url, expected_type=type_hints["sm_url"])
            check_type(argname="argument store_dashboard_sha256", value=store_dashboard_sha256, expected_type=type_hints["store_dashboard_sha256"])
            check_type(argname="argument tls_cert", value=tls_cert, expected_type=type_hints["tls_cert"])
            check_type(argname="argument tls_key", value=tls_key, expected_type=type_hints["tls_key"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alias is not None:
            self._values["alias"] = alias
        if auth is not None:
            self._values["auth"] = auth
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if cloud_api_key is not None:
            self._values["cloud_api_key"] = cloud_api_key
        if cloud_api_url is not None:
            self._values["cloud_api_url"] = cloud_api_url
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if oncall_access_token is not None:
            self._values["oncall_access_token"] = oncall_access_token
        if oncall_url is not None:
            self._values["oncall_url"] = oncall_url
        if org_id is not None:
            self._values["org_id"] = org_id
        if retries is not None:
            self._values["retries"] = retries
        if sm_access_token is not None:
            self._values["sm_access_token"] = sm_access_token
        if sm_url is not None:
            self._values["sm_url"] = sm_url
        if store_dashboard_sha256 is not None:
            self._values["store_dashboard_sha256"] = store_dashboard_sha256
        if tls_cert is not None:
            self._values["tls_cert"] = tls_cert
        if tls_key is not None:
            self._values["tls_key"] = tls_key
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''Alias name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#alias GrafanaProvider#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth(self) -> typing.Optional[builtins.str]:
        '''API token or basic auth ``username:password``. May alternatively be set via the ``GRAFANA_AUTH`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#auth GrafanaProvider#auth}
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''Certificate CA bundle to use to verify the Grafana server's certificate.

        May alternatively be set via the ``GRAFANA_CA_CERT`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#ca_cert GrafanaProvider#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_api_key(self) -> typing.Optional[builtins.str]:
        '''API key for Grafana Cloud. May alternatively be set via the ``GRAFANA_CLOUD_API_KEY`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#cloud_api_key GrafanaProvider#cloud_api_key}
        '''
        result = self._values.get("cloud_api_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_api_url(self) -> typing.Optional[builtins.str]:
        '''Grafana Cloud's API URL. May alternatively be set via the ``GRAFANA_CLOUD_API_URL`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#cloud_api_url GrafanaProvider#cloud_api_url}
        '''
        result = self._values.get("cloud_api_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        HTTP headers mapping keys to values used for accessing the Grafana API. May alternatively be set via the ``GRAFANA_HTTP_HEADERS`` environment variable in JSON format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#http_headers GrafanaProvider#http_headers}
        '''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Skip TLS certificate verification. May alternatively be set via the ``GRAFANA_INSECURE_SKIP_VERIFY`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#insecure_skip_verify GrafanaProvider#insecure_skip_verify}
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def oncall_access_token(self) -> typing.Optional[builtins.str]:
        '''A Grafana OnCall access token. May alternatively be set via the ``GRAFANA_ONCALL_ACCESS_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#oncall_access_token GrafanaProvider#oncall_access_token}
        '''
        result = self._values.get("oncall_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def oncall_url(self) -> typing.Optional[builtins.str]:
        '''An Grafana OnCall backend address. May alternatively be set via the ``GRAFANA_ONCALL_URL`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#oncall_url GrafanaProvider#oncall_url}
        '''
        result = self._values.get("oncall_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_id(self) -> typing.Optional[jsii.Number]:
        '''The default organization id to operate on within grafana.

        For resources that have an ``org_id`` attribute, the resource-level attribute has priority. May alternatively be set via the ``GRAFANA_ORG_ID`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#org_id GrafanaProvider#org_id}
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retries(self) -> typing.Optional[jsii.Number]:
        '''The amount of retries to use for Grafana API calls. May alternatively be set via the ``GRAFANA_RETRIES`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#retries GrafanaProvider#retries}
        '''
        result = self._values.get("retries")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sm_access_token(self) -> typing.Optional[builtins.str]:
        '''A Synthetic Monitoring access token. May alternatively be set via the ``GRAFANA_SM_ACCESS_TOKEN`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#sm_access_token GrafanaProvider#sm_access_token}
        '''
        result = self._values.get("sm_access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sm_url(self) -> typing.Optional[builtins.str]:
        '''Synthetic monitoring backend address.

        May alternatively be set via the ``GRAFANA_SM_URL`` environment variable. The correct value for each service region is cited in the `Synthetic Monitoring documentation <https://grafana.com/docs/grafana-cloud/synthetic-monitoring/private-probes/#probe-api-server-url>`_. Note the ``sm_url`` value is optional, but it must correspond with the value specified as the ``region_slug`` in the ``grafana_cloud_stack`` resource. Also note that when a Terraform configuration contains multiple provider instances managing SM resources associated with the same Grafana stack, specifying an explicit ``sm_url`` set to the same value for each provider ensures all providers interact with the same SM API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#sm_url GrafanaProvider#sm_url}
        '''
        result = self._values.get("sm_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def store_dashboard_sha256(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if you want to save only the sha256sum instead of complete dashboard model JSON in the tfstate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#store_dashboard_sha256 GrafanaProvider#store_dashboard_sha256}
        '''
        result = self._values.get("store_dashboard_sha256")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_cert(self) -> typing.Optional[builtins.str]:
        '''Client TLS certificate file to use to authenticate to the Grafana server.

        May alternatively be set via the ``GRAFANA_TLS_CERT`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#tls_cert GrafanaProvider#tls_cert}
        '''
        result = self._values.get("tls_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_key(self) -> typing.Optional[builtins.str]:
        '''Client TLS key file to use to authenticate to the Grafana server.

        May alternatively be set via the ``GRAFANA_TLS_KEY`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#tls_key GrafanaProvider#tls_key}
        '''
        result = self._values.get("tls_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The root URL of a Grafana server. May alternatively be set via the ``GRAFANA_URL`` environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana#url GrafanaProvider#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrafanaProviderConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GrafanaProvider",
    "GrafanaProviderConfig",
]

publication.publish()

def _typecheckingstub__ea14647038b77710b971782d7cedd3a8ad188dc45445ca2d7cf2ef91b2071ace(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: typing.Optional[builtins.str] = None,
    auth: typing.Optional[builtins.str] = None,
    ca_cert: typing.Optional[builtins.str] = None,
    cloud_api_key: typing.Optional[builtins.str] = None,
    cloud_api_url: typing.Optional[builtins.str] = None,
    http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    oncall_access_token: typing.Optional[builtins.str] = None,
    oncall_url: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[jsii.Number] = None,
    retries: typing.Optional[jsii.Number] = None,
    sm_access_token: typing.Optional[builtins.str] = None,
    sm_url: typing.Optional[builtins.str] = None,
    store_dashboard_sha256: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_cert: typing.Optional[builtins.str] = None,
    tls_key: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1c316442f4830b77ad66b2525ad3d63315664ad4b75e68422078bbac1fb23e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e58243389516b83c222afe3738cb1b1798673278a9c48fd23fd5059f64c08cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc7b6741b7522708e85e05e18d0e24c28570487f0ed8921fc8314ecc267913ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e66a0cb66ca2175b31766752add3d125e7f9ada8610a732b09b441c73b091bef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__129a094769e09872489cc92a15fc38eff678c28471cbd41fcf7046bb7585c64c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d1961b8e95d0279a2303028f28646cf1236d565f5ba9566c327ac7de76ea57(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1c0c043439eef92fa56c664b6200b50e12ff07afc50f72c0d23189ddc1276c(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74b5554c0b61b57c5d1e99f5c14d065ad399026782ee7cf7c2f8604e6c083f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b76c1f264fdb594275c532268e31623bcb4ac5cceaf036fef4bfe0170cd5384(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac2fe786ada8f25f342a27ec9cb8afbb15086f3a0cf0d863d6c3b2a4ff6236d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b39c5ad04e45aaa0a626e29e8f846ecd752a83521132974ddd89f5e8c4af79(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1cfad457438fd8f3c5ad019f69fcac46c47ddfbbac8b48ddbefdf2b6fbdffcf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3edb0c618396e9d81ebb70635f8345dfddbd010eda0fcdaea6529354fba67cfb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__760ed9178c6d3b02d85418c18bdb63e87745fb114dd02f83bd54e4eec60b1daf(
    value: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbbc1462ef79030b36c34587b41b1afc6939b26a46ff56455460b2ab28968825(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b7bfee309b7147bebb4da6031bc3a614e84bb196722f8fd24f467805f0a71a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cd86739f295b1a4dcc3a3b07167d2af12bb9123b95fb1d2b5f4080b17a64ef7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879ff60525ac5ce5d7787e0e2dd1b8189d403c412b55946137cf484f5c056271(
    *,
    alias: typing.Optional[builtins.str] = None,
    auth: typing.Optional[builtins.str] = None,
    ca_cert: typing.Optional[builtins.str] = None,
    cloud_api_key: typing.Optional[builtins.str] = None,
    cloud_api_url: typing.Optional[builtins.str] = None,
    http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    oncall_access_token: typing.Optional[builtins.str] = None,
    oncall_url: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[jsii.Number] = None,
    retries: typing.Optional[jsii.Number] = None,
    sm_access_token: typing.Optional[builtins.str] = None,
    sm_url: typing.Optional[builtins.str] = None,
    store_dashboard_sha256: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_cert: typing.Optional[builtins.str] = None,
    tls_key: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
