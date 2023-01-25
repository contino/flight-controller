'''
# `grafana_oncall_on_call_shift`

Refer to the Terraform Registory for docs: [`grafana_oncall_on_call_shift`](https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift).
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


class OncallOnCallShift(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallOnCallShift.OncallOnCallShift",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift grafana_oncall_on_call_shift}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        duration: jsii.Number,
        name: builtins.str,
        start: builtins.str,
        type: builtins.str,
        by_day: typing.Optional[typing.Sequence[builtins.str]] = None,
        by_month: typing.Optional[typing.Sequence[jsii.Number]] = None,
        by_monthday: typing.Optional[typing.Sequence[jsii.Number]] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        interval: typing.Optional[jsii.Number] = None,
        level: typing.Optional[jsii.Number] = None,
        rolling_users: typing.Optional[typing.Sequence[builtins.str]] = None,
        start_rotation_from_user_index: typing.Optional[jsii.Number] = None,
        team_id: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
        week_start: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift grafana_oncall_on_call_shift} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param duration: The duration of the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#duration OncallOnCallShift#duration}
        :param name: The shift's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#name OncallOnCallShift#name}
        :param start: The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#start OncallOnCallShift#start}
        :param type: The shift's type. Can be rolling_users, recurrent_event, single_event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#type OncallOnCallShift#type}
        :param by_day: This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_day OncallOnCallShift#by_day}
        :param by_month: This parameter takes a list of months. Valid values are 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_month OncallOnCallShift#by_month}
        :param by_monthday: This parameter takes a list of days of the month. Valid values are 1 to 31 or -31 to -1 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_monthday OncallOnCallShift#by_monthday}
        :param frequency: The frequency of the event. Can be daily, weekly, monthly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#frequency OncallOnCallShift#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#id OncallOnCallShift#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interval: The positive integer representing at which intervals the recurrence rule repeats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#interval OncallOnCallShift#interval}
        :param level: The priority level. The higher the value, the higher the priority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#level OncallOnCallShift#level}
        :param rolling_users: The list of lists with on-call users (for rolling_users event type). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#rolling_users OncallOnCallShift#rolling_users}
        :param start_rotation_from_user_index: The index of the list of users in rolling_users, from which on-call rotation starts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#start_rotation_from_user_index OncallOnCallShift#start_rotation_from_user_index}
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#team_id OncallOnCallShift#team_id}
        :param time_zone: The shift's timezone. Overrides schedule's timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#time_zone OncallOnCallShift#time_zone}
        :param users: The list of on-call users (for single_event and recurrent_event event type). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#users OncallOnCallShift#users}
        :param week_start: Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#week_start OncallOnCallShift#week_start}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b1341d2ad6412f55daa737538cd946489d2c16cbf0e69dbe95205c3d8c57853)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OncallOnCallShiftConfig(
            duration=duration,
            name=name,
            start=start,
            type=type,
            by_day=by_day,
            by_month=by_month,
            by_monthday=by_monthday,
            frequency=frequency,
            id=id,
            interval=interval,
            level=level,
            rolling_users=rolling_users,
            start_rotation_from_user_index=start_rotation_from_user_index,
            team_id=team_id,
            time_zone=time_zone,
            users=users,
            week_start=week_start,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetByDay")
    def reset_by_day(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetByDay", []))

    @jsii.member(jsii_name="resetByMonth")
    def reset_by_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetByMonth", []))

    @jsii.member(jsii_name="resetByMonthday")
    def reset_by_monthday(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetByMonthday", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetLevel")
    def reset_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLevel", []))

    @jsii.member(jsii_name="resetRollingUsers")
    def reset_rolling_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRollingUsers", []))

    @jsii.member(jsii_name="resetStartRotationFromUserIndex")
    def reset_start_rotation_from_user_index(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartRotationFromUserIndex", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetTimeZone")
    def reset_time_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeZone", []))

    @jsii.member(jsii_name="resetUsers")
    def reset_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsers", []))

    @jsii.member(jsii_name="resetWeekStart")
    def reset_week_start(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekStart", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="byDayInput")
    def by_day_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "byDayInput"))

    @builtins.property
    @jsii.member(jsii_name="byMonthdayInput")
    def by_monthday_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "byMonthdayInput"))

    @builtins.property
    @jsii.member(jsii_name="byMonthInput")
    def by_month_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "byMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="rollingUsersInput")
    def rolling_users_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "rollingUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="startRotationFromUserIndexInput")
    def start_rotation_from_user_index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startRotationFromUserIndexInput"))

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
    @jsii.member(jsii_name="usersInput")
    def users_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "usersInput"))

    @builtins.property
    @jsii.member(jsii_name="weekStartInput")
    def week_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weekStartInput"))

    @builtins.property
    @jsii.member(jsii_name="byDay")
    def by_day(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "byDay"))

    @by_day.setter
    def by_day(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab452006d859bd06bc02c320a14e16ccdddddf520d10da7a854c033cff5c389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "byDay", value)

    @builtins.property
    @jsii.member(jsii_name="byMonth")
    def by_month(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "byMonth"))

    @by_month.setter
    def by_month(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6344479916194005da5216e6717141bae1db4d2bbc1ec71eae026983e7e07ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "byMonth", value)

    @builtins.property
    @jsii.member(jsii_name="byMonthday")
    def by_monthday(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "byMonthday"))

    @by_monthday.setter
    def by_monthday(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55d2095ce3f7cb2faa737312cf0e1da36dea761ed224f7396d19284ad3f1f13f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "byMonthday", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1575e5eddd97ba989262137db64649f3ceede5b0ccd403bef9cda8e4dbfaea03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b86207fd930967c1a1c43570eadb2ba4df0b3948a482e2f8dc364d69b01168)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1a2f4ca307e29896ae46b9a58f7292715d6030dc993e0a6152ed41f55a86b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4febc227742d8ca641f683faf2b10e62b7955b35f3890334a177398961a00284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "level"))

    @level.setter
    def level(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37360d94644f16b51db0aca942ea26c368d352e2e91fd7817e3d444ad7c64591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b302d07b0076d7f4e62542254955428af71ef2a3bdb3a2d597d1978171b3e16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="rollingUsers")
    def rolling_users(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rollingUsers"))

    @rolling_users.setter
    def rolling_users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9d7a5fa8d9be0a04c16997baa7a53ab1b2cafb4442dd88b4ab6d4304a9c8fc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rollingUsers", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "start"))

    @start.setter
    def start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf73051b08116116fd8c030f2a8b4650685904db5d975f7d1f40f231c4c0bdb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="startRotationFromUserIndex")
    def start_rotation_from_user_index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startRotationFromUserIndex"))

    @start_rotation_from_user_index.setter
    def start_rotation_from_user_index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18bd79b7bed18e2f6962cf202b3a27e01d1c4747b063c59c61ef2109dcb940c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startRotationFromUserIndex", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6257567186f5657b4a1f56330238069bf65f08cae0ee9326659f1c1e647fd9d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a0ba2329d5e16e8558a89042df60ef1f2232306710de48512ad82794e180d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa02308214e2fd80a54d8c9abd0df88b5cbc6e171abcfcd87606c71ce24ab52e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "users"))

    @users.setter
    def users(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389b876c7e1b4ab63fad434cd06ff5538472b75b6b8d69bd164a26307ff9b3cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "users", value)

    @builtins.property
    @jsii.member(jsii_name="weekStart")
    def week_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weekStart"))

    @week_start.setter
    def week_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d615e92b5224971a7db811f48325be537819ecd6acfb14ae29a0caa00e5652bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekStart", value)


@jsii.data_type(
    jsii_type="grafana.oncallOnCallShift.OncallOnCallShiftConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "duration": "duration",
        "name": "name",
        "start": "start",
        "type": "type",
        "by_day": "byDay",
        "by_month": "byMonth",
        "by_monthday": "byMonthday",
        "frequency": "frequency",
        "id": "id",
        "interval": "interval",
        "level": "level",
        "rolling_users": "rollingUsers",
        "start_rotation_from_user_index": "startRotationFromUserIndex",
        "team_id": "teamId",
        "time_zone": "timeZone",
        "users": "users",
        "week_start": "weekStart",
    },
)
class OncallOnCallShiftConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        duration: jsii.Number,
        name: builtins.str,
        start: builtins.str,
        type: builtins.str,
        by_day: typing.Optional[typing.Sequence[builtins.str]] = None,
        by_month: typing.Optional[typing.Sequence[jsii.Number]] = None,
        by_monthday: typing.Optional[typing.Sequence[jsii.Number]] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        interval: typing.Optional[jsii.Number] = None,
        level: typing.Optional[jsii.Number] = None,
        rolling_users: typing.Optional[typing.Sequence[builtins.str]] = None,
        start_rotation_from_user_index: typing.Optional[jsii.Number] = None,
        team_id: typing.Optional[builtins.str] = None,
        time_zone: typing.Optional[builtins.str] = None,
        users: typing.Optional[typing.Sequence[builtins.str]] = None,
        week_start: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param duration: The duration of the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#duration OncallOnCallShift#duration}
        :param name: The shift's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#name OncallOnCallShift#name}
        :param start: The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00"). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#start OncallOnCallShift#start}
        :param type: The shift's type. Can be rolling_users, recurrent_event, single_event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#type OncallOnCallShift#type}
        :param by_day: This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_day OncallOnCallShift#by_day}
        :param by_month: This parameter takes a list of months. Valid values are 1 to 12. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_month OncallOnCallShift#by_month}
        :param by_monthday: This parameter takes a list of days of the month. Valid values are 1 to 31 or -31 to -1 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_monthday OncallOnCallShift#by_monthday}
        :param frequency: The frequency of the event. Can be daily, weekly, monthly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#frequency OncallOnCallShift#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#id OncallOnCallShift#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param interval: The positive integer representing at which intervals the recurrence rule repeats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#interval OncallOnCallShift#interval}
        :param level: The priority level. The higher the value, the higher the priority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#level OncallOnCallShift#level}
        :param rolling_users: The list of lists with on-call users (for rolling_users event type). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#rolling_users OncallOnCallShift#rolling_users}
        :param start_rotation_from_user_index: The index of the list of users in rolling_users, from which on-call rotation starts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#start_rotation_from_user_index OncallOnCallShift#start_rotation_from_user_index}
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#team_id OncallOnCallShift#team_id}
        :param time_zone: The shift's timezone. Overrides schedule's timezone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#time_zone OncallOnCallShift#time_zone}
        :param users: The list of on-call users (for single_event and recurrent_event event type). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#users OncallOnCallShift#users}
        :param week_start: Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#week_start OncallOnCallShift#week_start}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bdadbfc07dffefecd8e4ba1492e6cd1a019ed53f8e4555abcf2d9ffba159539)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument by_day", value=by_day, expected_type=type_hints["by_day"])
            check_type(argname="argument by_month", value=by_month, expected_type=type_hints["by_month"])
            check_type(argname="argument by_monthday", value=by_monthday, expected_type=type_hints["by_monthday"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument rolling_users", value=rolling_users, expected_type=type_hints["rolling_users"])
            check_type(argname="argument start_rotation_from_user_index", value=start_rotation_from_user_index, expected_type=type_hints["start_rotation_from_user_index"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
            check_type(argname="argument week_start", value=week_start, expected_type=type_hints["week_start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "duration": duration,
            "name": name,
            "start": start,
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
        if by_day is not None:
            self._values["by_day"] = by_day
        if by_month is not None:
            self._values["by_month"] = by_month
        if by_monthday is not None:
            self._values["by_monthday"] = by_monthday
        if frequency is not None:
            self._values["frequency"] = frequency
        if id is not None:
            self._values["id"] = id
        if interval is not None:
            self._values["interval"] = interval
        if level is not None:
            self._values["level"] = level
        if rolling_users is not None:
            self._values["rolling_users"] = rolling_users
        if start_rotation_from_user_index is not None:
            self._values["start_rotation_from_user_index"] = start_rotation_from_user_index
        if team_id is not None:
            self._values["team_id"] = team_id
        if time_zone is not None:
            self._values["time_zone"] = time_zone
        if users is not None:
            self._values["users"] = users
        if week_start is not None:
            self._values["week_start"] = week_start

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
    def duration(self) -> jsii.Number:
        '''The duration of the event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#duration OncallOnCallShift#duration}
        '''
        result = self._values.get("duration")
        assert result is not None, "Required property 'duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The shift's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#name OncallOnCallShift#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start(self) -> builtins.str:
        '''The start time of the on-call shift. This parameter takes a date format as yyyy-MM-dd'T'HH:mm:ss (for example "2020-09-05T08:00:00").

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#start OncallOnCallShift#start}
        '''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The shift's type. Can be rolling_users, recurrent_event, single_event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#type OncallOnCallShift#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def by_day(self) -> typing.Optional[typing.List[builtins.str]]:
        '''This parameter takes a list of days in iCal format. Can be MO, TU, WE, TH, FR, SA, SU.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_day OncallOnCallShift#by_day}
        '''
        result = self._values.get("by_day")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def by_month(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''This parameter takes a list of months. Valid values are 1 to 12.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_month OncallOnCallShift#by_month}
        '''
        result = self._values.get("by_month")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def by_monthday(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''This parameter takes a list of days of the month.

        Valid values are 1 to 31 or -31 to -1

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#by_monthday OncallOnCallShift#by_monthday}
        '''
        result = self._values.get("by_monthday")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''The frequency of the event. Can be daily, weekly, monthly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#frequency OncallOnCallShift#frequency}
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#id OncallOnCallShift#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''The positive integer representing at which intervals the recurrence rule repeats.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#interval OncallOnCallShift#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def level(self) -> typing.Optional[jsii.Number]:
        '''The priority level. The higher the value, the higher the priority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#level OncallOnCallShift#level}
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rolling_users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of lists with on-call users (for rolling_users event type).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#rolling_users OncallOnCallShift#rolling_users}
        '''
        result = self._values.get("rolling_users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def start_rotation_from_user_index(self) -> typing.Optional[jsii.Number]:
        '''The index of the list of users in rolling_users, from which on-call rotation starts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#start_rotation_from_user_index OncallOnCallShift#start_rotation_from_user_index}
        '''
        result = self._values.get("start_rotation_from_user_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the OnCall team.

        To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#team_id OncallOnCallShift#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_zone(self) -> typing.Optional[builtins.str]:
        '''The shift's timezone.  Overrides schedule's timezone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#time_zone OncallOnCallShift#time_zone}
        '''
        result = self._values.get("time_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def users(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of on-call users (for single_event and recurrent_event event type).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#users OncallOnCallShift#users}
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def week_start(self) -> typing.Optional[builtins.str]:
        '''Start day of the week in iCal format. Can be MO, TU, WE, TH, FR, SA, SU.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_on_call_shift#week_start OncallOnCallShift#week_start}
        '''
        result = self._values.get("week_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallOnCallShiftConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OncallOnCallShift",
    "OncallOnCallShiftConfig",
]

publication.publish()

def _typecheckingstub__5b1341d2ad6412f55daa737538cd946489d2c16cbf0e69dbe95205c3d8c57853(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    duration: jsii.Number,
    name: builtins.str,
    start: builtins.str,
    type: builtins.str,
    by_day: typing.Optional[typing.Sequence[builtins.str]] = None,
    by_month: typing.Optional[typing.Sequence[jsii.Number]] = None,
    by_monthday: typing.Optional[typing.Sequence[jsii.Number]] = None,
    frequency: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    interval: typing.Optional[jsii.Number] = None,
    level: typing.Optional[jsii.Number] = None,
    rolling_users: typing.Optional[typing.Sequence[builtins.str]] = None,
    start_rotation_from_user_index: typing.Optional[jsii.Number] = None,
    team_id: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
    week_start: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2ab452006d859bd06bc02c320a14e16ccdddddf520d10da7a854c033cff5c389(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6344479916194005da5216e6717141bae1db4d2bbc1ec71eae026983e7e07ef6(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55d2095ce3f7cb2faa737312cf0e1da36dea761ed224f7396d19284ad3f1f13f(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1575e5eddd97ba989262137db64649f3ceede5b0ccd403bef9cda8e4dbfaea03(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b86207fd930967c1a1c43570eadb2ba4df0b3948a482e2f8dc364d69b01168(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a2f4ca307e29896ae46b9a58f7292715d6030dc993e0a6152ed41f55a86b58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4febc227742d8ca641f683faf2b10e62b7955b35f3890334a177398961a00284(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37360d94644f16b51db0aca942ea26c368d352e2e91fd7817e3d444ad7c64591(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b302d07b0076d7f4e62542254955428af71ef2a3bdb3a2d597d1978171b3e16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d7a5fa8d9be0a04c16997baa7a53ab1b2cafb4442dd88b4ab6d4304a9c8fc8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf73051b08116116fd8c030f2a8b4650685904db5d975f7d1f40f231c4c0bdb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18bd79b7bed18e2f6962cf202b3a27e01d1c4747b063c59c61ef2109dcb940c4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6257567186f5657b4a1f56330238069bf65f08cae0ee9326659f1c1e647fd9d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a0ba2329d5e16e8558a89042df60ef1f2232306710de48512ad82794e180d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa02308214e2fd80a54d8c9abd0df88b5cbc6e171abcfcd87606c71ce24ab52e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389b876c7e1b4ab63fad434cd06ff5538472b75b6b8d69bd164a26307ff9b3cb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d615e92b5224971a7db811f48325be537819ecd6acfb14ae29a0caa00e5652bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bdadbfc07dffefecd8e4ba1492e6cd1a019ed53f8e4555abcf2d9ffba159539(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    duration: jsii.Number,
    name: builtins.str,
    start: builtins.str,
    type: builtins.str,
    by_day: typing.Optional[typing.Sequence[builtins.str]] = None,
    by_month: typing.Optional[typing.Sequence[jsii.Number]] = None,
    by_monthday: typing.Optional[typing.Sequence[jsii.Number]] = None,
    frequency: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    interval: typing.Optional[jsii.Number] = None,
    level: typing.Optional[jsii.Number] = None,
    rolling_users: typing.Optional[typing.Sequence[builtins.str]] = None,
    start_rotation_from_user_index: typing.Optional[jsii.Number] = None,
    team_id: typing.Optional[builtins.str] = None,
    time_zone: typing.Optional[builtins.str] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
    week_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
