'''
# `grafana_oncall_integration`

Refer to the Terraform Registory for docs: [`grafana_oncall_integration`](https://www.terraform.io/docs/providers/grafana/r/oncall_integration).
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


class OncallIntegration(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration grafana_oncall_integration}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        default_route: typing.Union["OncallIntegrationDefaultRoute", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        templates: typing.Optional[typing.Union["OncallIntegrationTemplates", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration grafana_oncall_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param default_route: default_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#default_route OncallIntegration#default_route}
        :param name: The name of the service integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#name OncallIntegration#name}
        :param type: The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#type OncallIntegration#type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#team_id OncallIntegration#team_id}
        :param templates: templates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#templates OncallIntegration#templates}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99cdc0f030e1df46edef831f72048d398b60edc0b545f0cf04446e2512548b37)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OncallIntegrationConfig(
            default_route=default_route,
            name=name,
            type=type,
            id=id,
            team_id=team_id,
            templates=templates,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDefaultRoute")
    def put_default_route(
        self,
        *,
        escalation_chain_id: typing.Optional[builtins.str] = None,
        msteams: typing.Optional[typing.Union["OncallIntegrationDefaultRouteMsteams", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["OncallIntegrationDefaultRouteSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        telegram: typing.Optional[typing.Union["OncallIntegrationDefaultRouteTelegram", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param escalation_chain_id: The ID of the escalation chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#escalation_chain_id OncallIntegration#escalation_chain_id}
        :param msteams: msteams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#msteams OncallIntegration#msteams}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#slack OncallIntegration#slack}
        :param telegram: telegram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#telegram OncallIntegration#telegram}
        '''
        value = OncallIntegrationDefaultRoute(
            escalation_chain_id=escalation_chain_id,
            msteams=msteams,
            slack=slack,
            telegram=telegram,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultRoute", [value]))

    @jsii.member(jsii_name="putTemplates")
    def put_templates(
        self,
        *,
        grouping_key: typing.Optional[builtins.str] = None,
        resolve_signal: typing.Optional[builtins.str] = None,
        slack: typing.Optional[typing.Union["OncallIntegrationTemplatesSlack", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grouping_key: Template for the key by which alerts are grouped. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#grouping_key OncallIntegration#grouping_key}
        :param resolve_signal: Template for sending a signal to resolve the Incident. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#resolve_signal OncallIntegration#resolve_signal}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#slack OncallIntegration#slack}
        '''
        value = OncallIntegrationTemplates(
            grouping_key=grouping_key, resolve_signal=resolve_signal, slack=slack
        )

        return typing.cast(None, jsii.invoke(self, "putTemplates", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetTemplates")
    def reset_templates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplates", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="defaultRoute")
    def default_route(self) -> "OncallIntegrationDefaultRouteOutputReference":
        return typing.cast("OncallIntegrationDefaultRouteOutputReference", jsii.get(self, "defaultRoute"))

    @builtins.property
    @jsii.member(jsii_name="link")
    def link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "link"))

    @builtins.property
    @jsii.member(jsii_name="templates")
    def templates(self) -> "OncallIntegrationTemplatesOutputReference":
        return typing.cast("OncallIntegrationTemplatesOutputReference", jsii.get(self, "templates"))

    @builtins.property
    @jsii.member(jsii_name="defaultRouteInput")
    def default_route_input(self) -> typing.Optional["OncallIntegrationDefaultRoute"]:
        return typing.cast(typing.Optional["OncallIntegrationDefaultRoute"], jsii.get(self, "defaultRouteInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="templatesInput")
    def templates_input(self) -> typing.Optional["OncallIntegrationTemplates"]:
        return typing.cast(typing.Optional["OncallIntegrationTemplates"], jsii.get(self, "templatesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22f32b4fe4015840a83a790e97a36390344111a929e0e110def35c6dd6d7f17a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac899570e3f9785542bede424720db986275941b2ef5669d37be601480aa1e0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d0ed0df1e39e5d6b0ad159c12beca46e029c0d15fac7fa911121fe98d447f61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4637079e365fa920254bab07b49c34e0f18ff1eb6eb1d2c21a0eb592e490db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "default_route": "defaultRoute",
        "name": "name",
        "type": "type",
        "id": "id",
        "team_id": "teamId",
        "templates": "templates",
    },
)
class OncallIntegrationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        default_route: typing.Union["OncallIntegrationDefaultRoute", typing.Dict[builtins.str, typing.Any]],
        name: builtins.str,
        type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        templates: typing.Optional[typing.Union["OncallIntegrationTemplates", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param default_route: default_route block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#default_route OncallIntegration#default_route}
        :param name: The name of the service integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#name OncallIntegration#name}
        :param type: The type of integration. Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#type OncallIntegration#type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#team_id OncallIntegration#team_id}
        :param templates: templates block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#templates OncallIntegration#templates}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_route, dict):
            default_route = OncallIntegrationDefaultRoute(**default_route)
        if isinstance(templates, dict):
            templates = OncallIntegrationTemplates(**templates)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70944b6a3530f1ad782265a73090579e0bb4bd65080d727da1ed18fae1746066)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument default_route", value=default_route, expected_type=type_hints["default_route"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument templates", value=templates, expected_type=type_hints["templates"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_route": default_route,
            "name": name,
            "type": type,
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
        if team_id is not None:
            self._values["team_id"] = team_id
        if templates is not None:
            self._values["templates"] = templates

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
    def default_route(self) -> "OncallIntegrationDefaultRoute":
        '''default_route block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#default_route OncallIntegration#default_route}
        '''
        result = self._values.get("default_route")
        assert result is not None, "Required property 'default_route' is missing"
        return typing.cast("OncallIntegrationDefaultRoute", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the service integration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#name OncallIntegration#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of integration.

        Can be grafana, grafana_alerting, webhook, alertmanager, kapacitor, fabric, newrelic, datadog, pagerduty, pingdom, elastalert, amazon_sns, curler, sentry, formatted_webhook, heartbeat, demo, manual, stackdriver, uptimerobot, sentry_platform, zabbix, prtg, slack_channel, inbound_email.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#type OncallIntegration#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the OnCall team.

        To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#team_id OncallIntegration#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def templates(self) -> typing.Optional["OncallIntegrationTemplates"]:
        '''templates block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#templates OncallIntegration#templates}
        '''
        result = self._values.get("templates")
        return typing.cast(typing.Optional["OncallIntegrationTemplates"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRoute",
    jsii_struct_bases=[],
    name_mapping={
        "escalation_chain_id": "escalationChainId",
        "msteams": "msteams",
        "slack": "slack",
        "telegram": "telegram",
    },
)
class OncallIntegrationDefaultRoute:
    def __init__(
        self,
        *,
        escalation_chain_id: typing.Optional[builtins.str] = None,
        msteams: typing.Optional[typing.Union["OncallIntegrationDefaultRouteMsteams", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["OncallIntegrationDefaultRouteSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        telegram: typing.Optional[typing.Union["OncallIntegrationDefaultRouteTelegram", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param escalation_chain_id: The ID of the escalation chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#escalation_chain_id OncallIntegration#escalation_chain_id}
        :param msteams: msteams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#msteams OncallIntegration#msteams}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#slack OncallIntegration#slack}
        :param telegram: telegram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#telegram OncallIntegration#telegram}
        '''
        if isinstance(msteams, dict):
            msteams = OncallIntegrationDefaultRouteMsteams(**msteams)
        if isinstance(slack, dict):
            slack = OncallIntegrationDefaultRouteSlack(**slack)
        if isinstance(telegram, dict):
            telegram = OncallIntegrationDefaultRouteTelegram(**telegram)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f6a38fdc93a0279c7256703785a0c88fc22e072a9b75f14827f9ada70bfe47)
            check_type(argname="argument escalation_chain_id", value=escalation_chain_id, expected_type=type_hints["escalation_chain_id"])
            check_type(argname="argument msteams", value=msteams, expected_type=type_hints["msteams"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument telegram", value=telegram, expected_type=type_hints["telegram"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if escalation_chain_id is not None:
            self._values["escalation_chain_id"] = escalation_chain_id
        if msteams is not None:
            self._values["msteams"] = msteams
        if slack is not None:
            self._values["slack"] = slack
        if telegram is not None:
            self._values["telegram"] = telegram

    @builtins.property
    def escalation_chain_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the escalation chain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#escalation_chain_id OncallIntegration#escalation_chain_id}
        '''
        result = self._values.get("escalation_chain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msteams(self) -> typing.Optional["OncallIntegrationDefaultRouteMsteams"]:
        '''msteams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#msteams OncallIntegration#msteams}
        '''
        result = self._values.get("msteams")
        return typing.cast(typing.Optional["OncallIntegrationDefaultRouteMsteams"], result)

    @builtins.property
    def slack(self) -> typing.Optional["OncallIntegrationDefaultRouteSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#slack OncallIntegration#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["OncallIntegrationDefaultRouteSlack"], result)

    @builtins.property
    def telegram(self) -> typing.Optional["OncallIntegrationDefaultRouteTelegram"]:
        '''telegram block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#telegram OncallIntegration#telegram}
        '''
        result = self._values.get("telegram")
        return typing.cast(typing.Optional["OncallIntegrationDefaultRouteTelegram"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallIntegrationDefaultRoute(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteMsteams",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "id": "id"},
)
class OncallIntegrationDefaultRouteMsteams:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in MS teams. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        :param id: MS teams channel id. Alerts will be directed to this channel in Microsoft teams. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66b730037525ac60023f242077725951f17013931216ec2914be3aa53551c102)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notification in MS teams. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''MS teams channel id. Alerts will be directed to this channel in Microsoft teams.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id}

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
        return "OncallIntegrationDefaultRouteMsteams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallIntegrationDefaultRouteMsteamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteMsteamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b09b93b48dbd25e4663b6e3953d3cc1c55cbb2d1c167b14748a25064f9af3d5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__0e98a1538d646320f6636920bf2ac2145d89cc4ce31f87d9474a6988f43bd2d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1195101d39a6217dc11879d0cf41e1f46031d75ce90d0aeb80ec4614cc8a2a7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallIntegrationDefaultRouteMsteams]:
        return typing.cast(typing.Optional[OncallIntegrationDefaultRouteMsteams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OncallIntegrationDefaultRouteMsteams],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b226af27718949bcad6adbf23b3269197fd6423cd7800f471454c2b3be0130)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class OncallIntegrationDefaultRouteOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7cae784056fdeca7eeb57520556590b6ac61305217a8c2ba2670ff4b295911f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMsteams")
    def put_msteams(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in MS teams. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        :param id: MS teams channel id. Alerts will be directed to this channel in Microsoft teams. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        value = OncallIntegrationDefaultRouteMsteams(enabled=enabled, id=id)

        return typing.cast(None, jsii.invoke(self, "putMsteams", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param channel_id: Slack channel id. Alerts will be directed to this channel in Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#channel_id OncallIntegration#channel_id}
        :param enabled: Enable notification in Slack. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        '''
        value = OncallIntegrationDefaultRouteSlack(
            channel_id=channel_id, enabled=enabled
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putTelegram")
    def put_telegram(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in Telegram. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        :param id: Telegram channel id. Alerts will be directed to this channel in Telegram. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        value = OncallIntegrationDefaultRouteTelegram(enabled=enabled, id=id)

        return typing.cast(None, jsii.invoke(self, "putTelegram", [value]))

    @jsii.member(jsii_name="resetEscalationChainId")
    def reset_escalation_chain_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEscalationChainId", []))

    @jsii.member(jsii_name="resetMsteams")
    def reset_msteams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsteams", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetTelegram")
    def reset_telegram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTelegram", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="msteams")
    def msteams(self) -> OncallIntegrationDefaultRouteMsteamsOutputReference:
        return typing.cast(OncallIntegrationDefaultRouteMsteamsOutputReference, jsii.get(self, "msteams"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "OncallIntegrationDefaultRouteSlackOutputReference":
        return typing.cast("OncallIntegrationDefaultRouteSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="telegram")
    def telegram(self) -> "OncallIntegrationDefaultRouteTelegramOutputReference":
        return typing.cast("OncallIntegrationDefaultRouteTelegramOutputReference", jsii.get(self, "telegram"))

    @builtins.property
    @jsii.member(jsii_name="escalationChainIdInput")
    def escalation_chain_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "escalationChainIdInput"))

    @builtins.property
    @jsii.member(jsii_name="msteamsInput")
    def msteams_input(self) -> typing.Optional[OncallIntegrationDefaultRouteMsteams]:
        return typing.cast(typing.Optional[OncallIntegrationDefaultRouteMsteams], jsii.get(self, "msteamsInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(self) -> typing.Optional["OncallIntegrationDefaultRouteSlack"]:
        return typing.cast(typing.Optional["OncallIntegrationDefaultRouteSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="telegramInput")
    def telegram_input(
        self,
    ) -> typing.Optional["OncallIntegrationDefaultRouteTelegram"]:
        return typing.cast(typing.Optional["OncallIntegrationDefaultRouteTelegram"], jsii.get(self, "telegramInput"))

    @builtins.property
    @jsii.member(jsii_name="escalationChainId")
    def escalation_chain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "escalationChainId"))

    @escalation_chain_id.setter
    def escalation_chain_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c3ab14e74a77ed8c07274a33d19d6db1ba9c4d5ce40616d80cc19bf26db799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "escalationChainId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallIntegrationDefaultRoute]:
        return typing.cast(typing.Optional[OncallIntegrationDefaultRoute], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OncallIntegrationDefaultRoute],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ac293e964789da9bb3648ca31c86b284e19ea514e6b50d730cd13c78b4f9cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteSlack",
    jsii_struct_bases=[],
    name_mapping={"channel_id": "channelId", "enabled": "enabled"},
)
class OncallIntegrationDefaultRouteSlack:
    def __init__(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param channel_id: Slack channel id. Alerts will be directed to this channel in Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#channel_id OncallIntegration#channel_id}
        :param enabled: Enable notification in Slack. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fa9022c4ae38b7b75b80bdac61d914580adb86dbf64afb5d92b39a4c1ddfb89)
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if channel_id is not None:
            self._values["channel_id"] = channel_id
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''Slack channel id. Alerts will be directed to this channel in Slack.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#channel_id OncallIntegration#channel_id}
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notification in Slack. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallIntegrationDefaultRouteSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallIntegrationDefaultRouteSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99ccf348d4c052eaabbd2859237fbd6df9776e30b03bf32ef92240c529ea6722)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChannelId")
    def reset_channel_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannelId", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="channelIdInput")
    def channel_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f31a47d146cdfe2cc8a6c6e6587c45fb0c8fdaa87c70b70c5521b4d7bf0a473)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelId", value)

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
            type_hints = typing.get_type_hints(_typecheckingstub__c09630ab942eaef1ad0de4a9bf774fc0031d64373bd8dd84f785ea854678255d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallIntegrationDefaultRouteSlack]:
        return typing.cast(typing.Optional[OncallIntegrationDefaultRouteSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OncallIntegrationDefaultRouteSlack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923e70d2f5cc690217d99fcf73ad985eab7d0e8972be2ba1df501a2ea830ca12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteTelegram",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "id": "id"},
)
class OncallIntegrationDefaultRouteTelegram:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in Telegram. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        :param id: Telegram channel id. Alerts will be directed to this channel in Telegram. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__906ec84830aecd08575d205f4e992fdc6c0e1cb4eee5d5a987a1827bb43df93e)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notification in Telegram. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#enabled OncallIntegration#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Telegram channel id. Alerts will be directed to this channel in Telegram.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#id OncallIntegration#id}

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
        return "OncallIntegrationDefaultRouteTelegram(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallIntegrationDefaultRouteTelegramOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegrationDefaultRouteTelegramOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b66038c1fb7ae957d2b6e4ceeaba494d54d331d2e0a8b82324db5010b6da873d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__33b841a6526a7fc60e48ffd3ed1c662ef4ffa259a00728ab26f4f0fbbfb84555)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae27457d2cdeb848164528b2c1ec58e2f803eba155d0c24cf0b2dfcde503c563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallIntegrationDefaultRouteTelegram]:
        return typing.cast(typing.Optional[OncallIntegrationDefaultRouteTelegram], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OncallIntegrationDefaultRouteTelegram],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367d19dd090707385a18ece71dd36618cef1532cdc6e7306cb526fb24a376213)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationTemplates",
    jsii_struct_bases=[],
    name_mapping={
        "grouping_key": "groupingKey",
        "resolve_signal": "resolveSignal",
        "slack": "slack",
    },
)
class OncallIntegrationTemplates:
    def __init__(
        self,
        *,
        grouping_key: typing.Optional[builtins.str] = None,
        resolve_signal: typing.Optional[builtins.str] = None,
        slack: typing.Optional[typing.Union["OncallIntegrationTemplatesSlack", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param grouping_key: Template for the key by which alerts are grouped. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#grouping_key OncallIntegration#grouping_key}
        :param resolve_signal: Template for sending a signal to resolve the Incident. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#resolve_signal OncallIntegration#resolve_signal}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#slack OncallIntegration#slack}
        '''
        if isinstance(slack, dict):
            slack = OncallIntegrationTemplatesSlack(**slack)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e62ad375af3d51a47a9b66cd48a244f1b81f1bbcfa6ef6bd41413abd74b06e53)
            check_type(argname="argument grouping_key", value=grouping_key, expected_type=type_hints["grouping_key"])
            check_type(argname="argument resolve_signal", value=resolve_signal, expected_type=type_hints["resolve_signal"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if grouping_key is not None:
            self._values["grouping_key"] = grouping_key
        if resolve_signal is not None:
            self._values["resolve_signal"] = resolve_signal
        if slack is not None:
            self._values["slack"] = slack

    @builtins.property
    def grouping_key(self) -> typing.Optional[builtins.str]:
        '''Template for the key by which alerts are grouped.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#grouping_key OncallIntegration#grouping_key}
        '''
        result = self._values.get("grouping_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolve_signal(self) -> typing.Optional[builtins.str]:
        '''Template for sending a signal to resolve the Incident.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#resolve_signal OncallIntegration#resolve_signal}
        '''
        result = self._values.get("resolve_signal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slack(self) -> typing.Optional["OncallIntegrationTemplatesSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#slack OncallIntegration#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["OncallIntegrationTemplatesSlack"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallIntegrationTemplates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallIntegrationTemplatesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegrationTemplatesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1eb8756a300974cdf2f851dd71a83de07217429bfdf7b40ecf051be9e8d0b5e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        *,
        image_url: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_url: Template for Alert image url. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#image_url OncallIntegration#image_url}
        :param message: Template for Alert message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#message OncallIntegration#message}
        :param title: Template for Alert title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#title OncallIntegration#title}
        '''
        value = OncallIntegrationTemplatesSlack(
            image_url=image_url, message=message, title=title
        )

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="resetGroupingKey")
    def reset_grouping_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupingKey", []))

    @jsii.member(jsii_name="resetResolveSignal")
    def reset_resolve_signal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolveSignal", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "OncallIntegrationTemplatesSlackOutputReference":
        return typing.cast("OncallIntegrationTemplatesSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="groupingKeyInput")
    def grouping_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupingKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolveSignalInput")
    def resolve_signal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolveSignalInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(self) -> typing.Optional["OncallIntegrationTemplatesSlack"]:
        return typing.cast(typing.Optional["OncallIntegrationTemplatesSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="groupingKey")
    def grouping_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupingKey"))

    @grouping_key.setter
    def grouping_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__365e63391c1015bcb2e595682c9aa76984a07da59982c25451882a1abcb1b4e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupingKey", value)

    @builtins.property
    @jsii.member(jsii_name="resolveSignal")
    def resolve_signal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolveSignal"))

    @resolve_signal.setter
    def resolve_signal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__254b72b0c0e2cda9728b4b7adb95749b1753cd748f18dca3a81f322850007a74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolveSignal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallIntegrationTemplates]:
        return typing.cast(typing.Optional[OncallIntegrationTemplates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OncallIntegrationTemplates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3808a8be681c6458aebebd1e25c75efb5a3d4816acebb2349676dda60638fd0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.oncallIntegration.OncallIntegrationTemplatesSlack",
    jsii_struct_bases=[],
    name_mapping={"image_url": "imageUrl", "message": "message", "title": "title"},
)
class OncallIntegrationTemplatesSlack:
    def __init__(
        self,
        *,
        image_url: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_url: Template for Alert image url. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#image_url OncallIntegration#image_url}
        :param message: Template for Alert message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#message OncallIntegration#message}
        :param title: Template for Alert title. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#title OncallIntegration#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faa329853e6ecebf8ae7f0a53240627c7463ef4ec8ad1f1aedcb6056098710b8)
            check_type(argname="argument image_url", value=image_url, expected_type=type_hints["image_url"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if image_url is not None:
            self._values["image_url"] = image_url
        if message is not None:
            self._values["message"] = message
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def image_url(self) -> typing.Optional[builtins.str]:
        '''Template for Alert image url.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#image_url OncallIntegration#image_url}
        '''
        result = self._values.get("image_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Template for Alert message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#message OncallIntegration#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Template for Alert title.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_integration#title OncallIntegration#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallIntegrationTemplatesSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallIntegrationTemplatesSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallIntegration.OncallIntegrationTemplatesSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76e4df8eb6d3a0ed2320bc52bc04d1fb8060d3b22895e4490196f19a57eec78d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetImageUrl")
    def reset_image_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageUrl", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="imageUrlInput")
    def image_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="imageUrl")
    def image_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageUrl"))

    @image_url.setter
    def image_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfc047bd49a299ba24ce400ef3791a72f0be91f8a870ed8f8f373734ef381ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUrl", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d076bc9814d4646ff86080ac83cc3ebfbeb615c14983028b9a86cbfb87dc8fdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f3f4f20f364fa8c7f724cbe9ce4bc33384d89e87d3ff2d15a3c474a9100c669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallIntegrationTemplatesSlack]:
        return typing.cast(typing.Optional[OncallIntegrationTemplatesSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[OncallIntegrationTemplatesSlack],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b64fb3c80cdc1471b0a937a391f1cadc2e6372539540234cbafbcb496fe83856)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OncallIntegration",
    "OncallIntegrationConfig",
    "OncallIntegrationDefaultRoute",
    "OncallIntegrationDefaultRouteMsteams",
    "OncallIntegrationDefaultRouteMsteamsOutputReference",
    "OncallIntegrationDefaultRouteOutputReference",
    "OncallIntegrationDefaultRouteSlack",
    "OncallIntegrationDefaultRouteSlackOutputReference",
    "OncallIntegrationDefaultRouteTelegram",
    "OncallIntegrationDefaultRouteTelegramOutputReference",
    "OncallIntegrationTemplates",
    "OncallIntegrationTemplatesOutputReference",
    "OncallIntegrationTemplatesSlack",
    "OncallIntegrationTemplatesSlackOutputReference",
]

publication.publish()

def _typecheckingstub__99cdc0f030e1df46edef831f72048d398b60edc0b545f0cf04446e2512548b37(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    default_route: typing.Union[OncallIntegrationDefaultRoute, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    templates: typing.Optional[typing.Union[OncallIntegrationTemplates, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__22f32b4fe4015840a83a790e97a36390344111a929e0e110def35c6dd6d7f17a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac899570e3f9785542bede424720db986275941b2ef5669d37be601480aa1e0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0ed0df1e39e5d6b0ad159c12beca46e029c0d15fac7fa911121fe98d447f61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4637079e365fa920254bab07b49c34e0f18ff1eb6eb1d2c21a0eb592e490db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70944b6a3530f1ad782265a73090579e0bb4bd65080d727da1ed18fae1746066(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_route: typing.Union[OncallIntegrationDefaultRoute, typing.Dict[builtins.str, typing.Any]],
    name: builtins.str,
    type: builtins.str,
    id: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    templates: typing.Optional[typing.Union[OncallIntegrationTemplates, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f6a38fdc93a0279c7256703785a0c88fc22e072a9b75f14827f9ada70bfe47(
    *,
    escalation_chain_id: typing.Optional[builtins.str] = None,
    msteams: typing.Optional[typing.Union[OncallIntegrationDefaultRouteMsteams, typing.Dict[builtins.str, typing.Any]]] = None,
    slack: typing.Optional[typing.Union[OncallIntegrationDefaultRouteSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    telegram: typing.Optional[typing.Union[OncallIntegrationDefaultRouteTelegram, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66b730037525ac60023f242077725951f17013931216ec2914be3aa53551c102(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b09b93b48dbd25e4663b6e3953d3cc1c55cbb2d1c167b14748a25064f9af3d5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e98a1538d646320f6636920bf2ac2145d89cc4ce31f87d9474a6988f43bd2d2(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1195101d39a6217dc11879d0cf41e1f46031d75ce90d0aeb80ec4614cc8a2a7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b226af27718949bcad6adbf23b3269197fd6423cd7800f471454c2b3be0130(
    value: typing.Optional[OncallIntegrationDefaultRouteMsteams],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cae784056fdeca7eeb57520556590b6ac61305217a8c2ba2670ff4b295911f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c3ab14e74a77ed8c07274a33d19d6db1ba9c4d5ce40616d80cc19bf26db799(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ac293e964789da9bb3648ca31c86b284e19ea514e6b50d730cd13c78b4f9cc5(
    value: typing.Optional[OncallIntegrationDefaultRoute],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fa9022c4ae38b7b75b80bdac61d914580adb86dbf64afb5d92b39a4c1ddfb89(
    *,
    channel_id: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ccf348d4c052eaabbd2859237fbd6df9776e30b03bf32ef92240c529ea6722(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f31a47d146cdfe2cc8a6c6e6587c45fb0c8fdaa87c70b70c5521b4d7bf0a473(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09630ab942eaef1ad0de4a9bf774fc0031d64373bd8dd84f785ea854678255d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923e70d2f5cc690217d99fcf73ad985eab7d0e8972be2ba1df501a2ea830ca12(
    value: typing.Optional[OncallIntegrationDefaultRouteSlack],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__906ec84830aecd08575d205f4e992fdc6c0e1cb4eee5d5a987a1827bb43df93e(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66038c1fb7ae957d2b6e4ceeaba494d54d331d2e0a8b82324db5010b6da873d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b841a6526a7fc60e48ffd3ed1c662ef4ffa259a00728ab26f4f0fbbfb84555(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae27457d2cdeb848164528b2c1ec58e2f803eba155d0c24cf0b2dfcde503c563(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367d19dd090707385a18ece71dd36618cef1532cdc6e7306cb526fb24a376213(
    value: typing.Optional[OncallIntegrationDefaultRouteTelegram],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e62ad375af3d51a47a9b66cd48a244f1b81f1bbcfa6ef6bd41413abd74b06e53(
    *,
    grouping_key: typing.Optional[builtins.str] = None,
    resolve_signal: typing.Optional[builtins.str] = None,
    slack: typing.Optional[typing.Union[OncallIntegrationTemplatesSlack, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb8756a300974cdf2f851dd71a83de07217429bfdf7b40ecf051be9e8d0b5e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365e63391c1015bcb2e595682c9aa76984a07da59982c25451882a1abcb1b4e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__254b72b0c0e2cda9728b4b7adb95749b1753cd748f18dca3a81f322850007a74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3808a8be681c6458aebebd1e25c75efb5a3d4816acebb2349676dda60638fd0e(
    value: typing.Optional[OncallIntegrationTemplates],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa329853e6ecebf8ae7f0a53240627c7463ef4ec8ad1f1aedcb6056098710b8(
    *,
    image_url: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e4df8eb6d3a0ed2320bc52bc04d1fb8060d3b22895e4490196f19a57eec78d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc047bd49a299ba24ce400ef3791a72f0be91f8a870ed8f8f373734ef381ac2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d076bc9814d4646ff86080ac83cc3ebfbeb615c14983028b9a86cbfb87dc8fdb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3f4f20f364fa8c7f724cbe9ce4bc33384d89e87d3ff2d15a3c474a9100c669(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b64fb3c80cdc1471b0a937a391f1cadc2e6372539540234cbafbcb496fe83856(
    value: typing.Optional[OncallIntegrationTemplatesSlack],
) -> None:
    """Type checking stubs"""
    pass
