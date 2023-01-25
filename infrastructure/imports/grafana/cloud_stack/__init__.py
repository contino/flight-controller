'''
# `grafana_cloud_stack`

Refer to the Terraform Registory for docs: [`grafana_cloud_stack`](https://www.terraform.io/docs/providers/grafana/r/cloud_stack).
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


class CloudStack(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.cloudStack.CloudStack",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack grafana_cloud_stack}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        slug: builtins.str,
        description: typing.Optional[builtins.str] = None,
        region_slug: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        wait_for_readiness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_for_readiness_timeout: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack grafana_cloud_stack} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of stack. Conventionally matches the url of the instance (e.g. “<stack_slug>.grafana.net”). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#name CloudStack#name}
        :param slug: Subdomain that the Grafana instance will be available at (i.e. setting slug to “<stack_slug>” will make the instance available at “https://<stack_slug>.grafana.net". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#slug CloudStack#slug}
        :param description: Description of stack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#description CloudStack#description}
        :param region_slug: Region slug to assign to this stack. Changing region will destroy the existing stack and create a new one in the desired region. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#region_slug CloudStack#region_slug}
        :param url: Custom URL for the Grafana instance. Must have a CNAME setup to point to ``.grafana.net`` before creating the stack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#url CloudStack#url}
        :param wait_for_readiness: Whether to wait for readiness of the stack after creating it. The check is a HEAD request to the stack URL (Grafana instance). Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#wait_for_readiness CloudStack#wait_for_readiness}
        :param wait_for_readiness_timeout: How long to wait for readiness (if enabled). Defaults to ``5m0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#wait_for_readiness_timeout CloudStack#wait_for_readiness_timeout}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9b2a136271e57a45b6dfb7fcaa8faeca9e9538d7520d0d2db4b2a2e383d0d82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = CloudStackConfig(
            name=name,
            slug=slug,
            description=description,
            region_slug=region_slug,
            url=url,
            wait_for_readiness=wait_for_readiness,
            wait_for_readiness_timeout=wait_for_readiness_timeout,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetRegionSlug")
    def reset_region_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegionSlug", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetWaitForReadiness")
    def reset_wait_for_readiness(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForReadiness", []))

    @jsii.member(jsii_name="resetWaitForReadinessTimeout")
    def reset_wait_for_readiness_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForReadinessTimeout", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerName")
    def alertmanager_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertmanagerName"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerStatus")
    def alertmanager_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertmanagerStatus"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerUrl")
    def alertmanager_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertmanagerUrl"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerUserId")
    def alertmanager_user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "alertmanagerUserId"))

    @builtins.property
    @jsii.member(jsii_name="graphiteName")
    def graphite_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "graphiteName"))

    @builtins.property
    @jsii.member(jsii_name="graphiteStatus")
    def graphite_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "graphiteStatus"))

    @builtins.property
    @jsii.member(jsii_name="graphiteUrl")
    def graphite_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "graphiteUrl"))

    @builtins.property
    @jsii.member(jsii_name="graphiteUserId")
    def graphite_user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "graphiteUserId"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="logsName")
    def logs_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logsName"))

    @builtins.property
    @jsii.member(jsii_name="logsStatus")
    def logs_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logsStatus"))

    @builtins.property
    @jsii.member(jsii_name="logsUrl")
    def logs_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logsUrl"))

    @builtins.property
    @jsii.member(jsii_name="logsUserId")
    def logs_user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logsUserId"))

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "orgId"))

    @builtins.property
    @jsii.member(jsii_name="orgName")
    def org_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgName"))

    @builtins.property
    @jsii.member(jsii_name="orgSlug")
    def org_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgSlug"))

    @builtins.property
    @jsii.member(jsii_name="prometheusName")
    def prometheus_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prometheusName"))

    @builtins.property
    @jsii.member(jsii_name="prometheusRemoteEndpoint")
    def prometheus_remote_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prometheusRemoteEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="prometheusRemoteWriteEndpoint")
    def prometheus_remote_write_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prometheusRemoteWriteEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="prometheusStatus")
    def prometheus_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prometheusStatus"))

    @builtins.property
    @jsii.member(jsii_name="prometheusUrl")
    def prometheus_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prometheusUrl"))

    @builtins.property
    @jsii.member(jsii_name="prometheusUserId")
    def prometheus_user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "prometheusUserId"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="tracesName")
    def traces_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tracesName"))

    @builtins.property
    @jsii.member(jsii_name="tracesStatus")
    def traces_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tracesStatus"))

    @builtins.property
    @jsii.member(jsii_name="tracesUrl")
    def traces_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tracesUrl"))

    @builtins.property
    @jsii.member(jsii_name="tracesUserId")
    def traces_user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tracesUserId"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionSlugInput")
    def region_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="slugInput")
    def slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slugInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForReadinessInput")
    def wait_for_readiness_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "waitForReadinessInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForReadinessTimeoutInput")
    def wait_for_readiness_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "waitForReadinessTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00c3fbad46692e6687638523abc60cb3ac04efc587f134f3a27cf5b99d6c4d19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1210e58aba38021e372d2089aaf993a6b58eeb993dec9ba257940011fbf5a3b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="regionSlug")
    def region_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionSlug"))

    @region_slug.setter
    def region_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5b64e1be3177f38fd7254a623f863a13a08858a5073d4e592682cbed496743e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionSlug", value)

    @builtins.property
    @jsii.member(jsii_name="slug")
    def slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slug"))

    @slug.setter
    def slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980a6cd1807e1ac6d1260380d1f4eb94f055bc702d1c720aafec10d344c78015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slug", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a94b8ac74ba730af8d10bd9ef3d5e8fb8c60c19ab4a28ab193b78477267715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="waitForReadiness")
    def wait_for_readiness(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "waitForReadiness"))

    @wait_for_readiness.setter
    def wait_for_readiness(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb9fffc448eae78cc0431e7f2e648c3dcfec13be0870feb3dba409e82959a03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForReadiness", value)

    @builtins.property
    @jsii.member(jsii_name="waitForReadinessTimeout")
    def wait_for_readiness_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "waitForReadinessTimeout"))

    @wait_for_readiness_timeout.setter
    def wait_for_readiness_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c862a21cc48cfead7c8fc9e195f77d7e6edb38536680d9b8d490b9802aba7f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForReadinessTimeout", value)


@jsii.data_type(
    jsii_type="grafana.cloudStack.CloudStackConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "slug": "slug",
        "description": "description",
        "region_slug": "regionSlug",
        "url": "url",
        "wait_for_readiness": "waitForReadiness",
        "wait_for_readiness_timeout": "waitForReadinessTimeout",
    },
)
class CloudStackConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: builtins.str,
        slug: builtins.str,
        description: typing.Optional[builtins.str] = None,
        region_slug: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        wait_for_readiness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        wait_for_readiness_timeout: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of stack. Conventionally matches the url of the instance (e.g. “<stack_slug>.grafana.net”). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#name CloudStack#name}
        :param slug: Subdomain that the Grafana instance will be available at (i.e. setting slug to “<stack_slug>” will make the instance available at “https://<stack_slug>.grafana.net". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#slug CloudStack#slug}
        :param description: Description of stack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#description CloudStack#description}
        :param region_slug: Region slug to assign to this stack. Changing region will destroy the existing stack and create a new one in the desired region. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#region_slug CloudStack#region_slug}
        :param url: Custom URL for the Grafana instance. Must have a CNAME setup to point to ``.grafana.net`` before creating the stack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#url CloudStack#url}
        :param wait_for_readiness: Whether to wait for readiness of the stack after creating it. The check is a HEAD request to the stack URL (Grafana instance). Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#wait_for_readiness CloudStack#wait_for_readiness}
        :param wait_for_readiness_timeout: How long to wait for readiness (if enabled). Defaults to ``5m0s``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#wait_for_readiness_timeout CloudStack#wait_for_readiness_timeout}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__360bf8f87e562f77468e57bc99105ecfa481e8d0ba83659c754511d38a2e8b98)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument slug", value=slug, expected_type=type_hints["slug"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument region_slug", value=region_slug, expected_type=type_hints["region_slug"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument wait_for_readiness", value=wait_for_readiness, expected_type=type_hints["wait_for_readiness"])
            check_type(argname="argument wait_for_readiness_timeout", value=wait_for_readiness_timeout, expected_type=type_hints["wait_for_readiness_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "slug": slug,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if description is not None:
            self._values["description"] = description
        if region_slug is not None:
            self._values["region_slug"] = region_slug
        if url is not None:
            self._values["url"] = url
        if wait_for_readiness is not None:
            self._values["wait_for_readiness"] = wait_for_readiness
        if wait_for_readiness_timeout is not None:
            self._values["wait_for_readiness_timeout"] = wait_for_readiness_timeout

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of stack. Conventionally matches the url of the instance (e.g. “<stack_slug>.grafana.net”).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#name CloudStack#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slug(self) -> builtins.str:
        '''Subdomain that the Grafana instance will be available at (i.e. setting slug to “<stack_slug>” will make the instance available at “https://<stack_slug>.grafana.net".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#slug CloudStack#slug}
        '''
        result = self._values.get("slug")
        assert result is not None, "Required property 'slug' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of stack.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#description CloudStack#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region_slug(self) -> typing.Optional[builtins.str]:
        '''Region slug to assign to this stack.

        Changing region will destroy the existing stack and create a new one in the desired region. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#region_slug CloudStack#region_slug}
        '''
        result = self._values.get("region_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Custom URL for the Grafana instance. Must have a CNAME setup to point to ``.grafana.net`` before creating the stack.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#url CloudStack#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wait_for_readiness(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to wait for readiness of the stack after creating it.

        The check is a HEAD request to the stack URL (Grafana instance). Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#wait_for_readiness CloudStack#wait_for_readiness}
        '''
        result = self._values.get("wait_for_readiness")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def wait_for_readiness_timeout(self) -> typing.Optional[builtins.str]:
        '''How long to wait for readiness (if enabled). Defaults to ``5m0s``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_stack#wait_for_readiness_timeout CloudStack#wait_for_readiness_timeout}
        '''
        result = self._values.get("wait_for_readiness_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudStackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CloudStack",
    "CloudStackConfig",
]

publication.publish()

def _typecheckingstub__c9b2a136271e57a45b6dfb7fcaa8faeca9e9538d7520d0d2db4b2a2e383d0d82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    slug: builtins.str,
    description: typing.Optional[builtins.str] = None,
    region_slug: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    wait_for_readiness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_for_readiness_timeout: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00c3fbad46692e6687638523abc60cb3ac04efc587f134f3a27cf5b99d6c4d19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1210e58aba38021e372d2089aaf993a6b58eeb993dec9ba257940011fbf5a3b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5b64e1be3177f38fd7254a623f863a13a08858a5073d4e592682cbed496743e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980a6cd1807e1ac6d1260380d1f4eb94f055bc702d1c720aafec10d344c78015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a94b8ac74ba730af8d10bd9ef3d5e8fb8c60c19ab4a28ab193b78477267715(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb9fffc448eae78cc0431e7f2e648c3dcfec13be0870feb3dba409e82959a03(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c862a21cc48cfead7c8fc9e195f77d7e6edb38536680d9b8d490b9802aba7f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__360bf8f87e562f77468e57bc99105ecfa481e8d0ba83659c754511d38a2e8b98(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    slug: builtins.str,
    description: typing.Optional[builtins.str] = None,
    region_slug: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    wait_for_readiness: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    wait_for_readiness_timeout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
