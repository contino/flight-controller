'''
# `grafana_synthetic_monitoring_installation`

Refer to the Terraform Registory for docs: [`grafana_synthetic_monitoring_installation`](https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation).
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


class SyntheticMonitoringInstallation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringInstallation.SyntheticMonitoringInstallation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation grafana_synthetic_monitoring_installation}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        logs_instance_id: jsii.Number,
        metrics_instance_id: jsii.Number,
        metrics_publisher_key: builtins.str,
        stack_id: jsii.Number,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation grafana_synthetic_monitoring_installation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param logs_instance_id: The ID of the logs instance to install SM on (stack's ``logs_user_id`` attribute). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#logs_instance_id SyntheticMonitoringInstallation#logs_instance_id}
        :param metrics_instance_id: The ID of the metrics instance to install SM on (stack's ``prometheus_user_id`` attribute). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#metrics_instance_id SyntheticMonitoringInstallation#metrics_instance_id}
        :param metrics_publisher_key: The Cloud API Key with the ``MetricsPublisher`` role used to publish metrics to the SM API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#metrics_publisher_key SyntheticMonitoringInstallation#metrics_publisher_key}
        :param stack_id: The ID of the stack to install SM on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#stack_id SyntheticMonitoringInstallation#stack_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#id SyntheticMonitoringInstallation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__badc21a102b04919f2436e539b33be753c7859cbf64881205f53f0dbbd57a7b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SyntheticMonitoringInstallationConfig(
            logs_instance_id=logs_instance_id,
            metrics_instance_id=metrics_instance_id,
            metrics_publisher_key=metrics_publisher_key,
            stack_id=stack_id,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="smAccessToken")
    def sm_access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "smAccessToken"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logsInstanceIdInput")
    def logs_instance_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logsInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsInstanceIdInput")
    def metrics_instance_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsInstanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPublisherKeyInput")
    def metrics_publisher_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricsPublisherKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="stackIdInput")
    def stack_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stackIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed81a67e14468a8b5cc70ffc60d925faa1315a01b60fe3f22171879f6371da1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="logsInstanceId")
    def logs_instance_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logsInstanceId"))

    @logs_instance_id.setter
    def logs_instance_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d3c9d0e0967e05bd9f49dc9c42e0fb9f72d7e5c26783aceeef9664ee2c1b06f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logsInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="metricsInstanceId")
    def metrics_instance_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsInstanceId"))

    @metrics_instance_id.setter
    def metrics_instance_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2afb5ab5e246f52717f45af78569003231d64c8d56e7b3dbaa44c93f9726929e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsInstanceId", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPublisherKey")
    def metrics_publisher_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metricsPublisherKey"))

    @metrics_publisher_key.setter
    def metrics_publisher_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a24b073b9fee15a08055567e13334bca1c93f4f276990c0582eab4b1521043d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPublisherKey", value)

    @builtins.property
    @jsii.member(jsii_name="stackId")
    def stack_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stackId"))

    @stack_id.setter
    def stack_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf07f9e4222c9dd7a41b58fc3eb0a993432d25ee1a7542221a036b9bc0b42ae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stackId", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringInstallation.SyntheticMonitoringInstallationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "logs_instance_id": "logsInstanceId",
        "metrics_instance_id": "metricsInstanceId",
        "metrics_publisher_key": "metricsPublisherKey",
        "stack_id": "stackId",
        "id": "id",
    },
)
class SyntheticMonitoringInstallationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        logs_instance_id: jsii.Number,
        metrics_instance_id: jsii.Number,
        metrics_publisher_key: builtins.str,
        stack_id: jsii.Number,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param logs_instance_id: The ID of the logs instance to install SM on (stack's ``logs_user_id`` attribute). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#logs_instance_id SyntheticMonitoringInstallation#logs_instance_id}
        :param metrics_instance_id: The ID of the metrics instance to install SM on (stack's ``prometheus_user_id`` attribute). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#metrics_instance_id SyntheticMonitoringInstallation#metrics_instance_id}
        :param metrics_publisher_key: The Cloud API Key with the ``MetricsPublisher`` role used to publish metrics to the SM API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#metrics_publisher_key SyntheticMonitoringInstallation#metrics_publisher_key}
        :param stack_id: The ID of the stack to install SM on. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#stack_id SyntheticMonitoringInstallation#stack_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#id SyntheticMonitoringInstallation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df79a60a813c94c6ff6a3f54b52286c2619dc56e5ee1d78571354e748ea2ac50)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument logs_instance_id", value=logs_instance_id, expected_type=type_hints["logs_instance_id"])
            check_type(argname="argument metrics_instance_id", value=metrics_instance_id, expected_type=type_hints["metrics_instance_id"])
            check_type(argname="argument metrics_publisher_key", value=metrics_publisher_key, expected_type=type_hints["metrics_publisher_key"])
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "logs_instance_id": logs_instance_id,
            "metrics_instance_id": metrics_instance_id,
            "metrics_publisher_key": metrics_publisher_key,
            "stack_id": stack_id,
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
        if id is not None:
            self._values["id"] = id

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
    def logs_instance_id(self) -> jsii.Number:
        '''The ID of the logs instance to install SM on (stack's ``logs_user_id`` attribute).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#logs_instance_id SyntheticMonitoringInstallation#logs_instance_id}
        '''
        result = self._values.get("logs_instance_id")
        assert result is not None, "Required property 'logs_instance_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metrics_instance_id(self) -> jsii.Number:
        '''The ID of the metrics instance to install SM on (stack's ``prometheus_user_id`` attribute).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#metrics_instance_id SyntheticMonitoringInstallation#metrics_instance_id}
        '''
        result = self._values.get("metrics_instance_id")
        assert result is not None, "Required property 'metrics_instance_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def metrics_publisher_key(self) -> builtins.str:
        '''The Cloud API Key with the ``MetricsPublisher`` role used to publish metrics to the SM API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#metrics_publisher_key SyntheticMonitoringInstallation#metrics_publisher_key}
        '''
        result = self._values.get("metrics_publisher_key")
        assert result is not None, "Required property 'metrics_publisher_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_id(self) -> jsii.Number:
        '''The ID of the stack to install SM on.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#stack_id SyntheticMonitoringInstallation#stack_id}
        '''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_installation#id SyntheticMonitoringInstallation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringInstallationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SyntheticMonitoringInstallation",
    "SyntheticMonitoringInstallationConfig",
]

publication.publish()

def _typecheckingstub__badc21a102b04919f2436e539b33be753c7859cbf64881205f53f0dbbd57a7b1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    logs_instance_id: jsii.Number,
    metrics_instance_id: jsii.Number,
    metrics_publisher_key: builtins.str,
    stack_id: jsii.Number,
    id: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__ed81a67e14468a8b5cc70ffc60d925faa1315a01b60fe3f22171879f6371da1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d3c9d0e0967e05bd9f49dc9c42e0fb9f72d7e5c26783aceeef9664ee2c1b06f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2afb5ab5e246f52717f45af78569003231d64c8d56e7b3dbaa44c93f9726929e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a24b073b9fee15a08055567e13334bca1c93f4f276990c0582eab4b1521043d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf07f9e4222c9dd7a41b58fc3eb0a993432d25ee1a7542221a036b9bc0b42ae5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df79a60a813c94c6ff6a3f54b52286c2619dc56e5ee1d78571354e748ea2ac50(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    logs_instance_id: jsii.Number,
    metrics_instance_id: jsii.Number,
    metrics_publisher_key: builtins.str,
    stack_id: jsii.Number,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
