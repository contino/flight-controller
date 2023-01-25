'''
# `grafana_cloud_access_policy`

Refer to the Terraform Registory for docs: [`grafana_cloud_access_policy`](https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy).
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


class CloudAccessPolicy(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicy",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy grafana_cloud_access_policy}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        realm: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudAccessPolicyRealm", typing.Dict[builtins.str, typing.Any]]]],
        region: builtins.str,
        scopes: typing.Sequence[builtins.str],
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy grafana_cloud_access_policy} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the access policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#name CloudAccessPolicy#name}
        :param realm: realm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#realm CloudAccessPolicy#realm}
        :param region: Region where the API is deployed. Generally where the stack is deployed. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#region CloudAccessPolicy#region}
        :param scopes: Scopes of the access policy. See https://grafana.com/docs/grafana-cloud/authentication-and-permissions/access-policies/#scopes for possible values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#scopes CloudAccessPolicy#scopes}
        :param display_name: Display name of the access policy. Defaults to the name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#display_name CloudAccessPolicy#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#id CloudAccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b3c20fbf8ce6dbc89fea2a085939b5003142e3f70083ff2e32463f09444d6b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudAccessPolicyConfig(
            name=name,
            realm=realm,
            region=region,
            scopes=scopes,
            display_name=display_name,
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

    @jsii.member(jsii_name="putRealm")
    def put_realm(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudAccessPolicyRealm", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4e53911e7dd73da70e422a46d36cc3644e27ade8fca8a7f37538830351156c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRealm", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

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
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="policyId")
    def policy_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policyId"))

    @builtins.property
    @jsii.member(jsii_name="realm")
    def realm(self) -> "CloudAccessPolicyRealmList":
        return typing.cast("CloudAccessPolicyRealmList", jsii.get(self, "realm"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="realmInput")
    def realm_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudAccessPolicyRealm"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudAccessPolicyRealm"]]], jsii.get(self, "realmInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="scopesInput")
    def scopes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "scopesInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__369426943c33a931828512df27383ad54cb570a0e95bf210cce83992f915b8d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dadd32c395049c99a2fd0bba055a3072ff72934add4c594382041cb60689bda1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aac60db016620458de487b2414320767285a2e1ab2bc31596296f02ea7a088e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cacd1753a5a00e0afc137c5c4fa11c9378a784ed50d3ef67ba41ad3ced84a32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="scopes")
    def scopes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "scopes"))

    @scopes.setter
    def scopes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e28f2ffffe355531ec2e875d5ce626ebc861be1714f0a25f33b2eb5f3dc11df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopes", value)


@jsii.data_type(
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyConfig",
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
        "realm": "realm",
        "region": "region",
        "scopes": "scopes",
        "display_name": "displayName",
        "id": "id",
    },
)
class CloudAccessPolicyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        realm: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudAccessPolicyRealm", typing.Dict[builtins.str, typing.Any]]]],
        region: builtins.str,
        scopes: typing.Sequence[builtins.str],
        display_name: typing.Optional[builtins.str] = None,
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
        :param name: Name of the access policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#name CloudAccessPolicy#name}
        :param realm: realm block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#realm CloudAccessPolicy#realm}
        :param region: Region where the API is deployed. Generally where the stack is deployed. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#region CloudAccessPolicy#region}
        :param scopes: Scopes of the access policy. See https://grafana.com/docs/grafana-cloud/authentication-and-permissions/access-policies/#scopes for possible values. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#scopes CloudAccessPolicy#scopes}
        :param display_name: Display name of the access policy. Defaults to the name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#display_name CloudAccessPolicy#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#id CloudAccessPolicy#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c551b455dd339b1e90cb23993256b1565a613d4930226cee7530c92132251276)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument realm", value=realm, expected_type=type_hints["realm"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "realm": realm,
            "region": region,
            "scopes": scopes,
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
        if display_name is not None:
            self._values["display_name"] = display_name
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
    def name(self) -> builtins.str:
        '''Name of the access policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#name CloudAccessPolicy#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def realm(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudAccessPolicyRealm"]]:
        '''realm block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#realm CloudAccessPolicy#realm}
        '''
        result = self._values.get("realm")
        assert result is not None, "Required property 'realm' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudAccessPolicyRealm"]], result)

    @builtins.property
    def region(self) -> builtins.str:
        '''Region where the API is deployed.

        Generally where the stack is deployed. Use the region list API to get the list of available regions: https://grafana.com/docs/grafana-cloud/reference/cloud-api/#list-regions.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#region CloudAccessPolicy#region}
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scopes(self) -> typing.List[builtins.str]:
        '''Scopes of the access policy. See https://grafana.com/docs/grafana-cloud/authentication-and-permissions/access-policies/#scopes for possible values.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#scopes CloudAccessPolicy#scopes}
        '''
        result = self._values.get("scopes")
        assert result is not None, "Required property 'scopes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Display name of the access policy. Defaults to the name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#display_name CloudAccessPolicy#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#id CloudAccessPolicy#id}.

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
        return "CloudAccessPolicyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyRealm",
    jsii_struct_bases=[],
    name_mapping={
        "identifier": "identifier",
        "type": "type",
        "label_policy": "labelPolicy",
    },
)
class CloudAccessPolicyRealm:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        type: builtins.str,
        label_policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CloudAccessPolicyRealmLabelPolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param identifier: The identifier of the org or stack. For orgs, this is the slug, for stacks, this is the stack ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#identifier CloudAccessPolicy#identifier}
        :param type: Whether a policy applies to a Cloud org or a specific stack. Should be one of ``org`` or ``stack``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#type CloudAccessPolicy#type}
        :param label_policy: label_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#label_policy CloudAccessPolicy#label_policy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d3dc6e3a75cc1a4a7f2e327ec0d6b2ad6252a0c7632a65cd88e6545e5771aa)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument label_policy", value=label_policy, expected_type=type_hints["label_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifier": identifier,
            "type": type,
        }
        if label_policy is not None:
            self._values["label_policy"] = label_policy

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The identifier of the org or stack.

        For orgs, this is the slug, for stacks, this is the stack ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#identifier CloudAccessPolicy#identifier}
        '''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Whether a policy applies to a Cloud org or a specific stack. Should be one of ``org`` or ``stack``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#type CloudAccessPolicy#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def label_policy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudAccessPolicyRealmLabelPolicy"]]]:
        '''label_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#label_policy CloudAccessPolicy#label_policy}
        '''
        result = self._values.get("label_policy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CloudAccessPolicyRealmLabelPolicy"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAccessPolicyRealm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyRealmLabelPolicy",
    jsii_struct_bases=[],
    name_mapping={"selector": "selector"},
)
class CloudAccessPolicyRealmLabelPolicy:
    def __init__(self, *, selector: builtins.str) -> None:
        '''
        :param selector: The label selector to match in metrics or logs query. Should be in PromQL or LogQL format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#selector CloudAccessPolicy#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adef1610622c792f5c3eec03b3e9b98731bc1c095abbe63093b54532c93511c4)
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "selector": selector,
        }

    @builtins.property
    def selector(self) -> builtins.str:
        '''The label selector to match in metrics or logs query. Should be in PromQL or LogQL format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/cloud_access_policy#selector CloudAccessPolicy#selector}
        '''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAccessPolicyRealmLabelPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAccessPolicyRealmLabelPolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyRealmLabelPolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcda1e51202691c2279c2f272806f555b80e99f923a059d691456b90a9cf9a63)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CloudAccessPolicyRealmLabelPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d02ab3e72bac4a202c167561476a8acb9417f03d0c4490d3bcf5202a32a5ac0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudAccessPolicyRealmLabelPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f83d50ed4592f4c965eec49f96919977dd33fa946362a79afb5c3db3077a46)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31d92e9b0d28ca4b24859f89fe295d4cbfa6395fe9c66c93c71457c7d77f7784)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ccd48b9bde07e5b0c64447c0815eef8fb0022098ae40160e21524b628e5ef67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealmLabelPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealmLabelPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealmLabelPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c05e8949cf2088854da94446c4b741aca2c044bf1ff0662b272447650743701)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudAccessPolicyRealmLabelPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyRealmLabelPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__949b1a13b7f06916ecab69715b25ad71f7ed82622ba7f66db9aab916b6083483)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19595dc0a4f9696ebc9787f84d0964de159b1a6ed165548f99af4f8ea1f0d727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudAccessPolicyRealmLabelPolicy, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudAccessPolicyRealmLabelPolicy, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudAccessPolicyRealmLabelPolicy, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aedbc5818c1682f38e5c0ed44b8c82b75de65f062b6b49a66786ff4dae5340a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudAccessPolicyRealmList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyRealmList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__58fa3bc0e36c1e25cfde6db00f6f77932bed6fa5fab11621322d5eb431bcc056)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CloudAccessPolicyRealmOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__658f863d9c9a51d848a7867ef327b18730851e5211d89ac30eee1ba5319de6e5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CloudAccessPolicyRealmOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e5494dba6060a4edae46e0d555fa25b7ad727c84492cd213beda5d4a16f70f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d950e97c675423b917f0975a5eb17d000fa0f28b08d84729849e66975d9d9c69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3233b2adfa92009d9fe5e10c2261c167dc534815f2bb76f2bca8883277ec5d87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealm]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e945b9fcacd3b11fcd10a82c9a1b01eece0ef8dcb7014f8150b1ccd7b0d30b4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CloudAccessPolicyRealmOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.cloudAccessPolicy.CloudAccessPolicyRealmOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7d9a57f9abb1d1a264e28fc74f2d465ed63cf183d51b19055516a416ef60a61)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLabelPolicy")
    def put_label_policy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudAccessPolicyRealmLabelPolicy, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c52d597439a217f5126cf7342752b83246e9da5cfff45ae4a93ad77ea5f5fc14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabelPolicy", [value]))

    @jsii.member(jsii_name="resetLabelPolicy")
    def reset_label_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="labelPolicy")
    def label_policy(self) -> CloudAccessPolicyRealmLabelPolicyList:
        return typing.cast(CloudAccessPolicyRealmLabelPolicyList, jsii.get(self, "labelPolicy"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="labelPolicyInput")
    def label_policy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealmLabelPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealmLabelPolicy]]], jsii.get(self, "labelPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34d62302896b8358dcd3216282ccb1528d23564864206534b4710b678e5d0c7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a29defdc1fc41c53e4bf98967aaae436c151e45089ee19d919dd7fadc700def)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CloudAccessPolicyRealm, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CloudAccessPolicyRealm, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CloudAccessPolicyRealm, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d726a63f2b9be3f1e55f569ae17b580a732a95c787d65be49d83d9e901af91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudAccessPolicy",
    "CloudAccessPolicyConfig",
    "CloudAccessPolicyRealm",
    "CloudAccessPolicyRealmLabelPolicy",
    "CloudAccessPolicyRealmLabelPolicyList",
    "CloudAccessPolicyRealmLabelPolicyOutputReference",
    "CloudAccessPolicyRealmList",
    "CloudAccessPolicyRealmOutputReference",
]

publication.publish()

def _typecheckingstub__54b3c20fbf8ce6dbc89fea2a085939b5003142e3f70083ff2e32463f09444d6b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    realm: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudAccessPolicyRealm, typing.Dict[builtins.str, typing.Any]]]],
    region: builtins.str,
    scopes: typing.Sequence[builtins.str],
    display_name: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__7d4e53911e7dd73da70e422a46d36cc3644e27ade8fca8a7f37538830351156c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudAccessPolicyRealm, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__369426943c33a931828512df27383ad54cb570a0e95bf210cce83992f915b8d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dadd32c395049c99a2fd0bba055a3072ff72934add4c594382041cb60689bda1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aac60db016620458de487b2414320767285a2e1ab2bc31596296f02ea7a088e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cacd1753a5a00e0afc137c5c4fa11c9378a784ed50d3ef67ba41ad3ced84a32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e28f2ffffe355531ec2e875d5ce626ebc861be1714f0a25f33b2eb5f3dc11df(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c551b455dd339b1e90cb23993256b1565a613d4930226cee7530c92132251276(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    realm: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudAccessPolicyRealm, typing.Dict[builtins.str, typing.Any]]]],
    region: builtins.str,
    scopes: typing.Sequence[builtins.str],
    display_name: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d3dc6e3a75cc1a4a7f2e327ec0d6b2ad6252a0c7632a65cd88e6545e5771aa(
    *,
    identifier: builtins.str,
    type: builtins.str,
    label_policy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudAccessPolicyRealmLabelPolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adef1610622c792f5c3eec03b3e9b98731bc1c095abbe63093b54532c93511c4(
    *,
    selector: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcda1e51202691c2279c2f272806f555b80e99f923a059d691456b90a9cf9a63(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d02ab3e72bac4a202c167561476a8acb9417f03d0c4490d3bcf5202a32a5ac0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f83d50ed4592f4c965eec49f96919977dd33fa946362a79afb5c3db3077a46(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d92e9b0d28ca4b24859f89fe295d4cbfa6395fe9c66c93c71457c7d77f7784(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ccd48b9bde07e5b0c64447c0815eef8fb0022098ae40160e21524b628e5ef67(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c05e8949cf2088854da94446c4b741aca2c044bf1ff0662b272447650743701(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealmLabelPolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__949b1a13b7f06916ecab69715b25ad71f7ed82622ba7f66db9aab916b6083483(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19595dc0a4f9696ebc9787f84d0964de159b1a6ed165548f99af4f8ea1f0d727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aedbc5818c1682f38e5c0ed44b8c82b75de65f062b6b49a66786ff4dae5340a5(
    value: typing.Optional[typing.Union[CloudAccessPolicyRealmLabelPolicy, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58fa3bc0e36c1e25cfde6db00f6f77932bed6fa5fab11621322d5eb431bcc056(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658f863d9c9a51d848a7867ef327b18730851e5211d89ac30eee1ba5319de6e5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e5494dba6060a4edae46e0d555fa25b7ad727c84492cd213beda5d4a16f70f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d950e97c675423b917f0975a5eb17d000fa0f28b08d84729849e66975d9d9c69(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3233b2adfa92009d9fe5e10c2261c167dc534815f2bb76f2bca8883277ec5d87(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e945b9fcacd3b11fcd10a82c9a1b01eece0ef8dcb7014f8150b1ccd7b0d30b4f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CloudAccessPolicyRealm]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d9a57f9abb1d1a264e28fc74f2d465ed63cf183d51b19055516a416ef60a61(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52d597439a217f5126cf7342752b83246e9da5cfff45ae4a93ad77ea5f5fc14(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CloudAccessPolicyRealmLabelPolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d62302896b8358dcd3216282ccb1528d23564864206534b4710b678e5d0c7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a29defdc1fc41c53e4bf98967aaae436c151e45089ee19d919dd7fadc700def(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d726a63f2b9be3f1e55f569ae17b580a732a95c787d65be49d83d9e901af91(
    value: typing.Optional[typing.Union[CloudAccessPolicyRealm, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
