'''
# `grafana_oncall_escalation`

Refer to the Terraform Registory for docs: [`grafana_oncall_escalation`](https://www.terraform.io/docs/providers/grafana/r/oncall_escalation).
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


class OncallEscalation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallEscalation.OncallEscalation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation grafana_oncall_escalation}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        escalation_chain_id: builtins.str,
        position: jsii.Number,
        action_to_trigger: typing.Optional[builtins.str] = None,
        duration: typing.Optional[jsii.Number] = None,
        group_to_notify: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        important: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        notify_if_time_from: typing.Optional[builtins.str] = None,
        notify_if_time_to: typing.Optional[builtins.str] = None,
        notify_on_call_from_schedule: typing.Optional[builtins.str] = None,
        persons_to_notify: typing.Optional[typing.Sequence[builtins.str]] = None,
        persons_to_notify_next_each_time: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation grafana_oncall_escalation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param escalation_chain_id: The ID of the escalation chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#escalation_chain_id OncallEscalation#escalation_chain_id}
        :param position: The position of the escalation step (starts from 0). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#position OncallEscalation#position}
        :param action_to_trigger: The ID of an Action for trigger_action type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#action_to_trigger OncallEscalation#action_to_trigger}
        :param duration: The duration of delay for wait type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#duration OncallEscalation#duration}
        :param group_to_notify: The ID of a User Group for notify_user_group type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#group_to_notify OncallEscalation#group_to_notify}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#id OncallEscalation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param important: Will activate "important" personal notification rules. Actual for steps: notify_persons, notify_on_call_from_schedule and notify_user_group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#important OncallEscalation#important}
        :param notify_if_time_from: The beginning of the time interval for notify_if_time_from_to type step in UTC (for example 08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_if_time_from OncallEscalation#notify_if_time_from}
        :param notify_if_time_to: The end of the time interval for notify_if_time_from_to type step in UTC (for example 18:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_if_time_to OncallEscalation#notify_if_time_to}
        :param notify_on_call_from_schedule: ID of a Schedule for notify_on_call_from_schedule type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_on_call_from_schedule OncallEscalation#notify_on_call_from_schedule}
        :param persons_to_notify: The list of ID's of users for notify_persons type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#persons_to_notify OncallEscalation#persons_to_notify}
        :param persons_to_notify_next_each_time: The list of ID's of users for notify_person_next_each_time type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#persons_to_notify_next_each_time OncallEscalation#persons_to_notify_next_each_time}
        :param type: The type of escalation policy. Can be wait, notify_persons, notify_person_next_each_time, notify_on_call_from_schedule, trigger_action, notify_user_group, resolve, notify_whole_channel, notify_if_time_from_to, repeat_escalation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#type OncallEscalation#type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c0ddd010e698de33431c8bcdb44d6087d22ccd58c2a5a4c652cfac12148445b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OncallEscalationConfig(
            escalation_chain_id=escalation_chain_id,
            position=position,
            action_to_trigger=action_to_trigger,
            duration=duration,
            group_to_notify=group_to_notify,
            id=id,
            important=important,
            notify_if_time_from=notify_if_time_from,
            notify_if_time_to=notify_if_time_to,
            notify_on_call_from_schedule=notify_on_call_from_schedule,
            persons_to_notify=persons_to_notify,
            persons_to_notify_next_each_time=persons_to_notify_next_each_time,
            type=type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetActionToTrigger")
    def reset_action_to_trigger(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActionToTrigger", []))

    @jsii.member(jsii_name="resetDuration")
    def reset_duration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDuration", []))

    @jsii.member(jsii_name="resetGroupToNotify")
    def reset_group_to_notify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupToNotify", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImportant")
    def reset_important(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImportant", []))

    @jsii.member(jsii_name="resetNotifyIfTimeFrom")
    def reset_notify_if_time_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyIfTimeFrom", []))

    @jsii.member(jsii_name="resetNotifyIfTimeTo")
    def reset_notify_if_time_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyIfTimeTo", []))

    @jsii.member(jsii_name="resetNotifyOnCallFromSchedule")
    def reset_notify_on_call_from_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotifyOnCallFromSchedule", []))

    @jsii.member(jsii_name="resetPersonsToNotify")
    def reset_persons_to_notify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersonsToNotify", []))

    @jsii.member(jsii_name="resetPersonsToNotifyNextEachTime")
    def reset_persons_to_notify_next_each_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersonsToNotifyNextEachTime", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="actionToTriggerInput")
    def action_to_trigger_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionToTriggerInput"))

    @builtins.property
    @jsii.member(jsii_name="durationInput")
    def duration_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationInput"))

    @builtins.property
    @jsii.member(jsii_name="escalationChainIdInput")
    def escalation_chain_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "escalationChainIdInput"))

    @builtins.property
    @jsii.member(jsii_name="groupToNotifyInput")
    def group_to_notify_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupToNotifyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importantInput")
    def important_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "importantInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyIfTimeFromInput")
    def notify_if_time_from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notifyIfTimeFromInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyIfTimeToInput")
    def notify_if_time_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notifyIfTimeToInput"))

    @builtins.property
    @jsii.member(jsii_name="notifyOnCallFromScheduleInput")
    def notify_on_call_from_schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notifyOnCallFromScheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="personsToNotifyInput")
    def persons_to_notify_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "personsToNotifyInput"))

    @builtins.property
    @jsii.member(jsii_name="personsToNotifyNextEachTimeInput")
    def persons_to_notify_next_each_time_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "personsToNotifyNextEachTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="positionInput")
    def position_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "positionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="actionToTrigger")
    def action_to_trigger(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "actionToTrigger"))

    @action_to_trigger.setter
    def action_to_trigger(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f58b51ee66266e9e28fae1b6784daa5be612fdad30459d9846a89232ac9d02c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionToTrigger", value)

    @builtins.property
    @jsii.member(jsii_name="duration")
    def duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "duration"))

    @duration.setter
    def duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dd8016af034e268826d4c50cf76d428bf5d4e099b1b0191509a322801f88d09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "duration", value)

    @builtins.property
    @jsii.member(jsii_name="escalationChainId")
    def escalation_chain_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "escalationChainId"))

    @escalation_chain_id.setter
    def escalation_chain_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66f6a91630b2672a4f5e46c93b3b79ef426c161eb412e1194fc6f64979113c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "escalationChainId", value)

    @builtins.property
    @jsii.member(jsii_name="groupToNotify")
    def group_to_notify(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupToNotify"))

    @group_to_notify.setter
    def group_to_notify(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7edff4805b4abd45beff4c87e67a7b5c0fc813bee0c8c928f80317e4122388d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupToNotify", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88444bafccbbc17311696d9acf9a05d3842dc0b92013f5e7add4f2168f738adf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="important")
    def important(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "important"))

    @important.setter
    def important(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__876c829a3002783361cb37f83457607fff4df5b9dea73ed56cfb37bb58e2fb1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "important", value)

    @builtins.property
    @jsii.member(jsii_name="notifyIfTimeFrom")
    def notify_if_time_from(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notifyIfTimeFrom"))

    @notify_if_time_from.setter
    def notify_if_time_from(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3b5dfa844ea3a53b914526e7f5e3b23a23ebd1e47c67f94f2cdc69405ef7f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyIfTimeFrom", value)

    @builtins.property
    @jsii.member(jsii_name="notifyIfTimeTo")
    def notify_if_time_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notifyIfTimeTo"))

    @notify_if_time_to.setter
    def notify_if_time_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f7916ea6bdde1643196aefc43cc1896e81bd659eb32764e2bdb5d0f77727f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyIfTimeTo", value)

    @builtins.property
    @jsii.member(jsii_name="notifyOnCallFromSchedule")
    def notify_on_call_from_schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notifyOnCallFromSchedule"))

    @notify_on_call_from_schedule.setter
    def notify_on_call_from_schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab99534ae630b28ff63f95922348d0a5f4a47323c884418aea513d91dae3dbc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notifyOnCallFromSchedule", value)

    @builtins.property
    @jsii.member(jsii_name="personsToNotify")
    def persons_to_notify(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "personsToNotify"))

    @persons_to_notify.setter
    def persons_to_notify(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b5c1dc662d50d5f450f83d25d5d5ce6de1699b8be3642f6f4310d44078f5dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "personsToNotify", value)

    @builtins.property
    @jsii.member(jsii_name="personsToNotifyNextEachTime")
    def persons_to_notify_next_each_time(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "personsToNotifyNextEachTime"))

    @persons_to_notify_next_each_time.setter
    def persons_to_notify_next_each_time(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dd788c0c9e7da776707fa8531b24769a74c7b8685ff9e9e9ccde108c0531b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "personsToNotifyNextEachTime", value)

    @builtins.property
    @jsii.member(jsii_name="position")
    def position(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "position"))

    @position.setter
    def position(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20577dfd3d0e234ab159a482bfc9842d7b28da5660a268e3a7a669393b692215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "position", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784e2b23f6065b7bb68ef7bc08cad263860dbcba06748592474822ad8ede8d06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="grafana.oncallEscalation.OncallEscalationConfig",
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
        "position": "position",
        "action_to_trigger": "actionToTrigger",
        "duration": "duration",
        "group_to_notify": "groupToNotify",
        "id": "id",
        "important": "important",
        "notify_if_time_from": "notifyIfTimeFrom",
        "notify_if_time_to": "notifyIfTimeTo",
        "notify_on_call_from_schedule": "notifyOnCallFromSchedule",
        "persons_to_notify": "personsToNotify",
        "persons_to_notify_next_each_time": "personsToNotifyNextEachTime",
        "type": "type",
    },
)
class OncallEscalationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        position: jsii.Number,
        action_to_trigger: typing.Optional[builtins.str] = None,
        duration: typing.Optional[jsii.Number] = None,
        group_to_notify: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        important: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        notify_if_time_from: typing.Optional[builtins.str] = None,
        notify_if_time_to: typing.Optional[builtins.str] = None,
        notify_on_call_from_schedule: typing.Optional[builtins.str] = None,
        persons_to_notify: typing.Optional[typing.Sequence[builtins.str]] = None,
        persons_to_notify_next_each_time: typing.Optional[typing.Sequence[builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param escalation_chain_id: The ID of the escalation chain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#escalation_chain_id OncallEscalation#escalation_chain_id}
        :param position: The position of the escalation step (starts from 0). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#position OncallEscalation#position}
        :param action_to_trigger: The ID of an Action for trigger_action type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#action_to_trigger OncallEscalation#action_to_trigger}
        :param duration: The duration of delay for wait type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#duration OncallEscalation#duration}
        :param group_to_notify: The ID of a User Group for notify_user_group type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#group_to_notify OncallEscalation#group_to_notify}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#id OncallEscalation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param important: Will activate "important" personal notification rules. Actual for steps: notify_persons, notify_on_call_from_schedule and notify_user_group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#important OncallEscalation#important}
        :param notify_if_time_from: The beginning of the time interval for notify_if_time_from_to type step in UTC (for example 08:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_if_time_from OncallEscalation#notify_if_time_from}
        :param notify_if_time_to: The end of the time interval for notify_if_time_from_to type step in UTC (for example 18:00:00Z). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_if_time_to OncallEscalation#notify_if_time_to}
        :param notify_on_call_from_schedule: ID of a Schedule for notify_on_call_from_schedule type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_on_call_from_schedule OncallEscalation#notify_on_call_from_schedule}
        :param persons_to_notify: The list of ID's of users for notify_persons type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#persons_to_notify OncallEscalation#persons_to_notify}
        :param persons_to_notify_next_each_time: The list of ID's of users for notify_person_next_each_time type step. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#persons_to_notify_next_each_time OncallEscalation#persons_to_notify_next_each_time}
        :param type: The type of escalation policy. Can be wait, notify_persons, notify_person_next_each_time, notify_on_call_from_schedule, trigger_action, notify_user_group, resolve, notify_whole_channel, notify_if_time_from_to, repeat_escalation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#type OncallEscalation#type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7938a7e1f33613e000055dc885911d2cdd0eadb34f12a6cf429e037ce2bf90a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument escalation_chain_id", value=escalation_chain_id, expected_type=type_hints["escalation_chain_id"])
            check_type(argname="argument position", value=position, expected_type=type_hints["position"])
            check_type(argname="argument action_to_trigger", value=action_to_trigger, expected_type=type_hints["action_to_trigger"])
            check_type(argname="argument duration", value=duration, expected_type=type_hints["duration"])
            check_type(argname="argument group_to_notify", value=group_to_notify, expected_type=type_hints["group_to_notify"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument important", value=important, expected_type=type_hints["important"])
            check_type(argname="argument notify_if_time_from", value=notify_if_time_from, expected_type=type_hints["notify_if_time_from"])
            check_type(argname="argument notify_if_time_to", value=notify_if_time_to, expected_type=type_hints["notify_if_time_to"])
            check_type(argname="argument notify_on_call_from_schedule", value=notify_on_call_from_schedule, expected_type=type_hints["notify_on_call_from_schedule"])
            check_type(argname="argument persons_to_notify", value=persons_to_notify, expected_type=type_hints["persons_to_notify"])
            check_type(argname="argument persons_to_notify_next_each_time", value=persons_to_notify_next_each_time, expected_type=type_hints["persons_to_notify_next_each_time"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "escalation_chain_id": escalation_chain_id,
            "position": position,
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
        if action_to_trigger is not None:
            self._values["action_to_trigger"] = action_to_trigger
        if duration is not None:
            self._values["duration"] = duration
        if group_to_notify is not None:
            self._values["group_to_notify"] = group_to_notify
        if id is not None:
            self._values["id"] = id
        if important is not None:
            self._values["important"] = important
        if notify_if_time_from is not None:
            self._values["notify_if_time_from"] = notify_if_time_from
        if notify_if_time_to is not None:
            self._values["notify_if_time_to"] = notify_if_time_to
        if notify_on_call_from_schedule is not None:
            self._values["notify_on_call_from_schedule"] = notify_on_call_from_schedule
        if persons_to_notify is not None:
            self._values["persons_to_notify"] = persons_to_notify
        if persons_to_notify_next_each_time is not None:
            self._values["persons_to_notify_next_each_time"] = persons_to_notify_next_each_time
        if type is not None:
            self._values["type"] = type

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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#escalation_chain_id OncallEscalation#escalation_chain_id}
        '''
        result = self._values.get("escalation_chain_id")
        assert result is not None, "Required property 'escalation_chain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def position(self) -> jsii.Number:
        '''The position of the escalation step (starts from 0).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#position OncallEscalation#position}
        '''
        result = self._values.get("position")
        assert result is not None, "Required property 'position' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def action_to_trigger(self) -> typing.Optional[builtins.str]:
        '''The ID of an Action for trigger_action type step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#action_to_trigger OncallEscalation#action_to_trigger}
        '''
        result = self._values.get("action_to_trigger")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def duration(self) -> typing.Optional[jsii.Number]:
        '''The duration of delay for wait type step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#duration OncallEscalation#duration}
        '''
        result = self._values.get("duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def group_to_notify(self) -> typing.Optional[builtins.str]:
        '''The ID of a User Group for notify_user_group type step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#group_to_notify OncallEscalation#group_to_notify}
        '''
        result = self._values.get("group_to_notify")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#id OncallEscalation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def important(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Will activate "important" personal notification rules. Actual for steps: notify_persons, notify_on_call_from_schedule and notify_user_group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#important OncallEscalation#important}
        '''
        result = self._values.get("important")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def notify_if_time_from(self) -> typing.Optional[builtins.str]:
        '''The beginning of the time interval for notify_if_time_from_to type step in UTC (for example 08:00:00Z).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_if_time_from OncallEscalation#notify_if_time_from}
        '''
        result = self._values.get("notify_if_time_from")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notify_if_time_to(self) -> typing.Optional[builtins.str]:
        '''The end of the time interval for notify_if_time_from_to type step in UTC (for example 18:00:00Z).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_if_time_to OncallEscalation#notify_if_time_to}
        '''
        result = self._values.get("notify_if_time_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notify_on_call_from_schedule(self) -> typing.Optional[builtins.str]:
        '''ID of a Schedule for notify_on_call_from_schedule type step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#notify_on_call_from_schedule OncallEscalation#notify_on_call_from_schedule}
        '''
        result = self._values.get("notify_on_call_from_schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def persons_to_notify(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of ID's of users for notify_persons type step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#persons_to_notify OncallEscalation#persons_to_notify}
        '''
        result = self._values.get("persons_to_notify")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def persons_to_notify_next_each_time(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of ID's of users for notify_person_next_each_time type step.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#persons_to_notify_next_each_time OncallEscalation#persons_to_notify_next_each_time}
        '''
        result = self._values.get("persons_to_notify_next_each_time")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of escalation policy. Can be wait, notify_persons, notify_person_next_each_time, notify_on_call_from_schedule, trigger_action, notify_user_group, resolve, notify_whole_channel, notify_if_time_from_to, repeat_escalation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_escalation#type OncallEscalation#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallEscalationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OncallEscalation",
    "OncallEscalationConfig",
]

publication.publish()

def _typecheckingstub__0c0ddd010e698de33431c8bcdb44d6087d22ccd58c2a5a4c652cfac12148445b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    escalation_chain_id: builtins.str,
    position: jsii.Number,
    action_to_trigger: typing.Optional[builtins.str] = None,
    duration: typing.Optional[jsii.Number] = None,
    group_to_notify: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    important: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    notify_if_time_from: typing.Optional[builtins.str] = None,
    notify_if_time_to: typing.Optional[builtins.str] = None,
    notify_on_call_from_schedule: typing.Optional[builtins.str] = None,
    persons_to_notify: typing.Optional[typing.Sequence[builtins.str]] = None,
    persons_to_notify_next_each_time: typing.Optional[typing.Sequence[builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__f58b51ee66266e9e28fae1b6784daa5be612fdad30459d9846a89232ac9d02c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dd8016af034e268826d4c50cf76d428bf5d4e099b1b0191509a322801f88d09(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66f6a91630b2672a4f5e46c93b3b79ef426c161eb412e1194fc6f64979113c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7edff4805b4abd45beff4c87e67a7b5c0fc813bee0c8c928f80317e4122388d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88444bafccbbc17311696d9acf9a05d3842dc0b92013f5e7add4f2168f738adf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__876c829a3002783361cb37f83457607fff4df5b9dea73ed56cfb37bb58e2fb1d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3b5dfa844ea3a53b914526e7f5e3b23a23ebd1e47c67f94f2cdc69405ef7f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f7916ea6bdde1643196aefc43cc1896e81bd659eb32764e2bdb5d0f77727f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab99534ae630b28ff63f95922348d0a5f4a47323c884418aea513d91dae3dbc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b5c1dc662d50d5f450f83d25d5d5ce6de1699b8be3642f6f4310d44078f5dc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd788c0c9e7da776707fa8531b24769a74c7b8685ff9e9e9ccde108c0531b1a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20577dfd3d0e234ab159a482bfc9842d7b28da5660a268e3a7a669393b692215(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784e2b23f6065b7bb68ef7bc08cad263860dbcba06748592474822ad8ede8d06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7938a7e1f33613e000055dc885911d2cdd0eadb34f12a6cf429e037ce2bf90a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    escalation_chain_id: builtins.str,
    position: jsii.Number,
    action_to_trigger: typing.Optional[builtins.str] = None,
    duration: typing.Optional[jsii.Number] = None,
    group_to_notify: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    important: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    notify_if_time_from: typing.Optional[builtins.str] = None,
    notify_if_time_to: typing.Optional[builtins.str] = None,
    notify_on_call_from_schedule: typing.Optional[builtins.str] = None,
    persons_to_notify: typing.Optional[typing.Sequence[builtins.str]] = None,
    persons_to_notify_next_each_time: typing.Optional[typing.Sequence[builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
