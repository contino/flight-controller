'''
# `grafana_alert_notification`

Refer to the Terraform Registory for docs: [`grafana_alert_notification`](https://www.terraform.io/docs/providers/grafana/r/alert_notification).
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


class AlertNotification(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.alertNotification.AlertNotification",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification grafana_alert_notification}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secure_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        send_reminder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uid: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification grafana_alert_notification} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the alert notification channel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#name AlertNotification#name}
        :param type: The type of the alert notification channel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#type AlertNotification#type}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#disable_resolve_message AlertNotification#disable_resolve_message}
        :param frequency: Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#frequency AlertNotification#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#id AlertNotification#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Is this the default channel for all your alerts. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#is_default AlertNotification#is_default}
        :param secure_settings: Additional secure settings, for full reference lookup `Grafana Supported Settings documentation <https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#secure_settings AlertNotification#secure_settings}
        :param send_reminder: Whether to send reminders for triggered alerts. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#send_reminder AlertNotification#send_reminder}
        :param settings: Additional settings, for full reference see `Grafana HTTP API documentation <https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#settings AlertNotification#settings}
        :param uid: Unique identifier. If unset, this will be automatically generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#uid AlertNotification#uid}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__230e4a79f93fbfdf50c3f6e7f5552baf431c998a0ef49fea9074836b45b60b7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AlertNotificationConfig(
            name=name,
            type=type,
            disable_resolve_message=disable_resolve_message,
            frequency=frequency,
            id=id,
            is_default=is_default,
            secure_settings=secure_settings,
            send_reminder=send_reminder,
            settings=settings,
            uid=uid,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="resetSecureSettings")
    def reset_secure_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureSettings", []))

    @jsii.member(jsii_name="resetSendReminder")
    def reset_send_reminder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendReminder", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetUid")
    def reset_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUid", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="secureSettingsInput")
    def secure_settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "secureSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="sendReminderInput")
    def send_reminder_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sendReminderInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53f09ebec09f27a9b616505d03345212c3fbe0effcf00364640cad5213b9ea15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a433200578806333c9d1017ea04776fd8269319cc3bcb6f3c5ec3a831b1b7f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d0d79e97b358e0f9d1b39c1768a9bd2173e854ce4107be11872f0988696985e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e49d28e8a824125a57ac4c0618d3e674341860a8c5d62a7377d71a129032e23d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e099780352da01a3cc876ac874d1148a89ad3fcebbb9e6fd34cd016f37af5b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secureSettings")
    def secure_settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "secureSettings"))

    @secure_settings.setter
    def secure_settings(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85bb4b046947064d310555b8eff6713cef35051e3886221bc0ee47cb52dc58a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureSettings", value)

    @builtins.property
    @jsii.member(jsii_name="sendReminder")
    def send_reminder(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sendReminder"))

    @send_reminder.setter
    def send_reminder(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b43d39dc6e307b12394086b78019b3213734ee6b94e9b62b1a9880c8a7ba5bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendReminder", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0808a29730e8bfeec0f9859f0f7bd9b9eca664b3ba0d25093c839691b08c3648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc316d0b66484f4fb4e729abf4093b392ed50737bb6c51a035842ff081ca658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__006c4fad81ff44d391f43f1247812aaa7e85b59f8e9b58b2eb3897b0d3ff846f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)


@jsii.data_type(
    jsii_type="grafana.alertNotification.AlertNotificationConfig",
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
        "disable_resolve_message": "disableResolveMessage",
        "frequency": "frequency",
        "id": "id",
        "is_default": "isDefault",
        "secure_settings": "secureSettings",
        "send_reminder": "sendReminder",
        "settings": "settings",
        "uid": "uid",
    },
)
class AlertNotificationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        frequency: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        secure_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        send_reminder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the alert notification channel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#name AlertNotification#name}
        :param type: The type of the alert notification channel. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#type AlertNotification#type}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#disable_resolve_message AlertNotification#disable_resolve_message}
        :param frequency: Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#frequency AlertNotification#frequency}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#id AlertNotification#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Is this the default channel for all your alerts. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#is_default AlertNotification#is_default}
        :param secure_settings: Additional secure settings, for full reference lookup `Grafana Supported Settings documentation <https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#secure_settings AlertNotification#secure_settings}
        :param send_reminder: Whether to send reminders for triggered alerts. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#send_reminder AlertNotification#send_reminder}
        :param settings: Additional settings, for full reference see `Grafana HTTP API documentation <https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#settings AlertNotification#settings}
        :param uid: Unique identifier. If unset, this will be automatically generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#uid AlertNotification#uid}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da08cb4de02c5864b6ca4a2ff8c30ff3cff5cac9a074a92eb9ad301fcd159bc)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument secure_settings", value=secure_settings, expected_type=type_hints["secure_settings"])
            check_type(argname="argument send_reminder", value=send_reminder, expected_type=type_hints["send_reminder"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
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
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if frequency is not None:
            self._values["frequency"] = frequency
        if id is not None:
            self._values["id"] = id
        if is_default is not None:
            self._values["is_default"] = is_default
        if secure_settings is not None:
            self._values["secure_settings"] = secure_settings
        if send_reminder is not None:
            self._values["send_reminder"] = send_reminder
        if settings is not None:
            self._values["settings"] = settings
        if uid is not None:
            self._values["uid"] = uid

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
        '''The name of the alert notification channel.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#name AlertNotification#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the alert notification channel.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#type AlertNotification#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#disable_resolve_message AlertNotification#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def frequency(self) -> typing.Optional[builtins.str]:
        '''Frequency of alert reminders. Frequency must be set if reminders are enabled. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#frequency AlertNotification#frequency}
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#id AlertNotification#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Is this the default channel for all your alerts. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#is_default AlertNotification#is_default}
        '''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def secure_settings(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional secure settings, for full reference lookup `Grafana Supported Settings documentation <https://grafana.com/docs/grafana/latest/administration/provisioning/#supported-settings>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#secure_settings AlertNotification#secure_settings}
        '''
        result = self._values.get("secure_settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def send_reminder(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to send reminders for triggered alerts. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#send_reminder AlertNotification#send_reminder}
        '''
        result = self._values.get("send_reminder")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional settings, for full reference see `Grafana HTTP API documentation <https://grafana.com/docs/grafana/latest/http_api/alerting_notification_channels/>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#settings AlertNotification#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def uid(self) -> typing.Optional[builtins.str]:
        '''Unique identifier. If unset, this will be automatically generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/alert_notification#uid AlertNotification#uid}
        '''
        result = self._values.get("uid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlertNotificationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AlertNotification",
    "AlertNotificationConfig",
]

publication.publish()

def _typecheckingstub__230e4a79f93fbfdf50c3f6e7f5552baf431c998a0ef49fea9074836b45b60b7a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    frequency: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secure_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    send_reminder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uid: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__53f09ebec09f27a9b616505d03345212c3fbe0effcf00364640cad5213b9ea15(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a433200578806333c9d1017ea04776fd8269319cc3bcb6f3c5ec3a831b1b7f2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0d79e97b358e0f9d1b39c1768a9bd2173e854ce4107be11872f0988696985e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e49d28e8a824125a57ac4c0618d3e674341860a8c5d62a7377d71a129032e23d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e099780352da01a3cc876ac874d1148a89ad3fcebbb9e6fd34cd016f37af5b0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85bb4b046947064d310555b8eff6713cef35051e3886221bc0ee47cb52dc58a0(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b43d39dc6e307b12394086b78019b3213734ee6b94e9b62b1a9880c8a7ba5bd(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0808a29730e8bfeec0f9859f0f7bd9b9eca664b3ba0d25093c839691b08c3648(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc316d0b66484f4fb4e729abf4093b392ed50737bb6c51a035842ff081ca658(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006c4fad81ff44d391f43f1247812aaa7e85b59f8e9b58b2eb3897b0d3ff846f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da08cb4de02c5864b6ca4a2ff8c30ff3cff5cac9a074a92eb9ad301fcd159bc(
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
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    frequency: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    secure_settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    send_reminder: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uid: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
