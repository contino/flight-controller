'''
# `grafana_dashboard_permission`

Refer to the Terraform Registory for docs: [`grafana_dashboard_permission`](https://www.terraform.io/docs/providers/grafana/r/dashboard_permission).
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


class DashboardPermission(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dashboardPermission.DashboardPermission",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission grafana_dashboard_permission}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        permissions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DashboardPermissionPermissions", typing.Dict[builtins.str, typing.Any]]]],
        dashboard_id: typing.Optional[jsii.Number] = None,
        dashboard_uid: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission grafana_dashboard_permission} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#permissions DashboardPermission#permissions}
        :param dashboard_id: ID of the dashboard to apply permissions to. Deprecated: use ``dashboard_uid`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#dashboard_id DashboardPermission#dashboard_id}
        :param dashboard_uid: UID of the dashboard to apply permissions to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#dashboard_uid DashboardPermission#dashboard_uid}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#id DashboardPermission#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af08a3e2cc407b870e96b0c1e35b62b1bbe3b591d9f5eaedae81ec3e9c795f30)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DashboardPermissionConfig(
            permissions=permissions,
            dashboard_id=dashboard_id,
            dashboard_uid=dashboard_uid,
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

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DashboardPermissionPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2465c055662c0b42a9f9345911da0894b6de92a8c16ec2c24d0eb6eaf8ac9bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="resetDashboardId")
    def reset_dashboard_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDashboardId", []))

    @jsii.member(jsii_name="resetDashboardUid")
    def reset_dashboard_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDashboardUid", []))

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
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "DashboardPermissionPermissionsList":
        return typing.cast("DashboardPermissionPermissionsList", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="dashboardIdInput")
    def dashboard_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardUidInput")
    def dashboard_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dashboardUidInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DashboardPermissionPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DashboardPermissionPermissions"]]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dashboardId"))

    @dashboard_id.setter
    def dashboard_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be8e89fb6a2f5fa46cf4b0457c946b6b0df3b34db4d24f78da00d9455d964799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="dashboardUid")
    def dashboard_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dashboardUid"))

    @dashboard_uid.setter
    def dashboard_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2200a33ff64fb4f2a67f0949ced498e9f0619765446297869f2d713a73b80c3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardUid", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be34dbbeae0aee698fe5debc48f1c75dccf126de95b5804048c7d9612b0315c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="grafana.dashboardPermission.DashboardPermissionConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "permissions": "permissions",
        "dashboard_id": "dashboardId",
        "dashboard_uid": "dashboardUid",
        "id": "id",
    },
)
class DashboardPermissionConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        permissions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DashboardPermissionPermissions", typing.Dict[builtins.str, typing.Any]]]],
        dashboard_id: typing.Optional[jsii.Number] = None,
        dashboard_uid: typing.Optional[builtins.str] = None,
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
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#permissions DashboardPermission#permissions}
        :param dashboard_id: ID of the dashboard to apply permissions to. Deprecated: use ``dashboard_uid`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#dashboard_id DashboardPermission#dashboard_id}
        :param dashboard_uid: UID of the dashboard to apply permissions to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#dashboard_uid DashboardPermission#dashboard_uid}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#id DashboardPermission#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6dd7b8cc2051bed5baab9262dee3172ef09d3495e40298a5c613e3aa4e77c79)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
            check_type(argname="argument dashboard_uid", value=dashboard_uid, expected_type=type_hints["dashboard_uid"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions": permissions,
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
        if dashboard_id is not None:
            self._values["dashboard_id"] = dashboard_id
        if dashboard_uid is not None:
            self._values["dashboard_uid"] = dashboard_uid
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
    def permissions(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DashboardPermissionPermissions"]]:
        '''permissions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#permissions DashboardPermission#permissions}
        '''
        result = self._values.get("permissions")
        assert result is not None, "Required property 'permissions' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DashboardPermissionPermissions"]], result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the dashboard to apply permissions to. Deprecated: use ``dashboard_uid`` instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#dashboard_id DashboardPermission#dashboard_id}
        '''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dashboard_uid(self) -> typing.Optional[builtins.str]:
        '''UID of the dashboard to apply permissions to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#dashboard_uid DashboardPermission#dashboard_uid}
        '''
        result = self._values.get("dashboard_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#id DashboardPermission#id}.

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
        return "DashboardPermissionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.dashboardPermission.DashboardPermissionPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "permission": "permission",
        "role": "role",
        "team_id": "teamId",
        "user_id": "userId",
    },
)
class DashboardPermissionPermissions:
    def __init__(
        self,
        *,
        permission: builtins.str,
        role: typing.Optional[builtins.str] = None,
        team_id: typing.Optional[jsii.Number] = None,
        user_id: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param permission: Permission to associate with item. Must be one of ``View``, ``Edit``, or ``Admin``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#permission DashboardPermission#permission}
        :param role: Manage permissions for ``Viewer`` or ``Editor`` roles. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#role DashboardPermission#role}
        :param team_id: ID of the team to manage permissions for. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#team_id DashboardPermission#team_id}
        :param user_id: ID of the user to manage permissions for. Defaults to ``0``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#user_id DashboardPermission#user_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb861bf8e2981baab1301d94628d1f36cc23f2d66e805dce9ed0221a3f4a3f8b)
            check_type(argname="argument permission", value=permission, expected_type=type_hints["permission"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permission": permission,
        }
        if role is not None:
            self._values["role"] = role
        if team_id is not None:
            self._values["team_id"] = team_id
        if user_id is not None:
            self._values["user_id"] = user_id

    @builtins.property
    def permission(self) -> builtins.str:
        '''Permission to associate with item. Must be one of ``View``, ``Edit``, or ``Admin``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#permission DashboardPermission#permission}
        '''
        result = self._values.get("permission")
        assert result is not None, "Required property 'permission' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''Manage permissions for ``Viewer`` or ``Editor`` roles.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#role DashboardPermission#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def team_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the team to manage permissions for. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#team_id DashboardPermission#team_id}
        '''
        result = self._values.get("team_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def user_id(self) -> typing.Optional[jsii.Number]:
        '''ID of the user to manage permissions for. Defaults to ``0``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/dashboard_permission#user_id DashboardPermission#user_id}
        '''
        result = self._values.get("user_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardPermissionPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DashboardPermissionPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dashboardPermission.DashboardPermissionPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b59305bc08f1de948e20b4042ee4728d8557a4a31154a4b44a5bc87e70e5be8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DashboardPermissionPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a2a0c5d66b5e7cc5587a3bd54233958411ec377563fbc1254ad4de950ac79af)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DashboardPermissionPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401c1e25a5df8aab475e2ebeee2d422a2587f3b8f2e56a0da184c71084cbf40e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a72a69297f188f082bffa00fb03b276b56524139f143190ef139c691b42cf1c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__26dedc5abddf96fae0cbdca86bf88c6326bf9258c285218953e2e921b4b0e36a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DashboardPermissionPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DashboardPermissionPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DashboardPermissionPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1939411722e1d80b794b1f2644a15c86f2ad921f9d4c884987f8a8ff5758055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DashboardPermissionPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dashboardPermission.DashboardPermissionPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a0ad932d2f8a472d389e66e2e554fab07aac4c3247c94bcad87b328412522b2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetTeamId")
    def reset_team_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeamId", []))

    @jsii.member(jsii_name="resetUserId")
    def reset_user_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserId", []))

    @builtins.property
    @jsii.member(jsii_name="permissionInput")
    def permission_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdInput")
    def user_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "userIdInput"))

    @builtins.property
    @jsii.member(jsii_name="permission")
    def permission(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permission"))

    @permission.setter
    def permission(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c4ba890f090529cea4fc9830df035ae8e8b19a19498ebb1259d3695696765a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permission", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52bbef3316a377f24685051cd5a1ae9d0386de7109169c391737243e7226cc01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f824cad999fd4c3a99d530644adb1d1371f331c9b441a038b6507d3a8cb30e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="userId")
    def user_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "userId"))

    @user_id.setter
    def user_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0197810075f2cd903537fb1c57ccc6cdb9f02276ea8711c5ab14a73cba78166b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DashboardPermissionPermissions, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DashboardPermissionPermissions, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DashboardPermissionPermissions, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e05d45457a5b7f6651d0976ab9d9a4b06b3c790f8f6d473d7dc99ff2473f5752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DashboardPermission",
    "DashboardPermissionConfig",
    "DashboardPermissionPermissions",
    "DashboardPermissionPermissionsList",
    "DashboardPermissionPermissionsOutputReference",
]

publication.publish()

def _typecheckingstub__af08a3e2cc407b870e96b0c1e35b62b1bbe3b591d9f5eaedae81ec3e9c795f30(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    permissions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DashboardPermissionPermissions, typing.Dict[builtins.str, typing.Any]]]],
    dashboard_id: typing.Optional[jsii.Number] = None,
    dashboard_uid: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a2465c055662c0b42a9f9345911da0894b6de92a8c16ec2c24d0eb6eaf8ac9bd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DashboardPermissionPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8e89fb6a2f5fa46cf4b0457c946b6b0df3b34db4d24f78da00d9455d964799(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2200a33ff64fb4f2a67f0949ced498e9f0619765446297869f2d713a73b80c3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be34dbbeae0aee698fe5debc48f1c75dccf126de95b5804048c7d9612b0315c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6dd7b8cc2051bed5baab9262dee3172ef09d3495e40298a5c613e3aa4e77c79(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    permissions: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DashboardPermissionPermissions, typing.Dict[builtins.str, typing.Any]]]],
    dashboard_id: typing.Optional[jsii.Number] = None,
    dashboard_uid: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb861bf8e2981baab1301d94628d1f36cc23f2d66e805dce9ed0221a3f4a3f8b(
    *,
    permission: builtins.str,
    role: typing.Optional[builtins.str] = None,
    team_id: typing.Optional[jsii.Number] = None,
    user_id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b59305bc08f1de948e20b4042ee4728d8557a4a31154a4b44a5bc87e70e5be8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a2a0c5d66b5e7cc5587a3bd54233958411ec377563fbc1254ad4de950ac79af(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__401c1e25a5df8aab475e2ebeee2d422a2587f3b8f2e56a0da184c71084cbf40e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72a69297f188f082bffa00fb03b276b56524139f143190ef139c691b42cf1c3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26dedc5abddf96fae0cbdca86bf88c6326bf9258c285218953e2e921b4b0e36a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1939411722e1d80b794b1f2644a15c86f2ad921f9d4c884987f8a8ff5758055(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DashboardPermissionPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0ad932d2f8a472d389e66e2e554fab07aac4c3247c94bcad87b328412522b2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4ba890f090529cea4fc9830df035ae8e8b19a19498ebb1259d3695696765a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52bbef3316a377f24685051cd5a1ae9d0386de7109169c391737243e7226cc01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f824cad999fd4c3a99d530644adb1d1371f331c9b441a038b6507d3a8cb30e0c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0197810075f2cd903537fb1c57ccc6cdb9f02276ea8711c5ab14a73cba78166b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e05d45457a5b7f6651d0976ab9d9a4b06b3c790f8f6d473d7dc99ff2473f5752(
    value: typing.Optional[typing.Union[DashboardPermissionPermissions, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
