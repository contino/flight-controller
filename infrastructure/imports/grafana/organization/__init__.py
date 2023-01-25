'''
# `grafana_organization`

Refer to the Terraform Registory for docs: [`grafana_organization`](https://www.terraform.io/docs/providers/grafana/r/organization).
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


class Organization(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.organization.Organization",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/organization grafana_organization}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        admins: typing.Optional[typing.Sequence[builtins.str]] = None,
        admin_user: typing.Optional[builtins.str] = None,
        create_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        editors: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        viewers: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/organization grafana_organization} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The display name for the Grafana organization created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#name Organization#name}
        :param admins: A list of email addresses corresponding to users who should be given admin access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#admins Organization#admins}
        :param admin_user: The login name of the configured default admin user for the Grafana installation. If unset, this value defaults to admin, the Grafana default. Grafana adds the default admin user to all organizations automatically upon creation, and this parameter keeps Terraform from removing it from organizations. Defaults to ``admin``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#admin_user Organization#admin_user}
        :param create_users: Whether or not to create Grafana users specified in the organization's membership if they don't already exist in Grafana. If unspecified, this parameter defaults to true, creating placeholder users with the name, login, and email set to the email of the user, and a random password. Setting this option to false will cause an error to be thrown for any users that do not already exist in Grafana. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#create_users Organization#create_users}
        :param editors: A list of email addresses corresponding to users who should be given editor access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#editors Organization#editors}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#id Organization#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param viewers: A list of email addresses corresponding to users who should be given viewer access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#viewers Organization#viewers}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf59847eddb2870c7d1de1bf12916448240197044469f208f3c2d1f169738a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OrganizationConfig(
            name=name,
            admins=admins,
            admin_user=admin_user,
            create_users=create_users,
            editors=editors,
            id=id,
            viewers=viewers,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAdmins")
    def reset_admins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdmins", []))

    @jsii.member(jsii_name="resetAdminUser")
    def reset_admin_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdminUser", []))

    @jsii.member(jsii_name="resetCreateUsers")
    def reset_create_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateUsers", []))

    @jsii.member(jsii_name="resetEditors")
    def reset_editors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEditors", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetViewers")
    def reset_viewers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViewers", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "orgId"))

    @builtins.property
    @jsii.member(jsii_name="adminsInput")
    def admins_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "adminsInput"))

    @builtins.property
    @jsii.member(jsii_name="adminUserInput")
    def admin_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminUserInput"))

    @builtins.property
    @jsii.member(jsii_name="createUsersInput")
    def create_users_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "createUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="editorsInput")
    def editors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "editorsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="viewersInput")
    def viewers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "viewersInput"))

    @builtins.property
    @jsii.member(jsii_name="admins")
    def admins(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "admins"))

    @admins.setter
    def admins(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9fa39647d893ee3b10ff31fcf47f6d5d79381c432965248a4308407a76e0e4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admins", value)

    @builtins.property
    @jsii.member(jsii_name="adminUser")
    def admin_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adminUser"))

    @admin_user.setter
    def admin_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8604a26c45471adf2fa74001f0e745adc4a186cbb5756b8bf178b71e1baf8a04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminUser", value)

    @builtins.property
    @jsii.member(jsii_name="createUsers")
    def create_users(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "createUsers"))

    @create_users.setter
    def create_users(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__427444ba6a95863c246661a7baef0f1fcc5683b05bf813621b0f89012f513810)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createUsers", value)

    @builtins.property
    @jsii.member(jsii_name="editors")
    def editors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "editors"))

    @editors.setter
    def editors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24295a4075f0f6fccc58faa0502a14282167c4931a57a8fea41218911f49d43e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "editors", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c5071462963a5906fa5e3af46161ce8c2523ece84663f1ab39a1e4bc59882f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bf225b0347343e8995f9c073b9d365eabbf655c993592e34d7499aac83d3bc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="viewers")
    def viewers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "viewers"))

    @viewers.setter
    def viewers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63f68c0577a90a859619e2aabfdaea14152673b1801b275cf2927c86e15a6cf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewers", value)


@jsii.data_type(
    jsii_type="grafana.organization.OrganizationConfig",
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
        "admins": "admins",
        "admin_user": "adminUser",
        "create_users": "createUsers",
        "editors": "editors",
        "id": "id",
        "viewers": "viewers",
    },
)
class OrganizationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        admins: typing.Optional[typing.Sequence[builtins.str]] = None,
        admin_user: typing.Optional[builtins.str] = None,
        create_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        editors: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        viewers: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The display name for the Grafana organization created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#name Organization#name}
        :param admins: A list of email addresses corresponding to users who should be given admin access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#admins Organization#admins}
        :param admin_user: The login name of the configured default admin user for the Grafana installation. If unset, this value defaults to admin, the Grafana default. Grafana adds the default admin user to all organizations automatically upon creation, and this parameter keeps Terraform from removing it from organizations. Defaults to ``admin``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#admin_user Organization#admin_user}
        :param create_users: Whether or not to create Grafana users specified in the organization's membership if they don't already exist in Grafana. If unspecified, this parameter defaults to true, creating placeholder users with the name, login, and email set to the email of the user, and a random password. Setting this option to false will cause an error to be thrown for any users that do not already exist in Grafana. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#create_users Organization#create_users}
        :param editors: A list of email addresses corresponding to users who should be given editor access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#editors Organization#editors}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#id Organization#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param viewers: A list of email addresses corresponding to users who should be given viewer access to the organization. Note: users specified here must already exist in Grafana unless 'create_users' is set to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#viewers Organization#viewers}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b845fc8ca5d9683dd8c3a1804a5478c889b1af10d1721bc8abd79f4a3cde21)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument admins", value=admins, expected_type=type_hints["admins"])
            check_type(argname="argument admin_user", value=admin_user, expected_type=type_hints["admin_user"])
            check_type(argname="argument create_users", value=create_users, expected_type=type_hints["create_users"])
            check_type(argname="argument editors", value=editors, expected_type=type_hints["editors"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument viewers", value=viewers, expected_type=type_hints["viewers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if admins is not None:
            self._values["admins"] = admins
        if admin_user is not None:
            self._values["admin_user"] = admin_user
        if create_users is not None:
            self._values["create_users"] = create_users
        if editors is not None:
            self._values["editors"] = editors
        if id is not None:
            self._values["id"] = id
        if viewers is not None:
            self._values["viewers"] = viewers

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
        '''The display name for the Grafana organization created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#name Organization#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of email addresses corresponding to users who should be given admin access to the organization.

        Note: users specified here must already exist in
        Grafana unless 'create_users' is set to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#admins Organization#admins}
        '''
        result = self._values.get("admins")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def admin_user(self) -> typing.Optional[builtins.str]:
        '''The login name of the configured default admin user for the Grafana installation.

        If unset, this value defaults to admin, the Grafana default.
        Grafana adds the default admin user to all organizations automatically upon
        creation, and this parameter keeps Terraform from removing it from
        organizations.
        Defaults to ``admin``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#admin_user Organization#admin_user}
        '''
        result = self._values.get("admin_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def create_users(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether or not to create Grafana users specified in the organization's membership if they don't already exist in Grafana.

        If unspecified, this
        parameter defaults to true, creating placeholder users with the name, login,
        and email set to the email of the user, and a random password. Setting this
        option to false will cause an error to be thrown for any users that do not
        already exist in Grafana.
        Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#create_users Organization#create_users}
        '''
        result = self._values.get("create_users")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def editors(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of email addresses corresponding to users who should be given editor access to the organization.

        Note: users specified here must already exist in
        Grafana unless 'create_users' is set to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#editors Organization#editors}
        '''
        result = self._values.get("editors")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#id Organization#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def viewers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of email addresses corresponding to users who should be given viewer access to the organization.

        Note: users specified here must already exist in
        Grafana unless 'create_users' is set to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization#viewers Organization#viewers}
        '''
        result = self._values.get("viewers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Organization",
    "OrganizationConfig",
]

publication.publish()

def _typecheckingstub__acf59847eddb2870c7d1de1bf12916448240197044469f208f3c2d1f169738a1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    admins: typing.Optional[typing.Sequence[builtins.str]] = None,
    admin_user: typing.Optional[builtins.str] = None,
    create_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    editors: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    viewers: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__c9fa39647d893ee3b10ff31fcf47f6d5d79381c432965248a4308407a76e0e4d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8604a26c45471adf2fa74001f0e745adc4a186cbb5756b8bf178b71e1baf8a04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__427444ba6a95863c246661a7baef0f1fcc5683b05bf813621b0f89012f513810(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24295a4075f0f6fccc58faa0502a14282167c4931a57a8fea41218911f49d43e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5071462963a5906fa5e3af46161ce8c2523ece84663f1ab39a1e4bc59882f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf225b0347343e8995f9c073b9d365eabbf655c993592e34d7499aac83d3bc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f68c0577a90a859619e2aabfdaea14152673b1801b275cf2927c86e15a6cf6(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b845fc8ca5d9683dd8c3a1804a5478c889b1af10d1721bc8abd79f4a3cde21(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    admins: typing.Optional[typing.Sequence[builtins.str]] = None,
    admin_user: typing.Optional[builtins.str] = None,
    create_users: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    editors: typing.Optional[typing.Sequence[builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    viewers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
