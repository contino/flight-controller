'''
# `grafana_rule_group`

Refer to the Terraform Registory for docs: [`grafana_rule_group`](https://www.terraform.io/docs/providers/grafana/r/rule_group).
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


class RuleGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.ruleGroup.RuleGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/rule_group grafana_rule_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        folder_uid: builtins.str,
        interval_seconds: jsii.Number,
        name: builtins.str,
        org_id: jsii.Number,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RuleGroupRule", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/rule_group grafana_rule_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param folder_uid: The UID of the folder that the group belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#folder_uid RuleGroup#folder_uid}
        :param interval_seconds: The interval, in seconds, at which all rules in the group are evaluated. If a group contains many rules, the rules are evaluated sequentially. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#interval_seconds RuleGroup#interval_seconds}
        :param name: The name of the rule group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#name RuleGroup#name}
        :param org_id: The ID of the org to which the group belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#org_id RuleGroup#org_id}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#rule RuleGroup#rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#id RuleGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50128c4e1c02fab7bbd499c813788bbf86ff420e4e25fa46e8f523b43c1c88e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RuleGroupConfig(
            folder_uid=folder_uid,
            interval_seconds=interval_seconds,
            name=name,
            org_id=org_id,
            rule=rule,
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

    @jsii.member(jsii_name="putRule")
    def put_rule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RuleGroupRule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d09afca9721143ae3ee180306b592b5ea9744f4d7c8d54cd35d29cf418ec5647)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRule", [value]))

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
    @jsii.member(jsii_name="rule")
    def rule(self) -> "RuleGroupRuleList":
        return typing.cast("RuleGroupRuleList", jsii.get(self, "rule"))

    @builtins.property
    @jsii.member(jsii_name="folderUidInput")
    def folder_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderUidInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalSecondsInput")
    def interval_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orgIdInput")
    def org_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orgIdInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RuleGroupRule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RuleGroupRule"]]], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="folderUid")
    def folder_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folderUid"))

    @folder_uid.setter
    def folder_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80aec6565f44be4336eb0232da3c282f6e57d1ab1c2dd58e6360745f2957f38a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folderUid", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cccd0606a5ff3ba4ffc0cf6ea09dcada2d72dd373b2afbbe1910bd6dc7754f9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="intervalSeconds")
    def interval_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "intervalSeconds"))

    @interval_seconds.setter
    def interval_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d446fe8ee5bec0a3290fab55691b34f993a01b5d2a13492f93451e243ee1a71a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "intervalSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3005574cb0a06a494bc028ae937c9e83ca92248121f7434ac652f0367247f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "orgId"))

    @org_id.setter
    def org_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba093fca01e631d467c3366165cfc22cdebcff1fd8330de4a0f12fa03427a0eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgId", value)


@jsii.data_type(
    jsii_type="grafana.ruleGroup.RuleGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "folder_uid": "folderUid",
        "interval_seconds": "intervalSeconds",
        "name": "name",
        "org_id": "orgId",
        "rule": "rule",
        "id": "id",
    },
)
class RuleGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        folder_uid: builtins.str,
        interval_seconds: jsii.Number,
        name: builtins.str,
        org_id: jsii.Number,
        rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RuleGroupRule", typing.Dict[builtins.str, typing.Any]]]],
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
        :param folder_uid: The UID of the folder that the group belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#folder_uid RuleGroup#folder_uid}
        :param interval_seconds: The interval, in seconds, at which all rules in the group are evaluated. If a group contains many rules, the rules are evaluated sequentially. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#interval_seconds RuleGroup#interval_seconds}
        :param name: The name of the rule group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#name RuleGroup#name}
        :param org_id: The ID of the org to which the group belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#org_id RuleGroup#org_id}
        :param rule: rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#rule RuleGroup#rule}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#id RuleGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6773ed1a88c39ec3e119bf9874ac3cbc8e7318d6de1ad5cf0225f802c0a2f676)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument folder_uid", value=folder_uid, expected_type=type_hints["folder_uid"])
            check_type(argname="argument interval_seconds", value=interval_seconds, expected_type=type_hints["interval_seconds"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "folder_uid": folder_uid,
            "interval_seconds": interval_seconds,
            "name": name,
            "org_id": org_id,
            "rule": rule,
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
    def folder_uid(self) -> builtins.str:
        '''The UID of the folder that the group belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#folder_uid RuleGroup#folder_uid}
        '''
        result = self._values.get("folder_uid")
        assert result is not None, "Required property 'folder_uid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def interval_seconds(self) -> jsii.Number:
        '''The interval, in seconds, at which all rules in the group are evaluated.

        If a group contains many rules, the rules are evaluated sequentially.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#interval_seconds RuleGroup#interval_seconds}
        '''
        result = self._values.get("interval_seconds")
        assert result is not None, "Required property 'interval_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#name RuleGroup#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def org_id(self) -> jsii.Number:
        '''The ID of the org to which the group belongs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#org_id RuleGroup#org_id}
        '''
        result = self._values.get("org_id")
        assert result is not None, "Required property 'org_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RuleGroupRule"]]:
        '''rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#rule RuleGroup#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RuleGroupRule"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#id RuleGroup#id}.

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
        return "RuleGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.ruleGroup.RuleGroupRule",
    jsii_struct_bases=[],
    name_mapping={
        "condition": "condition",
        "data": "data",
        "name": "name",
        "annotations": "annotations",
        "exec_err_state": "execErrState",
        "for_": "for",
        "labels": "labels",
        "no_data_state": "noDataState",
    },
)
class RuleGroupRule:
    def __init__(
        self,
        *,
        condition: builtins.str,
        data: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["RuleGroupRuleData", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        exec_err_state: typing.Optional[builtins.str] = None,
        for_: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        no_data_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param condition: The ``ref_id`` of the query node in the ``data`` field to use as the alert condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#condition RuleGroup#condition}
        :param data: data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#data RuleGroup#data}
        :param name: The name of the alert rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#name RuleGroup#name}
        :param annotations: Key-value pairs of metadata to attach to the alert rule that may add user-defined context, but cannot be used for matching, grouping, or routing. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#annotations RuleGroup#annotations}
        :param exec_err_state: Describes what state to enter when the rule's query is invalid and the rule cannot be executed. Options are OK, Error, and Alerting. Defaults to ``Alerting``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#exec_err_state RuleGroup#exec_err_state}
        :param for_: The amount of time for which the rule must be breached for the rule to be considered to be Firing. Before this time has elapsed, the rule is only considered to be Pending. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#for RuleGroup#for}
        :param labels: Key-value pairs to attach to the alert rule that can be used in matching, grouping, and routing. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#labels RuleGroup#labels}
        :param no_data_state: Describes what state to enter when the rule's query returns No Data. Options are OK, NoData, and Alerting. Defaults to ``NoData``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#no_data_state RuleGroup#no_data_state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ade6976a498025763ddb29d3cb7fc2a0c7ee0c0a22e5dd1ced1587c174a88c2)
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument exec_err_state", value=exec_err_state, expected_type=type_hints["exec_err_state"])
            check_type(argname="argument for_", value=for_, expected_type=type_hints["for_"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument no_data_state", value=no_data_state, expected_type=type_hints["no_data_state"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "condition": condition,
            "data": data,
            "name": name,
        }
        if annotations is not None:
            self._values["annotations"] = annotations
        if exec_err_state is not None:
            self._values["exec_err_state"] = exec_err_state
        if for_ is not None:
            self._values["for_"] = for_
        if labels is not None:
            self._values["labels"] = labels
        if no_data_state is not None:
            self._values["no_data_state"] = no_data_state

    @builtins.property
    def condition(self) -> builtins.str:
        '''The ``ref_id`` of the query node in the ``data`` field to use as the alert condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#condition RuleGroup#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RuleGroupRuleData"]]:
        '''data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#data RuleGroup#data}
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["RuleGroupRuleData"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the alert rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#name RuleGroup#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs of metadata to attach to the alert rule that may add user-defined context, but cannot be used for matching, grouping, or routing.

        Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#annotations RuleGroup#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def exec_err_state(self) -> typing.Optional[builtins.str]:
        '''Describes what state to enter when the rule's query is invalid and the rule cannot be executed.

        Options are OK, Error, and Alerting. Defaults to ``Alerting``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#exec_err_state RuleGroup#exec_err_state}
        '''
        result = self._values.get("exec_err_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def for_(self) -> typing.Optional[builtins.str]:
        '''The amount of time for which the rule must be breached for the rule to be considered to be Firing.

        Before this time has elapsed, the rule is only considered to be Pending. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#for RuleGroup#for}
        '''
        result = self._values.get("for_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Key-value pairs to attach to the alert rule that can be used in matching, grouping, and routing.

        Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#labels RuleGroup#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def no_data_state(self) -> typing.Optional[builtins.str]:
        '''Describes what state to enter when the rule's query returns No Data.

        Options are OK, NoData, and Alerting. Defaults to ``NoData``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#no_data_state RuleGroup#no_data_state}
        '''
        result = self._values.get("no_data_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleGroupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.ruleGroup.RuleGroupRuleData",
    jsii_struct_bases=[],
    name_mapping={
        "datasource_uid": "datasourceUid",
        "model": "model",
        "ref_id": "refId",
        "relative_time_range": "relativeTimeRange",
        "query_type": "queryType",
    },
)
class RuleGroupRuleData:
    def __init__(
        self,
        *,
        datasource_uid: builtins.str,
        model: builtins.str,
        ref_id: builtins.str,
        relative_time_range: typing.Union["RuleGroupRuleDataRelativeTimeRange", typing.Dict[builtins.str, typing.Any]],
        query_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datasource_uid: The UID of the datasource being queried, or "-100" if this stage is an expression stage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#datasource_uid RuleGroup#datasource_uid}
        :param model: Custom JSON data to send to the specified datasource when querying. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#model RuleGroup#model}
        :param ref_id: A unique string to identify this query stage within a rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#ref_id RuleGroup#ref_id}
        :param relative_time_range: relative_time_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#relative_time_range RuleGroup#relative_time_range}
        :param query_type: An optional identifier for the type of query being executed. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#query_type RuleGroup#query_type}
        '''
        if isinstance(relative_time_range, dict):
            relative_time_range = RuleGroupRuleDataRelativeTimeRange(**relative_time_range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df8dc6f2584d68eafc61bfe33e35754aad7f8ec9eaf4ecf46eee5b97743b7463)
            check_type(argname="argument datasource_uid", value=datasource_uid, expected_type=type_hints["datasource_uid"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
            check_type(argname="argument ref_id", value=ref_id, expected_type=type_hints["ref_id"])
            check_type(argname="argument relative_time_range", value=relative_time_range, expected_type=type_hints["relative_time_range"])
            check_type(argname="argument query_type", value=query_type, expected_type=type_hints["query_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datasource_uid": datasource_uid,
            "model": model,
            "ref_id": ref_id,
            "relative_time_range": relative_time_range,
        }
        if query_type is not None:
            self._values["query_type"] = query_type

    @builtins.property
    def datasource_uid(self) -> builtins.str:
        '''The UID of the datasource being queried, or "-100" if this stage is an expression stage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#datasource_uid RuleGroup#datasource_uid}
        '''
        result = self._values.get("datasource_uid")
        assert result is not None, "Required property 'datasource_uid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model(self) -> builtins.str:
        '''Custom JSON data to send to the specified datasource when querying.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#model RuleGroup#model}
        '''
        result = self._values.get("model")
        assert result is not None, "Required property 'model' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ref_id(self) -> builtins.str:
        '''A unique string to identify this query stage within a rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#ref_id RuleGroup#ref_id}
        '''
        result = self._values.get("ref_id")
        assert result is not None, "Required property 'ref_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relative_time_range(self) -> "RuleGroupRuleDataRelativeTimeRange":
        '''relative_time_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#relative_time_range RuleGroup#relative_time_range}
        '''
        result = self._values.get("relative_time_range")
        assert result is not None, "Required property 'relative_time_range' is missing"
        return typing.cast("RuleGroupRuleDataRelativeTimeRange", result)

    @builtins.property
    def query_type(self) -> typing.Optional[builtins.str]:
        '''An optional identifier for the type of query being executed. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#query_type RuleGroup#query_type}
        '''
        result = self._values.get("query_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleGroupRuleData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RuleGroupRuleDataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.ruleGroup.RuleGroupRuleDataList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16bc59691247a726a8675b1d959001c7e94011dc72c367db567f9a870e01dc98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RuleGroupRuleDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fb0ae4227361984cac30869ace22238bffbfef0e6c640db04fbd2d87dcfdf50)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RuleGroupRuleDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13b3b84ecc6ca869f002f01ae9a9fa3239b166bcb60cc0a586385f172b461be6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e95130d6751a8cbb79f1dfea345ef48a84029dbd5e40ed5adc4777bc200b0c1e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c984a82ec7aed80abcf801bfd0ea5ed49651d819e5c9d78ea29838d1a45c046)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRuleData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRuleData]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRuleData]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b09c43f1c7935b455cb3f5b3013eae3c0809a1c11b14f8f8a560166e644f1d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RuleGroupRuleDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.ruleGroup.RuleGroupRuleDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2aa52d1e771e3e6218129682dcde61e8e95778cee9e9c3ae709d5abdca737632)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRelativeTimeRange")
    def put_relative_time_range(self, *, from_: jsii.Number, to: jsii.Number) -> None:
        '''
        :param from_: The number of seconds in the past, relative to when the rule is evaluated, at which the time range begins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#from RuleGroup#from}
        :param to: The number of seconds in the past, relative to when the rule is evaluated, at which the time range ends. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#to RuleGroup#to}
        '''
        value = RuleGroupRuleDataRelativeTimeRange(from_=from_, to=to)

        return typing.cast(None, jsii.invoke(self, "putRelativeTimeRange", [value]))

    @jsii.member(jsii_name="resetQueryType")
    def reset_query_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryType", []))

    @builtins.property
    @jsii.member(jsii_name="relativeTimeRange")
    def relative_time_range(
        self,
    ) -> "RuleGroupRuleDataRelativeTimeRangeOutputReference":
        return typing.cast("RuleGroupRuleDataRelativeTimeRangeOutputReference", jsii.get(self, "relativeTimeRange"))

    @builtins.property
    @jsii.member(jsii_name="datasourceUidInput")
    def datasource_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasourceUidInput"))

    @builtins.property
    @jsii.member(jsii_name="modelInput")
    def model_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelInput"))

    @builtins.property
    @jsii.member(jsii_name="queryTypeInput")
    def query_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="refIdInput")
    def ref_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "refIdInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeTimeRangeInput")
    def relative_time_range_input(
        self,
    ) -> typing.Optional["RuleGroupRuleDataRelativeTimeRange"]:
        return typing.cast(typing.Optional["RuleGroupRuleDataRelativeTimeRange"], jsii.get(self, "relativeTimeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="datasourceUid")
    def datasource_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasourceUid"))

    @datasource_uid.setter
    def datasource_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e632b25c0bab2d1e0adee626a130ba2d3225635744336859381c0b8e171497b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasourceUid", value)

    @builtins.property
    @jsii.member(jsii_name="model")
    def model(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "model"))

    @model.setter
    def model(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d417f7dbbcfa5385cc3a4f86127ce3dcb7d9d86955cf6af2ea207f7f58d2ec61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "model", value)

    @builtins.property
    @jsii.member(jsii_name="queryType")
    def query_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryType"))

    @query_type.setter
    def query_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be7b64f15c8cbb80a0bc0713b9245878a4ffd1415c7f4dda6e25186b74e252a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryType", value)

    @builtins.property
    @jsii.member(jsii_name="refId")
    def ref_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "refId"))

    @ref_id.setter
    def ref_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc5487ab35e20ef79d8472332b2c63497722ae431eb7e697fd5956bdbc81594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RuleGroupRuleData, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RuleGroupRuleData, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RuleGroupRuleData, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5daf07d5730d2e686a2f50173d9fbf08620de01511cbb78749ff05d2a4160431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.ruleGroup.RuleGroupRuleDataRelativeTimeRange",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class RuleGroupRuleDataRelativeTimeRange:
    def __init__(self, *, from_: jsii.Number, to: jsii.Number) -> None:
        '''
        :param from_: The number of seconds in the past, relative to when the rule is evaluated, at which the time range begins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#from RuleGroup#from}
        :param to: The number of seconds in the past, relative to when the rule is evaluated, at which the time range ends. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#to RuleGroup#to}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bb87b68554d249ee24db35a7320a34f1be4fc502018832ae8c256b4f223575c)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument to", value=to, expected_type=type_hints["to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "from_": from_,
            "to": to,
        }

    @builtins.property
    def from_(self) -> jsii.Number:
        '''The number of seconds in the past, relative to when the rule is evaluated, at which the time range begins.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#from RuleGroup#from}
        '''
        result = self._values.get("from_")
        assert result is not None, "Required property 'from_' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def to(self) -> jsii.Number:
        '''The number of seconds in the past, relative to when the rule is evaluated, at which the time range ends.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/rule_group#to RuleGroup#to}
        '''
        result = self._values.get("to")
        assert result is not None, "Required property 'to' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleGroupRuleDataRelativeTimeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RuleGroupRuleDataRelativeTimeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.ruleGroup.RuleGroupRuleDataRelativeTimeRangeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78028c0324f5ebd8f90bf27c03de9fca8f6680cdec6d9641815219e4b7d6ab46)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="toInput")
    def to_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "toInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de4b7ed18b1e9c7f0eb0aabf31b5097e369f337b6d2c8ffbdaf70181f84adf94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "to"))

    @to.setter
    def to(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59576f7b0b3d54dc0c1e159bbcdf3cf06d85d3df90e2cfd95b5d0b0331a1d487)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "to", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RuleGroupRuleDataRelativeTimeRange]:
        return typing.cast(typing.Optional[RuleGroupRuleDataRelativeTimeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[RuleGroupRuleDataRelativeTimeRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d98961a613caab811a3b57c249cf93900b3dd891ce527be8ca44ea79dd2662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RuleGroupRuleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.ruleGroup.RuleGroupRuleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__347981d94c21d38b6d268c17677d3249457b8f4e4afd24b7937c26e8399119f7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RuleGroupRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02fbbb2f334d2e2157a200a9682c4b6d2629f8ababab7f1aeee87a1a1f0e4867)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RuleGroupRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7486efe7c15f3151e1bc0676920f199d14346c052c4298eb1177370579e58375)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba9745a35d1a74c2c07558b76c3ddd7ac24fb4fc283a5bd85a156c4fc45c2fe9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8034242dc59b03574bddd962aba33795f1b007d75b19f390a16460aa29d1b7ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf7317f51f35f4b07201de5c1771bb2908c8551ec1c6c4b53734c2fd024383a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RuleGroupRuleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.ruleGroup.RuleGroupRuleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0285f08ebb7f8b631ac324b36af0337ca1b4d75e3b3acae564b5bd06de1583aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putData")
    def put_data(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RuleGroupRuleData, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eff53a0cd9673d8245f7d3de93dc712b1ab9221081f7a63fd7516772fea06714)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putData", [value]))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetExecErrState")
    def reset_exec_err_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecErrState", []))

    @jsii.member(jsii_name="resetFor")
    def reset_for(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFor", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetNoDataState")
    def reset_no_data_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoDataState", []))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> RuleGroupRuleDataList:
        return typing.cast(RuleGroupRuleDataList, jsii.get(self, "data"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRuleData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRuleData]]], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="execErrStateInput")
    def exec_err_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "execErrStateInput"))

    @builtins.property
    @jsii.member(jsii_name="forInput")
    def for_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="noDataStateInput")
    def no_data_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noDataStateInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62cb01749d7c4b2ea74c434b20b7127672ca567a9d7f8fdd1b152e7b70f570bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "condition"))

    @condition.setter
    def condition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ca994ea85da034603ced4f0d3b17321f84fc84efe25947824d8f55e9a6b3080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "condition", value)

    @builtins.property
    @jsii.member(jsii_name="execErrState")
    def exec_err_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "execErrState"))

    @exec_err_state.setter
    def exec_err_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bc35a2cf8bcbb3c7f03a5b61681b21b2e08ebda4f0a3379d9bff392797584b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "execErrState", value)

    @builtins.property
    @jsii.member(jsii_name="for")
    def for_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "for"))

    @for_.setter
    def for_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b3f0a6d744c2e91253be7fb18bcaa8fa2ccd1f6bea87bb206a7f2a9229d50c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "for", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd9e5e49eb73728c2e52ab37d641afa8f40e0d98a8feeb9f02d78ba135f86fa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06996b718b10d89af3ef7887b77121d73f16f414cc89749b27602bdb1740fadd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="noDataState")
    def no_data_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noDataState"))

    @no_data_state.setter
    def no_data_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4980fd46f6bd956bc85f46147ea0e54bfd4b3aeb0f1682310c7dcfcca8ebbe27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noDataState", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RuleGroupRule, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RuleGroupRule, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RuleGroupRule, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f52fafa7df5acc2cd3bf664e3bf85a6835cb6e858561c8e0f81b7a75c5effad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RuleGroup",
    "RuleGroupConfig",
    "RuleGroupRule",
    "RuleGroupRuleData",
    "RuleGroupRuleDataList",
    "RuleGroupRuleDataOutputReference",
    "RuleGroupRuleDataRelativeTimeRange",
    "RuleGroupRuleDataRelativeTimeRangeOutputReference",
    "RuleGroupRuleList",
    "RuleGroupRuleOutputReference",
]

