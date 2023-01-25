'''
# `grafana_synthetic_monitoring_check`

Refer to the Terraform Registory for docs: [`grafana_synthetic_monitoring_check`](https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check).
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


class SyntheticMonitoringCheck(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheck",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check grafana_synthetic_monitoring_check}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        job: builtins.str,
        probes: typing.Sequence[jsii.Number],
        settings: typing.Union["SyntheticMonitoringCheckSettings", typing.Dict[builtins.str, typing.Any]],
        target: builtins.str,
        alert_sensitivity: typing.Optional[builtins.str] = None,
        basic_metrics_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        frequency: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check grafana_synthetic_monitoring_check} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param job: Name used for job label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#job SyntheticMonitoringCheck#job}
        :param probes: List of probe location IDs where this target will be checked from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#probes SyntheticMonitoringCheck#probes}
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#settings SyntheticMonitoringCheck#settings}
        :param target: Hostname to ping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#target SyntheticMonitoringCheck#target}
        :param alert_sensitivity: Can be set to ``none``, ``low``, ``medium``, or ``high`` to correspond to the check `alert levels <https://grafana.com/docs/grafana-cloud/synthetic-monitoring/synthetic-monitoring-alerting/>`_. Defaults to ``none``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#alert_sensitivity SyntheticMonitoringCheck#alert_sensitivity}
        :param basic_metrics_only: Metrics are reduced by default. Set this to ``false`` if you'd like to publish all metrics. We maintain a `full list of metrics <https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata>`_ collected for each. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#basic_metrics_only SyntheticMonitoringCheck#basic_metrics_only}
        :param enabled: Whether to enable the check. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#enabled SyntheticMonitoringCheck#enabled}
        :param frequency: How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to ``60000``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#frequency SyntheticMonitoringCheck#frequency}
        :param labels: Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#labels SyntheticMonitoringCheck#labels}
        :param timeout: Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to ``3000``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#timeout SyntheticMonitoringCheck#timeout}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ebee3c7ff13c7e643ed6e9d76209daa4a0f05c16db6079ba0ce3ea292c4cd2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = SyntheticMonitoringCheckConfig(
            job=job,
            probes=probes,
            settings=settings,
            target=target,
            alert_sensitivity=alert_sensitivity,
            basic_metrics_only=basic_metrics_only,
            enabled=enabled,
            frequency=frequency,
            labels=labels,
            timeout=timeout,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        *,
        dns: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsDns", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        ping: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsPing", typing.Dict[builtins.str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsTcp", typing.Dict[builtins.str, typing.Any]]] = None,
        traceroute: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsTraceroute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#dns SyntheticMonitoringCheck#dns}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#http SyntheticMonitoringCheck#http}
        :param ping: ping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ping SyntheticMonitoringCheck#ping}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tcp SyntheticMonitoringCheck#tcp}
        :param traceroute: traceroute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#traceroute SyntheticMonitoringCheck#traceroute}
        '''
        value = SyntheticMonitoringCheckSettings(
            dns=dns, http=http, ping=ping, tcp=tcp, traceroute=traceroute
        )

        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="resetAlertSensitivity")
    def reset_alert_sensitivity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertSensitivity", []))

    @jsii.member(jsii_name="resetBasicMetricsOnly")
    def reset_basic_metrics_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicMetricsOnly", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "SyntheticMonitoringCheckSettingsOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsOutputReference", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tenantId"))

    @builtins.property
    @jsii.member(jsii_name="alertSensitivityInput")
    def alert_sensitivity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertSensitivityInput"))

    @builtins.property
    @jsii.member(jsii_name="basicMetricsOnlyInput")
    def basic_metrics_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "basicMetricsOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="jobInput")
    def job_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="probesInput")
    def probes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "probesInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(self) -> typing.Optional["SyntheticMonitoringCheckSettings"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettings"], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="alertSensitivity")
    def alert_sensitivity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertSensitivity"))

    @alert_sensitivity.setter
    def alert_sensitivity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c8ea96fc76f7fb683d8fb0ba8dd3da99080e9d5f080666b8980adbbc7b689f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertSensitivity", value)

    @builtins.property
    @jsii.member(jsii_name="basicMetricsOnly")
    def basic_metrics_only(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "basicMetricsOnly"))

    @basic_metrics_only.setter
    def basic_metrics_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aef57ddf6ca6ecd29d7b0f17d778b9d2828359a0cd28331e304ab2438343450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicMetricsOnly", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df0a8841813d716eefe88f7c912a5606943320932c88cfde85425b67a6df389b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f57fc609696d660c034738e6b079a03238683872077142e27dc47924eb8d2303)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="job")
    def job(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "job"))

    @job.setter
    def job(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bca432a75219a2c6123997061844b5a0259f0d1295f9f33344ee189f941bd0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "job", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55be7c3737c47f216beb0908ede9799ace8677e0017a813b6e47dbf8356a7966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="probes")
    def probes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "probes"))

    @probes.setter
    def probes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38512ef7b10f2474c772c743631e41f2cbfedf10d4e65be034d02ef6b63df00b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "probes", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fef72cfca93b40ad77bc820a8f68b15ec74383bdacd3fb44bfeccaf307ce369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d656bc798c79bb84054c5349e89b1499b752db1e57b82a450a4e75bdd724ca7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "job": "job",
        "probes": "probes",
        "settings": "settings",
        "target": "target",
        "alert_sensitivity": "alertSensitivity",
        "basic_metrics_only": "basicMetricsOnly",
        "enabled": "enabled",
        "frequency": "frequency",
        "labels": "labels",
        "timeout": "timeout",
    },
)
class SyntheticMonitoringCheckConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        job: builtins.str,
        probes: typing.Sequence[jsii.Number],
        settings: typing.Union["SyntheticMonitoringCheckSettings", typing.Dict[builtins.str, typing.Any]],
        target: builtins.str,
        alert_sensitivity: typing.Optional[builtins.str] = None,
        basic_metrics_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        frequency: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param job: Name used for job label. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#job SyntheticMonitoringCheck#job}
        :param probes: List of probe location IDs where this target will be checked from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#probes SyntheticMonitoringCheck#probes}
        :param settings: settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#settings SyntheticMonitoringCheck#settings}
        :param target: Hostname to ping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#target SyntheticMonitoringCheck#target}
        :param alert_sensitivity: Can be set to ``none``, ``low``, ``medium``, or ``high`` to correspond to the check `alert levels <https://grafana.com/docs/grafana-cloud/synthetic-monitoring/synthetic-monitoring-alerting/>`_. Defaults to ``none``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#alert_sensitivity SyntheticMonitoringCheck#alert_sensitivity}
        :param basic_metrics_only: Metrics are reduced by default. Set this to ``false`` if you'd like to publish all metrics. We maintain a `full list of metrics <https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata>`_ collected for each. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#basic_metrics_only SyntheticMonitoringCheck#basic_metrics_only}
        :param enabled: Whether to enable the check. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#enabled SyntheticMonitoringCheck#enabled}
        :param frequency: How often the check runs in milliseconds (the value is not truly a "frequency" but a "period"). The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to ``60000``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#frequency SyntheticMonitoringCheck#frequency}
        :param labels: Custom labels to be included with collected metrics and logs. The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#labels SyntheticMonitoringCheck#labels}
        :param timeout: Specifies the maximum running time for the check in milliseconds. The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to ``3000``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#timeout SyntheticMonitoringCheck#timeout}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(settings, dict):
            settings = SyntheticMonitoringCheckSettings(**settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__119366c701453b2f9e2b6a2579f3060bf559778a9a09abc0543407cdb7f4668f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument job", value=job, expected_type=type_hints["job"])
            check_type(argname="argument probes", value=probes, expected_type=type_hints["probes"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument alert_sensitivity", value=alert_sensitivity, expected_type=type_hints["alert_sensitivity"])
            check_type(argname="argument basic_metrics_only", value=basic_metrics_only, expected_type=type_hints["basic_metrics_only"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job": job,
            "probes": probes,
            "settings": settings,
            "target": target,
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
        if alert_sensitivity is not None:
            self._values["alert_sensitivity"] = alert_sensitivity
        if basic_metrics_only is not None:
            self._values["basic_metrics_only"] = basic_metrics_only
        if enabled is not None:
            self._values["enabled"] = enabled
        if frequency is not None:
            self._values["frequency"] = frequency
        if labels is not None:
            self._values["labels"] = labels
        if timeout is not None:
            self._values["timeout"] = timeout

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
    def job(self) -> builtins.str:
        '''Name used for job label.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#job SyntheticMonitoringCheck#job}
        '''
        result = self._values.get("job")
        assert result is not None, "Required property 'job' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def probes(self) -> typing.List[jsii.Number]:
        '''List of probe location IDs where this target will be checked from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#probes SyntheticMonitoringCheck#probes}
        '''
        result = self._values.get("probes")
        assert result is not None, "Required property 'probes' is missing"
        return typing.cast(typing.List[jsii.Number], result)

    @builtins.property
    def settings(self) -> "SyntheticMonitoringCheckSettings":
        '''settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#settings SyntheticMonitoringCheck#settings}
        '''
        result = self._values.get("settings")
        assert result is not None, "Required property 'settings' is missing"
        return typing.cast("SyntheticMonitoringCheckSettings", result)

    @builtins.property
    def target(self) -> builtins.str:
        '''Hostname to ping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#target SyntheticMonitoringCheck#target}
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_sensitivity(self) -> typing.Optional[builtins.str]:
        '''Can be set to ``none``, ``low``, ``medium``, or ``high`` to correspond to the check `alert levels <https://grafana.com/docs/grafana-cloud/synthetic-monitoring/synthetic-monitoring-alerting/>`_. Defaults to ``none``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#alert_sensitivity SyntheticMonitoringCheck#alert_sensitivity}
        '''
        result = self._values.get("alert_sensitivity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_metrics_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Metrics are reduced by default.

        Set this to ``false`` if you'd like to publish all metrics. We maintain a `full list of metrics <https://github.com/grafana/synthetic-monitoring-agent/tree/main/internal/scraper/testdata>`_ collected for each. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#basic_metrics_only SyntheticMonitoringCheck#basic_metrics_only}
        '''
        result = self._values.get("basic_metrics_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to enable the check. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#enabled SyntheticMonitoringCheck#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def frequency(self) -> typing.Optional[jsii.Number]:
        '''How often the check runs in milliseconds (the value is not truly a "frequency" but a "period").

        The minimum acceptable value is 1 second (1000 ms), and the maximum is 120 seconds (120000 ms). Defaults to ``60000``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#frequency SyntheticMonitoringCheck#frequency}
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom labels to be included with collected metrics and logs.

        The maximum number of labels that can be specified per check is 5. These are applied, along with the probe-specific labels, to the outgoing metrics. The names and values of the labels cannot be empty, and the maximum length is 32 bytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#labels SyntheticMonitoringCheck#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Specifies the maximum running time for the check in milliseconds.

        The minimum acceptable value is 1 second (1000 ms), and the maximum 10 seconds (10000 ms). Defaults to ``3000``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#timeout SyntheticMonitoringCheck#timeout}
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettings",
    jsii_struct_bases=[],
    name_mapping={
        "dns": "dns",
        "http": "http",
        "ping": "ping",
        "tcp": "tcp",
        "traceroute": "traceroute",
    },
)
class SyntheticMonitoringCheckSettings:
    def __init__(
        self,
        *,
        dns: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsDns", typing.Dict[builtins.str, typing.Any]]] = None,
        http: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsHttp", typing.Dict[builtins.str, typing.Any]]] = None,
        ping: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsPing", typing.Dict[builtins.str, typing.Any]]] = None,
        tcp: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsTcp", typing.Dict[builtins.str, typing.Any]]] = None,
        traceroute: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsTraceroute", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#dns SyntheticMonitoringCheck#dns}
        :param http: http block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#http SyntheticMonitoringCheck#http}
        :param ping: ping block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ping SyntheticMonitoringCheck#ping}
        :param tcp: tcp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tcp SyntheticMonitoringCheck#tcp}
        :param traceroute: traceroute block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#traceroute SyntheticMonitoringCheck#traceroute}
        '''
        if isinstance(dns, dict):
            dns = SyntheticMonitoringCheckSettingsDns(**dns)
        if isinstance(http, dict):
            http = SyntheticMonitoringCheckSettingsHttp(**http)
        if isinstance(ping, dict):
            ping = SyntheticMonitoringCheckSettingsPing(**ping)
        if isinstance(tcp, dict):
            tcp = SyntheticMonitoringCheckSettingsTcp(**tcp)
        if isinstance(traceroute, dict):
            traceroute = SyntheticMonitoringCheckSettingsTraceroute(**traceroute)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a43490fa145b3e0a00395a98775fea012455ca2aec00a0a3931db8685090faa3)
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument http", value=http, expected_type=type_hints["http"])
            check_type(argname="argument ping", value=ping, expected_type=type_hints["ping"])
            check_type(argname="argument tcp", value=tcp, expected_type=type_hints["tcp"])
            check_type(argname="argument traceroute", value=traceroute, expected_type=type_hints["traceroute"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dns is not None:
            self._values["dns"] = dns
        if http is not None:
            self._values["http"] = http
        if ping is not None:
            self._values["ping"] = ping
        if tcp is not None:
            self._values["tcp"] = tcp
        if traceroute is not None:
            self._values["traceroute"] = traceroute

    @builtins.property
    def dns(self) -> typing.Optional["SyntheticMonitoringCheckSettingsDns"]:
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#dns SyntheticMonitoringCheck#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsDns"], result)

    @builtins.property
    def http(self) -> typing.Optional["SyntheticMonitoringCheckSettingsHttp"]:
        '''http block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#http SyntheticMonitoringCheck#http}
        '''
        result = self._values.get("http")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsHttp"], result)

    @builtins.property
    def ping(self) -> typing.Optional["SyntheticMonitoringCheckSettingsPing"]:
        '''ping block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ping SyntheticMonitoringCheck#ping}
        '''
        result = self._values.get("ping")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsPing"], result)

    @builtins.property
    def tcp(self) -> typing.Optional["SyntheticMonitoringCheckSettingsTcp"]:
        '''tcp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tcp SyntheticMonitoringCheck#tcp}
        '''
        result = self._values.get("tcp")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsTcp"], result)

    @builtins.property
    def traceroute(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsTraceroute"]:
        '''traceroute block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#traceroute SyntheticMonitoringCheck#traceroute}
        '''
        result = self._values.get("traceroute")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsTraceroute"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDns",
    jsii_struct_bases=[],
    name_mapping={
        "ip_version": "ipVersion",
        "port": "port",
        "protocol": "protocol",
        "record_type": "recordType",
        "server": "server",
        "source_ip_address": "sourceIpAddress",
        "validate_additional_rrs": "validateAdditionalRrs",
        "validate_answer_rrs": "validateAnswerRrs",
        "validate_authority_rrs": "validateAuthorityRrs",
        "valid_r_codes": "validRCodes",
    },
)
class SyntheticMonitoringCheckSettingsDns:
    def __init__(
        self,
        *,
        ip_version: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
        source_ip_address: typing.Optional[builtins.str] = None,
        validate_additional_rrs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs", typing.Dict[builtins.str, typing.Any]]]]] = None,
        validate_answer_rrs: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs", typing.Dict[builtins.str, typing.Any]]] = None,
        validate_authority_rrs: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs", typing.Dict[builtins.str, typing.Any]]] = None,
        valid_r_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param port: Port to target. Defaults to ``53``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#port SyntheticMonitoringCheck#port}
        :param protocol: ``TCP`` or ``UDP``. Defaults to ``UDP``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#protocol SyntheticMonitoringCheck#protocol}
        :param record_type: One of ``ANY``, ``A``, ``AAAA``, ``CNAME``, ``MX``, ``NS``, ``PTR``, ``SOA``, ``SRV``, ``TXT``. Defaults to ``A``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#record_type SyntheticMonitoringCheck#record_type}
        :param server: DNS server address to target. Defaults to ``8.8.8.8``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server SyntheticMonitoringCheck#server}
        :param source_ip_address: Source IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        :param validate_additional_rrs: validate_additional_rrs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_additional_rrs SyntheticMonitoringCheck#validate_additional_rrs}
        :param validate_answer_rrs: validate_answer_rrs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_answer_rrs SyntheticMonitoringCheck#validate_answer_rrs}
        :param validate_authority_rrs: validate_authority_rrs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_authority_rrs SyntheticMonitoringCheck#validate_authority_rrs}
        :param valid_r_codes: List of valid response codes. Options include ``NOERROR``, ``BADALG``, ``BADMODE``, ``BADKEY``, ``BADCOOKIE``, ``BADNAME``, ``BADSIG``, ``BADTIME``, ``BADTRUNC``, ``BADVERS``, ``FORMERR``, ``NOTIMP``, ``NOTAUTH``, ``NOTZONE``, ``NXDOMAIN``, ``NXRRSET``, ``REFUSED``, ``SERVFAIL``, ``YXDOMAIN``, ``YXRRSET``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_r_codes SyntheticMonitoringCheck#valid_r_codes}
        '''
        if isinstance(validate_answer_rrs, dict):
            validate_answer_rrs = SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs(**validate_answer_rrs)
        if isinstance(validate_authority_rrs, dict):
            validate_authority_rrs = SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs(**validate_authority_rrs)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad9f5efa1b5635a334f2cccf2072d11c51627d04bb2b4e128f15711fbc8f58b)
            check_type(argname="argument ip_version", value=ip_version, expected_type=type_hints["ip_version"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument source_ip_address", value=source_ip_address, expected_type=type_hints["source_ip_address"])
            check_type(argname="argument validate_additional_rrs", value=validate_additional_rrs, expected_type=type_hints["validate_additional_rrs"])
            check_type(argname="argument validate_answer_rrs", value=validate_answer_rrs, expected_type=type_hints["validate_answer_rrs"])
            check_type(argname="argument validate_authority_rrs", value=validate_authority_rrs, expected_type=type_hints["validate_authority_rrs"])
            check_type(argname="argument valid_r_codes", value=valid_r_codes, expected_type=type_hints["valid_r_codes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip_version is not None:
            self._values["ip_version"] = ip_version
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if record_type is not None:
            self._values["record_type"] = record_type
        if server is not None:
            self._values["server"] = server
        if source_ip_address is not None:
            self._values["source_ip_address"] = source_ip_address
        if validate_additional_rrs is not None:
            self._values["validate_additional_rrs"] = validate_additional_rrs
        if validate_answer_rrs is not None:
            self._values["validate_answer_rrs"] = validate_answer_rrs
        if validate_authority_rrs is not None:
            self._values["validate_authority_rrs"] = validate_authority_rrs
        if valid_r_codes is not None:
            self._values["valid_r_codes"] = valid_r_codes

    @builtins.property
    def ip_version(self) -> typing.Optional[builtins.str]:
        '''Options are ``V4``, ``V6``, ``Any``.

        Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        '''
        result = self._values.get("ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port to target. Defaults to ``53``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#port SyntheticMonitoringCheck#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''``TCP`` or ``UDP``. Defaults to ``UDP``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#protocol SyntheticMonitoringCheck#protocol}
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_type(self) -> typing.Optional[builtins.str]:
        '''One of ``ANY``, ``A``, ``AAAA``, ``CNAME``, ``MX``, ``NS``, ``PTR``, ``SOA``, ``SRV``, ``TXT``. Defaults to ``A``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#record_type SyntheticMonitoringCheck#record_type}
        '''
        result = self._values.get("record_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server(self) -> typing.Optional[builtins.str]:
        '''DNS server address to target. Defaults to ``8.8.8.8``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server SyntheticMonitoringCheck#server}
        '''
        result = self._values.get("server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ip_address(self) -> typing.Optional[builtins.str]:
        '''Source IP address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        '''
        result = self._values.get("source_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validate_additional_rrs(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs"]]]:
        '''validate_additional_rrs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_additional_rrs SyntheticMonitoringCheck#validate_additional_rrs}
        '''
        result = self._values.get("validate_additional_rrs")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs"]]], result)

    @builtins.property
    def validate_answer_rrs(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs"]:
        '''validate_answer_rrs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_answer_rrs SyntheticMonitoringCheck#validate_answer_rrs}
        '''
        result = self._values.get("validate_answer_rrs")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs"], result)

    @builtins.property
    def validate_authority_rrs(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs"]:
        '''validate_authority_rrs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_authority_rrs SyntheticMonitoringCheck#validate_authority_rrs}
        '''
        result = self._values.get("validate_authority_rrs")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs"], result)

    @builtins.property
    def valid_r_codes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of valid response codes.

        Options include ``NOERROR``, ``BADALG``, ``BADMODE``, ``BADKEY``, ``BADCOOKIE``, ``BADNAME``, ``BADSIG``, ``BADTIME``, ``BADTRUNC``, ``BADVERS``, ``FORMERR``, ``NOTIMP``, ``NOTAUTH``, ``NOTZONE``, ``NXDOMAIN``, ``NXRRSET``, ``REFUSED``, ``SERVFAIL``, ``YXDOMAIN``, ``YXRRSET``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_r_codes SyntheticMonitoringCheck#valid_r_codes}
        '''
        result = self._values.get("valid_r_codes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsDnsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0e22250033b2d7f5b9c61f0333373a6dac7685ff0a6b18df2264f43ff97fe0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putValidateAdditionalRrs")
    def put_validate_additional_rrs(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a666d1f29f887e61758ae9e9f0c0beed465e537817d1d63db60041e48e157625)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putValidateAdditionalRrs", [value]))

    @jsii.member(jsii_name="putValidateAnswerRrs")
    def put_validate_answer_rrs(
        self,
        *,
        fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fail_if_matches_regexp: Fail if value matches regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        :param fail_if_not_matches_regexp: Fail if value does not match regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        value = SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs(
            fail_if_matches_regexp=fail_if_matches_regexp,
            fail_if_not_matches_regexp=fail_if_not_matches_regexp,
        )

        return typing.cast(None, jsii.invoke(self, "putValidateAnswerRrs", [value]))

    @jsii.member(jsii_name="putValidateAuthorityRrs")
    def put_validate_authority_rrs(
        self,
        *,
        fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fail_if_matches_regexp: Fail if value matches regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        :param fail_if_not_matches_regexp: Fail if value does not match regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        value = SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs(
            fail_if_matches_regexp=fail_if_matches_regexp,
            fail_if_not_matches_regexp=fail_if_not_matches_regexp,
        )

        return typing.cast(None, jsii.invoke(self, "putValidateAuthorityRrs", [value]))

    @jsii.member(jsii_name="resetIpVersion")
    def reset_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersion", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetRecordType")
    def reset_record_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecordType", []))

    @jsii.member(jsii_name="resetServer")
    def reset_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServer", []))

    @jsii.member(jsii_name="resetSourceIpAddress")
    def reset_source_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpAddress", []))

    @jsii.member(jsii_name="resetValidateAdditionalRrs")
    def reset_validate_additional_rrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateAdditionalRrs", []))

    @jsii.member(jsii_name="resetValidateAnswerRrs")
    def reset_validate_answer_rrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateAnswerRrs", []))

    @jsii.member(jsii_name="resetValidateAuthorityRrs")
    def reset_validate_authority_rrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidateAuthorityRrs", []))

    @jsii.member(jsii_name="resetValidRCodes")
    def reset_valid_r_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidRCodes", []))

    @builtins.property
    @jsii.member(jsii_name="validateAdditionalRrs")
    def validate_additional_rrs(
        self,
    ) -> "SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsList":
        return typing.cast("SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsList", jsii.get(self, "validateAdditionalRrs"))

    @builtins.property
    @jsii.member(jsii_name="validateAnswerRrs")
    def validate_answer_rrs(
        self,
    ) -> "SyntheticMonitoringCheckSettingsDnsValidateAnswerRrsOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsDnsValidateAnswerRrsOutputReference", jsii.get(self, "validateAnswerRrs"))

    @builtins.property
    @jsii.member(jsii_name="validateAuthorityRrs")
    def validate_authority_rrs(
        self,
    ) -> "SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrsOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrsOutputReference", jsii.get(self, "validateAuthorityRrs"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionInput")
    def ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="recordTypeInput")
    def record_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recordTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpAddressInput")
    def source_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="validateAdditionalRrsInput")
    def validate_additional_rrs_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs"]]], jsii.get(self, "validateAdditionalRrsInput"))

    @builtins.property
    @jsii.member(jsii_name="validateAnswerRrsInput")
    def validate_answer_rrs_input(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs"], jsii.get(self, "validateAnswerRrsInput"))

    @builtins.property
    @jsii.member(jsii_name="validateAuthorityRrsInput")
    def validate_authority_rrs_input(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs"], jsii.get(self, "validateAuthorityRrsInput"))

    @builtins.property
    @jsii.member(jsii_name="validRCodesInput")
    def valid_r_codes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "validRCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersion")
    def ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipVersion"))

    @ip_version.setter
    def ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ebf2f7410e80e7ecb62214f4fcd27225c1215afae145d7e1a2404fc0d3b1cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersion", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0aa2ffdefa339dde87fa484c592f4da58e26a60af354e3c9039ac3e11185a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e3e48e8a348e3e8733685b195302ab29c88ca9119667e2b3d467c297ac07e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="recordType")
    def record_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recordType"))

    @record_type.setter
    def record_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a5b3cbc05d556233fb65499f1742cd722a55b575da428733b3f8af5b586ac03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordType", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e1efeedeea309e8b533fd3fb4e11d83e4b0162788ec97f7b460fc6f8912f1a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpAddress")
    def source_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIpAddress"))

    @source_ip_address.setter
    def source_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f19ea672783e1a86613de7dc34be5435ec1b13e06233ef9f8ffc439751de4669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="validRCodes")
    def valid_r_codes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "validRCodes"))

    @valid_r_codes.setter
    def valid_r_codes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3af6a15fff091a4b626272aace9a685ace1326fa78d4052d44a14588088a3d8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validRCodes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticMonitoringCheckSettingsDns]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsDns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95efb44d386c8be758ec0b0451e91bb72520e5a872fb4bdf99150d2f7a5bdc7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs",
    jsii_struct_bases=[],
    name_mapping={
        "fail_if_matches_regexp": "failIfMatchesRegexp",
        "fail_if_not_matches_regexp": "failIfNotMatchesRegexp",
    },
)
class SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs:
    def __init__(
        self,
        *,
        fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fail_if_matches_regexp: Fail if value matches regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        :param fail_if_not_matches_regexp: Fail if value does not match regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c1b8a0909805b150e2dfbe8cc10e4a54fd4cc3d391ab21b70e9b18af026c15b)
            check_type(argname="argument fail_if_matches_regexp", value=fail_if_matches_regexp, expected_type=type_hints["fail_if_matches_regexp"])
            check_type(argname="argument fail_if_not_matches_regexp", value=fail_if_not_matches_regexp, expected_type=type_hints["fail_if_not_matches_regexp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fail_if_matches_regexp is not None:
            self._values["fail_if_matches_regexp"] = fail_if_matches_regexp
        if fail_if_not_matches_regexp is not None:
            self._values["fail_if_not_matches_regexp"] = fail_if_not_matches_regexp

    @builtins.property
    def fail_if_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fail if value matches regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        '''
        result = self._values.get("fail_if_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fail_if_not_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fail if value does not match regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        result = self._values.get("fail_if_not_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36273a7d35e714fcc53cfef1c3eb753cdeca8c1ba7fed50a428b9ac8a3ff77a6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f39aa8fe174b6d733bc8bf7f8611234dcdc638fadd0fdef327ce3d41d06fd94d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1edc22ec84c592350f5cfee7a73331c7cb820a3aa61d8b68677eb9a0517f40d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86241a8d3f8aa3c1313f15403e6c070972803917f710be782d459daa2ee6662a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e6d5704b165248745fb100493925fdd13efa14a44031286b9175007e279d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d67f7e065df8c421f83883e61692a525254de21aff9688b23ee4b43d98290b8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5246356d9e63ff18893dee75af44bfc5dbf4f0fbc3bdb513cecfa318a225dce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetFailIfMatchesRegexp")
    def reset_fail_if_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfNotMatchesRegexp")
    def reset_fail_if_not_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfNotMatchesRegexp", []))

    @builtins.property
    @jsii.member(jsii_name="failIfMatchesRegexpInput")
    def fail_if_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfNotMatchesRegexpInput")
    def fail_if_not_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfNotMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfMatchesRegexp")
    def fail_if_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfMatchesRegexp"))

    @fail_if_matches_regexp.setter
    def fail_if_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1622eb8b522bf494e4112b96cc0b14f08c14044bfd0e3617b507793b3e0bc50f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="failIfNotMatchesRegexp")
    def fail_if_not_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfNotMatchesRegexp"))

    @fail_if_not_matches_regexp.setter
    def fail_if_not_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a37d2a65a9231b04fc2bdaf05d2991d044f401859bfd1a4b8e0f5d8aa7eeadce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfNotMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e719a88a8770df596922f1ad07eef39e85416b289fb6524392154c3e7b633eba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs",
    jsii_struct_bases=[],
    name_mapping={
        "fail_if_matches_regexp": "failIfMatchesRegexp",
        "fail_if_not_matches_regexp": "failIfNotMatchesRegexp",
    },
)
class SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs:
    def __init__(
        self,
        *,
        fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fail_if_matches_regexp: Fail if value matches regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        :param fail_if_not_matches_regexp: Fail if value does not match regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37191c5e59d53df999a08d20949add90f8ecb93016c2f0ee8f3c6bea4a8946ff)
            check_type(argname="argument fail_if_matches_regexp", value=fail_if_matches_regexp, expected_type=type_hints["fail_if_matches_regexp"])
            check_type(argname="argument fail_if_not_matches_regexp", value=fail_if_not_matches_regexp, expected_type=type_hints["fail_if_not_matches_regexp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fail_if_matches_regexp is not None:
            self._values["fail_if_matches_regexp"] = fail_if_matches_regexp
        if fail_if_not_matches_regexp is not None:
            self._values["fail_if_not_matches_regexp"] = fail_if_not_matches_regexp

    @builtins.property
    def fail_if_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fail if value matches regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        '''
        result = self._values.get("fail_if_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fail_if_not_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fail if value does not match regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        result = self._values.get("fail_if_not_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsDnsValidateAnswerRrsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAnswerRrsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd135bcb89c6b6c1e50e03515a80e99a8c7eef2f7f02830da4f5b5ca9d6168dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFailIfMatchesRegexp")
    def reset_fail_if_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfNotMatchesRegexp")
    def reset_fail_if_not_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfNotMatchesRegexp", []))

    @builtins.property
    @jsii.member(jsii_name="failIfMatchesRegexpInput")
    def fail_if_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfNotMatchesRegexpInput")
    def fail_if_not_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfNotMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfMatchesRegexp")
    def fail_if_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfMatchesRegexp"))

    @fail_if_matches_regexp.setter
    def fail_if_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55214703a837d807a4cd44310fdca8160216a022abb761ee22834454c08ad7fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="failIfNotMatchesRegexp")
    def fail_if_not_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfNotMatchesRegexp"))

    @fail_if_not_matches_regexp.setter
    def fail_if_not_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c11454449bce72f9f73b90b142dfbce87ec8c8b78b4849ee59cea34ed4cc82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfNotMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b30ebd3f5cd9a68203c0c94be484594a8084bcfd04ad25b212ef7957d34d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs",
    jsii_struct_bases=[],
    name_mapping={
        "fail_if_matches_regexp": "failIfMatchesRegexp",
        "fail_if_not_matches_regexp": "failIfNotMatchesRegexp",
    },
)
class SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs:
    def __init__(
        self,
        *,
        fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fail_if_matches_regexp: Fail if value matches regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        :param fail_if_not_matches_regexp: Fail if value does not match regex. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__518378517fcdb5ef5bb6ab75c0e2a193b24e34ed4331a44d68594e6ec3ca7bfa)
            check_type(argname="argument fail_if_matches_regexp", value=fail_if_matches_regexp, expected_type=type_hints["fail_if_matches_regexp"])
            check_type(argname="argument fail_if_not_matches_regexp", value=fail_if_not_matches_regexp, expected_type=type_hints["fail_if_not_matches_regexp"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if fail_if_matches_regexp is not None:
            self._values["fail_if_matches_regexp"] = fail_if_matches_regexp
        if fail_if_not_matches_regexp is not None:
            self._values["fail_if_not_matches_regexp"] = fail_if_not_matches_regexp

    @builtins.property
    def fail_if_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fail if value matches regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_matches_regexp SyntheticMonitoringCheck#fail_if_matches_regexp}
        '''
        result = self._values.get("fail_if_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fail_if_not_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Fail if value does not match regex.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_matches_regexp SyntheticMonitoringCheck#fail_if_not_matches_regexp}
        '''
        result = self._values.get("fail_if_not_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc63980fd9c89b7ef96e70a8d0be018c70af3c8064928fffc4671423b8605f51)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFailIfMatchesRegexp")
    def reset_fail_if_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfNotMatchesRegexp")
    def reset_fail_if_not_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfNotMatchesRegexp", []))

    @builtins.property
    @jsii.member(jsii_name="failIfMatchesRegexpInput")
    def fail_if_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfNotMatchesRegexpInput")
    def fail_if_not_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfNotMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfMatchesRegexp")
    def fail_if_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfMatchesRegexp"))

    @fail_if_matches_regexp.setter
    def fail_if_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d008fab72d50219c4ef1006033c83ed006baab066ad504a13ffeb09e3b4831de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="failIfNotMatchesRegexp")
    def fail_if_not_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfNotMatchesRegexp"))

    @fail_if_not_matches_regexp.setter
    def fail_if_not_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a437bfca49bca0ec40f506d270bcca9336c01338a50ace1fa236da7d765202c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfNotMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0186af46149a1d663e8c516a8ebca45ad98962d7149a3157f43ff5a64bfda21c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttp",
    jsii_struct_bases=[],
    name_mapping={
        "basic_auth": "basicAuth",
        "bearer_token": "bearerToken",
        "body": "body",
        "cache_busting_query_param_name": "cacheBustingQueryParamName",
        "fail_if_body_matches_regexp": "failIfBodyMatchesRegexp",
        "fail_if_body_not_matches_regexp": "failIfBodyNotMatchesRegexp",
        "fail_if_header_matches_regexp": "failIfHeaderMatchesRegexp",
        "fail_if_header_not_matches_regexp": "failIfHeaderNotMatchesRegexp",
        "fail_if_not_ssl": "failIfNotSsl",
        "fail_if_ssl": "failIfSsl",
        "headers": "headers",
        "ip_version": "ipVersion",
        "method": "method",
        "no_follow_redirects": "noFollowRedirects",
        "proxy_url": "proxyUrl",
        "tls_config": "tlsConfig",
        "valid_http_versions": "validHttpVersions",
        "valid_status_codes": "validStatusCodes",
    },
)
class SyntheticMonitoringCheckSettingsHttp:
    def __init__(
        self,
        *,
        basic_auth: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsHttpBasicAuth", typing.Dict[builtins.str, typing.Any]]] = None,
        bearer_token: typing.Optional[builtins.str] = None,
        body: typing.Optional[builtins.str] = None,
        cache_busting_query_param_name: typing.Optional[builtins.str] = None,
        fail_if_body_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_body_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_header_matches_regexp: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fail_if_header_not_matches_regexp: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fail_if_not_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fail_if_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_version: typing.Optional[builtins.str] = None,
        method: typing.Optional[builtins.str] = None,
        no_follow_redirects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        tls_config: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsHttpTlsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        valid_http_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        valid_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#basic_auth SyntheticMonitoringCheck#basic_auth}
        :param bearer_token: Token for use with bearer authorization header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#bearer_token SyntheticMonitoringCheck#bearer_token}
        :param body: The body of the HTTP request used in probe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#body SyntheticMonitoringCheck#body}
        :param cache_busting_query_param_name: The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#cache_busting_query_param_name SyntheticMonitoringCheck#cache_busting_query_param_name}
        :param fail_if_body_matches_regexp: List of regexes. If any match the response body, the check will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_body_matches_regexp SyntheticMonitoringCheck#fail_if_body_matches_regexp}
        :param fail_if_body_not_matches_regexp: List of regexes. If any do not match the response body, the check will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_body_not_matches_regexp SyntheticMonitoringCheck#fail_if_body_not_matches_regexp}
        :param fail_if_header_matches_regexp: fail_if_header_matches_regexp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_header_matches_regexp SyntheticMonitoringCheck#fail_if_header_matches_regexp}
        :param fail_if_header_not_matches_regexp: fail_if_header_not_matches_regexp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_header_not_matches_regexp SyntheticMonitoringCheck#fail_if_header_not_matches_regexp}
        :param fail_if_not_ssl: Fail if SSL is not present. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_ssl SyntheticMonitoringCheck#fail_if_not_ssl}
        :param fail_if_ssl: Fail if SSL is present. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_ssl SyntheticMonitoringCheck#fail_if_ssl}
        :param headers: The HTTP headers set for the probe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#headers SyntheticMonitoringCheck#headers}
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param method: Request method. One of ``GET``, ``CONNECT``, ``DELETE``, ``HEAD``, ``OPTIONS``, ``POST``, ``PUT``, ``TRACE`` Defaults to ``GET``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#method SyntheticMonitoringCheck#method}
        :param no_follow_redirects: Do not follow redirects. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#no_follow_redirects SyntheticMonitoringCheck#no_follow_redirects}
        :param proxy_url: Proxy URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#proxy_url SyntheticMonitoringCheck#proxy_url}
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls_config SyntheticMonitoringCheck#tls_config}
        :param valid_http_versions: List of valid HTTP versions. Options include ``HTTP/1.0``, ``HTTP/1.1``, ``HTTP/2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_http_versions SyntheticMonitoringCheck#valid_http_versions}
        :param valid_status_codes: Accepted status codes. If unset, defaults to 2xx. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_status_codes SyntheticMonitoringCheck#valid_status_codes}
        '''
        if isinstance(basic_auth, dict):
            basic_auth = SyntheticMonitoringCheckSettingsHttpBasicAuth(**basic_auth)
        if isinstance(tls_config, dict):
            tls_config = SyntheticMonitoringCheckSettingsHttpTlsConfig(**tls_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bca66f386f132f6aea4ab3b6dc28f393da62c22a544e25dc6a377fd5435c64a)
            check_type(argname="argument basic_auth", value=basic_auth, expected_type=type_hints["basic_auth"])
            check_type(argname="argument bearer_token", value=bearer_token, expected_type=type_hints["bearer_token"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument cache_busting_query_param_name", value=cache_busting_query_param_name, expected_type=type_hints["cache_busting_query_param_name"])
            check_type(argname="argument fail_if_body_matches_regexp", value=fail_if_body_matches_regexp, expected_type=type_hints["fail_if_body_matches_regexp"])
            check_type(argname="argument fail_if_body_not_matches_regexp", value=fail_if_body_not_matches_regexp, expected_type=type_hints["fail_if_body_not_matches_regexp"])
            check_type(argname="argument fail_if_header_matches_regexp", value=fail_if_header_matches_regexp, expected_type=type_hints["fail_if_header_matches_regexp"])
            check_type(argname="argument fail_if_header_not_matches_regexp", value=fail_if_header_not_matches_regexp, expected_type=type_hints["fail_if_header_not_matches_regexp"])
            check_type(argname="argument fail_if_not_ssl", value=fail_if_not_ssl, expected_type=type_hints["fail_if_not_ssl"])
            check_type(argname="argument fail_if_ssl", value=fail_if_ssl, expected_type=type_hints["fail_if_ssl"])
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument ip_version", value=ip_version, expected_type=type_hints["ip_version"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument no_follow_redirects", value=no_follow_redirects, expected_type=type_hints["no_follow_redirects"])
            check_type(argname="argument proxy_url", value=proxy_url, expected_type=type_hints["proxy_url"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
            check_type(argname="argument valid_http_versions", value=valid_http_versions, expected_type=type_hints["valid_http_versions"])
            check_type(argname="argument valid_status_codes", value=valid_status_codes, expected_type=type_hints["valid_status_codes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if basic_auth is not None:
            self._values["basic_auth"] = basic_auth
        if bearer_token is not None:
            self._values["bearer_token"] = bearer_token
        if body is not None:
            self._values["body"] = body
        if cache_busting_query_param_name is not None:
            self._values["cache_busting_query_param_name"] = cache_busting_query_param_name
        if fail_if_body_matches_regexp is not None:
            self._values["fail_if_body_matches_regexp"] = fail_if_body_matches_regexp
        if fail_if_body_not_matches_regexp is not None:
            self._values["fail_if_body_not_matches_regexp"] = fail_if_body_not_matches_regexp
        if fail_if_header_matches_regexp is not None:
            self._values["fail_if_header_matches_regexp"] = fail_if_header_matches_regexp
        if fail_if_header_not_matches_regexp is not None:
            self._values["fail_if_header_not_matches_regexp"] = fail_if_header_not_matches_regexp
        if fail_if_not_ssl is not None:
            self._values["fail_if_not_ssl"] = fail_if_not_ssl
        if fail_if_ssl is not None:
            self._values["fail_if_ssl"] = fail_if_ssl
        if headers is not None:
            self._values["headers"] = headers
        if ip_version is not None:
            self._values["ip_version"] = ip_version
        if method is not None:
            self._values["method"] = method
        if no_follow_redirects is not None:
            self._values["no_follow_redirects"] = no_follow_redirects
        if proxy_url is not None:
            self._values["proxy_url"] = proxy_url
        if tls_config is not None:
            self._values["tls_config"] = tls_config
        if valid_http_versions is not None:
            self._values["valid_http_versions"] = valid_http_versions
        if valid_status_codes is not None:
            self._values["valid_status_codes"] = valid_status_codes

    @builtins.property
    def basic_auth(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsHttpBasicAuth"]:
        '''basic_auth block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#basic_auth SyntheticMonitoringCheck#basic_auth}
        '''
        result = self._values.get("basic_auth")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsHttpBasicAuth"], result)

    @builtins.property
    def bearer_token(self) -> typing.Optional[builtins.str]:
        '''Token for use with bearer authorization header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#bearer_token SyntheticMonitoringCheck#bearer_token}
        '''
        result = self._values.get("bearer_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def body(self) -> typing.Optional[builtins.str]:
        '''The body of the HTTP request used in probe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#body SyntheticMonitoringCheck#body}
        '''
        result = self._values.get("body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cache_busting_query_param_name(self) -> typing.Optional[builtins.str]:
        '''The name of the query parameter used to prevent the server from using a cached response.

        Each probe will assign a random value to this parameter each time a request is made.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#cache_busting_query_param_name SyntheticMonitoringCheck#cache_busting_query_param_name}
        '''
        result = self._values.get("cache_busting_query_param_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fail_if_body_matches_regexp(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of regexes. If any match the response body, the check will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_body_matches_regexp SyntheticMonitoringCheck#fail_if_body_matches_regexp}
        '''
        result = self._values.get("fail_if_body_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fail_if_body_not_matches_regexp(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''List of regexes. If any do not match the response body, the check will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_body_not_matches_regexp SyntheticMonitoringCheck#fail_if_body_not_matches_regexp}
        '''
        result = self._values.get("fail_if_body_not_matches_regexp")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fail_if_header_matches_regexp(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp"]]]:
        '''fail_if_header_matches_regexp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_header_matches_regexp SyntheticMonitoringCheck#fail_if_header_matches_regexp}
        '''
        result = self._values.get("fail_if_header_matches_regexp")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp"]]], result)

    @builtins.property
    def fail_if_header_not_matches_regexp(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp"]]]:
        '''fail_if_header_not_matches_regexp block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_header_not_matches_regexp SyntheticMonitoringCheck#fail_if_header_not_matches_regexp}
        '''
        result = self._values.get("fail_if_header_not_matches_regexp")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp"]]], result)

    @builtins.property
    def fail_if_not_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Fail if SSL is not present. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_ssl SyntheticMonitoringCheck#fail_if_not_ssl}
        '''
        result = self._values.get("fail_if_not_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def fail_if_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Fail if SSL is present. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_ssl SyntheticMonitoringCheck#fail_if_ssl}
        '''
        result = self._values.get("fail_if_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The HTTP headers set for the probe.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#headers SyntheticMonitoringCheck#headers}
        '''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_version(self) -> typing.Optional[builtins.str]:
        '''Options are ``V4``, ``V6``, ``Any``.

        Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        '''
        result = self._values.get("ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def method(self) -> typing.Optional[builtins.str]:
        '''Request method. One of ``GET``, ``CONNECT``, ``DELETE``, ``HEAD``, ``OPTIONS``, ``POST``, ``PUT``, ``TRACE`` Defaults to ``GET``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#method SyntheticMonitoringCheck#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def no_follow_redirects(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Do not follow redirects. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#no_follow_redirects SyntheticMonitoringCheck#no_follow_redirects}
        '''
        result = self._values.get("no_follow_redirects")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def proxy_url(self) -> typing.Optional[builtins.str]:
        '''Proxy URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#proxy_url SyntheticMonitoringCheck#proxy_url}
        '''
        result = self._values.get("proxy_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_config(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsHttpTlsConfig"]:
        '''tls_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls_config SyntheticMonitoringCheck#tls_config}
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsHttpTlsConfig"], result)

    @builtins.property
    def valid_http_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of valid HTTP versions. Options include ``HTTP/1.0``, ``HTTP/1.1``, ``HTTP/2``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_http_versions SyntheticMonitoringCheck#valid_http_versions}
        '''
        result = self._values.get("valid_http_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def valid_status_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Accepted status codes. If unset, defaults to 2xx.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_status_codes SyntheticMonitoringCheck#valid_status_codes}
        '''
        result = self._values.get("valid_status_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsHttp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpBasicAuth",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class SyntheticMonitoringCheckSettingsHttpBasicAuth:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Basic auth password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#password SyntheticMonitoringCheck#password}
        :param username: Basic auth username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#username SyntheticMonitoringCheck#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b602512249b76a968bce3e6b6a2b5966c96e2bc531ea423850689223ab96f8d)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Basic auth password.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#password SyntheticMonitoringCheck#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Basic auth username.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#username SyntheticMonitoringCheck#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsHttpBasicAuth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsHttpBasicAuthOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpBasicAuthOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7f8ba59e669a9ec299b04027c7257fa8b411aaea33b29fe27790fcf29ec708)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdfbcfcda09e59aa787811a4ef2cf5cdacc3c904c8cf1dc7971a5cc9a2e6976f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9983fcd34ec6867b5c0b9b9f4dad28636568fbfa48f1fd7787c2fe83979a73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsHttpBasicAuth]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsHttpBasicAuth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsHttpBasicAuth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e7b14d9b78d5abf503a2bba340f063473d7d274b9d7538f2d8475eee40055c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp",
    jsii_struct_bases=[],
    name_mapping={
        "header": "header",
        "regexp": "regexp",
        "allow_missing": "allowMissing",
    },
)
class SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp:
    def __init__(
        self,
        *,
        header: builtins.str,
        regexp: builtins.str,
        allow_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param header: Header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#header SyntheticMonitoringCheck#header}
        :param regexp: Regex that header value should match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#regexp SyntheticMonitoringCheck#regexp}
        :param allow_missing: Allow header to be missing from responses. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#allow_missing SyntheticMonitoringCheck#allow_missing}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f60856e1fca1803d35307ea4b11d0ef73af13f2f38ba7ec474a23342310d28f5)
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument regexp", value=regexp, expected_type=type_hints["regexp"])
            check_type(argname="argument allow_missing", value=allow_missing, expected_type=type_hints["allow_missing"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "header": header,
            "regexp": regexp,
        }
        if allow_missing is not None:
            self._values["allow_missing"] = allow_missing

    @builtins.property
    def header(self) -> builtins.str:
        '''Header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#header SyntheticMonitoringCheck#header}
        '''
        result = self._values.get("header")
        assert result is not None, "Required property 'header' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regexp(self) -> builtins.str:
        '''Regex that header value should match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#regexp SyntheticMonitoringCheck#regexp}
        '''
        result = self._values.get("regexp")
        assert result is not None, "Required property 'regexp' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allow header to be missing from responses. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#allow_missing SyntheticMonitoringCheck#allow_missing}
        '''
        result = self._values.get("allow_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6868c645088f71c5fd0605043b26f99d48a73dc6eef0bac0150d0a24a1ea9099)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c91a5bb7081e94652f80f9539fb7dc726773b7d7d8a095d25c53f4c1515020)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d4f2bfbb5aa5300838ecc7fb739e2ca0ac52e50204aafeee524257f69d5a2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbfbec3934b3a8f9c802399ed5d634f305e7285bf6874b904e97a3bf18d0f8fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc85d783e89fc9f46d29056507e4e9c01d224fd1bd8c4ac1ff42415ab444e0ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a77ec7fa797f94844818b4fa84d8ae8961def4774d8788d1e9ce60c4fb01ffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6558fe2e22a28b05059a48a020f1e95182452c9cd892e69ac3b1557a9d3838b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowMissing")
    def reset_allow_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMissing", []))

    @builtins.property
    @jsii.member(jsii_name="allowMissingInput")
    def allow_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="regexpInput")
    def regexp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexpInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMissing")
    def allow_missing(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowMissing"))

    @allow_missing.setter
    def allow_missing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a15e51086d792dbf490ebfa76184e4a88755adfecadbb38c59cf61c269d67a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMissing", value)

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "header"))

    @header.setter
    def header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1987ddac1a1fee776c032c1179fd1099d077af705b3d01a4f131880d2dd111e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="regexp")
    def regexp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexp"))

    @regexp.setter
    def regexp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dffe6ca14b9d62d654e45f72209606dce2de2480bdd3a614163c83a07de9ff4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f898f5ce9d8b99ed460c9056db17c58f9171406c87b868be8a420aec512109)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp",
    jsii_struct_bases=[],
    name_mapping={
        "header": "header",
        "regexp": "regexp",
        "allow_missing": "allowMissing",
    },
)
class SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp:
    def __init__(
        self,
        *,
        header: builtins.str,
        regexp: builtins.str,
        allow_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param header: Header name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#header SyntheticMonitoringCheck#header}
        :param regexp: Regex that header value should match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#regexp SyntheticMonitoringCheck#regexp}
        :param allow_missing: Allow header to be missing from responses. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#allow_missing SyntheticMonitoringCheck#allow_missing}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19cec9ac9ec35c22a3049b74bf62dbea6f32a9ae5b8655bdf4ba3e4f14c46dd7)
            check_type(argname="argument header", value=header, expected_type=type_hints["header"])
            check_type(argname="argument regexp", value=regexp, expected_type=type_hints["regexp"])
            check_type(argname="argument allow_missing", value=allow_missing, expected_type=type_hints["allow_missing"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "header": header,
            "regexp": regexp,
        }
        if allow_missing is not None:
            self._values["allow_missing"] = allow_missing

    @builtins.property
    def header(self) -> builtins.str:
        '''Header name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#header SyntheticMonitoringCheck#header}
        '''
        result = self._values.get("header")
        assert result is not None, "Required property 'header' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regexp(self) -> builtins.str:
        '''Regex that header value should match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#regexp SyntheticMonitoringCheck#regexp}
        '''
        result = self._values.get("regexp")
        assert result is not None, "Required property 'regexp' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_missing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Allow header to be missing from responses. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#allow_missing SyntheticMonitoringCheck#allow_missing}
        '''
        result = self._values.get("allow_missing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d1009f69162d13c565f11b14605b7dea9e9c40abfc9186d3a53ade4f449efa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f63cda3142c35c5d45cd3a8ca2161a7642d0cd47f28c6636b12456821fd3ac42)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e808796c5beb0b160eb7da38a89d82c3be19dca27dec49b35da693e7787cef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e0d70b7d40e11ca9eaed9cba4fc93599c3bfb0df7a27210789f0112a364f435)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57730eef22644c2b642ccdd44a15cf9f5d1badbb7b9d2844eb0329ba66c07555)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__739cb39bd5f99260a261576066ccadbe6ef6334a6f674e5fe07f43623d294898)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234c6a647c0f9040ce9fdc2f405e60d83eac3d38543b846bb5edab0d4e7a7483)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowMissing")
    def reset_allow_missing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMissing", []))

    @builtins.property
    @jsii.member(jsii_name="allowMissingInput")
    def allow_missing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowMissingInput"))

    @builtins.property
    @jsii.member(jsii_name="headerInput")
    def header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "headerInput"))

    @builtins.property
    @jsii.member(jsii_name="regexpInput")
    def regexp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexpInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMissing")
    def allow_missing(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowMissing"))

    @allow_missing.setter
    def allow_missing(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70308ec6e060579f8050b2ba0e05a4df84d1a106faf4b9eac9f20e86236a9b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMissing", value)

    @builtins.property
    @jsii.member(jsii_name="header")
    def header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "header"))

    @header.setter
    def header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fddb1e56b13ce6a02d3d0b996a1dedb38430d8a0f0fd7b4a4ce1a67fccc182d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "header", value)

    @builtins.property
    @jsii.member(jsii_name="regexp")
    def regexp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexp"))

    @regexp.setter
    def regexp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e7e8198d1dca47bbc9d5a7dc71e32da930ee0ff24ee946da0f7333c87074e0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexp", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59599c6db6e47a3b581b74e0f406be6eea8126d181cd13ed7d03bb9fb5dba8ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticMonitoringCheckSettingsHttpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2d0fd066397aaf0e5049898219d818ce36521ba4ecc075d68ad4f354308db7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBasicAuth")
    def put_basic_auth(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Basic auth password. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#password SyntheticMonitoringCheck#password}
        :param username: Basic auth username. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#username SyntheticMonitoringCheck#username}
        '''
        value = SyntheticMonitoringCheckSettingsHttpBasicAuth(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putBasicAuth", [value]))

    @jsii.member(jsii_name="putFailIfHeaderMatchesRegexp")
    def put_fail_if_header_matches_regexp(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42e536307bef064c1b272f7b311ae8789df2cf540f8498f4b6ac993277ef50c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFailIfHeaderMatchesRegexp", [value]))

    @jsii.member(jsii_name="putFailIfHeaderNotMatchesRegexp")
    def put_fail_if_header_not_matches_regexp(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85fcfa0225fddb0bfbb8deb6f13aa3cb67256e4174b25c59f0afb43bc11b0f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFailIfHeaderNotMatchesRegexp", [value]))

    @jsii.member(jsii_name="putTlsConfig")
    def put_tls_config(
        self,
        *,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_cert: CA certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ca_cert SyntheticMonitoringCheck#ca_cert}
        :param client_cert: Client certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_cert SyntheticMonitoringCheck#client_cert}
        :param client_key: Client key in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_key SyntheticMonitoringCheck#client_key}
        :param insecure_skip_verify: Disable target certificate validation. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#insecure_skip_verify SyntheticMonitoringCheck#insecure_skip_verify}
        :param server_name: Used to verify the hostname for the targets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server_name SyntheticMonitoringCheck#server_name}
        '''
        value = SyntheticMonitoringCheckSettingsHttpTlsConfig(
            ca_cert=ca_cert,
            client_cert=client_cert,
            client_key=client_key,
            insecure_skip_verify=insecure_skip_verify,
            server_name=server_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTlsConfig", [value]))

    @jsii.member(jsii_name="resetBasicAuth")
    def reset_basic_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuth", []))

    @jsii.member(jsii_name="resetBearerToken")
    def reset_bearer_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBearerToken", []))

    @jsii.member(jsii_name="resetBody")
    def reset_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBody", []))

    @jsii.member(jsii_name="resetCacheBustingQueryParamName")
    def reset_cache_busting_query_param_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCacheBustingQueryParamName", []))

    @jsii.member(jsii_name="resetFailIfBodyMatchesRegexp")
    def reset_fail_if_body_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfBodyMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfBodyNotMatchesRegexp")
    def reset_fail_if_body_not_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfBodyNotMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfHeaderMatchesRegexp")
    def reset_fail_if_header_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfHeaderMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfHeaderNotMatchesRegexp")
    def reset_fail_if_header_not_matches_regexp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfHeaderNotMatchesRegexp", []))

    @jsii.member(jsii_name="resetFailIfNotSsl")
    def reset_fail_if_not_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfNotSsl", []))

    @jsii.member(jsii_name="resetFailIfSsl")
    def reset_fail_if_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailIfSsl", []))

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetIpVersion")
    def reset_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersion", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetNoFollowRedirects")
    def reset_no_follow_redirects(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoFollowRedirects", []))

    @jsii.member(jsii_name="resetProxyUrl")
    def reset_proxy_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyUrl", []))

    @jsii.member(jsii_name="resetTlsConfig")
    def reset_tls_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsConfig", []))

    @jsii.member(jsii_name="resetValidHttpVersions")
    def reset_valid_http_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidHttpVersions", []))

    @jsii.member(jsii_name="resetValidStatusCodes")
    def reset_valid_status_codes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidStatusCodes", []))

    @builtins.property
    @jsii.member(jsii_name="basicAuth")
    def basic_auth(
        self,
    ) -> SyntheticMonitoringCheckSettingsHttpBasicAuthOutputReference:
        return typing.cast(SyntheticMonitoringCheckSettingsHttpBasicAuthOutputReference, jsii.get(self, "basicAuth"))

    @builtins.property
    @jsii.member(jsii_name="failIfHeaderMatchesRegexp")
    def fail_if_header_matches_regexp(
        self,
    ) -> SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpList:
        return typing.cast(SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpList, jsii.get(self, "failIfHeaderMatchesRegexp"))

    @builtins.property
    @jsii.member(jsii_name="failIfHeaderNotMatchesRegexp")
    def fail_if_header_not_matches_regexp(
        self,
    ) -> SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpList:
        return typing.cast(SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpList, jsii.get(self, "failIfHeaderNotMatchesRegexp"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfig")
    def tls_config(
        self,
    ) -> "SyntheticMonitoringCheckSettingsHttpTlsConfigOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsHttpTlsConfigOutputReference", jsii.get(self, "tlsConfig"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthInput")
    def basic_auth_input(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsHttpBasicAuth]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsHttpBasicAuth], jsii.get(self, "basicAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="bearerTokenInput")
    def bearer_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bearerTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="cacheBustingQueryParamNameInput")
    def cache_busting_query_param_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheBustingQueryParamNameInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfBodyMatchesRegexpInput")
    def fail_if_body_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfBodyMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfBodyNotMatchesRegexpInput")
    def fail_if_body_not_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "failIfBodyNotMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfHeaderMatchesRegexpInput")
    def fail_if_header_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp]]], jsii.get(self, "failIfHeaderMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfHeaderNotMatchesRegexpInput")
    def fail_if_header_not_matches_regexp_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp]]], jsii.get(self, "failIfHeaderNotMatchesRegexpInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfNotSslInput")
    def fail_if_not_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failIfNotSslInput"))

    @builtins.property
    @jsii.member(jsii_name="failIfSslInput")
    def fail_if_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "failIfSslInput"))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionInput")
    def ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="noFollowRedirectsInput")
    def no_follow_redirects_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "noFollowRedirectsInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyUrlInput")
    def proxy_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfigInput")
    def tls_config_input(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsHttpTlsConfig"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsHttpTlsConfig"], jsii.get(self, "tlsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="validHttpVersionsInput")
    def valid_http_versions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "validHttpVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="validStatusCodesInput")
    def valid_status_codes_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "validStatusCodesInput"))

    @builtins.property
    @jsii.member(jsii_name="bearerToken")
    def bearer_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bearerToken"))

    @bearer_token.setter
    def bearer_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__457285ce56940109585f6a8bd7b60b75478a3e4ea1d05f42582ffcde4ebd803f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bearerToken", value)

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ef5959cd4796c5070d26f4c676155b44480e64daa6b8df33f1889610fbcb51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="cacheBustingQueryParamName")
    def cache_busting_query_param_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cacheBustingQueryParamName"))

    @cache_busting_query_param_name.setter
    def cache_busting_query_param_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e77c89f750c049782ce750b2623887a85e9984b8fcdae764ca25e0cf28d2e204)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheBustingQueryParamName", value)

    @builtins.property
    @jsii.member(jsii_name="failIfBodyMatchesRegexp")
    def fail_if_body_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfBodyMatchesRegexp"))

    @fail_if_body_matches_regexp.setter
    def fail_if_body_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30274d4092308afe2855022a8374417f8e324371dc43524bab849e99c44a78a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfBodyMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="failIfBodyNotMatchesRegexp")
    def fail_if_body_not_matches_regexp(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "failIfBodyNotMatchesRegexp"))

    @fail_if_body_not_matches_regexp.setter
    def fail_if_body_not_matches_regexp(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5179e917a6606aaf97287d4e35b200b047070f7b7fa747a8c5462582f4b3a2c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfBodyNotMatchesRegexp", value)

    @builtins.property
    @jsii.member(jsii_name="failIfNotSsl")
    def fail_if_not_ssl(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failIfNotSsl"))

    @fail_if_not_ssl.setter
    def fail_if_not_ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee926f14999b731558b1d482d0a80d8d17a1941211d41a34b89a5aa469786667)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfNotSsl", value)

    @builtins.property
    @jsii.member(jsii_name="failIfSsl")
    def fail_if_ssl(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "failIfSsl"))

    @fail_if_ssl.setter
    def fail_if_ssl(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5037ced20146194e6dd9d4c6cf456bcd620b71f4e23d8f16cc4606a69963462)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failIfSsl", value)

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "headers"))

    @headers.setter
    def headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec188460a03612090940d2ac878bc596c03350d3db8498558c00045ccfff90d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="ipVersion")
    def ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipVersion"))

    @ip_version.setter
    def ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec9ea35024ccbf003237d177756160579faafcc9e2320cf7dc388f08f57cb393)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersion", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "method"))

    @method.setter
    def method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7aad9ab4b5d5e6b713961781b82123661b61948aa01332318183b04f23f2d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="noFollowRedirects")
    def no_follow_redirects(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "noFollowRedirects"))

    @no_follow_redirects.setter
    def no_follow_redirects(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44501bb1439c93eb9923f2881b5e94efb753ce24cc03b60076e2d1e4993cb59f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noFollowRedirects", value)

    @builtins.property
    @jsii.member(jsii_name="proxyUrl")
    def proxy_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyUrl"))

    @proxy_url.setter
    def proxy_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba5a3c6cc8537c34fd04ecde12109e6f84591f7f541aacddf7a8dd4e282cd39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="validHttpVersions")
    def valid_http_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "validHttpVersions"))

    @valid_http_versions.setter
    def valid_http_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0676c9e121a337c45dd9bfe3f6be7a9cb9c0311512dd5c1fa94b7a2f7de5e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validHttpVersions", value)

    @builtins.property
    @jsii.member(jsii_name="validStatusCodes")
    def valid_status_codes(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "validStatusCodes"))

    @valid_status_codes.setter
    def valid_status_codes(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5698d42b33b1947745462e879c8cdeeb83988a6e42afffc13b3ef7bdc39e3900)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validStatusCodes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticMonitoringCheckSettingsHttp]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsHttp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsHttp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__674ea93aef110699cc71c09a197a6d4f37d235ea4dc521d5bddaf23ecc0d17a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpTlsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "ca_cert": "caCert",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "insecure_skip_verify": "insecureSkipVerify",
        "server_name": "serverName",
    },
)
class SyntheticMonitoringCheckSettingsHttpTlsConfig:
    def __init__(
        self,
        *,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_cert: CA certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ca_cert SyntheticMonitoringCheck#ca_cert}
        :param client_cert: Client certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_cert SyntheticMonitoringCheck#client_cert}
        :param client_key: Client key in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_key SyntheticMonitoringCheck#client_key}
        :param insecure_skip_verify: Disable target certificate validation. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#insecure_skip_verify SyntheticMonitoringCheck#insecure_skip_verify}
        :param server_name: Used to verify the hostname for the targets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server_name SyntheticMonitoringCheck#server_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f459460b7db4cba9705ac64a2a4bec298bbf5cae417e568dc112b073ebbe2b)
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument insecure_skip_verify", value=insecure_skip_verify, expected_type=type_hints["insecure_skip_verify"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if server_name is not None:
            self._values["server_name"] = server_name

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''CA certificate in PEM format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ca_cert SyntheticMonitoringCheck#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''Client certificate in PEM format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_cert SyntheticMonitoringCheck#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''Client key in PEM format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_key SyntheticMonitoringCheck#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Disable target certificate validation. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#insecure_skip_verify SyntheticMonitoringCheck#insecure_skip_verify}
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''Used to verify the hostname for the targets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server_name SyntheticMonitoringCheck#server_name}
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsHttpTlsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsHttpTlsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsHttpTlsConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c6c8da497cc082f0a6cbeab30ce4de5c8711ae510c892ab5488632a5ef3aeb9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetInsecureSkipVerify")
    def reset_insecure_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipVerify", []))

    @jsii.member(jsii_name="resetServerName")
    def reset_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerName", []))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerifyInput")
    def insecure_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5fe893c10e4bde15fa41c7fb0be6ed41d730a72311e92b385967a05b3c4bbf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c1869c4b6ce7fa1db2f7ec5f357d32f7af342e4c650ce14cb4dbfd9bf80bb63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c82db1de01a6f9783a5644b327c416045e646b403411295b3f6c6867f26945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerify")
    def insecure_skip_verify(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecureSkipVerify"))

    @insecure_skip_verify.setter
    def insecure_skip_verify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4aa368d2401f86641516c8f23a69cc887798c73d36a767e7c43a5f893eb5c43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__768e62d00b7ed26e5e1dc45f983c8c6d1a4fc32fe77ec338fda0b48569bc6816)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsHttpTlsConfig]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsHttpTlsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsHttpTlsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d6b7f93db482cdfe5aab8bc74c6e79f01168dd8691c0a0f54b12b032ff4178)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticMonitoringCheckSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6681e817db10b8ebbace748326dbc6b9eee86f4cd462a5a948757f50c926ca90)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDns")
    def put_dns(
        self,
        *,
        ip_version: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        record_type: typing.Optional[builtins.str] = None,
        server: typing.Optional[builtins.str] = None,
        source_ip_address: typing.Optional[builtins.str] = None,
        validate_additional_rrs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, typing.Dict[builtins.str, typing.Any]]]]] = None,
        validate_answer_rrs: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs, typing.Dict[builtins.str, typing.Any]]] = None,
        validate_authority_rrs: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs, typing.Dict[builtins.str, typing.Any]]] = None,
        valid_r_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param port: Port to target. Defaults to ``53``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#port SyntheticMonitoringCheck#port}
        :param protocol: ``TCP`` or ``UDP``. Defaults to ``UDP``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#protocol SyntheticMonitoringCheck#protocol}
        :param record_type: One of ``ANY``, ``A``, ``AAAA``, ``CNAME``, ``MX``, ``NS``, ``PTR``, ``SOA``, ``SRV``, ``TXT``. Defaults to ``A``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#record_type SyntheticMonitoringCheck#record_type}
        :param server: DNS server address to target. Defaults to ``8.8.8.8``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server SyntheticMonitoringCheck#server}
        :param source_ip_address: Source IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        :param validate_additional_rrs: validate_additional_rrs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_additional_rrs SyntheticMonitoringCheck#validate_additional_rrs}
        :param validate_answer_rrs: validate_answer_rrs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_answer_rrs SyntheticMonitoringCheck#validate_answer_rrs}
        :param validate_authority_rrs: validate_authority_rrs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#validate_authority_rrs SyntheticMonitoringCheck#validate_authority_rrs}
        :param valid_r_codes: List of valid response codes. Options include ``NOERROR``, ``BADALG``, ``BADMODE``, ``BADKEY``, ``BADCOOKIE``, ``BADNAME``, ``BADSIG``, ``BADTIME``, ``BADTRUNC``, ``BADVERS``, ``FORMERR``, ``NOTIMP``, ``NOTAUTH``, ``NOTZONE``, ``NXDOMAIN``, ``NXRRSET``, ``REFUSED``, ``SERVFAIL``, ``YXDOMAIN``, ``YXRRSET``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_r_codes SyntheticMonitoringCheck#valid_r_codes}
        '''
        value = SyntheticMonitoringCheckSettingsDns(
            ip_version=ip_version,
            port=port,
            protocol=protocol,
            record_type=record_type,
            server=server,
            source_ip_address=source_ip_address,
            validate_additional_rrs=validate_additional_rrs,
            validate_answer_rrs=validate_answer_rrs,
            validate_authority_rrs=validate_authority_rrs,
            valid_r_codes=valid_r_codes,
        )

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putHttp")
    def put_http(
        self,
        *,
        basic_auth: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
        bearer_token: typing.Optional[builtins.str] = None,
        body: typing.Optional[builtins.str] = None,
        cache_busting_query_param_name: typing.Optional[builtins.str] = None,
        fail_if_body_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_body_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
        fail_if_header_matches_regexp: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]]] = None,
        fail_if_header_not_matches_regexp: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]]] = None,
        fail_if_not_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        fail_if_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_version: typing.Optional[builtins.str] = None,
        method: typing.Optional[builtins.str] = None,
        no_follow_redirects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        proxy_url: typing.Optional[builtins.str] = None,
        tls_config: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpTlsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        valid_http_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        valid_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param basic_auth: basic_auth block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#basic_auth SyntheticMonitoringCheck#basic_auth}
        :param bearer_token: Token for use with bearer authorization header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#bearer_token SyntheticMonitoringCheck#bearer_token}
        :param body: The body of the HTTP request used in probe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#body SyntheticMonitoringCheck#body}
        :param cache_busting_query_param_name: The name of the query parameter used to prevent the server from using a cached response. Each probe will assign a random value to this parameter each time a request is made. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#cache_busting_query_param_name SyntheticMonitoringCheck#cache_busting_query_param_name}
        :param fail_if_body_matches_regexp: List of regexes. If any match the response body, the check will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_body_matches_regexp SyntheticMonitoringCheck#fail_if_body_matches_regexp}
        :param fail_if_body_not_matches_regexp: List of regexes. If any do not match the response body, the check will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_body_not_matches_regexp SyntheticMonitoringCheck#fail_if_body_not_matches_regexp}
        :param fail_if_header_matches_regexp: fail_if_header_matches_regexp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_header_matches_regexp SyntheticMonitoringCheck#fail_if_header_matches_regexp}
        :param fail_if_header_not_matches_regexp: fail_if_header_not_matches_regexp block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_header_not_matches_regexp SyntheticMonitoringCheck#fail_if_header_not_matches_regexp}
        :param fail_if_not_ssl: Fail if SSL is not present. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_not_ssl SyntheticMonitoringCheck#fail_if_not_ssl}
        :param fail_if_ssl: Fail if SSL is present. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#fail_if_ssl SyntheticMonitoringCheck#fail_if_ssl}
        :param headers: The HTTP headers set for the probe. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#headers SyntheticMonitoringCheck#headers}
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param method: Request method. One of ``GET``, ``CONNECT``, ``DELETE``, ``HEAD``, ``OPTIONS``, ``POST``, ``PUT``, ``TRACE`` Defaults to ``GET``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#method SyntheticMonitoringCheck#method}
        :param no_follow_redirects: Do not follow redirects. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#no_follow_redirects SyntheticMonitoringCheck#no_follow_redirects}
        :param proxy_url: Proxy URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#proxy_url SyntheticMonitoringCheck#proxy_url}
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls_config SyntheticMonitoringCheck#tls_config}
        :param valid_http_versions: List of valid HTTP versions. Options include ``HTTP/1.0``, ``HTTP/1.1``, ``HTTP/2``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_http_versions SyntheticMonitoringCheck#valid_http_versions}
        :param valid_status_codes: Accepted status codes. If unset, defaults to 2xx. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#valid_status_codes SyntheticMonitoringCheck#valid_status_codes}
        '''
        value = SyntheticMonitoringCheckSettingsHttp(
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            body=body,
            cache_busting_query_param_name=cache_busting_query_param_name,
            fail_if_body_matches_regexp=fail_if_body_matches_regexp,
            fail_if_body_not_matches_regexp=fail_if_body_not_matches_regexp,
            fail_if_header_matches_regexp=fail_if_header_matches_regexp,
            fail_if_header_not_matches_regexp=fail_if_header_not_matches_regexp,
            fail_if_not_ssl=fail_if_not_ssl,
            fail_if_ssl=fail_if_ssl,
            headers=headers,
            ip_version=ip_version,
            method=method,
            no_follow_redirects=no_follow_redirects,
            proxy_url=proxy_url,
            tls_config=tls_config,
            valid_http_versions=valid_http_versions,
            valid_status_codes=valid_status_codes,
        )

        return typing.cast(None, jsii.invoke(self, "putHttp", [value]))

    @jsii.member(jsii_name="putPing")
    def put_ping(
        self,
        *,
        dont_fragment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_version: typing.Optional[builtins.str] = None,
        payload_size: typing.Optional[jsii.Number] = None,
        source_ip_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dont_fragment: Set the DF-bit in the IP-header. Only works with ipV4. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#dont_fragment SyntheticMonitoringCheck#dont_fragment}
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param payload_size: Payload size. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#payload_size SyntheticMonitoringCheck#payload_size}
        :param source_ip_address: Source IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        '''
        value = SyntheticMonitoringCheckSettingsPing(
            dont_fragment=dont_fragment,
            ip_version=ip_version,
            payload_size=payload_size,
            source_ip_address=source_ip_address,
        )

        return typing.cast(None, jsii.invoke(self, "putPing", [value]))

    @jsii.member(jsii_name="putTcp")
    def put_tcp(
        self,
        *,
        ip_version: typing.Optional[builtins.str] = None,
        query_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsTcpQueryResponse", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_ip_address: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_config: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsTcpTlsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param query_response: query_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#query_response SyntheticMonitoringCheck#query_response}
        :param source_ip_address: Source IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        :param tls: Whether or not TLS is used when the connection is initiated. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls SyntheticMonitoringCheck#tls}
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls_config SyntheticMonitoringCheck#tls_config}
        '''
        value = SyntheticMonitoringCheckSettingsTcp(
            ip_version=ip_version,
            query_response=query_response,
            source_ip_address=source_ip_address,
            tls=tls,
            tls_config=tls_config,
        )

        return typing.cast(None, jsii.invoke(self, "putTcp", [value]))

    @jsii.member(jsii_name="putTraceroute")
    def put_traceroute(
        self,
        *,
        max_hops: typing.Optional[jsii.Number] = None,
        max_unknown_hops: typing.Optional[jsii.Number] = None,
        ptr_lookup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param max_hops: Maximum TTL for the trace Defaults to ``64``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#max_hops SyntheticMonitoringCheck#max_hops}
        :param max_unknown_hops: Maximum number of hosts to travers that give no response Defaults to ``15``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#max_unknown_hops SyntheticMonitoringCheck#max_unknown_hops}
        :param ptr_lookup: Reverse lookup hostnames from IP addresses Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ptr_lookup SyntheticMonitoringCheck#ptr_lookup}
        '''
        value = SyntheticMonitoringCheckSettingsTraceroute(
            max_hops=max_hops, max_unknown_hops=max_unknown_hops, ptr_lookup=ptr_lookup
        )

        return typing.cast(None, jsii.invoke(self, "putTraceroute", [value]))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetHttp")
    def reset_http(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttp", []))

    @jsii.member(jsii_name="resetPing")
    def reset_ping(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPing", []))

    @jsii.member(jsii_name="resetTcp")
    def reset_tcp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTcp", []))

    @jsii.member(jsii_name="resetTraceroute")
    def reset_traceroute(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTraceroute", []))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> SyntheticMonitoringCheckSettingsDnsOutputReference:
        return typing.cast(SyntheticMonitoringCheckSettingsDnsOutputReference, jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="http")
    def http(self) -> SyntheticMonitoringCheckSettingsHttpOutputReference:
        return typing.cast(SyntheticMonitoringCheckSettingsHttpOutputReference, jsii.get(self, "http"))

    @builtins.property
    @jsii.member(jsii_name="ping")
    def ping(self) -> "SyntheticMonitoringCheckSettingsPingOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsPingOutputReference", jsii.get(self, "ping"))

    @builtins.property
    @jsii.member(jsii_name="tcp")
    def tcp(self) -> "SyntheticMonitoringCheckSettingsTcpOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsTcpOutputReference", jsii.get(self, "tcp"))

    @builtins.property
    @jsii.member(jsii_name="traceroute")
    def traceroute(self) -> "SyntheticMonitoringCheckSettingsTracerouteOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsTracerouteOutputReference", jsii.get(self, "traceroute"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[SyntheticMonitoringCheckSettingsDns]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsDns], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="httpInput")
    def http_input(self) -> typing.Optional[SyntheticMonitoringCheckSettingsHttp]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsHttp], jsii.get(self, "httpInput"))

    @builtins.property
    @jsii.member(jsii_name="pingInput")
    def ping_input(self) -> typing.Optional["SyntheticMonitoringCheckSettingsPing"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsPing"], jsii.get(self, "pingInput"))

    @builtins.property
    @jsii.member(jsii_name="tcpInput")
    def tcp_input(self) -> typing.Optional["SyntheticMonitoringCheckSettingsTcp"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsTcp"], jsii.get(self, "tcpInput"))

    @builtins.property
    @jsii.member(jsii_name="tracerouteInput")
    def traceroute_input(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsTraceroute"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsTraceroute"], jsii.get(self, "tracerouteInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticMonitoringCheckSettings]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ade6d981f314607daf98229a621a1e60adf7637ae2f1aebf0be3f511c69e9193)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsPing",
    jsii_struct_bases=[],
    name_mapping={
        "dont_fragment": "dontFragment",
        "ip_version": "ipVersion",
        "payload_size": "payloadSize",
        "source_ip_address": "sourceIpAddress",
    },
)
class SyntheticMonitoringCheckSettingsPing:
    def __init__(
        self,
        *,
        dont_fragment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        ip_version: typing.Optional[builtins.str] = None,
        payload_size: typing.Optional[jsii.Number] = None,
        source_ip_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dont_fragment: Set the DF-bit in the IP-header. Only works with ipV4. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#dont_fragment SyntheticMonitoringCheck#dont_fragment}
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param payload_size: Payload size. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#payload_size SyntheticMonitoringCheck#payload_size}
        :param source_ip_address: Source IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69a32f611e8a46139587159764f83970877c42a4eddb8ed46b18e530bec20ad8)
            check_type(argname="argument dont_fragment", value=dont_fragment, expected_type=type_hints["dont_fragment"])
            check_type(argname="argument ip_version", value=ip_version, expected_type=type_hints["ip_version"])
            check_type(argname="argument payload_size", value=payload_size, expected_type=type_hints["payload_size"])
            check_type(argname="argument source_ip_address", value=source_ip_address, expected_type=type_hints["source_ip_address"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dont_fragment is not None:
            self._values["dont_fragment"] = dont_fragment
        if ip_version is not None:
            self._values["ip_version"] = ip_version
        if payload_size is not None:
            self._values["payload_size"] = payload_size
        if source_ip_address is not None:
            self._values["source_ip_address"] = source_ip_address

    @builtins.property
    def dont_fragment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set the DF-bit in the IP-header. Only works with ipV4. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#dont_fragment SyntheticMonitoringCheck#dont_fragment}
        '''
        result = self._values.get("dont_fragment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def ip_version(self) -> typing.Optional[builtins.str]:
        '''Options are ``V4``, ``V6``, ``Any``.

        Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        '''
        result = self._values.get("ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_size(self) -> typing.Optional[jsii.Number]:
        '''Payload size. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#payload_size SyntheticMonitoringCheck#payload_size}
        '''
        result = self._values.get("payload_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_ip_address(self) -> typing.Optional[builtins.str]:
        '''Source IP address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        '''
        result = self._values.get("source_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsPing(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsPingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsPingOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec8cfea7345fde2b5fa4d6899b4c8de1dc82b90a7cbc82b2df71e6c262ad6509)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDontFragment")
    def reset_dont_fragment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDontFragment", []))

    @jsii.member(jsii_name="resetIpVersion")
    def reset_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersion", []))

    @jsii.member(jsii_name="resetPayloadSize")
    def reset_payload_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPayloadSize", []))

    @jsii.member(jsii_name="resetSourceIpAddress")
    def reset_source_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpAddress", []))

    @builtins.property
    @jsii.member(jsii_name="dontFragmentInput")
    def dont_fragment_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "dontFragmentInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionInput")
    def ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="payloadSizeInput")
    def payload_size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "payloadSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpAddressInput")
    def source_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="dontFragment")
    def dont_fragment(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "dontFragment"))

    @dont_fragment.setter
    def dont_fragment(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6be7990cf80e9e94d4e19e556d0f81ed853c6603836b8edaae328287c6893e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dontFragment", value)

    @builtins.property
    @jsii.member(jsii_name="ipVersion")
    def ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipVersion"))

    @ip_version.setter
    def ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__863eab52c308c9a56e5c737edaa6ed55c559c926665218950df3a113736b499f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersion", value)

    @builtins.property
    @jsii.member(jsii_name="payloadSize")
    def payload_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "payloadSize"))

    @payload_size.setter
    def payload_size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba129925906449bf153d9e50d4dbc1c31008f1756c540fbf58782244c377a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadSize", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpAddress")
    def source_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIpAddress"))

    @source_ip_address.setter
    def source_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0da3526c85d1b818565b41449feabe41b8604ae85cde403608f901d6b8e232)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticMonitoringCheckSettingsPing]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsPing], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsPing],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c554e0b04db714461c7d3f594be7c7c5537aa5d6380d0a8a1d6cedca249020e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcp",
    jsii_struct_bases=[],
    name_mapping={
        "ip_version": "ipVersion",
        "query_response": "queryResponse",
        "source_ip_address": "sourceIpAddress",
        "tls": "tls",
        "tls_config": "tlsConfig",
    },
)
class SyntheticMonitoringCheckSettingsTcp:
    def __init__(
        self,
        *,
        ip_version: typing.Optional[builtins.str] = None,
        query_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsTcpQueryResponse", typing.Dict[builtins.str, typing.Any]]]]] = None,
        source_ip_address: typing.Optional[builtins.str] = None,
        tls: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_config: typing.Optional[typing.Union["SyntheticMonitoringCheckSettingsTcpTlsConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ip_version: Options are ``V4``, ``V6``, ``Any``. Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        :param query_response: query_response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#query_response SyntheticMonitoringCheck#query_response}
        :param source_ip_address: Source IP address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        :param tls: Whether or not TLS is used when the connection is initiated. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls SyntheticMonitoringCheck#tls}
        :param tls_config: tls_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls_config SyntheticMonitoringCheck#tls_config}
        '''
        if isinstance(tls_config, dict):
            tls_config = SyntheticMonitoringCheckSettingsTcpTlsConfig(**tls_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f538630f0232198649efb0a4cc7958357233646ddbb413ba732cf8b8dccb2f3d)
            check_type(argname="argument ip_version", value=ip_version, expected_type=type_hints["ip_version"])
            check_type(argname="argument query_response", value=query_response, expected_type=type_hints["query_response"])
            check_type(argname="argument source_ip_address", value=source_ip_address, expected_type=type_hints["source_ip_address"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip_version is not None:
            self._values["ip_version"] = ip_version
        if query_response is not None:
            self._values["query_response"] = query_response
        if source_ip_address is not None:
            self._values["source_ip_address"] = source_ip_address
        if tls is not None:
            self._values["tls"] = tls
        if tls_config is not None:
            self._values["tls_config"] = tls_config

    @builtins.property
    def ip_version(self) -> typing.Optional[builtins.str]:
        '''Options are ``V4``, ``V6``, ``Any``.

        Specifies whether the corresponding check will be performed using IPv4 or IPv6. The ``Any`` value indicates that IPv6 should be used, falling back to IPv4 if that's not available. Defaults to ``V4``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ip_version SyntheticMonitoringCheck#ip_version}
        '''
        result = self._values.get("ip_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_response(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsTcpQueryResponse"]]]:
        '''query_response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#query_response SyntheticMonitoringCheck#query_response}
        '''
        result = self._values.get("query_response")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsTcpQueryResponse"]]], result)

    @builtins.property
    def source_ip_address(self) -> typing.Optional[builtins.str]:
        '''Source IP address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#source_ip_address SyntheticMonitoringCheck#source_ip_address}
        '''
        result = self._values.get("source_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not TLS is used when the connection is initiated. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls SyntheticMonitoringCheck#tls}
        '''
        result = self._values.get("tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_config(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsTcpTlsConfig"]:
        '''tls_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#tls_config SyntheticMonitoringCheck#tls_config}
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsTcpTlsConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsTcp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsTcpOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcpOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9895d29409ece683d99e64d9c86df02b49e1603c59d01d433f1e3530ed8bbac6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putQueryResponse")
    def put_query_response(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SyntheticMonitoringCheckSettingsTcpQueryResponse", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7f2be5250f8ecc7ee28ab0ca790e3b8c99de1f166a5420db552b04420967c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putQueryResponse", [value]))

    @jsii.member(jsii_name="putTlsConfig")
    def put_tls_config(
        self,
        *,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_cert: CA certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ca_cert SyntheticMonitoringCheck#ca_cert}
        :param client_cert: Client certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_cert SyntheticMonitoringCheck#client_cert}
        :param client_key: Client key in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_key SyntheticMonitoringCheck#client_key}
        :param insecure_skip_verify: Disable target certificate validation. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#insecure_skip_verify SyntheticMonitoringCheck#insecure_skip_verify}
        :param server_name: Used to verify the hostname for the targets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server_name SyntheticMonitoringCheck#server_name}
        '''
        value = SyntheticMonitoringCheckSettingsTcpTlsConfig(
            ca_cert=ca_cert,
            client_cert=client_cert,
            client_key=client_key,
            insecure_skip_verify=insecure_skip_verify,
            server_name=server_name,
        )

        return typing.cast(None, jsii.invoke(self, "putTlsConfig", [value]))

    @jsii.member(jsii_name="resetIpVersion")
    def reset_ip_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpVersion", []))

    @jsii.member(jsii_name="resetQueryResponse")
    def reset_query_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryResponse", []))

    @jsii.member(jsii_name="resetSourceIpAddress")
    def reset_source_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceIpAddress", []))

    @jsii.member(jsii_name="resetTls")
    def reset_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTls", []))

    @jsii.member(jsii_name="resetTlsConfig")
    def reset_tls_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsConfig", []))

    @builtins.property
    @jsii.member(jsii_name="queryResponse")
    def query_response(self) -> "SyntheticMonitoringCheckSettingsTcpQueryResponseList":
        return typing.cast("SyntheticMonitoringCheckSettingsTcpQueryResponseList", jsii.get(self, "queryResponse"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfig")
    def tls_config(
        self,
    ) -> "SyntheticMonitoringCheckSettingsTcpTlsConfigOutputReference":
        return typing.cast("SyntheticMonitoringCheckSettingsTcpTlsConfigOutputReference", jsii.get(self, "tlsConfig"))

    @builtins.property
    @jsii.member(jsii_name="ipVersionInput")
    def ip_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="queryResponseInput")
    def query_response_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsTcpQueryResponse"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SyntheticMonitoringCheckSettingsTcpQueryResponse"]]], jsii.get(self, "queryResponseInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceIpAddressInput")
    def source_ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceIpAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfigInput")
    def tls_config_input(
        self,
    ) -> typing.Optional["SyntheticMonitoringCheckSettingsTcpTlsConfig"]:
        return typing.cast(typing.Optional["SyntheticMonitoringCheckSettingsTcpTlsConfig"], jsii.get(self, "tlsConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipVersion")
    def ip_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipVersion"))

    @ip_version.setter
    def ip_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab79730adbd6ab517bd53f06eafff9f33914ccb473b9a4c21eed9bb6c821110)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipVersion", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIpAddress")
    def source_ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceIpAddress"))

    @source_ip_address.setter
    def source_ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f354274b6531a337913223b5ff8593a7b956a67101af606b018c1855b77e5ef3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tls"))

    @tls.setter
    def tls(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a0e953c9ff96c96c9d9d9ba78c13534ec4f14f1d4d3941d71e91fae24d6168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tls", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SyntheticMonitoringCheckSettingsTcp]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsTcp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsTcp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c293ebd634f6062711ef7df81653854074b570f85356e36612f7e843b7194289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcpQueryResponse",
    jsii_struct_bases=[],
    name_mapping={"expect": "expect", "send": "send", "start_tls": "startTls"},
)
class SyntheticMonitoringCheckSettingsTcpQueryResponse:
    def __init__(
        self,
        *,
        expect: builtins.str,
        send: builtins.str,
        start_tls: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param expect: Response to expect. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#expect SyntheticMonitoringCheck#expect}
        :param send: Data to send. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#send SyntheticMonitoringCheck#send}
        :param start_tls: Upgrade TCP connection to TLS. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#start_tls SyntheticMonitoringCheck#start_tls}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cefadf3e366282a19d4434edd393710edc1e9a5b52c1330dffe0f98d1434380a)
            check_type(argname="argument expect", value=expect, expected_type=type_hints["expect"])
            check_type(argname="argument send", value=send, expected_type=type_hints["send"])
            check_type(argname="argument start_tls", value=start_tls, expected_type=type_hints["start_tls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expect": expect,
            "send": send,
        }
        if start_tls is not None:
            self._values["start_tls"] = start_tls

    @builtins.property
    def expect(self) -> builtins.str:
        '''Response to expect.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#expect SyntheticMonitoringCheck#expect}
        '''
        result = self._values.get("expect")
        assert result is not None, "Required property 'expect' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def send(self) -> builtins.str:
        '''Data to send.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#send SyntheticMonitoringCheck#send}
        '''
        result = self._values.get("send")
        assert result is not None, "Required property 'send' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_tls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Upgrade TCP connection to TLS. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#start_tls SyntheticMonitoringCheck#start_tls}
        '''
        result = self._values.get("start_tls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsTcpQueryResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsTcpQueryResponseList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcpQueryResponseList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882b595fd27199b68287ef4ad12442cd163b1054e8b774a4c05edfb08e827f21)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SyntheticMonitoringCheckSettingsTcpQueryResponseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d90b46e7ba322767805424073e178ec87f5aee4bb6a3f385482710b98609b1b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SyntheticMonitoringCheckSettingsTcpQueryResponseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8efe641dc677f2ae13da496796bd5eb63b259a16522cfd875a9407e80dd8218c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df8ed70d6742f51a1139b1781f6788ce000a82582089a8fa6f37239625c40e58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ef68f84fedad6733e7f4d80e0c8639c0401beb51a88fc747780a9a2a0a7d023)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsTcpQueryResponse]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsTcpQueryResponse]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsTcpQueryResponse]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d8f11e3ddea06c41d4125f269d1f7a204b1ec2c2f370c02c60ac5aeb267e3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class SyntheticMonitoringCheckSettingsTcpQueryResponseOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcpQueryResponseOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f6fe281cbcecc837601d5aa0391f7c18de21a89ade21f73beefb6349630daa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStartTls")
    def reset_start_tls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTls", []))

    @builtins.property
    @jsii.member(jsii_name="expectInput")
    def expect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expectInput"))

    @builtins.property
    @jsii.member(jsii_name="sendInput")
    def send_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sendInput"))

    @builtins.property
    @jsii.member(jsii_name="startTlsInput")
    def start_tls_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "startTlsInput"))

    @builtins.property
    @jsii.member(jsii_name="expect")
    def expect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expect"))

    @expect.setter
    def expect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f6d6976df1f9226867f3dd565c3b8a9364aafca09cf8ea12aa90489583e1d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expect", value)

    @builtins.property
    @jsii.member(jsii_name="send")
    def send(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "send"))

    @send.setter
    def send(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8508acff10558f6108cf35d01f78a39c7e129a4768f9ae79ac03cbe368748432)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "send", value)

    @builtins.property
    @jsii.member(jsii_name="startTls")
    def start_tls(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "startTls"))

    @start_tls.setter
    def start_tls(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738ffcc1b259eddbcb9c8abe6d74da9efc62f1faa72423eb011db92e1117baad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTls", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTcpQueryResponse, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTcpQueryResponse, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTcpQueryResponse, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8054cb3db823369c879fb8f0a255e01f7a4b030d6b9ef5dd1f269f1473767c6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcpTlsConfig",
    jsii_struct_bases=[],
    name_mapping={
        "ca_cert": "caCert",
        "client_cert": "clientCert",
        "client_key": "clientKey",
        "insecure_skip_verify": "insecureSkipVerify",
        "server_name": "serverName",
    },
)
class SyntheticMonitoringCheckSettingsTcpTlsConfig:
    def __init__(
        self,
        *,
        ca_cert: typing.Optional[builtins.str] = None,
        client_cert: typing.Optional[builtins.str] = None,
        client_key: typing.Optional[builtins.str] = None,
        insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        server_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ca_cert: CA certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ca_cert SyntheticMonitoringCheck#ca_cert}
        :param client_cert: Client certificate in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_cert SyntheticMonitoringCheck#client_cert}
        :param client_key: Client key in PEM format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_key SyntheticMonitoringCheck#client_key}
        :param insecure_skip_verify: Disable target certificate validation. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#insecure_skip_verify SyntheticMonitoringCheck#insecure_skip_verify}
        :param server_name: Used to verify the hostname for the targets. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server_name SyntheticMonitoringCheck#server_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6644a847efe32deb175793465d0063d2aa65524226fda4b9ece3bc48bb352494)
            check_type(argname="argument ca_cert", value=ca_cert, expected_type=type_hints["ca_cert"])
            check_type(argname="argument client_cert", value=client_cert, expected_type=type_hints["client_cert"])
            check_type(argname="argument client_key", value=client_key, expected_type=type_hints["client_key"])
            check_type(argname="argument insecure_skip_verify", value=insecure_skip_verify, expected_type=type_hints["insecure_skip_verify"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ca_cert is not None:
            self._values["ca_cert"] = ca_cert
        if client_cert is not None:
            self._values["client_cert"] = client_cert
        if client_key is not None:
            self._values["client_key"] = client_key
        if insecure_skip_verify is not None:
            self._values["insecure_skip_verify"] = insecure_skip_verify
        if server_name is not None:
            self._values["server_name"] = server_name

    @builtins.property
    def ca_cert(self) -> typing.Optional[builtins.str]:
        '''CA certificate in PEM format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ca_cert SyntheticMonitoringCheck#ca_cert}
        '''
        result = self._values.get("ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_cert(self) -> typing.Optional[builtins.str]:
        '''Client certificate in PEM format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_cert SyntheticMonitoringCheck#client_cert}
        '''
        result = self._values.get("client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_key(self) -> typing.Optional[builtins.str]:
        '''Client key in PEM format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#client_key SyntheticMonitoringCheck#client_key}
        '''
        result = self._values.get("client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def insecure_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Disable target certificate validation. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#insecure_skip_verify SyntheticMonitoringCheck#insecure_skip_verify}
        '''
        result = self._values.get("insecure_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''Used to verify the hostname for the targets.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#server_name SyntheticMonitoringCheck#server_name}
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsTcpTlsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsTcpTlsConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTcpTlsConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22259bfcc28bccd512bfc9fa03cd8e885f868e1b6c557924eed7588d936570b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCaCert")
    def reset_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaCert", []))

    @jsii.member(jsii_name="resetClientCert")
    def reset_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientCert", []))

    @jsii.member(jsii_name="resetClientKey")
    def reset_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientKey", []))

    @jsii.member(jsii_name="resetInsecureSkipVerify")
    def reset_insecure_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInsecureSkipVerify", []))

    @jsii.member(jsii_name="resetServerName")
    def reset_server_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerName", []))

    @builtins.property
    @jsii.member(jsii_name="caCertInput")
    def ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "caCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientCertInput")
    def client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="clientKeyInput")
    def client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerifyInput")
    def insecure_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "insecureSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverNameInput")
    def server_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverNameInput"))

    @builtins.property
    @jsii.member(jsii_name="caCert")
    def ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caCert"))

    @ca_cert.setter
    def ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__270f31a77048048465325f5efd4e711e8e3fd908a7d962ad9ed67a87b9d33f3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientCert")
    def client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientCert"))

    @client_cert.setter
    def client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d707000b31de89194c994bf0e1bf21efe71372803df8ba0ad77a625467c602)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCert", value)

    @builtins.property
    @jsii.member(jsii_name="clientKey")
    def client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientKey"))

    @client_key.setter
    def client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3778212e587936b48347e4bcc2029fdd16d4d4ddc87f6ddcd5baf4df74afb0a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientKey", value)

    @builtins.property
    @jsii.member(jsii_name="insecureSkipVerify")
    def insecure_skip_verify(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "insecureSkipVerify"))

    @insecure_skip_verify.setter
    def insecure_skip_verify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93240b1dbedbd0980b5018d52c6ffa5136e9c18fc111c3ff051c50c73a68b12a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insecureSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84708d6779bb839485490cc5d6d16dab4861e43ff229ff302a24d1a5bd343854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsTcpTlsConfig]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsTcpTlsConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsTcpTlsConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979cbc7c9963f8524c4952631bf48e150027c7e9c87df7ba147a665847391592)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTraceroute",
    jsii_struct_bases=[],
    name_mapping={
        "max_hops": "maxHops",
        "max_unknown_hops": "maxUnknownHops",
        "ptr_lookup": "ptrLookup",
    },
)
class SyntheticMonitoringCheckSettingsTraceroute:
    def __init__(
        self,
        *,
        max_hops: typing.Optional[jsii.Number] = None,
        max_unknown_hops: typing.Optional[jsii.Number] = None,
        ptr_lookup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param max_hops: Maximum TTL for the trace Defaults to ``64``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#max_hops SyntheticMonitoringCheck#max_hops}
        :param max_unknown_hops: Maximum number of hosts to travers that give no response Defaults to ``15``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#max_unknown_hops SyntheticMonitoringCheck#max_unknown_hops}
        :param ptr_lookup: Reverse lookup hostnames from IP addresses Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ptr_lookup SyntheticMonitoringCheck#ptr_lookup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a5b41555c1b6a40b63b44f7ef31f2616f1f5eb25cb8492d729efb47b2efd934)
            check_type(argname="argument max_hops", value=max_hops, expected_type=type_hints["max_hops"])
            check_type(argname="argument max_unknown_hops", value=max_unknown_hops, expected_type=type_hints["max_unknown_hops"])
            check_type(argname="argument ptr_lookup", value=ptr_lookup, expected_type=type_hints["ptr_lookup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_hops is not None:
            self._values["max_hops"] = max_hops
        if max_unknown_hops is not None:
            self._values["max_unknown_hops"] = max_unknown_hops
        if ptr_lookup is not None:
            self._values["ptr_lookup"] = ptr_lookup

    @builtins.property
    def max_hops(self) -> typing.Optional[jsii.Number]:
        '''Maximum TTL for the trace Defaults to ``64``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#max_hops SyntheticMonitoringCheck#max_hops}
        '''
        result = self._values.get("max_hops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_unknown_hops(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of hosts to travers that give no response Defaults to ``15``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#max_unknown_hops SyntheticMonitoringCheck#max_unknown_hops}
        '''
        result = self._values.get("max_unknown_hops")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ptr_lookup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Reverse lookup hostnames from IP addresses Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/synthetic_monitoring_check#ptr_lookup SyntheticMonitoringCheck#ptr_lookup}
        '''
        result = self._values.get("ptr_lookup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticMonitoringCheckSettingsTraceroute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SyntheticMonitoringCheckSettingsTracerouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.syntheticMonitoringCheck.SyntheticMonitoringCheckSettingsTracerouteOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fda8f489b19dbc3c15d02ec5c8eda0f3e8beaf1a09f5e67d7401b136621cd5e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxHops")
    def reset_max_hops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHops", []))

    @jsii.member(jsii_name="resetMaxUnknownHops")
    def reset_max_unknown_hops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxUnknownHops", []))

    @jsii.member(jsii_name="resetPtrLookup")
    def reset_ptr_lookup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPtrLookup", []))

    @builtins.property
    @jsii.member(jsii_name="maxHopsInput")
    def max_hops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxHopsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxUnknownHopsInput")
    def max_unknown_hops_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxUnknownHopsInput"))

    @builtins.property
    @jsii.member(jsii_name="ptrLookupInput")
    def ptr_lookup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "ptrLookupInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHops")
    def max_hops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxHops"))

    @max_hops.setter
    def max_hops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__074ddbb14c4c84288d6a16f78d0e33d6f0a9c49d157f2f78d506097c98125dc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHops", value)

    @builtins.property
    @jsii.member(jsii_name="maxUnknownHops")
    def max_unknown_hops(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxUnknownHops"))

    @max_unknown_hops.setter
    def max_unknown_hops(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aadb20a5d26097aa23daa1adb5dad376cd421dbd83ffa0ca98e8fc4f58f3eafb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnknownHops", value)

    @builtins.property
    @jsii.member(jsii_name="ptrLookup")
    def ptr_lookup(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "ptrLookup"))

    @ptr_lookup.setter
    def ptr_lookup(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64d37d895becbdcd166164823db3eb3d092822810c8ace58102444ff59e0a245)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ptrLookup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SyntheticMonitoringCheckSettingsTraceroute]:
        return typing.cast(typing.Optional[SyntheticMonitoringCheckSettingsTraceroute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SyntheticMonitoringCheckSettingsTraceroute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a5e1b0a16f0e4ff9511717e296a17254b66acc6e264e2448d57d75f5962173f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "SyntheticMonitoringCheck",
    "SyntheticMonitoringCheckConfig",
    "SyntheticMonitoringCheckSettings",
    "SyntheticMonitoringCheckSettingsDns",
    "SyntheticMonitoringCheckSettingsDnsOutputReference",
    "SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs",
    "SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsList",
    "SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrsOutputReference",
    "SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs",
    "SyntheticMonitoringCheckSettingsDnsValidateAnswerRrsOutputReference",
    "SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs",
    "SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrsOutputReference",
    "SyntheticMonitoringCheckSettingsHttp",
    "SyntheticMonitoringCheckSettingsHttpBasicAuth",
    "SyntheticMonitoringCheckSettingsHttpBasicAuthOutputReference",
    "SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp",
    "SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpList",
    "SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexpOutputReference",
    "SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp",
    "SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpList",
    "SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexpOutputReference",
    "SyntheticMonitoringCheckSettingsHttpOutputReference",
    "SyntheticMonitoringCheckSettingsHttpTlsConfig",
    "SyntheticMonitoringCheckSettingsHttpTlsConfigOutputReference",
    "SyntheticMonitoringCheckSettingsOutputReference",
    "SyntheticMonitoringCheckSettingsPing",
    "SyntheticMonitoringCheckSettingsPingOutputReference",
    "SyntheticMonitoringCheckSettingsTcp",
    "SyntheticMonitoringCheckSettingsTcpOutputReference",
    "SyntheticMonitoringCheckSettingsTcpQueryResponse",
    "SyntheticMonitoringCheckSettingsTcpQueryResponseList",
    "SyntheticMonitoringCheckSettingsTcpQueryResponseOutputReference",
    "SyntheticMonitoringCheckSettingsTcpTlsConfig",
    "SyntheticMonitoringCheckSettingsTcpTlsConfigOutputReference",
    "SyntheticMonitoringCheckSettingsTraceroute",
    "SyntheticMonitoringCheckSettingsTracerouteOutputReference",
]

publication.publish()

def _typecheckingstub__2ebee3c7ff13c7e643ed6e9d76209daa4a0f05c16db6079ba0ce3ea292c4cd2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    job: builtins.str,
    probes: typing.Sequence[jsii.Number],
    settings: typing.Union[SyntheticMonitoringCheckSettings, typing.Dict[builtins.str, typing.Any]],
    target: builtins.str,
    alert_sensitivity: typing.Optional[builtins.str] = None,
    basic_metrics_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    frequency: typing.Optional[jsii.Number] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__5c8ea96fc76f7fb683d8fb0ba8dd3da99080e9d5f080666b8980adbbc7b689f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aef57ddf6ca6ecd29d7b0f17d778b9d2828359a0cd28331e304ab2438343450(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df0a8841813d716eefe88f7c912a5606943320932c88cfde85425b67a6df389b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57fc609696d660c034738e6b079a03238683872077142e27dc47924eb8d2303(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bca432a75219a2c6123997061844b5a0259f0d1295f9f33344ee189f941bd0c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55be7c3737c47f216beb0908ede9799ace8677e0017a813b6e47dbf8356a7966(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38512ef7b10f2474c772c743631e41f2cbfedf10d4e65be034d02ef6b63df00b(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fef72cfca93b40ad77bc820a8f68b15ec74383bdacd3fb44bfeccaf307ce369(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d656bc798c79bb84054c5349e89b1499b752db1e57b82a450a4e75bdd724ca7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__119366c701453b2f9e2b6a2579f3060bf559778a9a09abc0543407cdb7f4668f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    job: builtins.str,
    probes: typing.Sequence[jsii.Number],
    settings: typing.Union[SyntheticMonitoringCheckSettings, typing.Dict[builtins.str, typing.Any]],
    target: builtins.str,
    alert_sensitivity: typing.Optional[builtins.str] = None,
    basic_metrics_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    frequency: typing.Optional[jsii.Number] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43490fa145b3e0a00395a98775fea012455ca2aec00a0a3931db8685090faa3(
    *,
    dns: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDns, typing.Dict[builtins.str, typing.Any]]] = None,
    http: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttp, typing.Dict[builtins.str, typing.Any]]] = None,
    ping: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsPing, typing.Dict[builtins.str, typing.Any]]] = None,
    tcp: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTcp, typing.Dict[builtins.str, typing.Any]]] = None,
    traceroute: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTraceroute, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad9f5efa1b5635a334f2cccf2072d11c51627d04bb2b4e128f15711fbc8f58b(
    *,
    ip_version: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    record_type: typing.Optional[builtins.str] = None,
    server: typing.Optional[builtins.str] = None,
    source_ip_address: typing.Optional[builtins.str] = None,
    validate_additional_rrs: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, typing.Dict[builtins.str, typing.Any]]]]] = None,
    validate_answer_rrs: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs, typing.Dict[builtins.str, typing.Any]]] = None,
    validate_authority_rrs: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs, typing.Dict[builtins.str, typing.Any]]] = None,
    valid_r_codes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0e22250033b2d7f5b9c61f0333373a6dac7685ff0a6b18df2264f43ff97fe0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a666d1f29f887e61758ae9e9f0c0beed465e537817d1d63db60041e48e157625(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ebf2f7410e80e7ecb62214f4fcd27225c1215afae145d7e1a2404fc0d3b1cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0aa2ffdefa339dde87fa484c592f4da58e26a60af354e3c9039ac3e11185a13(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3e48e8a348e3e8733685b195302ab29c88ca9119667e2b3d467c297ac07e4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a5b3cbc05d556233fb65499f1742cd722a55b575da428733b3f8af5b586ac03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1efeedeea309e8b533fd3fb4e11d83e4b0162788ec97f7b460fc6f8912f1a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19ea672783e1a86613de7dc34be5435ec1b13e06233ef9f8ffc439751de4669(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af6a15fff091a4b626272aace9a685ace1326fa78d4052d44a14588088a3d8e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95efb44d386c8be758ec0b0451e91bb72520e5a872fb4bdf99150d2f7a5bdc7f(
    value: typing.Optional[SyntheticMonitoringCheckSettingsDns],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c1b8a0909805b150e2dfbe8cc10e4a54fd4cc3d391ab21b70e9b18af026c15b(
    *,
    fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36273a7d35e714fcc53cfef1c3eb753cdeca8c1ba7fed50a428b9ac8a3ff77a6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f39aa8fe174b6d733bc8bf7f8611234dcdc638fadd0fdef327ce3d41d06fd94d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1edc22ec84c592350f5cfee7a73331c7cb820a3aa61d8b68677eb9a0517f40d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86241a8d3f8aa3c1313f15403e6c070972803917f710be782d459daa2ee6662a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e6d5704b165248745fb100493925fdd13efa14a44031286b9175007e279d21(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d67f7e065df8c421f83883e61692a525254de21aff9688b23ee4b43d98290b8a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5246356d9e63ff18893dee75af44bfc5dbf4f0fbc3bdb513cecfa318a225dce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1622eb8b522bf494e4112b96cc0b14f08c14044bfd0e3617b507793b3e0bc50f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37d2a65a9231b04fc2bdaf05d2991d044f401859bfd1a4b8e0f5d8aa7eeadce(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e719a88a8770df596922f1ad07eef39e85416b289fb6524392154c3e7b633eba(
    value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsDnsValidateAdditionalRrs, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37191c5e59d53df999a08d20949add90f8ecb93016c2f0ee8f3c6bea4a8946ff(
    *,
    fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd135bcb89c6b6c1e50e03515a80e99a8c7eef2f7f02830da4f5b5ca9d6168dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55214703a837d807a4cd44310fdca8160216a022abb761ee22834454c08ad7fc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c11454449bce72f9f73b90b142dfbce87ec8c8b78b4849ee59cea34ed4cc82(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b30ebd3f5cd9a68203c0c94be484594a8084bcfd04ad25b212ef7957d34d82(
    value: typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAnswerRrs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__518378517fcdb5ef5bb6ab75c0e2a193b24e34ed4331a44d68594e6ec3ca7bfa(
    *,
    fail_if_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    fail_if_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc63980fd9c89b7ef96e70a8d0be018c70af3c8064928fffc4671423b8605f51(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d008fab72d50219c4ef1006033c83ed006baab066ad504a13ffeb09e3b4831de(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a437bfca49bca0ec40f506d270bcca9336c01338a50ace1fa236da7d765202c8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0186af46149a1d663e8c516a8ebca45ad98962d7149a3157f43ff5a64bfda21c(
    value: typing.Optional[SyntheticMonitoringCheckSettingsDnsValidateAuthorityRrs],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bca66f386f132f6aea4ab3b6dc28f393da62c22a544e25dc6a377fd5435c64a(
    *,
    basic_auth: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpBasicAuth, typing.Dict[builtins.str, typing.Any]]] = None,
    bearer_token: typing.Optional[builtins.str] = None,
    body: typing.Optional[builtins.str] = None,
    cache_busting_query_param_name: typing.Optional[builtins.str] = None,
    fail_if_body_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    fail_if_body_not_matches_regexp: typing.Optional[typing.Sequence[builtins.str]] = None,
    fail_if_header_matches_regexp: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fail_if_header_not_matches_regexp: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fail_if_not_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    fail_if_ssl: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ip_version: typing.Optional[builtins.str] = None,
    method: typing.Optional[builtins.str] = None,
    no_follow_redirects: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    proxy_url: typing.Optional[builtins.str] = None,
    tls_config: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpTlsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    valid_http_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    valid_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b602512249b76a968bce3e6b6a2b5966c96e2bc531ea423850689223ab96f8d(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7f8ba59e669a9ec299b04027c7257fa8b411aaea33b29fe27790fcf29ec708(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdfbcfcda09e59aa787811a4ef2cf5cdacc3c904c8cf1dc7971a5cc9a2e6976f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9983fcd34ec6867b5c0b9b9f4dad28636568fbfa48f1fd7787c2fe83979a73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e7b14d9b78d5abf503a2bba340f063473d7d274b9d7538f2d8475eee40055c1(
    value: typing.Optional[SyntheticMonitoringCheckSettingsHttpBasicAuth],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60856e1fca1803d35307ea4b11d0ef73af13f2f38ba7ec474a23342310d28f5(
    *,
    header: builtins.str,
    regexp: builtins.str,
    allow_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6868c645088f71c5fd0605043b26f99d48a73dc6eef0bac0150d0a24a1ea9099(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c91a5bb7081e94652f80f9539fb7dc726773b7d7d8a095d25c53f4c1515020(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d4f2bfbb5aa5300838ecc7fb739e2ca0ac52e50204aafeee524257f69d5a2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbfbec3934b3a8f9c802399ed5d634f305e7285bf6874b904e97a3bf18d0f8fd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc85d783e89fc9f46d29056507e4e9c01d224fd1bd8c4ac1ff42415ab444e0ae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a77ec7fa797f94844818b4fa84d8ae8961def4774d8788d1e9ce60c4fb01ffe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6558fe2e22a28b05059a48a020f1e95182452c9cd892e69ac3b1557a9d3838b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a15e51086d792dbf490ebfa76184e4a88755adfecadbb38c59cf61c269d67a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1987ddac1a1fee776c032c1179fd1099d077af705b3d01a4f131880d2dd111e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dffe6ca14b9d62d654e45f72209606dce2de2480bdd3a614163c83a07de9ff4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f898f5ce9d8b99ed460c9056db17c58f9171406c87b868be8a420aec512109(
    value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19cec9ac9ec35c22a3049b74bf62dbea6f32a9ae5b8655bdf4ba3e4f14c46dd7(
    *,
    header: builtins.str,
    regexp: builtins.str,
    allow_missing: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d1009f69162d13c565f11b14605b7dea9e9c40abfc9186d3a53ade4f449efa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63cda3142c35c5d45cd3a8ca2161a7642d0cd47f28c6636b12456821fd3ac42(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e808796c5beb0b160eb7da38a89d82c3be19dca27dec49b35da693e7787cef0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e0d70b7d40e11ca9eaed9cba4fc93599c3bfb0df7a27210789f0112a364f435(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57730eef22644c2b642ccdd44a15cf9f5d1badbb7b9d2844eb0329ba66c07555(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__739cb39bd5f99260a261576066ccadbe6ef6334a6f674e5fe07f43623d294898(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234c6a647c0f9040ce9fdc2f405e60d83eac3d38543b846bb5edab0d4e7a7483(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70308ec6e060579f8050b2ba0e05a4df84d1a106faf4b9eac9f20e86236a9b8d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fddb1e56b13ce6a02d3d0b996a1dedb38430d8a0f0fd7b4a4ce1a67fccc182d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7e8198d1dca47bbc9d5a7dc71e32da930ee0ff24ee946da0f7333c87074e0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59599c6db6e47a3b581b74e0f406be6eea8126d181cd13ed7d03bb9fb5dba8ce(
    value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2d0fd066397aaf0e5049898219d818ce36521ba4ecc075d68ad4f354308db7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42e536307bef064c1b272f7b311ae8789df2cf540f8498f4b6ac993277ef50c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85fcfa0225fddb0bfbb8deb6f13aa3cb67256e4174b25c59f0afb43bc11b0f82(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsHttpFailIfHeaderNotMatchesRegexp, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__457285ce56940109585f6a8bd7b60b75478a3e4ea1d05f42582ffcde4ebd803f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ef5959cd4796c5070d26f4c676155b44480e64daa6b8df33f1889610fbcb51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e77c89f750c049782ce750b2623887a85e9984b8fcdae764ca25e0cf28d2e204(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30274d4092308afe2855022a8374417f8e324371dc43524bab849e99c44a78a7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5179e917a6606aaf97287d4e35b200b047070f7b7fa747a8c5462582f4b3a2c9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee926f14999b731558b1d482d0a80d8d17a1941211d41a34b89a5aa469786667(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5037ced20146194e6dd9d4c6cf456bcd620b71f4e23d8f16cc4606a69963462(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec188460a03612090940d2ac878bc596c03350d3db8498558c00045ccfff90d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec9ea35024ccbf003237d177756160579faafcc9e2320cf7dc388f08f57cb393(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7aad9ab4b5d5e6b713961781b82123661b61948aa01332318183b04f23f2d98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44501bb1439c93eb9923f2881b5e94efb753ce24cc03b60076e2d1e4993cb59f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba5a3c6cc8537c34fd04ecde12109e6f84591f7f541aacddf7a8dd4e282cd39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0676c9e121a337c45dd9bfe3f6be7a9cb9c0311512dd5c1fa94b7a2f7de5e1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5698d42b33b1947745462e879c8cdeeb83988a6e42afffc13b3ef7bdc39e3900(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__674ea93aef110699cc71c09a197a6d4f37d235ea4dc521d5bddaf23ecc0d17a9(
    value: typing.Optional[SyntheticMonitoringCheckSettingsHttp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f459460b7db4cba9705ac64a2a4bec298bbf5cae417e568dc112b073ebbe2b(
    *,
    ca_cert: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6c8da497cc082f0a6cbeab30ce4de5c8711ae510c892ab5488632a5ef3aeb9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5fe893c10e4bde15fa41c7fb0be6ed41d730a72311e92b385967a05b3c4bbf6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c1869c4b6ce7fa1db2f7ec5f357d32f7af342e4c650ce14cb4dbfd9bf80bb63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c82db1de01a6f9783a5644b327c416045e646b403411295b3f6c6867f26945(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4aa368d2401f86641516c8f23a69cc887798c73d36a767e7c43a5f893eb5c43(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__768e62d00b7ed26e5e1dc45f983c8c6d1a4fc32fe77ec338fda0b48569bc6816(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d6b7f93db482cdfe5aab8bc74c6e79f01168dd8691c0a0f54b12b032ff4178(
    value: typing.Optional[SyntheticMonitoringCheckSettingsHttpTlsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6681e817db10b8ebbace748326dbc6b9eee86f4cd462a5a948757f50c926ca90(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade6d981f314607daf98229a621a1e60adf7637ae2f1aebf0be3f511c69e9193(
    value: typing.Optional[SyntheticMonitoringCheckSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a32f611e8a46139587159764f83970877c42a4eddb8ed46b18e530bec20ad8(
    *,
    dont_fragment: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ip_version: typing.Optional[builtins.str] = None,
    payload_size: typing.Optional[jsii.Number] = None,
    source_ip_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8cfea7345fde2b5fa4d6899b4c8de1dc82b90a7cbc82b2df71e6c262ad6509(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6be7990cf80e9e94d4e19e556d0f81ed853c6603836b8edaae328287c6893e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__863eab52c308c9a56e5c737edaa6ed55c559c926665218950df3a113736b499f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba129925906449bf153d9e50d4dbc1c31008f1756c540fbf58782244c377a4b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0da3526c85d1b818565b41449feabe41b8604ae85cde403608f901d6b8e232(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c554e0b04db714461c7d3f594be7c7c5537aa5d6380d0a8a1d6cedca249020e(
    value: typing.Optional[SyntheticMonitoringCheckSettingsPing],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f538630f0232198649efb0a4cc7958357233646ddbb413ba732cf8b8dccb2f3d(
    *,
    ip_version: typing.Optional[builtins.str] = None,
    query_response: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsTcpQueryResponse, typing.Dict[builtins.str, typing.Any]]]]] = None,
    source_ip_address: typing.Optional[builtins.str] = None,
    tls: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_config: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTcpTlsConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9895d29409ece683d99e64d9c86df02b49e1603c59d01d433f1e3530ed8bbac6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f2be5250f8ecc7ee28ab0ca790e3b8c99de1f166a5420db552b04420967c53(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SyntheticMonitoringCheckSettingsTcpQueryResponse, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab79730adbd6ab517bd53f06eafff9f33914ccb473b9a4c21eed9bb6c821110(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f354274b6531a337913223b5ff8593a7b956a67101af606b018c1855b77e5ef3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a0e953c9ff96c96c9d9d9ba78c13534ec4f14f1d4d3941d71e91fae24d6168(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c293ebd634f6062711ef7df81653854074b570f85356e36612f7e843b7194289(
    value: typing.Optional[SyntheticMonitoringCheckSettingsTcp],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefadf3e366282a19d4434edd393710edc1e9a5b52c1330dffe0f98d1434380a(
    *,
    expect: builtins.str,
    send: builtins.str,
    start_tls: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882b595fd27199b68287ef4ad12442cd163b1054e8b774a4c05edfb08e827f21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d90b46e7ba322767805424073e178ec87f5aee4bb6a3f385482710b98609b1b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8efe641dc677f2ae13da496796bd5eb63b259a16522cfd875a9407e80dd8218c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8ed70d6742f51a1139b1781f6788ce000a82582089a8fa6f37239625c40e58(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef68f84fedad6733e7f4d80e0c8639c0401beb51a88fc747780a9a2a0a7d023(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d8f11e3ddea06c41d4125f269d1f7a204b1ec2c2f370c02c60ac5aeb267e3b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SyntheticMonitoringCheckSettingsTcpQueryResponse]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f6fe281cbcecc837601d5aa0391f7c18de21a89ade21f73beefb6349630daa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f6d6976df1f9226867f3dd565c3b8a9364aafca09cf8ea12aa90489583e1d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8508acff10558f6108cf35d01f78a39c7e129a4768f9ae79ac03cbe368748432(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738ffcc1b259eddbcb9c8abe6d74da9efc62f1faa72423eb011db92e1117baad(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8054cb3db823369c879fb8f0a255e01f7a4b030d6b9ef5dd1f269f1473767c6d(
    value: typing.Optional[typing.Union[SyntheticMonitoringCheckSettingsTcpQueryResponse, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6644a847efe32deb175793465d0063d2aa65524226fda4b9ece3bc48bb352494(
    *,
    ca_cert: typing.Optional[builtins.str] = None,
    client_cert: typing.Optional[builtins.str] = None,
    client_key: typing.Optional[builtins.str] = None,
    insecure_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    server_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22259bfcc28bccd512bfc9fa03cd8e885f868e1b6c557924eed7588d936570b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__270f31a77048048465325f5efd4e711e8e3fd908a7d962ad9ed67a87b9d33f3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d707000b31de89194c994bf0e1bf21efe71372803df8ba0ad77a625467c602(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3778212e587936b48347e4bcc2029fdd16d4d4ddc87f6ddcd5baf4df74afb0a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93240b1dbedbd0980b5018d52c6ffa5136e9c18fc111c3ff051c50c73a68b12a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84708d6779bb839485490cc5d6d16dab4861e43ff229ff302a24d1a5bd343854(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979cbc7c9963f8524c4952631bf48e150027c7e9c87df7ba147a665847391592(
    value: typing.Optional[SyntheticMonitoringCheckSettingsTcpTlsConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a5b41555c1b6a40b63b44f7ef31f2616f1f5eb25cb8492d729efb47b2efd934(
    *,
    max_hops: typing.Optional[jsii.Number] = None,
    max_unknown_hops: typing.Optional[jsii.Number] = None,
    ptr_lookup: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fda8f489b19dbc3c15d02ec5c8eda0f3e8beaf1a09f5e67d7401b136621cd5e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__074ddbb14c4c84288d6a16f78d0e33d6f0a9c49d157f2f78d506097c98125dc7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aadb20a5d26097aa23daa1adb5dad376cd421dbd83ffa0ca98e8fc4f58f3eafb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d37d895becbdcd166164823db3eb3d092822810c8ace58102444ff59e0a245(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a5e1b0a16f0e4ff9511717e296a17254b66acc6e264e2448d57d75f5962173f(
    value: typing.Optional[SyntheticMonitoringCheckSettingsTraceroute],
) -> None:
    """Type checking stubs"""
    pass
