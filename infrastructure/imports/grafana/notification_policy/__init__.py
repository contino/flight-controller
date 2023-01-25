'''
# `grafana_notification_policy`

Refer to the Terraform Registory for docs: [`grafana_notification_policy`](https://www.terraform.io/docs/providers/grafana/r/notification_policy).
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


class NotificationPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.notificationPolicy.NotificationPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy grafana_notification_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        contact_point: builtins.str,
        group_by: typing.Sequence[builtins.str],
        group_interval: typing.Optional[builtins.str] = None,
        group_wait: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        repeat_interval: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy grafana_notification_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param contact_point: The default contact point to route all unmatched notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#contact_point NotificationPolicy#contact_point}
        :param group_by: A list of alert labels to group alerts into notifications by. Use the special label ``...`` to group alerts by all labels, effectively disabling grouping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_by NotificationPolicy#group_by}
        :param group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_interval NotificationPolicy#group_interval}
        :param group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_wait NotificationPolicy#group_wait}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#policy NotificationPolicy#policy}
        :param repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#repeat_interval NotificationPolicy#repeat_interval}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bce565b6db2279c3f5d8fff3770bf1a256f91c5e0cd96fcc74bf2452291b8cb4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = NotificationPolicyConfig(
            contact_point=contact_point,
            group_by=group_by,
            group_interval=group_interval,
            group_wait=group_wait,
            id=id,
            policy=policy,
            repeat_interval=repeat_interval,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPolicy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8ae5510ebd1ce63e648613531ea6500dd69055c2f59da92b7531e36790ff150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetGroupInterval")
    def reset_group_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupInterval", []))

    @jsii.member(jsii_name="resetGroupWait")
    def reset_group_wait(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupWait", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetRepeatInterval")
    def reset_repeat_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepeatInterval", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "NotificationPolicyPolicyList":
        return typing.cast("NotificationPolicyPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="contactPointInput")
    def contact_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactPointInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByInput")
    def group_by_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIntervalInput")
    def group_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="groupWaitInput")
    def group_wait_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupWaitInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="repeatIntervalInput")
    def repeat_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repeatIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="contactPoint")
    def contact_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactPoint"))

    @contact_point.setter
    def contact_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50af456760b885915bffbf8cda9a6b2d8ecdc5767c289f9df85ef2460fe0c322)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPoint", value)

    @builtins.property
    @jsii.member(jsii_name="groupBy")
    def group_by(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupBy"))

    @group_by.setter
    def group_by(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d800b31da61e0e2dc76c8033307903adad94150e67708ea2c4debe74407078b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupBy", value)

    @builtins.property
    @jsii.member(jsii_name="groupInterval")
    def group_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupInterval"))

    @group_interval.setter
    def group_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9bab2a71c71eaa17aa5a7ef7ddc0b18d349a88794ec206efd2ac51863c7477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupInterval", value)

    @builtins.property
    @jsii.member(jsii_name="groupWait")
    def group_wait(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupWait"))

    @group_wait.setter
    def group_wait(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b082345e2356ddba899976d95df263a343654d4a1ed25df78333ed031a42f39e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupWait", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20988768fbd8a9bbf00ccfa8d564ea3bb11978d84a765fcc5f3711ade16c3b4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="repeatInterval")
    def repeat_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repeatInterval"))

    @repeat_interval.setter
    def repeat_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__531530f4290bbc1acd22ef76f9be48ec10de1ee3a1795bf0d6e0048d55231c8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repeatInterval", value)


@jsii.data_type(
    jsii_type="grafana.notificationPolicy.NotificationPolicyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "contact_point": "contactPoint",
        "group_by": "groupBy",
        "group_interval": "groupInterval",
        "group_wait": "groupWait",
        "id": "id",
        "policy": "policy",
        "repeat_interval": "repeatInterval",
    },
)
class NotificationPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        contact_point: builtins.str,
        group_by: typing.Sequence[builtins.str],
        group_interval: typing.Optional[builtins.str] = None,
        group_wait: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        repeat_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param contact_point: The default contact point to route all unmatched notifications to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#contact_point NotificationPolicy#contact_point}
        :param group_by: A list of alert labels to group alerts into notifications by. Use the special label ``...`` to group alerts by all labels, effectively disabling grouping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_by NotificationPolicy#group_by}
        :param group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_interval NotificationPolicy#group_interval}
        :param group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_wait NotificationPolicy#group_wait}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#id NotificationPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#policy NotificationPolicy#policy}
        :param repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#repeat_interval NotificationPolicy#repeat_interval}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c7ff14dbfd7d743876fd240ccf13dacb0fd2fc00b08b9aa2bf37eda766f4c8)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument contact_point", value=contact_point, expected_type=type_hints["contact_point"])
            check_type(argname="argument group_by", value=group_by, expected_type=type_hints["group_by"])
            check_type(argname="argument group_interval", value=group_interval, expected_type=type_hints["group_interval"])
            check_type(argname="argument group_wait", value=group_wait, expected_type=type_hints["group_wait"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument repeat_interval", value=repeat_interval, expected_type=type_hints["repeat_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_point": contact_point,
            "group_by": group_by,
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
        if group_interval is not None:
            self._values["group_interval"] = group_interval
        if group_wait is not None:
            self._values["group_wait"] = group_wait
        if id is not None:
            self._values["id"] = id
        if policy is not None:
            self._values["policy"] = policy
        if repeat_interval is not None:
            self._values["repeat_interval"] = repeat_interval

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
    def contact_point(self) -> builtins.str:
        '''The default contact point to route all unmatched notifications to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#contact_point NotificationPolicy#contact_point}
        '''
        result = self._values.get("contact_point")
        assert result is not None, "Required property 'contact_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_by(self) -> typing.List[builtins.str]:
        '''A list of alert labels to group alerts into notifications by.

        Use the special label ``...`` to group alerts by all labels, effectively disabling grouping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_by NotificationPolicy#group_by}
        '''
        result = self._values.get("group_by")
        assert result is not None, "Required property 'group_by' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def group_interval(self) -> typing.Optional[builtins.str]:
        '''Minimum time interval between two notifications for the same group. Default is 5 minutes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_interval NotificationPolicy#group_interval}
        '''
        result = self._values.get("group_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_wait(self) -> typing.Optional[builtins.str]:
        '''Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_wait NotificationPolicy#group_wait}
        '''
        result = self._values.get("group_wait")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#id NotificationPolicy#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicy"]]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#policy NotificationPolicy#policy}
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicy"]]], result)

    @builtins.property
    def repeat_interval(self) -> typing.Optional[builtins.str]:
        '''Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#repeat_interval NotificationPolicy#repeat_interval}
        '''
        result = self._values.get("repeat_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.notificationPolicy.NotificationPolicyPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "contact_point": "contactPoint",
        "group_by": "groupBy",
        "continue_": "continue",
        "group_interval": "groupInterval",
        "group_wait": "groupWait",
        "matcher": "matcher",
        "mute_timings": "muteTimings",
        "policy": "policy",
        "repeat_interval": "repeatInterval",
    },
)
class NotificationPolicyPolicy:
    def __init__(
        self,
        *,
        contact_point: builtins.str,
        group_by: typing.Sequence[builtins.str],
        continue_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group_interval: typing.Optional[builtins.str] = None,
        group_wait: typing.Optional[builtins.str] = None,
        matcher: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPolicyMatcher", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mute_timings: typing.Optional[typing.Sequence[builtins.str]] = None,
        policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["NotificationPolicyPolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        repeat_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param contact_point: The contact point to route notifications that match this rule to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#contact_point NotificationPolicy#contact_point}
        :param group_by: A list of alert labels to group alerts into notifications by. Use the special label ``...`` to group alerts by all labels, effectively disabling grouping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_by NotificationPolicy#group_by}
        :param continue_: Whether to continue matching subsequent rules if an alert matches the current rule. Otherwise, the rule will be 'consumed' by the first policy to match it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#continue NotificationPolicy#continue}
        :param group_interval: Minimum time interval between two notifications for the same group. Default is 5 minutes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_interval NotificationPolicy#group_interval}
        :param group_wait: Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_wait NotificationPolicy#group_wait}
        :param matcher: matcher block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#matcher NotificationPolicy#matcher}
        :param mute_timings: A list of mute timing names to apply to alerts that match this policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#mute_timings NotificationPolicy#mute_timings}
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#policy NotificationPolicy#policy}
        :param repeat_interval: Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#repeat_interval NotificationPolicy#repeat_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b34c76bdfca40defc5d949b4766683367d78eb70548acf407719275fb295168)
            check_type(argname="argument contact_point", value=contact_point, expected_type=type_hints["contact_point"])
            check_type(argname="argument group_by", value=group_by, expected_type=type_hints["group_by"])
            check_type(argname="argument continue_", value=continue_, expected_type=type_hints["continue_"])
            check_type(argname="argument group_interval", value=group_interval, expected_type=type_hints["group_interval"])
            check_type(argname="argument group_wait", value=group_wait, expected_type=type_hints["group_wait"])
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument mute_timings", value=mute_timings, expected_type=type_hints["mute_timings"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument repeat_interval", value=repeat_interval, expected_type=type_hints["repeat_interval"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_point": contact_point,
            "group_by": group_by,
        }
        if continue_ is not None:
            self._values["continue_"] = continue_
        if group_interval is not None:
            self._values["group_interval"] = group_interval
        if group_wait is not None:
            self._values["group_wait"] = group_wait
        if matcher is not None:
            self._values["matcher"] = matcher
        if mute_timings is not None:
            self._values["mute_timings"] = mute_timings
        if policy is not None:
            self._values["policy"] = policy
        if repeat_interval is not None:
            self._values["repeat_interval"] = repeat_interval

    @builtins.property
    def contact_point(self) -> builtins.str:
        '''The contact point to route notifications that match this rule to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#contact_point NotificationPolicy#contact_point}
        '''
        result = self._values.get("contact_point")
        assert result is not None, "Required property 'contact_point' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_by(self) -> typing.List[builtins.str]:
        '''A list of alert labels to group alerts into notifications by.

        Use the special label ``...`` to group alerts by all labels, effectively disabling grouping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_by NotificationPolicy#group_by}
        '''
        result = self._values.get("group_by")
        assert result is not None, "Required property 'group_by' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def continue_(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to continue matching subsequent rules if an alert matches the current rule.

        Otherwise, the rule will be 'consumed' by the first policy to match it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#continue NotificationPolicy#continue}
        '''
        result = self._values.get("continue_")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def group_interval(self) -> typing.Optional[builtins.str]:
        '''Minimum time interval between two notifications for the same group. Default is 5 minutes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_interval NotificationPolicy#group_interval}
        '''
        result = self._values.get("group_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def group_wait(self) -> typing.Optional[builtins.str]:
        '''Time to wait to buffer alerts of the same group before sending a notification. Default is 30 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#group_wait NotificationPolicy#group_wait}
        '''
        result = self._values.get("group_wait")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def matcher(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicyMatcher"]]]:
        '''matcher block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#matcher NotificationPolicy#matcher}
        '''
        result = self._values.get("matcher")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicyMatcher"]]], result)

    @builtins.property
    def mute_timings(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mute timing names to apply to alerts that match this policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#mute_timings NotificationPolicy#mute_timings}
        '''
        result = self._values.get("mute_timings")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def policy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicy"]]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#policy NotificationPolicy#policy}
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["NotificationPolicyPolicy"]]], result)

    @builtins.property
    def repeat_interval(self) -> typing.Optional[builtins.str]:
        '''Minimum time interval for re-sending a notification if an alert is still firing. Default is 4 hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#repeat_interval NotificationPolicy#repeat_interval}
        '''
        result = self._values.get("repeat_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyPolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.notificationPolicy.NotificationPolicyPolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2f135c373b4e37edd9122044f30c2d7a6fa135d4ba04a1abca20ae005ceb00e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "NotificationPolicyPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d26977c20a9469cfc60c0ef1de35215414be28312764e22700869026a2007de)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bda4158139c4bf302ec3889d26a563fbb35a5e30fbcacfab2fc6b6c388c646f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1c255bc02c040bd37fd53a28b0a318a06263a37da6c7568cba6b5fb35ee3245)
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
            type_hints = typing.get_type_hints(_typecheckingstub__187f7ba189e399b22a26f85a3c5b2723083c715a927f71b0775a0fcf8fa65202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f324ba8a65c8fc2c0e8e808b792f944b9d3182b97ace7ed6362ef10f81730b88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.notificationPolicy.NotificationPolicyPolicyMatcher",
    jsii_struct_bases=[],
    name_mapping={"label": "label", "match": "match", "value": "value"},
)
class NotificationPolicyPolicyMatcher:
    def __init__(
        self,
        *,
        label: builtins.str,
        match: builtins.str,
        value: builtins.str,
    ) -> None:
        '''
        :param label: The name of the label to match against. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#label NotificationPolicy#label}
        :param match: The operator to apply when matching values of the given label. Allowed operators are ``=`` for equality, ``!=`` for negated equality, ``=~`` for regex equality, and ``!~`` for negated regex equality. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#match NotificationPolicy#match}
        :param value: The label value to match against. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#value NotificationPolicy#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3a5555eef86b2f33a5454bc9ce0640c0a58f0f20eaf20ffd486fa683547e7d6)
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "label": label,
            "match": match,
            "value": value,
        }

    @builtins.property
    def label(self) -> builtins.str:
        '''The name of the label to match against.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#label NotificationPolicy#label}
        '''
        result = self._values.get("label")
        assert result is not None, "Required property 'label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match(self) -> builtins.str:
        '''The operator to apply when matching values of the given label.

        Allowed operators are ``=`` for equality, ``!=`` for negated equality, ``=~`` for regex equality, and ``!~`` for negated regex equality.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#match NotificationPolicy#match}
        '''
        result = self._values.get("match")
        assert result is not None, "Required property 'match' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The label value to match against.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/notification_policy#value NotificationPolicy#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationPolicyPolicyMatcher(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NotificationPolicyPolicyMatcherList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.notificationPolicy.NotificationPolicyPolicyMatcherList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76a6bfb8cb2f79d72415d580c3e8445afcd673f76a34b89ad8106ebe07cc6bb1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "NotificationPolicyPolicyMatcherOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89156658b8412577ce728c4cd4c48e0ce27a42616a81bfb6d34a026b11d53fd7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("NotificationPolicyPolicyMatcherOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__653fd2e2406f80e3861f801e17c45d8e67b722331539f3531ad8eaeef87d4b0f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__823faff63c96f7691bad4232e7de17aa1c93525b7a97e38bc76f1b353c5d0c57)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3051722b3e8b614b4ce66abecbdf7a2edee3518f827ebffbc68338fa9be1b99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicyMatcher]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicyMatcher]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicyMatcher]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f18fde91e8505118f8722fa1a0ad25104c512c3edc62994b2a0a89f6721cb655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NotificationPolicyPolicyMatcherOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.notificationPolicy.NotificationPolicyPolicyMatcherOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d8c3d20bcb9f709834a9ab6ffd12367a30db3a4c8bb5a7e8db790b8bd84cf7d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__648b7cfaa931a12f3dab2256473ba490d573811a4153d2f4838d564abaf8ccce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "match"))

    @match.setter
    def match(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032e8570bcff35d1a49b7573353fccd89dc7cbdede37c9b47b9299d91642cf81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "match", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad66fe5557254a806e4bcd656e332d68e2c3b733eee237db494493fcafceb309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NotificationPolicyPolicyMatcher, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NotificationPolicyPolicyMatcher, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NotificationPolicyPolicyMatcher, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16f86fb8825497f75c3e44bdfa77f1caa17b53ca3a98e50c86316ada52aaed26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class NotificationPolicyPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.notificationPolicy.NotificationPolicyPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__121c7eba916779cf18fcfac77c76412e7bd31e1ed2bb96731df453b5e7d919e5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatcher")
    def put_matcher(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicyMatcher, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c592243d40bcd71c555e9aa8ac6114ede2af4fd7851ac0e3a83639011a460475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatcher", [value]))

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicy, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d198c4dd5842a7276a074de179f687b884a8e64c5e4e9e1b39ecb7e9eb26010)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetContinue")
    def reset_continue(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinue", []))

    @jsii.member(jsii_name="resetGroupInterval")
    def reset_group_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupInterval", []))

    @jsii.member(jsii_name="resetGroupWait")
    def reset_group_wait(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupWait", []))

    @jsii.member(jsii_name="resetMatcher")
    def reset_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatcher", []))

    @jsii.member(jsii_name="resetMuteTimings")
    def reset_mute_timings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMuteTimings", []))

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @jsii.member(jsii_name="resetRepeatInterval")
    def reset_repeat_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepeatInterval", []))

    @builtins.property
    @jsii.member(jsii_name="matcher")
    def matcher(self) -> NotificationPolicyPolicyMatcherList:
        return typing.cast(NotificationPolicyPolicyMatcherList, jsii.get(self, "matcher"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> NotificationPolicyPolicyList:
        return typing.cast(NotificationPolicyPolicyList, jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="contactPointInput")
    def contact_point_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactPointInput"))

    @builtins.property
    @jsii.member(jsii_name="continueInput")
    def continue_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "continueInput"))

    @builtins.property
    @jsii.member(jsii_name="groupByInput")
    def group_by_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "groupByInput"))

    @builtins.property
    @jsii.member(jsii_name="groupIntervalInput")
    def group_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="groupWaitInput")
    def group_wait_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupWaitInput"))

    @builtins.property
    @jsii.member(jsii_name="matcherInput")
    def matcher_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicyMatcher]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicyMatcher]]], jsii.get(self, "matcherInput"))

    @builtins.property
    @jsii.member(jsii_name="muteTimingsInput")
    def mute_timings_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "muteTimingsInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicy]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="repeatIntervalInput")
    def repeat_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repeatIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="contactPoint")
    def contact_point(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactPoint"))

    @contact_point.setter
    def contact_point(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22099fef87c1b4dcd1d081353354a8f77095b67382e610f401ffdc894fdb53f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactPoint", value)

    @builtins.property
    @jsii.member(jsii_name="continue")
    def continue_(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "continue"))

    @continue_.setter
    def continue_(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bb527b10039b14c5aa1c20dd55004a57bf6c8c29e007bf5736ccd89ac87a027)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continue", value)

    @builtins.property
    @jsii.member(jsii_name="groupBy")
    def group_by(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "groupBy"))

    @group_by.setter
    def group_by(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68c16168ac7f8e13ee269e2528cd06d2ae311375c34f7f09e47ffcda2b3cf878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupBy", value)

    @builtins.property
    @jsii.member(jsii_name="groupInterval")
    def group_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupInterval"))

    @group_interval.setter
    def group_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7864c9d6bd12376df37495162f245c7bd7039b4819b203809ac93016a96ff7ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupInterval", value)

    @builtins.property
    @jsii.member(jsii_name="groupWait")
    def group_wait(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "groupWait"))

    @group_wait.setter
    def group_wait(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d34d68d17c3ca0d1b991730865a3fb58e71b691c2e7439e1c1325a3caec5b37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupWait", value)

    @builtins.property
    @jsii.member(jsii_name="muteTimings")
    def mute_timings(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "muteTimings"))

    @mute_timings.setter
    def mute_timings(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04d3fd16c4720f3099c835ff6b4dbe76cc55bc561e211aee3caa835bdfd98ca3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "muteTimings", value)

    @builtins.property
    @jsii.member(jsii_name="repeatInterval")
    def repeat_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repeatInterval"))

    @repeat_interval.setter
    def repeat_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4af5e51f7068047a137bae4efedd403d26d893135216d168f2b4fadd3deddeb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repeatInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[NotificationPolicyPolicy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[NotificationPolicyPolicy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[NotificationPolicyPolicy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f639c5af5231ab60bb2910236d4a059e79f2f03608461b9600595ce5ed621b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "NotificationPolicy",
    "NotificationPolicyConfig",
    "NotificationPolicyPolicy",
    "NotificationPolicyPolicyList",
    "NotificationPolicyPolicyMatcher",
    "NotificationPolicyPolicyMatcherList",
    "NotificationPolicyPolicyMatcherOutputReference",
    "NotificationPolicyPolicyOutputReference",
]

publication.publish()

def _typecheckingstub__bce565b6db2279c3f5d8fff3770bf1a256f91c5e0cd96fcc74bf2452291b8cb4(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    contact_point: builtins.str,
    group_by: typing.Sequence[builtins.str],
    group_interval: typing.Optional[builtins.str] = None,
    group_wait: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    repeat_interval: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__c8ae5510ebd1ce63e648613531ea6500dd69055c2f59da92b7531e36790ff150(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50af456760b885915bffbf8cda9a6b2d8ecdc5767c289f9df85ef2460fe0c322(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d800b31da61e0e2dc76c8033307903adad94150e67708ea2c4debe74407078b5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9bab2a71c71eaa17aa5a7ef7ddc0b18d349a88794ec206efd2ac51863c7477(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b082345e2356ddba899976d95df263a343654d4a1ed25df78333ed031a42f39e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20988768fbd8a9bbf00ccfa8d564ea3bb11978d84a765fcc5f3711ade16c3b4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531530f4290bbc1acd22ef76f9be48ec10de1ee3a1795bf0d6e0048d55231c8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c7ff14dbfd7d743876fd240ccf13dacb0fd2fc00b08b9aa2bf37eda766f4c8(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    contact_point: builtins.str,
    group_by: typing.Sequence[builtins.str],
    group_interval: typing.Optional[builtins.str] = None,
    group_wait: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    repeat_interval: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b34c76bdfca40defc5d949b4766683367d78eb70548acf407719275fb295168(
    *,
    contact_point: builtins.str,
    group_by: typing.Sequence[builtins.str],
    continue_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group_interval: typing.Optional[builtins.str] = None,
    group_wait: typing.Optional[builtins.str] = None,
    matcher: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicyMatcher, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mute_timings: typing.Optional[typing.Sequence[builtins.str]] = None,
    policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    repeat_interval: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f135c373b4e37edd9122044f30c2d7a6fa135d4ba04a1abca20ae005ceb00e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d26977c20a9469cfc60c0ef1de35215414be28312764e22700869026a2007de(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bda4158139c4bf302ec3889d26a563fbb35a5e30fbcacfab2fc6b6c388c646f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c255bc02c040bd37fd53a28b0a318a06263a37da6c7568cba6b5fb35ee3245(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187f7ba189e399b22a26f85a3c5b2723083c715a927f71b0775a0fcf8fa65202(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f324ba8a65c8fc2c0e8e808b792f944b9d3182b97ace7ed6362ef10f81730b88(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3a5555eef86b2f33a5454bc9ce0640c0a58f0f20eaf20ffd486fa683547e7d6(
    *,
    label: builtins.str,
    match: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a6bfb8cb2f79d72415d580c3e8445afcd673f76a34b89ad8106ebe07cc6bb1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89156658b8412577ce728c4cd4c48e0ce27a42616a81bfb6d34a026b11d53fd7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__653fd2e2406f80e3861f801e17c45d8e67b722331539f3531ad8eaeef87d4b0f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__823faff63c96f7691bad4232e7de17aa1c93525b7a97e38bc76f1b353c5d0c57(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3051722b3e8b614b4ce66abecbdf7a2edee3518f827ebffbc68338fa9be1b99(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f18fde91e8505118f8722fa1a0ad25104c512c3edc62994b2a0a89f6721cb655(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[NotificationPolicyPolicyMatcher]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d8c3d20bcb9f709834a9ab6ffd12367a30db3a4c8bb5a7e8db790b8bd84cf7d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648b7cfaa931a12f3dab2256473ba490d573811a4153d2f4838d564abaf8ccce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032e8570bcff35d1a49b7573353fccd89dc7cbdede37c9b47b9299d91642cf81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad66fe5557254a806e4bcd656e332d68e2c3b733eee237db494493fcafceb309(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16f86fb8825497f75c3e44bdfa77f1caa17b53ca3a98e50c86316ada52aaed26(
    value: typing.Optional[typing.Union[NotificationPolicyPolicyMatcher, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121c7eba916779cf18fcfac77c76412e7bd31e1ed2bb96731df453b5e7d919e5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c592243d40bcd71c555e9aa8ac6114ede2af4fd7851ac0e3a83639011a460475(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicyMatcher, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d198c4dd5842a7276a074de179f687b884a8e64c5e4e9e1b39ecb7e9eb26010(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[NotificationPolicyPolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22099fef87c1b4dcd1d081353354a8f77095b67382e610f401ffdc894fdb53f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bb527b10039b14c5aa1c20dd55004a57bf6c8c29e007bf5736ccd89ac87a027(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c16168ac7f8e13ee269e2528cd06d2ae311375c34f7f09e47ffcda2b3cf878(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7864c9d6bd12376df37495162f245c7bd7039b4819b203809ac93016a96ff7ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d34d68d17c3ca0d1b991730865a3fb58e71b691c2e7439e1c1325a3caec5b37(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04d3fd16c4720f3099c835ff6b4dbe76cc55bc561e211aee3caa835bdfd98ca3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4af5e51f7068047a137bae4efedd403d26d893135216d168f2b4fadd3deddeb0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f639c5af5231ab60bb2910236d4a059e79f2f03608461b9600595ce5ed621b1(
    value: typing.Optional[typing.Union[NotificationPolicyPolicy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
