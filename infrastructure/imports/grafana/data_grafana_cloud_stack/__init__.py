'''
# `data_grafana_cloud_stack`

Refer to the Terraform Registory for docs: [`data_grafana_cloud_stack`](https://www.terraform.io/docs/providers/grafana/d/cloud_stack).
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


class DataGrafanaCloudStack(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataGrafanaCloudStack.DataGrafanaCloudStack",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/d/cloud_stack grafana_cloud_stack}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        slug: builtins.str,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/d/cloud_stack grafana_cloud_stack} Data Source.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param slug: Subdomain that the Grafana instance will be available at (i.e. setting slug to “<stack_slug>” will make the instance available at “https://<stack_slug>.grafana.net". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/d/cloud_stack#slug DataGrafanaCloudStack#slug}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef6ff66db52575ce00607ae64588aea760c57426faa31ec7195f172d9ba6b35d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = DataGrafanaCloudStackConfig(
            slug=slug,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

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
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

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
    @jsii.member(jsii_name="regionSlug")
    def region_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regionSlug"))

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
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="slugInput")
    def slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slugInput"))

    @builtins.property
    @jsii.member(jsii_name="slug")
    def slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slug"))

    @slug.setter
    def slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb034f8ba375c5cb81b4e05f9f361f4e563f90551359ce1fc7b9f06b45291c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slug", value)


@jsii.data_type(
    jsii_type="grafana.dataGrafanaCloudStack.DataGrafanaCloudStackConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "slug": "slug",
    },
)
class DataGrafanaCloudStackConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        slug: builtins.str,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param slug: Subdomain that the Grafana instance will be available at (i.e. setting slug to “<stack_slug>” will make the instance available at “https://<stack_slug>.grafana.net". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/d/cloud_stack#slug DataGrafanaCloudStack#slug}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d38e7e697e8a130a98edd71e748f8ae82f1900cbf438d6772f50eca71cc708e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument slug", value=slug, expected_type=type_hints["slug"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
    def slug(self) -> builtins.str:
        '''Subdomain that the Grafana instance will be available at (i.e. setting slug to “<stack_slug>” will make the instance available at “https://<stack_slug>.grafana.net".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/d/cloud_stack#slug DataGrafanaCloudStack#slug}
        '''
        result = self._values.get("slug")
        assert result is not None, "Required property 'slug' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataGrafanaCloudStackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataGrafanaCloudStack",
    "DataGrafanaCloudStackConfig",
]

publication.publish()

def _typecheckingstub__ef6ff66db52575ce00607ae64588aea760c57426faa31ec7195f172d9ba6b35d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    slug: builtins.str,
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

def _typecheckingstub__deb034f8ba375c5cb81b4e05f9f361f4e563f90551359ce1fc7b9f06b45291c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d38e7e697e8a130a98edd71e748f8ae82f1900cbf438d6772f50eca71cc708e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    slug: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
