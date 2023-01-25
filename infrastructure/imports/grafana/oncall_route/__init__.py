'''
# `grafana_oncall_route`

Refer to the Terraform Registory for docs: [`grafana_oncall_route`](https://www.terraform.io/docs/providers/grafana/r/oncall_route).
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


class OncallRoute(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallRoute.OncallRoute",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route grafana_oncall_route}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        escalation_chain_id: builtins.str,
        integration_id: builtins.str,
        position: jsii.Number,
        routing_regex: builtins.str,
        id: typing.Optional[builtins.str] = None,
        msteams: typing.Optional[typing.Union["OncallRouteMsteams", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["OncallRouteSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        telegram: typing.Optional[typing.Union["OncallRouteTelegram", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route grafana_oncall_route} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param escalation_chain_id: The ID of the escalation chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#escalation_chain_id OncallRoute#escalation_chain_id}
        :param integration_id: The ID of the integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#integration_id OncallRoute#integration_id}
        :param position: The position of the route (starts from 0). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#position OncallRoute#position}
        :param routing_regex: Python Regex query. Route is chosen for an alert if there is a match inside the alert payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#routing_regex OncallRoute#routing_regex}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param msteams: msteams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#msteams OncallRoute#msteams}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#slack OncallRoute#slack}
        :param telegram: telegram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#telegram OncallRoute#telegram}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a7eab597c3b376453bd6ac0e62c200c474e587fde150a147e0a181e47244a9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OncallRouteConfig(
            escalation_chain_id=escalation_chain_id,
            integration_id=integration_id,
            position=position,
            routing_regex=routing_regex,
            id=id,
            msteams=msteams,
            slack=slack,
            telegram=telegram,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMsteams")
    def put_msteams(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in MS teams. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        :param id: MS teams channel id. Alerts will be directed to this channel in Microsoft teams. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        value = OncallRouteMsteams(enabled=enabled, id=id)

        return typing.cast(None, jsii.invoke(self, "putMsteams", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param channel_id: Slack channel id. Alerts will be directed to this channel in Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#channel_id OncallRoute#channel_id}
        :param enabled: Enable notification in Slack. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        '''
        value = OncallRouteSlack(channel_id=channel_id, enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putTelegram")
    def put_telegram(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in Telegram. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        :param id: Telegram channel id. Alerts will be directed to this channel in Telegram. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        value = OncallRouteTelegram(enabled=enabled, id=id)

        return typing.cast(None, jsii.invoke(self, "putTelegram", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMsteams")
    def reset_msteams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsteams", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetTelegram")
    def reset_telegram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTelegram", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="msteams")
    def msteams(self) -> "OncallRouteMsteamsOutputReference":
        return typing.cast("OncallRouteMsteamsOutputReference", jsii.get(self, "msteams"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "OncallRouteSlackOutputReference":
        return typing.cast("OncallRouteSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="telegram")
    def telegram(self) -> "OncallRouteTelegramOutputReference":
        return typing.cast("OncallRouteTelegramOutputReference", jsii.get(self, "telegram"))

    @builtins.property
    @jsii.member(jsii_name="escalationChainIdInput")
    def escalation_chain_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "escalationChainIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationIdInput")
    def integration_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="msteamsInput")
    def msteams_input(self) -> typing.Optional["OncallRouteMsteams"]:
        return typing.cast(typing.Optional["OncallRouteMsteams"], jsii.get(self, "msteamsInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="routingRegexInput")
    def routing_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routingRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(self) -> typing.Optional["OncallRouteSlack"]:
        return typing.cast(typing.Optional["OncallRouteSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="telegramInput")
    def telegram_input(self) -> typing.Optional["OncallRouteTelegram"]:
        return typing.cast(typing.Optional["OncallRouteTelegram"], jsii.get(self, "telegramInput"))

    @builtins.property
    @jsii.member(jsii_name="escalationChainId")
    def escalation_chain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "escalationChainId"))

    @escalation_chain_id.setter
    def escalation_chain_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a11bf7a8bc6a8a9be1e4b60e2d7d0915d1ddf3b4e4687b9b00c32527b0f153c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "escalationChainId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58594583896e353a9d386d8a98bc2198ca127ef231b84e315ef4329a335cb870)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationId")
    def integration_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationId"))

    @integration_id.setter
    def integration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57eabd08029e1e0f01eed8bc7d6362bbe4c000237068d9e8945ad2af3dfac9a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationId", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "position"))

    @position.setter
    def position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fe014a05e7ccc4402f05fa765701dd89dbef32fceb1d2b7fcca9511a3e35d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @builtins.property
    @jsii.member(jsii_name="routingRegex")
    def routing_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "routingRegex"))

    @routing_regex.setter
    def routing_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2a22aff875193f0a03b1ceca573c20b51dbad391f1d84e7c67ba5b1e819600)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingRegex", value)


@jsii.data_type(
    jsii_type="grafana.oncallRoute.OncallRouteConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "escalation_chain_id": "escalationChainId",
        "integration_id": "integrationId",
        "position": "position",
        "routing_regex": "routingRegex",
        "id": "id",
        "msteams": "msteams",
        "slack": "slack",
        "telegram": "telegram",
    },
)
class OncallRouteConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        escalation_chain_id: builtins.str,
        integration_id: builtins.str,
        position: jsii.Number,
        routing_regex: builtins.str,
        id: typing.Optional[builtins.str] = None,
        msteams: typing.Optional[typing.Union["OncallRouteMsteams", typing.Dict[builtins.str, typing.Any]]] = None,
        slack: typing.Optional[typing.Union["OncallRouteSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        telegram: typing.Optional[typing.Union["OncallRouteTelegram", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param escalation_chain_id: The ID of the escalation chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#escalation_chain_id OncallRoute#escalation_chain_id}
        :param integration_id: The ID of the integration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#integration_id OncallRoute#integration_id}
        :param position: The position of the route (starts from 0). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#position OncallRoute#position}
        :param routing_regex: Python Regex query. Route is chosen for an alert if there is a match inside the alert payload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#routing_regex OncallRoute#routing_regex}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param msteams: msteams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#msteams OncallRoute#msteams}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#slack OncallRoute#slack}
        :param telegram: telegram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#telegram OncallRoute#telegram}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(msteams, dict):
            msteams = OncallRouteMsteams(**msteams)
        if isinstance(slack, dict):
            slack = OncallRouteSlack(**slack)
        if isinstance(telegram, dict):
            telegram = OncallRouteTelegram(**telegram)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22b16cebe85e10c1e86c5ef6e78a3257374bfe4dcdd83ee67db8d14ba8c171fe)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument escalation_chain_id", value=escalation_chain_id, expected_type=type_hints["escalation_chain_id"])
            check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument routing_regex", value=routing_regex, expected_type=type_hints["routing_regex"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument msteams", value=msteams, expected_type=type_hints["msteams"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument telegram", value=telegram, expected_type=type_hints["telegram"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "escalation_chain_id": escalation_chain_id,
            "integration_id": integration_id,
            "position": position,
            "routing_regex": routing_regex,
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
        if msteams is not None:
            self._values["msteams"] = msteams
        if slack is not None:
            self._values["slack"] = slack
        if telegram is not None:
            self._values["telegram"] = telegram

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
    def escalation_chain_id(self) -> builtins.str:
        '''The ID of the escalation chain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#escalation_chain_id OncallRoute#escalation_chain_id}
        '''
        result = self._values.get("escalation_chain_id")
        assert result is not None, "Required property 'escalation_chain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_id(self) -> builtins.str:
        '''The ID of the integration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#integration_id OncallRoute#integration_id}
        '''
        result = self._values.get("integration_id")
        assert result is not None, "Required property 'integration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def position(self) -> jsii.Number:
        '''The position of the route (starts from 0).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#position OncallRoute#position}
        '''
        result = self._values.get("position")
        assert result is not None, "Required property 'position' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def routing_regex(self) -> builtins.str:
        '''Python Regex query. Route is chosen for an alert if there is a match inside the alert payload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#routing_regex OncallRoute#routing_regex}
        '''
        result = self._values.get("routing_regex")
        assert result is not None, "Required property 'routing_regex' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def msteams(self) -> typing.Optional["OncallRouteMsteams"]:
        '''msteams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#msteams OncallRoute#msteams}
        '''
        result = self._values.get("msteams")
        return typing.cast(typing.Optional["OncallRouteMsteams"], result)

    @builtins.property
    def slack(self) -> typing.Optional["OncallRouteSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#slack OncallRoute#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["OncallRouteSlack"], result)

    @builtins.property
    def telegram(self) -> typing.Optional["OncallRouteTelegram"]:
        '''telegram block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#telegram OncallRoute#telegram}
        '''
        result = self._values.get("telegram")
        return typing.cast(typing.Optional["OncallRouteTelegram"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallRouteConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.oncallRoute.OncallRouteMsteams",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "id": "id"},
)
class OncallRouteMsteams:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in MS teams. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        :param id: MS teams channel id. Alerts will be directed to this channel in Microsoft teams. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d6d6fe5f83dd753d657c1003e8635538fa918e8e9b150d64f3ccb7ede5543fb)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''MS teams channel id. Alerts will be directed to this channel in Microsoft teams.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id}

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
        return "OncallRouteMsteams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallRouteMsteamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallRoute.OncallRouteMsteamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__323acffaf9aa80fa8861acf877caf58c674aed64f7e767d756f02901a55e9d42)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b2480493b1272ec569951c44264997fa42cf499c7844b8175721affadf07758)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c6565384bcd3d1243a486c3322fe241b4ad1196d1fd09b408c5a4f26b8f0c35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallRouteMsteams]:
        return typing.cast(typing.Optional[OncallRouteMsteams], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OncallRouteMsteams]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7084fad27e54ed48a2647be7d1723ca72e8be2cdac74604ae31deb8259e112fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.oncallRoute.OncallRouteSlack",
    jsii_struct_bases=[],
    name_mapping={"channel_id": "channelId", "enabled": "enabled"},
)
class OncallRouteSlack:
    def __init__(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param channel_id: Slack channel id. Alerts will be directed to this channel in Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#channel_id OncallRoute#channel_id}
        :param enabled: Enable notification in Slack. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13533769ca4cd2a0bc1223ece08228c6139a2e05ceb1f89225f48a650a487933)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#channel_id OncallRoute#channel_id}
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Enable notification in Slack. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallRouteSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallRouteSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallRoute.OncallRouteSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__89305fc6cd79a37c54fd0ed800f65579a35fa3fbb2a92dfc51dffb7e329bdd3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e9c430d9fb7e788b36dd4857b00d430d1f9056976d67c19bd42e164ac621c28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfab069b470092ab5ca425f470cb2595083d146b217483bc4267245851f1eeb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallRouteSlack]:
        return typing.cast(typing.Optional[OncallRouteSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OncallRouteSlack]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__103624b181272397ffc552186b00842035d348a67dcdc9a4f41d9d69d53d4ae3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.oncallRoute.OncallRouteTelegram",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "id": "id"},
)
class OncallRouteTelegram:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Enable notification in Telegram. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        :param id: Telegram channel id. Alerts will be directed to this channel in Telegram. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e6bfe798d72d1503ae534cae872fb345a13b117b67b549a1b199a7dadc737b)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#enabled OncallRoute#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Telegram channel id. Alerts will be directed to this channel in Telegram.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_route#id OncallRoute#id}

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
        return "OncallRouteTelegram(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallRouteTelegramOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallRoute.OncallRouteTelegramOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__289d481b8e0485a8213d2d813766cf4d377d0193cc75a35f68741aeac6e56479)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f884ac0dceacbb43f9b2289836fc5c47b1adba1714ca98c71e9d86c2b18d639)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce087e5b9c19e0126bff969181bd95f4fce67a8c9f6f8fe92731bfaa6354edb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallRouteTelegram]:
        return typing.cast(typing.Optional[OncallRouteTelegram], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OncallRouteTelegram]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5415625a68781dafdbb4b4faef9c9c8638e2e45ae8a3e83eee43d937aaa86dc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OncallRoute",
    "OncallRouteConfig",
    "OncallRouteMsteams",
    "OncallRouteMsteamsOutputReference",
    "OncallRouteSlack",
    "OncallRouteSlackOutputReference",
    "OncallRouteTelegram",
    "OncallRouteTelegramOutputReference",
]

