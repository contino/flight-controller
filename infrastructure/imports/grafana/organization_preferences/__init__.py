'''
# `grafana_organization_preferences`

Refer to the Terraform Registory for docs: [`grafana_organization_preferences`](https://www.terraform.io/docs/providers/grafana/r/organization_preferences).
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


class OrganizationPreferences(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.organizationPreferences.OrganizationPreferences",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences grafana_organization_preferences}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        home_dashboard_id: typing.Optional[jsii.Number] = None,
        home_dashboard_uid: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[jsii.Number] = None,
        theme: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        week_start: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences grafana_organization_preferences} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param home_dashboard_id: The Organization home dashboard ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#home_dashboard_id OrganizationPreferences#home_dashboard_id}
        :param home_dashboard_uid: The Organization home dashboard UID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#home_dashboard_uid OrganizationPreferences#home_dashboard_uid}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#id OrganizationPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#org_id OrganizationPreferences#org_id}
        :param theme: The Organization theme. Available values are ``light``, ``dark``, or an empty string for the default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#theme OrganizationPreferences#theme}
        :param timezone: The Organization timezone. Available values are ``utc``, ``browser``, or an empty string for the default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#timezone OrganizationPreferences#timezone}
        :param week_start: The Organization week start. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#week_start OrganizationPreferences#week_start}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84f21f0ac415f2e6283fcc41aea144dbee1ddde086c07f68cbbb8e60df061496)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = OrganizationPreferencesConfig(
            home_dashboard_id=home_dashboard_id,
            home_dashboard_uid=home_dashboard_uid,
            id=id,
            org_id=org_id,
            theme=theme,
            timezone=timezone,
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

    @jsii.member(jsii_name="resetHomeDashboardId")
    def reset_home_dashboard_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDashboardId", []))

    @jsii.member(jsii_name="resetHomeDashboardUid")
    def reset_home_dashboard_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeDashboardUid", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOrgId")
    def reset_org_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgId", []))

    @jsii.member(jsii_name="resetTheme")
    def reset_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTheme", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

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
    @jsii.member(jsii_name="homeDashboardIdInput")
    def home_dashboard_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "homeDashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDashboardUidInput")
    def home_dashboard_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDashboardUidInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="orgIdInput")
    def org_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orgIdInput"))

    @builtins.property
    @jsii.member(jsii_name="themeInput")
    def theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "themeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="weekStartInput")
    def week_start_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weekStartInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDashboardId")
    def home_dashboard_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "homeDashboardId"))

    @home_dashboard_id.setter
    def home_dashboard_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce733080d0ea53ae803b9f666a8b0558ce6c582b5bd405f09266c66703a9a0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="homeDashboardUid")
    def home_dashboard_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeDashboardUid"))

    @home_dashboard_uid.setter
    def home_dashboard_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f7b50c8786d86a6cc670133b2a65a1a3e60eccf713c201096f822f0e97818e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDashboardUid", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bc372fd5deb2c7219c4c9363f2c5e75bcb2de73f806205dc0997f9a0972ac3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="orgId")
    def org_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "orgId"))

    @org_id.setter
    def org_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057012dcfc2a6b1845d0ddc781fd9d933725b7369d1b9a2e4990417d76428447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgId", value)

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "theme"))

    @theme.setter
    def theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8055961ab4cc7f9f1706500122682ee46c73db30f599f136e9569ce69b49ed6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "theme", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad611a808ecbadce32b95d052c4eefd129fb7beb0c5e75c192ba442d0d0f8744)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)

    @builtins.property
    @jsii.member(jsii_name="weekStart")
    def week_start(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weekStart"))

    @week_start.setter
    def week_start(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aee0cc3b8ef90eadde243395f4c81e8e1fca527449ec57783c34b05e4e6c0eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekStart", value)


@jsii.data_type(
    jsii_type="grafana.organizationPreferences.OrganizationPreferencesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "home_dashboard_id": "homeDashboardId",
        "home_dashboard_uid": "homeDashboardUid",
        "id": "id",
        "org_id": "orgId",
        "theme": "theme",
        "timezone": "timezone",
        "week_start": "weekStart",
    },
)
class OrganizationPreferencesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        home_dashboard_id: typing.Optional[jsii.Number] = None,
        home_dashboard_uid: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        org_id: typing.Optional[jsii.Number] = None,
        theme: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
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
        :param home_dashboard_id: The Organization home dashboard ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#home_dashboard_id OrganizationPreferences#home_dashboard_id}
        :param home_dashboard_uid: The Organization home dashboard UID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#home_dashboard_uid OrganizationPreferences#home_dashboard_uid}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#id OrganizationPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param org_id: The Organization ID. If not set, the Org ID defined in the provider block will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#org_id OrganizationPreferences#org_id}
        :param theme: The Organization theme. Available values are ``light``, ``dark``, or an empty string for the default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#theme OrganizationPreferences#theme}
        :param timezone: The Organization timezone. Available values are ``utc``, ``browser``, or an empty string for the default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#timezone OrganizationPreferences#timezone}
        :param week_start: The Organization week start. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#week_start OrganizationPreferences#week_start}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__027df0c58921a147bc8ba076ec379d654aebe771413edad101831fcfcf5e63af)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument home_dashboard_id", value=home_dashboard_id, expected_type=type_hints["home_dashboard_id"])
            check_type(argname="argument home_dashboard_uid", value=home_dashboard_uid, expected_type=type_hints["home_dashboard_uid"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument org_id", value=org_id, expected_type=type_hints["org_id"])
            check_type(argname="argument theme", value=theme, expected_type=type_hints["theme"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument week_start", value=week_start, expected_type=type_hints["week_start"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if home_dashboard_id is not None:
            self._values["home_dashboard_id"] = home_dashboard_id
        if home_dashboard_uid is not None:
            self._values["home_dashboard_uid"] = home_dashboard_uid
        if id is not None:
            self._values["id"] = id
        if org_id is not None:
            self._values["org_id"] = org_id
        if theme is not None:
            self._values["theme"] = theme
        if timezone is not None:
            self._values["timezone"] = timezone
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
    def home_dashboard_id(self) -> typing.Optional[jsii.Number]:
        '''The Organization home dashboard ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#home_dashboard_id OrganizationPreferences#home_dashboard_id}
        '''
        result = self._values.get("home_dashboard_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def home_dashboard_uid(self) -> typing.Optional[builtins.str]:
        '''The Organization home dashboard UID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#home_dashboard_uid OrganizationPreferences#home_dashboard_uid}
        '''
        result = self._values.get("home_dashboard_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#id OrganizationPreferences#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_id(self) -> typing.Optional[jsii.Number]:
        '''The Organization ID. If not set, the Org ID defined in the provider block will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#org_id OrganizationPreferences#org_id}
        '''
        result = self._values.get("org_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def theme(self) -> typing.Optional[builtins.str]:
        '''The Organization theme. Available values are ``light``, ``dark``, or an empty string for the default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#theme OrganizationPreferences#theme}
        '''
        result = self._values.get("theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The Organization timezone. Available values are ``utc``, ``browser``, or an empty string for the default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#timezone OrganizationPreferences#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def week_start(self) -> typing.Optional[builtins.str]:
        '''The Organization week start.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/organization_preferences#week_start OrganizationPreferences#week_start}
        '''
        result = self._values.get("week_start")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationPreferencesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OrganizationPreferences",
    "OrganizationPreferencesConfig",
]

publication.publish()

def _typecheckingstub__84f21f0ac415f2e6283fcc41aea144dbee1ddde086c07f68cbbb8e60df061496(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    home_dashboard_id: typing.Optional[jsii.Number] = None,
    home_dashboard_uid: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[jsii.Number] = None,
    theme: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__2ce733080d0ea53ae803b9f666a8b0558ce6c582b5bd405f09266c66703a9a0c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7b50c8786d86a6cc670133b2a65a1a3e60eccf713c201096f822f0e97818e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bc372fd5deb2c7219c4c9363f2c5e75bcb2de73f806205dc0997f9a0972ac3b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057012dcfc2a6b1845d0ddc781fd9d933725b7369d1b9a2e4990417d76428447(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8055961ab4cc7f9f1706500122682ee46c73db30f599f136e9569ce69b49ed6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad611a808ecbadce32b95d052c4eefd129fb7beb0c5e75c192ba442d0d0f8744(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aee0cc3b8ef90eadde243395f4c81e8e1fca527449ec57783c34b05e4e6c0eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027df0c58921a147bc8ba076ec379d654aebe771413edad101831fcfcf5e63af(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    home_dashboard_id: typing.Optional[jsii.Number] = None,
    home_dashboard_uid: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    org_id: typing.Optional[jsii.Number] = None,
    theme: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
    week_start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
