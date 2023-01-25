'''
# `grafana_oncall_outgoing_webhook`

Refer to the Terraform Registory for docs: [`grafana_oncall_outgoing_webhook`](https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook).
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


class OncallOutgoingWebhook(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.oncallOutgoingWebhook.OncallOutgoingWebhook",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook grafana_oncall_outgoing_webhook}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        url: builtins.str,
        authorization_header: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        forward_whole_payload: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook grafana_oncall_outgoing_webhook} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the outgoing webhook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#name OncallOutgoingWebhook#name}
        :param url: The webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#url OncallOutgoingWebhook#url}
        :param authorization_header: The auth data of the webhook. Used in Authorization header instead of user/password auth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#authorization_header OncallOutgoingWebhook#authorization_header}
        :param data: The data of the webhook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#data OncallOutgoingWebhook#data}
        :param forward_whole_payload: Forwards whole payload of the alert to the webhook's url as POST data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#forward_whole_payload OncallOutgoingWebhook#forward_whole_payload}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#id OncallOutgoingWebhook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: The auth data of the webhook. Used for Basic authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#password OncallOutgoingWebhook#password}
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#team_id OncallOutgoingWebhook#team_id}
        :param user: The auth data of the webhook. Used for Basic authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#user OncallOutgoingWebhook#user}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a087acdd23e85372aff86a39916337baacd3b3439f176103ebf7eed1ce3539b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OncallOutgoingWebhookConfig(
            name=name,
            url=url,
            authorization_header=authorization_header,
            data=data,
            forward_whole_payload=forward_whole_payload,
            id=id,
            password=password,
            team_id=team_id,
            user=user,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAuthorizationHeader")
    def reset_authorization_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationHeader", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetForwardWholePayload")
    def reset_forward_whole_payload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardWholePayload", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="authorizationHeaderInput")
    def authorization_header_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardWholePayloadInput")
    def forward_whole_payload_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "forwardWholePayloadInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationHeader")
    def authorization_header(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationHeader"))

    @authorization_header.setter
    def authorization_header(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74f2badd194ed35b4730c36250aa226107041d98b64783d58eacd271629d8f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationHeader", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcefbf908b487b62c3ae9eebd5d98fc6537e0c91b0cfbe7b1afd4a1f61895350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="forwardWholePayload")
    def forward_whole_payload(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "forwardWholePayload"))

    @forward_whole_payload.setter
    def forward_whole_payload(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6f3aaff69b546ae03045c1ba8e02f235ebab1f23d039265e41e726b5e738ffc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardWholePayload", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5394aeea948c736bdd677dfec89fd4fe8515e92bce7cc1fdbe4a99a1a58018bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87f615df95032693fe0457e89c6913eb10f77af3240f9412bb821465efeb3d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50906df5d002ed9f6193762cced09ab6100bf8f1c72e77ab666b1b15b1a8ce39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5814b6e07b571ca43007eeba4354123facf64b7889519ac67d91a7e3976463c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__293376f3f0a5eac1bc89aee3dfefe651300696000181f0a8cd25ac64854d8993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f93301c53ad204d25231c0d973d7c1a51cbc451b0b9598ac3c78263f2eb61ea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)


@jsii.data_type(
    jsii_type="grafana.oncallOutgoingWebhook.OncallOutgoingWebhookConfig",
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
        "url": "url",
        "authorization_header": "authorizationHeader",
        "data": "data",
        "forward_whole_payload": "forwardWholePayload",
        "id": "id",
        "password": "password",
        "team_id": "teamId",
        "user": "user",
    },
)
class OncallOutgoingWebhookConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        url: builtins.str,
        authorization_header: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        forward_whole_payload: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[builtins.str] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the outgoing webhook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#name OncallOutgoingWebhook#name}
        :param url: The webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#url OncallOutgoingWebhook#url}
        :param authorization_header: The auth data of the webhook. Used in Authorization header instead of user/password auth. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#authorization_header OncallOutgoingWebhook#authorization_header}
        :param data: The data of the webhook. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#data OncallOutgoingWebhook#data}
        :param forward_whole_payload: Forwards whole payload of the alert to the webhook's url as POST data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#forward_whole_payload OncallOutgoingWebhook#forward_whole_payload}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#id OncallOutgoingWebhook#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: The auth data of the webhook. Used for Basic authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#password OncallOutgoingWebhook#password}
        :param team_id: The ID of the OnCall team. To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#team_id OncallOutgoingWebhook#team_id}
        :param user: The auth data of the webhook. Used for Basic authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#user OncallOutgoingWebhook#user}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b771ee4f13a776c7de12991a0b61123fc9c4de7b280462852be60f6e0f3fa39e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument authorization_header", value=authorization_header, expected_type=type_hints["authorization_header"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument forward_whole_payload", value=forward_whole_payload, expected_type=type_hints["forward_whole_payload"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "url": url,
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
        if authorization_header is not None:
            self._values["authorization_header"] = authorization_header
        if data is not None:
            self._values["data"] = data
        if forward_whole_payload is not None:
            self._values["forward_whole_payload"] = forward_whole_payload
        if id is not None:
            self._values["id"] = id
        if password is not None:
            self._values["password"] = password
        if team_id is not None:
            self._values["team_id"] = team_id
        if user is not None:
            self._values["user"] = user

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
        '''The name of the outgoing webhook.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#name OncallOutgoingWebhook#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#url OncallOutgoingWebhook#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_header(self) -> typing.Optional[builtins.str]:
        '''The auth data of the webhook. Used in Authorization header instead of user/password auth.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#authorization_header OncallOutgoingWebhook#authorization_header}
        '''
        result = self._values.get("authorization_header")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''The data of the webhook.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#data OncallOutgoingWebhook#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forward_whole_payload(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Forwards whole payload of the alert to the webhook's url as POST data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#forward_whole_payload OncallOutgoingWebhook#forward_whole_payload}
        '''
        result = self._values.get("forward_whole_payload")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#id OncallOutgoingWebhook#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The auth data of the webhook. Used for Basic authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#password OncallOutgoingWebhook#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the OnCall team.

        To get one, create a team in Grafana, and navigate to the OnCall plugin (to sync the team with OnCall). You can then get the ID using the ``grafana_oncall_team`` datasource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#team_id OncallOutgoingWebhook#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''The auth data of the webhook. Used for Basic authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/oncall_outgoing_webhook#user OncallOutgoingWebhook#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OncallOutgoingWebhookConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OncallOutgoingWebhook",
    "OncallOutgoingWebhookConfig",
]

publication.publish()

def _typecheckingstub__2a087acdd23e85372aff86a39916337baacd3b3439f176103ebf7eed1ce3539b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    url: builtins.str,
    authorization_header: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    forward_whole_payload: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__b74f2badd194ed35b4730c36250aa226107041d98b64783d58eacd271629d8f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcefbf908b487b62c3ae9eebd5d98fc6537e0c91b0cfbe7b1afd4a1f61895350(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f3aaff69b546ae03045c1ba8e02f235ebab1f23d039265e41e726b5e738ffc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5394aeea948c736bdd677dfec89fd4fe8515e92bce7cc1fdbe4a99a1a58018bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87f615df95032693fe0457e89c6913eb10f77af3240f9412bb821465efeb3d5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50906df5d002ed9f6193762cced09ab6100bf8f1c72e77ab666b1b15b1a8ce39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5814b6e07b571ca43007eeba4354123facf64b7889519ac67d91a7e3976463c8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__293376f3f0a5eac1bc89aee3dfefe651300696000181f0a8cd25ac64854d8993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f93301c53ad204d25231c0d973d7c1a51cbc451b0b9598ac3c78263f2eb61ea0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b771ee4f13a776c7de12991a0b61123fc9c4de7b280462852be60f6e0f3fa39e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    url: builtins.str,
    authorization_header: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    forward_whole_payload: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[builtins.str] = None,
    user: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