publication.publish()

def _typecheckingstub__e6a7eab597c3b376453bd6ac0e62c200c474e587fde150a147e0a181e47244a9(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    escalation_chain_id: builtins.str,
    integration_id: builtins.str,
    position: jsii.Number,
    routing_regex: builtins.str,
    id: typing.Optional[builtins.str] = None,
    msteams: typing.Optional[typing.Union[OncallRouteMsteams, typing.Dict[builtins.str, typing.Any]]] = None,
    slack: typing.Optional[typing.Union[OncallRouteSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    telegram: typing.Optional[typing.Union[OncallRouteTelegram, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__a11bf7a8bc6a8a9be1e4b60e2d7d0915d1ddf3b4e4687b9b00c32527b0f153c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58594583896e353a9d386d8a98bc2198ca127ef231b84e315ef4329a335cb870(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57eabd08029e1e0f01eed8bc7d6362bbe4c000237068d9e8945ad2af3dfac9a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fe014a05e7ccc4402f05fa765701dd89dbef32fceb1d2b7fcca9511a3e35d82(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2a22aff875193f0a03b1ceca573c20b51dbad391f1d84e7c67ba5b1e819600(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22b16cebe85e10c1e86c5ef6e78a3257374bfe4dcdd83ee67db8d14ba8c171fe(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    escalation_chain_id: builtins.str,
    integration_id: builtins.str,
    position: jsii.Number,
    routing_regex: builtins.str,
    id: typing.Optional[builtins.str] = None,
    msteams: typing.Optional[typing.Union[OncallRouteMsteams, typing.Dict[builtins.str, typing.Any]]] = None,
    slack: typing.Optional[typing.Union[OncallRouteSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    telegram: typing.Optional[typing.Union[OncallRouteTelegram, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d6d6fe5f83dd753d657c1003e8635538fa918e8e9b150d64f3ccb7ede5543fb(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__323acffaf9aa80fa8861acf877caf58c674aed64f7e767d756f02901a55e9d42(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b2480493b1272ec569951c44264997fa42cf499c7844b8175721affadf07758(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6565384bcd3d1243a486c3322fe241b4ad1196d1fd09b408c5a4f26b8f0c35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7084fad27e54ed48a2647be7d1723ca72e8be2cdac74604ae31deb8259e112fb(
    value: typing.Optional[OncallRouteMsteams],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13533769ca4cd2a0bc1223ece08228c6139a2e05ceb1f89225f48a650a487933(
    *,
    channel_id: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89305fc6cd79a37c54fd0ed800f65579a35fa3fbb2a92dfc51dffb7e329bdd3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e9c430d9fb7e788b36dd4857b00d430d1f9056976d67c19bd42e164ac621c28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfab069b470092ab5ca425f470cb2595083d146b217483bc4267245851f1eeb6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__103624b181272397ffc552186b00842035d348a67dcdc9a4f41d9d69d53d4ae3(
    value: typing.Optional[OncallRouteSlack],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e6bfe798d72d1503ae534cae872fb345a13b117b67b549a1b199a7dadc737b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289d481b8e0485a8213d2d813766cf4d377d0193cc75a35f68741aeac6e56479(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f884ac0dceacbb43f9b2289836fc5c47b1adba1714ca98c71e9d86c2b18d639(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce087e5b9c19e0126bff969181bd95f4fce67a8c9f6f8fe92731bfaa6354edb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5415625a68781dafdbb4b4faef9c9c8638e2e45ae8a3e83eee43d937aaa86dc6(
    value: typing.Optional[OncallRouteTelegram],
) -> None:
    """Type checking stubs"""
    pass