publication.publish()

def _typecheckingstub__50128c4e1c02fab7bbd499c813788bbf86ff420e4e25fa46e8f523b43c1c88e7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    folder_uid: builtins.str,
    interval_seconds: jsii.Number,
    name: builtins.str,
    org_id: jsii.Number,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RuleGroupRule, typing.Dict[builtins.str, typing.Any]]]],
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

def _typecheckingstub__d09afca9721143ae3ee180306b592b5ea9744f4d7c8d54cd35d29cf418ec5647(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RuleGroupRule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80aec6565f44be4336eb0232da3c282f6e57d1ab1c2dd58e6360745f2957f38a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cccd0606a5ff3ba4ffc0cf6ea09dcada2d72dd373b2afbbe1910bd6dc7754f9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d446fe8ee5bec0a3290fab55691b34f993a01b5d2a13492f93451e243ee1a71a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3005574cb0a06a494bc028ae937c9e83ca92248121f7434ac652f0367247f7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba093fca01e631d467c3366165cfc22cdebcff1fd8330de4a0f12fa03427a0eb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6773ed1a88c39ec3e119bf9874ac3cbc8e7318d6de1ad5cf0225f802c0a2f676(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    folder_uid: builtins.str,
    interval_seconds: jsii.Number,
    name: builtins.str,
    org_id: jsii.Number,
    rule: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RuleGroupRule, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ade6976a498025763ddb29d3cb7fc2a0c7ee0c0a22e5dd1ced1587c174a88c2(
    *,
    condition: builtins.str,
    data: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RuleGroupRuleData, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    exec_err_state: typing.Optional[builtins.str] = None,
    for_: typing.Optional[builtins.str] = None,
    labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    no_data_state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df8dc6f2584d68eafc61bfe33e35754aad7f8ec9eaf4ecf46eee5b97743b7463(
    *,
    datasource_uid: builtins.str,
    model: builtins.str,
    ref_id: builtins.str,
    relative_time_range: typing.Union[RuleGroupRuleDataRelativeTimeRange, typing.Dict[builtins.str, typing.Any]],
    query_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16bc59691247a726a8675b1d959001c7e94011dc72c367db567f9a870e01dc98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fb0ae4227361984cac30869ace22238bffbfef0e6c640db04fbd2d87dcfdf50(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13b3b84ecc6ca869f002f01ae9a9fa3239b166bcb60cc0a586385f172b461be6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e95130d6751a8cbb79f1dfea345ef48a84029dbd5e40ed5adc4777bc200b0c1e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c984a82ec7aed80abcf801bfd0ea5ed49651d819e5c9d78ea29838d1a45c046(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09c43f1c7935b455cb3f5b3013eae3c0809a1c11b14f8f8a560166e644f1d80(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRuleData]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa52d1e771e3e6218129682dcde61e8e95778cee9e9c3ae709d5abdca737632(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e632b25c0bab2d1e0adee626a130ba2d3225635744336859381c0b8e171497b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d417f7dbbcfa5385cc3a4f86127ce3dcb7d9d86955cf6af2ea207f7f58d2ec61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be7b64f15c8cbb80a0bc0713b9245878a4ffd1415c7f4dda6e25186b74e252a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fc5487ab35e20ef79d8472332b2c63497722ae431eb7e697fd5956bdbc81594(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5daf07d5730d2e686a2f50173d9fbf08620de01511cbb78749ff05d2a4160431(
    value: typing.Optional[typing.Union[RuleGroupRuleData, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb87b68554d249ee24db35a7320a34f1be4fc502018832ae8c256b4f223575c(
    *,
    from_: jsii.Number,
    to: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78028c0324f5ebd8f90bf27c03de9fca8f6680cdec6d9641815219e4b7d6ab46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de4b7ed18b1e9c7f0eb0aabf31b5097e369f337b6d2c8ffbdaf70181f84adf94(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59576f7b0b3d54dc0c1e159bbcdf3cf06d85d3df90e2cfd95b5d0b0331a1d487(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d98961a613caab811a3b57c249cf93900b3dd891ce527be8ca44ea79dd2662(
    value: typing.Optional[RuleGroupRuleDataRelativeTimeRange],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__347981d94c21d38b6d268c17677d3249457b8f4e4afd24b7937c26e8399119f7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02fbbb2f334d2e2157a200a9682c4b6d2629f8ababab7f1aeee87a1a1f0e4867(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7486efe7c15f3151e1bc0676920f199d14346c052c4298eb1177370579e58375(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9745a35d1a74c2c07558b76c3ddd7ac24fb4fc283a5bd85a156c4fc45c2fe9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8034242dc59b03574bddd962aba33795f1b007d75b19f390a16460aa29d1b7ad(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf7317f51f35f4b07201de5c1771bb2908c8551ec1c6c4b53734c2fd024383a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[RuleGroupRule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0285f08ebb7f8b631ac324b36af0337ca1b4d75e3b3acae564b5bd06de1583aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eff53a0cd9673d8245f7d3de93dc712b1ab9221081f7a63fd7516772fea06714(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[RuleGroupRuleData, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62cb01749d7c4b2ea74c434b20b7127672ca567a9d7f8fdd1b152e7b70f570bf(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ca994ea85da034603ced4f0d3b17321f84fc84efe25947824d8f55e9a6b3080(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc35a2cf8bcbb3c7f03a5b61681b21b2e08ebda4f0a3379d9bff392797584b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b3f0a6d744c2e91253be7fb18bcaa8fa2ccd1f6bea87bb206a7f2a9229d50c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd9e5e49eb73728c2e52ab37d641afa8f40e0d98a8feeb9f02d78ba135f86fa4(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06996b718b10d89af3ef7887b77121d73f16f414cc89749b27602bdb1740fadd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4980fd46f6bd956bc85f46147ea0e54bfd4b3aeb0f1682310c7dcfcca8ebbe27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52fafa7df5acc2cd3bf664e3bf85a6835cb6e858561c8e0f81b7a75c5effad7(
    value: typing.Optional[typing.Union[RuleGroupRule, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
