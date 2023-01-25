'''
# `grafana_dashboard`

Refer to the Terraform Registory for docs: [`grafana_dashboard`](https://www.terraform.io/docs/providers/grafana/r/dashboard).
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


class Dashboard(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dashboard.Dashboard",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/dashboard grafana_dashboard}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        config_json: builtins.str,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[jsii.Number] = None,
        overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/dashboard grafana_dashboard} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_json: The complete dashboard model JSON. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#config_json Dashboard#config_json}
        :param folder: The id of the folder to save the dashboard in. This attribute is a string to reflect the type of the folder's id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#folder Dashboard#folder}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#id Dashboard#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param message: Set a commit message for the version history. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#message Dashboard#message}
        :param org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#org_id Dashboard#org_id}
        :param overwrite: Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#overwrite Dashboard#overwrite}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14b3bc755d242c218d6c3d08c057f71d8c77a778c31e8780a748c3209ee3f228)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DashboardConfig(
            config_json=config_json,
            folder=folder,
            id=id,
            message=message,
            org_id=org_id,
            overwrite=overwrite,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetFolder")
    def reset_folder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFolder", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetOrgId")
    def reset_org_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgId", []))

    @jsii.member(jsii_name="resetOverwrite")
    def reset_overwrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverwrite", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dashboardId"))

    @builtins.property
    @jsii.member(jsii_name="slug")
    def slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slug"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="configJsonInput")
    def config_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="folderInput")
    def folder_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "folderInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="orgIdInput")
    def org_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orgIdInput"))

    @builtins.property
    @jsii.member(jsii_name="overwriteInput")
    def overwrite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overwriteInput"))

    @builtins.property
    @jsii.member(jsii_name="configJson")
    def config_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configJson"))

    @config_json.setter
    def config_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__437eb816901a1e6f5389d1255e4353e0c5570a0746a3e05ba99f527cd6885d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configJson", value)

    @builtins.property
    @jsii.member(jsii_name="folder")
    def folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "folder"))

    @folder.setter
    def folder(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7b4a708d63c420379eb0e4aac9010655738394b2650879c70cd652f0092a70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "folder", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c206a25d18c384dc991e5fe4445ee45c99c38390fe2b79c00dc2311dc85f1d2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf6be16470912f6533abd2f5726c7e2f5910a1b0a35a6811ab59a10b67096f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "orgId"))

    @org_id.setter
    def org_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dc69b006b63d6aebe98a88ba4e2ed4f40b06016b91bd784fb79d15e504260a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgId", value)

    @builtins.property
    @jsii.member(jsii_name="overwrite")
    def overwrite(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "overwrite"))

    @overwrite.setter
    def overwrite(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5adf1c06163f44abe2bcf5f8989adaf50d8bff6a15c471cd1cfb642760ab05d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overwrite", value)


@jsii.data_type(
    jsii_type="grafana.dashboard.DashboardConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config_json": "configJson",
        "folder": "folder",
        "id": "id",
        "message": "message",
        "org_id": "orgId",
        "overwrite": "overwrite",
    },
)
class DashboardConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        config_json: builtins.str,
        folder: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[jsii.Number] = None,
        overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_json: The complete dashboard model JSON. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#config_json Dashboard#config_json}
        :param folder: The id of the folder to save the dashboard in. This attribute is a string to reflect the type of the folder's id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#folder Dashboard#folder}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#id Dashboard#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param message: Set a commit message for the version history. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#message Dashboard#message}
        :param org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#org_id Dashboard#org_id}
        :param overwrite: Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#overwrite Dashboard#overwrite}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d1f83ad4d1705b21920da22f9ba5ca1b44503fd713e28bba772490d8814516)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_json", value=config_json, expected_type=type_hints["config_json"])
            check_type(argname="argument folder", value=folder, expected_type=type_hints["folder"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument overwrite", value=overwrite, expected_type=type_hints["overwrite"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_json": config_json,
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
        if folder is not None:
            self._values["folder"] = folder
        if id is not None:
            self._values["id"] = id
        if message is not None:
            self._values["message"] = message
        if org_id is not None:
            self._values["org_id"] = org_id
        if overwrite is not None:
            self._values["overwrite"] = overwrite

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
    def config_json(self) -> builtins.str:
        '''The complete dashboard model JSON.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#config_json Dashboard#config_json}
        '''
        result = self._values.get("config_json")
        assert result is not None, "Required property 'config_json' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def folder(self) -> typing.Optional[builtins.str]:
        '''The id of the folder to save the dashboard in.

        This attribute is a string to reflect the type of the folder's id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#folder Dashboard#folder}
        '''
        result = self._values.get("folder")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#id Dashboard#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Set a commit message for the version history.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#message Dashboard#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_id(self) -> typing.Optional[jsii.Number]:
        '''The Organization ID. If not set, the Org ID defined in the provider block will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#org_id Dashboard#org_id}
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def overwrite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Set to true if you want to overwrite existing dashboard with newer version, same dashboard title in folder or same dashboard uid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard#overwrite Dashboard#overwrite}
        '''
        result = self._values.get("overwrite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Dashboard",
    "DashboardConfig",
]

publication.publish()

def _typecheckingstub__14b3bc755d242c218d6c3d08c057f71d8c77a778c31e8780a748c3209ee3f228(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    config_json: builtins.str,
    folder: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[jsii.Number] = None,
    overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__437eb816901a1e6f5389d1255e4353e0c5570a0746a3e05ba99f527cd6885d82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7b4a708d63c420379eb0e4aac9010655738394b2650879c70cd652f0092a70(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c206a25d18c384dc991e5fe4445ee45c99c38390fe2b79c00dc2311dc85f1d2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf6be16470912f6533abd2f5726c7e2f5910a1b0a35a6811ab59a10b67096f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc69b006b63d6aebe98a88ba4e2ed4f40b06016b91bd784fb79d15e504260a7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5adf1c06163f44abe2bcf5f8989adaf50d8bff6a15c471cd1cfb642760ab05d7(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d1f83ad4d1705b21920da22f9ba5ca1b44503fd713e28bba772490d8814516(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    config_json: builtins.str,
    folder: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[jsii.Number] = None,
    overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
