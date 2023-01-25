'''
# `grafana_team_preferences`

Refer to the Terraform Registory for docs: [`grafana_team_preferences`](https://www.terraform.io/docs/providers/grafana/r/team_preferences).
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


class TeamPreferences(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.teamPreferences.TeamPreferences",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences grafana_team_preferences}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        team_id: jsii.Number,
        home_dashboard_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        theme: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences grafana_team_preferences} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param team_id: The numeric team ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#team_id TeamPreferences#team_id}
        :param home_dashboard_id: The numeric ID of the dashboard to display when a team member logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#home_dashboard_id TeamPreferences#home_dashboard_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#id TeamPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param theme: The theme for the specified team. Available themes are ``light``, ``dark``, or an empty string for the default theme. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#theme TeamPreferences#theme}
        :param timezone: The timezone for the specified team. Available values are ``utc``, ``browser``, or an empty string for the default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#timezone TeamPreferences#timezone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14d170fd631306f35f3a52072797b771eed4c7b8af9a057cc51e45e172e8daf3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = TeamPreferencesConfig(
            team_id=team_id,
            home_dashboard_id=home_dashboard_id,
            id=id,
            theme=theme,
            timezone=timezone,
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

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTheme")
    def reset_theme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTheme", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

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
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="teamIdInput")
    def team_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "teamIdInput"))

    @builtins.property
    @jsii.member(jsii_name="themeInput")
    def theme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "themeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="homeDashboardId")
    def home_dashboard_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "homeDashboardId"))

    @home_dashboard_id.setter
    def home_dashboard_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df4afaffd099b675fc2618a94ec4d774e83c60fb9df8ec4a1e368ac8b2b3bb44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a793c23d3fc00ee84631748cfb61eeb38e59ac18bc9de323b72c8e5e49321387)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b03b17cd4e2b81cd20d43f5088d361fda1b0489c2a0ad3b908e5ffbe5a0f07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "theme"))

    @theme.setter
    def theme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d96689483b56c87e6818ab01fb7eefeeb1fc337dd8530e732594006c8b208cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "theme", value)

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timezone"))

    @timezone.setter
    def timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9710cea87034d04b8d5b94bfedb4f8a62ac5d69da858e9d299b6214375080013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timezone", value)


@jsii.data_type(
    jsii_type="grafana.teamPreferences.TeamPreferencesConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "team_id": "teamId",
        "home_dashboard_id": "homeDashboardId",
        "id": "id",
        "theme": "theme",
        "timezone": "timezone",
    },
)
class TeamPreferencesConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        team_id: jsii.Number,
        home_dashboard_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        theme: typing.Optional[builtins.str] = None,
        timezone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param team_id: The numeric team ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#team_id TeamPreferences#team_id}
        :param home_dashboard_id: The numeric ID of the dashboard to display when a team member logs in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#home_dashboard_id TeamPreferences#home_dashboard_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#id TeamPreferences#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param theme: The theme for the specified team. Available themes are ``light``, ``dark``, or an empty string for the default theme. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#theme TeamPreferences#theme}
        :param timezone: The timezone for the specified team. Available values are ``utc``, ``browser``, or an empty string for the default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#timezone TeamPreferences#timezone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ded592cdc85f4065d310cd03777ae9b3256cb4338ee83289994223301fcd76)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument home_dashboard_id", value=home_dashboard_id, expected_type=type_hints["home_dashboard_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument theme", value=theme, expected_type=type_hints["theme"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "team_id": team_id,
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
        if home_dashboard_id is not None:
            self._values["home_dashboard_id"] = home_dashboard_id
        if id is not None:
            self._values["id"] = id
        if theme is not None:
            self._values["theme"] = theme
        if timezone is not None:
            self._values["timezone"] = timezone

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
    def team_id(self) -> jsii.Number:
        '''The numeric team ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#team_id TeamPreferences#team_id}
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def home_dashboard_id(self) -> typing.Optional[jsii.Number]:
        '''The numeric ID of the dashboard to display when a team member logs in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#home_dashboard_id TeamPreferences#home_dashboard_id}
        '''
        result = self._values.get("home_dashboard_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#id TeamPreferences#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme(self) -> typing.Optional[builtins.str]:
        '''The theme for the specified team. Available themes are ``light``, ``dark``, or an empty string for the default theme.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#theme TeamPreferences#theme}
        '''
        result = self._values.get("theme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone for the specified team. Available values are ``utc``, ``browser``, or an empty string for the default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/team_preferences#timezone TeamPreferences#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TeamPreferencesConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "TeamPreferences",
    "TeamPreferencesConfig",
]

publication.publish()

def _typecheckingstub__14d170fd631306f35f3a52072797b771eed4c7b8af9a057cc51e45e172e8daf3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    team_id: jsii.Number,
    home_dashboard_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    theme: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__df4afaffd099b675fc2618a94ec4d774e83c60fb9df8ec4a1e368ac8b2b3bb44(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a793c23d3fc00ee84631748cfb61eeb38e59ac18bc9de323b72c8e5e49321387(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b03b17cd4e2b81cd20d43f5088d361fda1b0489c2a0ad3b908e5ffbe5a0f07(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d96689483b56c87e6818ab01fb7eefeeb1fc337dd8530e732594006c8b208cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9710cea87034d04b8d5b94bfedb4f8a62ac5d69da858e9d299b6214375080013(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ded592cdc85f4065d310cd03777ae9b3256cb4338ee83289994223301fcd76(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    team_id: jsii.Number,
    home_dashboard_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    theme: typing.Optional[builtins.str] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
