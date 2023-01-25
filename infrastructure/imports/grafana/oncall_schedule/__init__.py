'''
# `grafana_oncall_schedule`

Refer to the Terraform Registory for docs: [`grafana_oncall_schedule`](https://www.terraform.io/docs/providers/grafana/r/oncall_schedule).
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


class OncallSchedule(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallSchedule.OncallSchedule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule grafana_oncall_schedule}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        ical_url_overrides: typing.Optional[builtins.str] = None,
        ical_url_primary: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        shifts: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union["OncallScheduleSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        team_id: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule grafana_oncall_schedule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The schedule's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#name OncallSchedule#name}
        :param type: The schedule's type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#type OncallSchedule#type}
        :param ical_url_overrides: The URL of external iCal calendar which override primary events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#ical_url_overrides OncallSchedule#ical_url_overrides}
        :param ical_url_primary: The URL of the external calendar iCal file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#ical_url_primary OncallSchedule#ical_url_primary}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#id OncallSchedule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param shifts: The list of ID's of on-call shifts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#shifts OncallSchedule#shifts}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#slack OncallSchedule#slack}
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#team_id OncallSchedule#team_id}
        :param time_zone: The schedule's time zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#time_zone OncallSchedule#time_zone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ffdfe095f005031cb5bb4ee4a765135ad1171dda8c5e2b5c97e2755b530677)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OncallScheduleConfig(
            name=name,
            type=type,
            ical_url_overrides=ical_url_overrides,
            ical_url_primary=ical_url_primary,
            id=id,
            shifts=shifts,
            slack=slack,
            team_id=team_id,
            time_zone=time_zone,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        user_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param channel_id: Slack channel id. Reminder about schedule shifts will be directed to this channel in Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#channel_id OncallSchedule#channel_id}
        :param user_group_id: Slack user group id. Members of user group will be updated when on-call users change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#user_group_id OncallSchedule#user_group_id}
        '''
        value = OncallScheduleSlack(channel_id=channel_id, user_group_id=user_group_id)

        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="resetIcalUrlOverrides")
    def reset_ical_url_overrides(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcalUrlOverrides", []))

    @jsii.member(jsii_name="resetIcalUrlPrimary")
    def reset_ical_url_primary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcalUrlPrimary", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetShifts")
    def reset_shifts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetShifts", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "OncallScheduleSlackOutputReference":
        return typing.cast("OncallScheduleSlackOutputReference", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="icalUrlOverridesInput")
    def ical_url_overrides_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icalUrlOverridesInput"))

    @builtins.property
    @jsii.member(jsii_name="icalUrlPrimaryInput")
    def ical_url_primary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icalUrlPrimaryInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="shiftsInput")
    def shifts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "shiftsInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(self) -> typing.Optional["OncallScheduleSlack"]:
        return typing.cast(typing.Optional["OncallScheduleSlack"], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeZoneInput")
    def time_zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeZoneInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="icalUrlOverrides")
    def ical_url_overrides(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icalUrlOverrides"))

    @ical_url_overrides.setter
    def ical_url_overrides(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55fb63ce3710af319c61ced00b69b71deda8eb54bc8283e71f6bc69b94145ae6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icalUrlOverrides", value)

    @builtins.property
    @jsii.member(jsii_name="icalUrlPrimary")
    def ical_url_primary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icalUrlPrimary"))

    @ical_url_primary.setter
    def ical_url_primary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f56c92d684bd2834b16f9c9ab6e70764279c5cfb6f4c04c9440c0952484a3d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icalUrlPrimary", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04d90ebcd38547f110405eb9919b6d094d3ff3690b26ed9525a22b4eab41577d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8941c7f946a668277a8e2d9a87c74a9509ff22a6eb3dce4eb590e99d927cd72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="shifts")
    def shifts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "shifts"))

    @shifts.setter
    def shifts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2234677d45d52196105916a39e615cf0cd684631a8727fb2c41effe268d9584e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shifts", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca25373fc1aaa3ed69ec7bf692a9738471a5a3ba78c5fdbd8cf412e601752ac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__222f558da4599852f82dee992bb32a0057c51a905d910b86038aa49dc5e61d36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff6a36aaad459752926beb34308934a4d73830b0570bc643c2bf8f58103c2a0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="grafana.oncallSchedule.OncallScheduleConfig",
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
        "type": "type",
        "ical_url_overrides": "icalUrlOverrides",
        "ical_url_primary": "icalUrlPrimary",
        "id": "id",
        "shifts": "shifts",
        "slack": "slack",
        "team_id": "teamId",
        "time_zone": "timeZone",
    },
)
class OncallScheduleConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        type: builtins.str,
        ical_url_overrides: typing.Optional[builtins.str] = None,
        ical_url_primary: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        shifts: typing.Optional[typing.Sequence[builtins.str]] = None,
        slack: typing.Optional[typing.Union["OncallScheduleSlack", typing.Dict[builtins.str, typing.Any]]] = None,
        team_id: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The schedule's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#name OncallSchedule#name}
        :param type: The schedule's type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#type OncallSchedule#type}
        :param ical_url_overrides: The URL of external iCal calendar which override primary events. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#ical_url_overrides OncallSchedule#ical_url_overrides}
        :param ical_url_primary: The URL of the external calendar iCal file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#ical_url_primary OncallSchedule#ical_url_primary}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#id OncallSchedule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param shifts: The list of ID's of on-call shifts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#shifts OncallSchedule#shifts}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#slack OncallSchedule#slack}
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#team_id OncallSchedule#team_id}
        :param time_zone: The schedule's time zone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#time_zone OncallSchedule#time_zone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(slack, dict):
            slack = OncallScheduleSlack(**slack)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c257d0f5ca0b82aee36643ec322b3d8b2a6661d9569e37c21fd2dace7e1345)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument ical_url_overrides", value=ical_url_overrides, expected_type=type_hints["ical_url_overrides"])
            check_type(argname="argument ical_url_primary", value=ical_url_primary, expected_type=type_hints["ical_url_primary"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument shifts", value=shifts, expected_type=type_hints["shifts"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if ical_url_overrides is not None:
            self._values["ical_url_overrides"] = ical_url_overrides
        if ical_url_primary is not None:
            self._values["ical_url_primary"] = ical_url_primary
        if id is not None:
            self._values["id"] = id
        if shifts is not None:
            self._values["shifts"] = shifts
        if slack is not None:
            self._values["slack"] = slack
        if team_id is not None:
            self._values["team_id"] = team_id
        if time_zone is not None:
            self._values["time_zone"] = time_zone

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
        '''The schedule's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#name OncallSchedule#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The schedule's type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#type OncallSchedule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ical_url_overrides(self) -> typing.Optional[builtins.str]:
        '''The URL of external iCal calendar which override primary events.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#ical_url_overrides OncallSchedule#ical_url_overrides}
        '''
        result = self._values.get("ical_url_overrides")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ical_url_primary(self) -> typing.Optional[builtins.str]:
        '''The URL of the external calendar iCal file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#ical_url_primary OncallSchedule#ical_url_primary}
        '''
        result = self._values.get("ical_url_primary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#id OncallSchedule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def shifts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of ID's of on-call shifts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#shifts OncallSchedule#shifts}
        '''
        result = self._values.get("shifts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slack(self) -> typing.Optional["OncallScheduleSlack"]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#slack OncallSchedule#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional["OncallScheduleSlack"], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the OnCall team.

        To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#team_id OncallSchedule#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The schedule's time zone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#time_zone OncallSchedule#time_zone}
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallScheduleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.oncallSchedule.OncallScheduleSlack",
    jsii_struct_bases=[],
    name_mapping={"channel_id": "channelId", "user_group_id": "userGroupId"},
)
class OncallScheduleSlack:
    def __init__(
        self,
        *,
        channel_id: typing.Optional[builtins.str] = None,
        user_group_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param channel_id: Slack channel id. Reminder about schedule shifts will be directed to this channel in Slack. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#channel_id OncallSchedule#channel_id}
        :param user_group_id: Slack user group id. Members of user group will be updated when on-call users change. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#user_group_id OncallSchedule#user_group_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a6dc50230ea4f2e092942cc8a2c3d5e7c462a923361ad70e935f9a96de5e829)
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            check_type(argname="argument user_group_id", value=user_group_id, expected_type=type_hints["user_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if channel_id is not None:
            self._values["channel_id"] = channel_id
        if user_group_id is not None:
            self._values["user_group_id"] = user_group_id

    @builtins.property
    def channel_id(self) -> typing.Optional[builtins.str]:
        '''Slack channel id. Reminder about schedule shifts will be directed to this channel in Slack.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#channel_id OncallSchedule#channel_id}
        '''
        result = self._values.get("channel_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_group_id(self) -> typing.Optional[builtins.str]:
        '''Slack user group id. Members of user group will be updated when on-call users change.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_schedule#user_group_id OncallSchedule#user_group_id}
        '''
        result = self._values.get("user_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallScheduleSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OncallScheduleSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallSchedule.OncallScheduleSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1a56eca6f13be2989656c2da033d4fd526aceb3c81762713c59c18169a6d941)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetChannelId")
    def reset_channel_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannelId", []))

    @jsii.member(jsii_name="resetUserGroupId")
    def reset_user_group_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserGroupId", []))

    @builtins.property
    @jsii.member(jsii_name="channelIdInput")
    def channel_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupIdInput")
    def user_group_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupIdInput"))

    @builtins.property
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78e9f4bfed8f90edd4fccaef1b6ff04ebbd02c295366924d0bca9311caedbfd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelId", value)

    @builtins.property
    @jsii.member(jsii_name="userGroupId")
    def user_group_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userGroupId"))

    @user_group_id.setter
    def user_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa14458cb26fd03a455513f2422d5e5c6eed204cdd5a66cbdc37159c13936e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[OncallScheduleSlack]:
        return typing.cast(typing.Optional[OncallScheduleSlack], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[OncallScheduleSlack]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5db4d0b3866ffe709732f58b35388a48dda3b9537a33d5992b3365d1c33ec2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "OncallSchedule",
    "OncallScheduleConfig",
    "OncallScheduleSlack",
    "OncallScheduleSlackOutputReference",
]

publication.publish()

def _typecheckingstub__63ffdfe095f005031cb5bb4ee4a765135ad1171dda8c5e2b5c97e2755b530677(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    ical_url_overrides: typing.Optional[builtins.str] = None,
    ical_url_primary: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    shifts: typing.Optional[typing.Sequence[builtins.str]] = None,
    slack: typing.Optional[typing.Union[OncallScheduleSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    team_id: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__55fb63ce3710af319c61ced00b69b71deda8eb54bc8283e71f6bc69b94145ae6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f56c92d684bd2834b16f9c9ab6e70764279c5cfb6f4c04c9440c0952484a3d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04d90ebcd38547f110405eb9919b6d094d3ff3690b26ed9525a22b4eab41577d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8941c7f946a668277a8e2d9a87c74a9509ff22a6eb3dce4eb590e99d927cd72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2234677d45d52196105916a39e615cf0cd684631a8727fb2c41effe268d9584e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca25373fc1aaa3ed69ec7bf692a9738471a5a3ba78c5fdbd8cf412e601752ac4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__222f558da4599852f82dee992bb32a0057c51a905d910b86038aa49dc5e61d36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6a36aaad459752926beb34308934a4d73830b0570bc643c2bf8f58103c2a0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c257d0f5ca0b82aee36643ec322b3d8b2a6661d9569e37c21fd2dace7e1345(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    type: builtins.str,
    ical_url_overrides: typing.Optional[builtins.str] = None,
    ical_url_primary: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    shifts: typing.Optional[typing.Sequence[builtins.str]] = None,
    slack: typing.Optional[typing.Union[OncallScheduleSlack, typing.Dict[builtins.str, typing.Any]]] = None,
    team_id: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6dc50230ea4f2e092942cc8a2c3d5e7c462a923361ad70e935f9a96de5e829(
    *,
    channel_id: typing.Optional[builtins.str] = None,
    user_group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a56eca6f13be2989656c2da033d4fd526aceb3c81762713c59c18169a6d941(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78e9f4bfed8f90edd4fccaef1b6ff04ebbd02c295366924d0bca9311caedbfd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfa14458cb26fd03a455513f2422d5e5c6eed204cdd5a66cbdc37159c13936e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5db4d0b3866ffe709732f58b35388a48dda3b9537a33d5992b3365d1c33ec2d(
    value: typing.Optional[OncallScheduleSlack],
) -> None:
    """Type checking stubs"""
    pass
