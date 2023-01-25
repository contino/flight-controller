'''
# `grafana_data_source`

Refer to the Terraform Registory for docs: [`grafana_data_source`](https://www.terraform.io/docs/providers/grafana/r/data_source).
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


class DataSource(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSource",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/data_source grafana_data_source}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        access_mode: typing.Optional[builtins.str] = None,
        basic_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        basic_auth_password: typing.Optional[builtins.str] = None,
        basic_auth_username: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceJsonData", typing.Dict[builtins.str, typing.Any]]]]] = None,
        json_data_encoded: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        secure_json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceSecureJsonData", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secure_json_data_encoded: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/data_source grafana_data_source} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: A unique name for the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#name DataSource#name}
        :param type: The data source type. Must be one of the supported data source keywords. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#type DataSource#type}
        :param access_mode: The method by which Grafana will access the data source: ``proxy`` or ``direct``. Defaults to ``proxy``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_mode DataSource#access_mode}
        :param basic_auth_enabled: Whether to enable basic auth for the data source. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_enabled DataSource#basic_auth_enabled}
        :param basic_auth_password: Use secure_json_data_encoded.basicAuthPassword instead. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_password DataSource#basic_auth_password}
        :param basic_auth_username: Basic auth username. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_username DataSource#basic_auth_username}
        :param database_name: (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#database_name DataSource#database_name}
        :param http_headers: Custom HTTP headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#http_headers DataSource#http_headers}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#id DataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Whether to set the data source as default. This should only be ``true`` to a single data source. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#is_default DataSource#is_default}
        :param json_data: json_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#json_data DataSource#json_data}
        :param json_data_encoded: Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#json_data_encoded DataSource#json_data_encoded}
        :param password: Use secure_json_data_encoded.password instead. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#password DataSource#password}
        :param secure_json_data: secure_json_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secure_json_data DataSource#secure_json_data}
        :param secure_json_data_encoded: Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secure_json_data_encoded DataSource#secure_json_data_encoded}
        :param uid: Unique identifier. If unset, this will be automatically generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#uid DataSource#uid}
        :param url: The URL for the data source. The type of URL required varies depending on the chosen data source type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#url DataSource#url}
        :param username: (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#username DataSource#username}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b8dec4b48d7119e7578e5f174056cdb59f1c04c2b0697a78287c6e6206a815)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataSourceConfig(
            name=name,
            type=type,
            access_mode=access_mode,
            basic_auth_enabled=basic_auth_enabled,
            basic_auth_password=basic_auth_password,
            basic_auth_username=basic_auth_username,
            database_name=database_name,
            http_headers=http_headers,
            id=id,
            is_default=is_default,
            json_data=json_data,
            json_data_encoded=json_data_encoded,
            password=password,
            secure_json_data=secure_json_data,
            secure_json_data_encoded=secure_json_data_encoded,
            uid=uid,
            url=url,
            username=username,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putJsonData")
    def put_json_data(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceJsonData", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7120ce6719f2019de75de8012b5a544302c7a8d7d0c255579c0622a6776dfa2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putJsonData", [value]))

    @jsii.member(jsii_name="putSecureJsonData")
    def put_secure_json_data(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceSecureJsonData", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1603318e5a629e9795bc96703b533bd23dabd53b19ade144dde77b60bf07244)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecureJsonData", [value]))

    @jsii.member(jsii_name="resetAccessMode")
    def reset_access_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessMode", []))

    @jsii.member(jsii_name="resetBasicAuthEnabled")
    def reset_basic_auth_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthEnabled", []))

    @jsii.member(jsii_name="resetBasicAuthPassword")
    def reset_basic_auth_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthPassword", []))

    @jsii.member(jsii_name="resetBasicAuthUsername")
    def reset_basic_auth_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthUsername", []))

    @jsii.member(jsii_name="resetDatabaseName")
    def reset_database_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseName", []))

    @jsii.member(jsii_name="resetHttpHeaders")
    def reset_http_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpHeaders", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="resetJsonData")
    def reset_json_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonData", []))

    @jsii.member(jsii_name="resetJsonDataEncoded")
    def reset_json_data_encoded(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonDataEncoded", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSecureJsonData")
    def reset_secure_json_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureJsonData", []))

    @jsii.member(jsii_name="resetSecureJsonDataEncoded")
    def reset_secure_json_data_encoded(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecureJsonDataEncoded", []))

    @jsii.member(jsii_name="resetUid")
    def reset_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUid", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="jsonData")
    def json_data(self) -> "DataSourceJsonDataList":
        return typing.cast("DataSourceJsonDataList", jsii.get(self, "jsonData"))

    @builtins.property
    @jsii.member(jsii_name="secureJsonData")
    def secure_json_data(self) -> "DataSourceSecureJsonDataList":
        return typing.cast("DataSourceSecureJsonDataList", jsii.get(self, "secureJsonData"))

    @builtins.property
    @jsii.member(jsii_name="accessModeInput")
    def access_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessModeInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthEnabledInput")
    def basic_auth_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "basicAuthEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthPasswordInput")
    def basic_auth_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthUsernameInput")
    def basic_auth_username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseNameInput")
    def database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="httpHeadersInput")
    def http_headers_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "httpHeadersInput"))

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
    @jsii.member(jsii_name="jsonDataEncodedInput")
    def json_data_encoded_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonDataEncodedInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonDataInput")
    def json_data_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceJsonData"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceJsonData"]]], jsii.get(self, "jsonDataInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="secureJsonDataEncodedInput")
    def secure_json_data_encoded_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secureJsonDataEncodedInput"))

    @builtins.property
    @jsii.member(jsii_name="secureJsonDataInput")
    def secure_json_data_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceSecureJsonData"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceSecureJsonData"]]], jsii.get(self, "secureJsonDataInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="accessMode")
    def access_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessMode"))

    @access_mode.setter
    def access_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734c391bb5835007a6c3c859845fec868baa66beac8d7358e60bb8881b76641c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessMode", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthEnabled")
    def basic_auth_enabled(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "basicAuthEnabled"))

    @basic_auth_enabled.setter
    def basic_auth_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51fcbe00ae3fe694dbd9fef8686d66740adb691dc1e3d19fbe14201df14998a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthPassword")
    def basic_auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthPassword"))

    @basic_auth_password.setter
    def basic_auth_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7df44787d1d3ca335850f181fc9bdab687cffe9e994f9bde17037df03b4f128f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthPassword", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthUsername")
    def basic_auth_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthUsername"))

    @basic_auth_username.setter
    def basic_auth_username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89db1f21e30975157b4d964120833a900b96d7957b975df1fa840111285045b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthUsername", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__864d1f88dd58d3e06048170a0569a782f97a6d9d629632938a3372bc822249ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="httpHeaders")
    def http_headers(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "httpHeaders"))

    @http_headers.setter
    def http_headers(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c527cb764c8792228f69ed81ea4c1cb2b685b709ccc38375377aa6e39056cecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75312fec482c3d8141b59691b0d6a274d55e63d5f29229e2e6ab10ee0a5912f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c4bc7bc9fc8968727bfa977d4e521062a5adbfac88316d493f1c7b147f54dfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="jsonDataEncoded")
    def json_data_encoded(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonDataEncoded"))

    @json_data_encoded.setter
    def json_data_encoded(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1337e6ad9b7a3e0c9463a95f27edc010f4a4a14f7500adc98b0bc39c393fc65b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonDataEncoded", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fe948bd39650f414260dd2b3b75e27fd738ca1e0194198ee2963ae1c1e99dbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f637e76b24dfe237a5ea116fb85d53b00c1d93545c474eb349acffa47ecaefa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="secureJsonDataEncoded")
    def secure_json_data_encoded(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secureJsonDataEncoded"))

    @secure_json_data_encoded.setter
    def secure_json_data_encoded(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c0234e4d7ad783729ae57ae2bfe2ed0e51ba3d5ddc67df4513214a916dd114)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secureJsonDataEncoded", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c8e1797e5439540d412281d456f8126070487d1f89687bdd71f5611b25df21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec3911837ba8e539883990d29874e784bfb72d4244f43f6d7dd1f00260649346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d834bec290bb01ba66aea76c7c74bdf1f4b32b5ab739f8b6db393115277842f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42d5a32c2285f82ec5f6939c75a923c2642be7e51136f3f66d316f36282355fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="grafana.dataSource.DataSourceConfig",
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
        "access_mode": "accessMode",
        "basic_auth_enabled": "basicAuthEnabled",
        "basic_auth_password": "basicAuthPassword",
        "basic_auth_username": "basicAuthUsername",
        "database_name": "databaseName",
        "http_headers": "httpHeaders",
        "id": "id",
        "is_default": "isDefault",
        "json_data": "jsonData",
        "json_data_encoded": "jsonDataEncoded",
        "password": "password",
        "secure_json_data": "secureJsonData",
        "secure_json_data_encoded": "secureJsonDataEncoded",
        "uid": "uid",
        "url": "url",
        "username": "username",
    },
)
class DataSourceConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        access_mode: typing.Optional[builtins.str] = None,
        basic_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        basic_auth_password: typing.Optional[builtins.str] = None,
        basic_auth_username: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceJsonData", typing.Dict[builtins.str, typing.Any]]]]] = None,
        json_data_encoded: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        secure_json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceSecureJsonData", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secure_json_data_encoded: typing.Optional[builtins.str] = None,
        uid: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: A unique name for the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#name DataSource#name}
        :param type: The data source type. Must be one of the supported data source keywords. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#type DataSource#type}
        :param access_mode: The method by which Grafana will access the data source: ``proxy`` or ``direct``. Defaults to ``proxy``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_mode DataSource#access_mode}
        :param basic_auth_enabled: Whether to enable basic auth for the data source. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_enabled DataSource#basic_auth_enabled}
        :param basic_auth_password: Use secure_json_data_encoded.basicAuthPassword instead. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_password DataSource#basic_auth_password}
        :param basic_auth_username: Basic auth username. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_username DataSource#basic_auth_username}
        :param database_name: (Required by some data source types) The name of the database to use on the selected data source server. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#database_name DataSource#database_name}
        :param http_headers: Custom HTTP headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#http_headers DataSource#http_headers}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#id DataSource#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Whether to set the data source as default. This should only be ``true`` to a single data source. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#is_default DataSource#is_default}
        :param json_data: json_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#json_data DataSource#json_data}
        :param json_data_encoded: Serialized JSON string containing the json data. This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#json_data_encoded DataSource#json_data_encoded}
        :param password: Use secure_json_data_encoded.password instead. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#password DataSource#password}
        :param secure_json_data: secure_json_data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secure_json_data DataSource#secure_json_data}
        :param secure_json_data_encoded: Serialized JSON string containing the secure json data. This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secure_json_data_encoded DataSource#secure_json_data_encoded}
        :param uid: Unique identifier. If unset, this will be automatically generated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#uid DataSource#uid}
        :param url: The URL for the data source. The type of URL required varies depending on the chosen data source type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#url DataSource#url}
        :param username: (Required by some data source types) The username to use to authenticate to the data source. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#username DataSource#username}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cecf55e8dd515cf51605327eb35b25f495dae0ac159c3ad09d0c27ff93c8177)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument access_mode", value=access_mode, expected_type=type_hints["access_mode"])
            check_type(argname="argument basic_auth_enabled", value=basic_auth_enabled, expected_type=type_hints["basic_auth_enabled"])
            check_type(argname="argument basic_auth_password", value=basic_auth_password, expected_type=type_hints["basic_auth_password"])
            check_type(argname="argument basic_auth_username", value=basic_auth_username, expected_type=type_hints["basic_auth_username"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument http_headers", value=http_headers, expected_type=type_hints["http_headers"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
            check_type(argname="argument json_data", value=json_data, expected_type=type_hints["json_data"])
            check_type(argname="argument json_data_encoded", value=json_data_encoded, expected_type=type_hints["json_data_encoded"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument secure_json_data", value=secure_json_data, expected_type=type_hints["secure_json_data"])
            check_type(argname="argument secure_json_data_encoded", value=secure_json_data_encoded, expected_type=type_hints["secure_json_data_encoded"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
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
        if access_mode is not None:
            self._values["access_mode"] = access_mode
        if basic_auth_enabled is not None:
            self._values["basic_auth_enabled"] = basic_auth_enabled
        if basic_auth_password is not None:
            self._values["basic_auth_password"] = basic_auth_password
        if basic_auth_username is not None:
            self._values["basic_auth_username"] = basic_auth_username
        if database_name is not None:
            self._values["database_name"] = database_name
        if http_headers is not None:
            self._values["http_headers"] = http_headers
        if id is not None:
            self._values["id"] = id
        if is_default is not None:
            self._values["is_default"] = is_default
        if json_data is not None:
            self._values["json_data"] = json_data
        if json_data_encoded is not None:
            self._values["json_data_encoded"] = json_data_encoded
        if password is not None:
            self._values["password"] = password
        if secure_json_data is not None:
            self._values["secure_json_data"] = secure_json_data
        if secure_json_data_encoded is not None:
            self._values["secure_json_data_encoded"] = secure_json_data_encoded
        if uid is not None:
            self._values["uid"] = uid
        if url is not None:
            self._values["url"] = url
        if username is not None:
            self._values["username"] = username

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
        '''A unique name for the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#name DataSource#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The data source type. Must be one of the supported data source keywords.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#type DataSource#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_mode(self) -> typing.Optional[builtins.str]:
        '''The method by which Grafana will access the data source: ``proxy`` or ``direct``. Defaults to ``proxy``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_mode DataSource#access_mode}
        '''
        result = self._values.get("access_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_auth_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to enable basic auth for the data source. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_enabled DataSource#basic_auth_enabled}
        '''
        result = self._values.get("basic_auth_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def basic_auth_password(self) -> typing.Optional[builtins.str]:
        '''Use secure_json_data_encoded.basicAuthPassword instead. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_password DataSource#basic_auth_password}
        '''
        result = self._values.get("basic_auth_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_auth_username(self) -> typing.Optional[builtins.str]:
        '''Basic auth username. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_username DataSource#basic_auth_username}
        '''
        result = self._values.get("basic_auth_username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''(Required by some data source types) The name of the database to use on the selected data source server.

        Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#database_name DataSource#database_name}
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Custom HTTP headers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#http_headers DataSource#http_headers}
        '''
        result = self._values.get("http_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#id DataSource#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to set the data source as default.

        This should only be ``true`` to a single data source. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#is_default DataSource#is_default}
        '''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def json_data(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceJsonData"]]]:
        '''json_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#json_data DataSource#json_data}
        '''
        result = self._values.get("json_data")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceJsonData"]]], result)

    @builtins.property
    def json_data_encoded(self) -> typing.Optional[builtins.str]:
        '''Serialized JSON string containing the json data.

        This attribute can be used to pass configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#json_data_encoded DataSource#json_data_encoded}
        '''
        result = self._values.get("json_data_encoded")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Use secure_json_data_encoded.password instead. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#password DataSource#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secure_json_data(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceSecureJsonData"]]]:
        '''secure_json_data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secure_json_data DataSource#secure_json_data}
        '''
        result = self._values.get("secure_json_data")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceSecureJsonData"]]], result)

    @builtins.property
    def secure_json_data_encoded(self) -> typing.Optional[builtins.str]:
        '''Serialized JSON string containing the secure json data.

        This attribute can be used to pass secure configuration options to the data source. To figure out what options a datasource has available, see its docs or inspect the network data when saving it from the Grafana UI. Note that keys in this map are usually camelCased.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secure_json_data_encoded DataSource#secure_json_data_encoded}
        '''
        result = self._values.get("secure_json_data_encoded")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uid(self) -> typing.Optional[builtins.str]:
        '''Unique identifier. If unset, this will be automatically generated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#uid DataSource#uid}
        '''
        result = self._values.get("uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''The URL for the data source. The type of URL required varies depending on the chosen data source type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#url DataSource#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''(Required by some data source types) The username to use to authenticate to the data source. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#username DataSource#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.dataSource.DataSourceJsonData",
    jsii_struct_bases=[],
    name_mapping={
        "alertmanager_uid": "alertmanagerUid",
        "assume_role_arn": "assumeRoleArn",
        "authentication_type": "authenticationType",
        "auth_type": "authType",
        "catalog": "catalog",
        "client_email": "clientEmail",
        "client_id": "clientId",
        "cloud_name": "cloudName",
        "conn_max_lifetime": "connMaxLifetime",
        "custom_metrics_namespaces": "customMetricsNamespaces",
        "database": "database",
        "default_bucket": "defaultBucket",
        "default_project": "defaultProject",
        "default_region": "defaultRegion",
        "derived_field": "derivedField",
        "encrypt": "encrypt",
        "es_version": "esVersion",
        "external_id": "externalId",
        "github_url": "githubUrl",
        "graphite_version": "graphiteVersion",
        "http_method": "httpMethod",
        "implementation": "implementation",
        "interval": "interval",
        "log_level_field": "logLevelField",
        "log_message_field": "logMessageField",
        "manage_alerts": "manageAlerts",
        "max_concurrent_shard_requests": "maxConcurrentShardRequests",
        "max_idle_conns": "maxIdleConns",
        "max_lines": "maxLines",
        "max_open_conns": "maxOpenConns",
        "organization": "organization",
        "org_slug": "orgSlug",
        "output_location": "outputLocation",
        "postgres_version": "postgresVersion",
        "profile": "profile",
        "query_timeout": "queryTimeout",
        "sigv4_assume_role_arn": "sigv4AssumeRoleArn",
        "sigv4_auth": "sigv4Auth",
        "sigv4_auth_type": "sigv4AuthType",
        "sigv4_external_id": "sigv4ExternalId",
        "sigv4_profile": "sigv4Profile",
        "sigv4_region": "sigv4Region",
        "ssl_mode": "sslMode",
        "subscription_id": "subscriptionId",
        "tenant_id": "tenantId",
        "time_field": "timeField",
        "time_interval": "timeInterval",
        "timescaledb": "timescaledb",
        "tls_auth": "tlsAuth",
        "tls_auth_with_ca_cert": "tlsAuthWithCaCert",
        "tls_configuration_method": "tlsConfigurationMethod",
        "tls_skip_verify": "tlsSkipVerify",
        "token_uri": "tokenUri",
        "tracing_datasource_uid": "tracingDatasourceUid",
        "tsdb_resolution": "tsdbResolution",
        "tsdb_version": "tsdbVersion",
        "version": "version",
        "workgroup": "workgroup",
        "xpack_enabled": "xpackEnabled",
    },
)
class DataSourceJsonData:
    def __init__(
        self,
        *,
        alertmanager_uid: typing.Optional[builtins.str] = None,
        assume_role_arn: typing.Optional[builtins.str] = None,
        authentication_type: typing.Optional[builtins.str] = None,
        auth_type: typing.Optional[builtins.str] = None,
        catalog: typing.Optional[builtins.str] = None,
        client_email: typing.Optional[builtins.str] = None,
        client_id: typing.Optional[builtins.str] = None,
        cloud_name: typing.Optional[builtins.str] = None,
        conn_max_lifetime: typing.Optional[jsii.Number] = None,
        custom_metrics_namespaces: typing.Optional[builtins.str] = None,
        database: typing.Optional[builtins.str] = None,
        default_bucket: typing.Optional[builtins.str] = None,
        default_project: typing.Optional[builtins.str] = None,
        default_region: typing.Optional[builtins.str] = None,
        derived_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataSourceJsonDataDerivedField", typing.Dict[builtins.str, typing.Any]]]]] = None,
        encrypt: typing.Optional[builtins.str] = None,
        es_version: typing.Optional[builtins.str] = None,
        external_id: typing.Optional[builtins.str] = None,
        github_url: typing.Optional[builtins.str] = None,
        graphite_version: typing.Optional[builtins.str] = None,
        http_method: typing.Optional[builtins.str] = None,
        implementation: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        log_level_field: typing.Optional[builtins.str] = None,
        log_message_field: typing.Optional[builtins.str] = None,
        manage_alerts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        max_concurrent_shard_requests: typing.Optional[jsii.Number] = None,
        max_idle_conns: typing.Optional[jsii.Number] = None,
        max_lines: typing.Optional[jsii.Number] = None,
        max_open_conns: typing.Optional[jsii.Number] = None,
        organization: typing.Optional[builtins.str] = None,
        org_slug: typing.Optional[builtins.str] = None,
        output_location: typing.Optional[builtins.str] = None,
        postgres_version: typing.Optional[jsii.Number] = None,
        profile: typing.Optional[builtins.str] = None,
        query_timeout: typing.Optional[builtins.str] = None,
        sigv4_assume_role_arn: typing.Optional[builtins.str] = None,
        sigv4_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        sigv4_auth_type: typing.Optional[builtins.str] = None,
        sigv4_external_id: typing.Optional[builtins.str] = None,
        sigv4_profile: typing.Optional[builtins.str] = None,
        sigv4_region: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        subscription_id: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
        time_field: typing.Optional[builtins.str] = None,
        time_interval: typing.Optional[builtins.str] = None,
        timescaledb: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_auth_with_ca_cert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        tls_configuration_method: typing.Optional[builtins.str] = None,
        tls_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        token_uri: typing.Optional[builtins.str] = None,
        tracing_datasource_uid: typing.Optional[builtins.str] = None,
        tsdb_resolution: typing.Optional[jsii.Number] = None,
        tsdb_version: typing.Optional[jsii.Number] = None,
        version: typing.Optional[builtins.str] = None,
        workgroup: typing.Optional[builtins.str] = None,
        xpack_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param alertmanager_uid: (Prometheus) The name of the Alertmanager datasource to manage alerts via UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#alertmanager_uid DataSource#alertmanager_uid}
        :param assume_role_arn: (CloudWatch, Athena) The ARN of the role to be assumed by Grafana when using the CloudWatch or Athena data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#assume_role_arn DataSource#assume_role_arn}
        :param authentication_type: (Stackdriver) The authentication type: ``jwt`` or ``gce``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#authentication_type DataSource#authentication_type}
        :param auth_type: (CloudWatch, Athena) The authentication type used to access the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#auth_type DataSource#auth_type}
        :param catalog: (Athena) Athena catalog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#catalog DataSource#catalog}
        :param client_email: (Stackdriver) Service account email address. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#client_email DataSource#client_email}
        :param client_id: (Azure Monitor) The service account client id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#client_id DataSource#client_id}
        :param cloud_name: (Azure Monitor) The cloud name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#cloud_name DataSource#cloud_name}
        :param conn_max_lifetime: (MySQL, PostgreSQL, and MSSQL) Maximum amount of time in seconds a connection may be reused (Grafana v5.4+). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#conn_max_lifetime DataSource#conn_max_lifetime}
        :param custom_metrics_namespaces: (CloudWatch) A comma-separated list of custom namespaces to be queried by the CloudWatch data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#custom_metrics_namespaces DataSource#custom_metrics_namespaces}
        :param database: (Athena) Name of the database within the catalog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#database DataSource#database}
        :param default_bucket: (InfluxDB) The default bucket for the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#default_bucket DataSource#default_bucket}
        :param default_project: (Stackdriver) The default project for the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#default_project DataSource#default_project}
        :param default_region: (CloudWatch, Athena) The default region for the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#default_region DataSource#default_region}
        :param derived_field: derived_field block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#derived_field DataSource#derived_field}
        :param encrypt: (MSSQL) Connection SSL encryption handling: 'disable', 'false' or 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#encrypt DataSource#encrypt}
        :param es_version: (Elasticsearch) Elasticsearch semantic version (Grafana v8.0+). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#es_version DataSource#es_version}
        :param external_id: (CloudWatch, Athena) If you are assuming a role in another account, that has been created with an external ID, specify the external ID here. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#external_id DataSource#external_id}
        :param github_url: (Github) Github URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#github_url DataSource#github_url}
        :param graphite_version: (Graphite) Graphite version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#graphite_version DataSource#graphite_version}
        :param http_method: (Prometheus) HTTP method to use for making requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#http_method DataSource#http_method}
        :param implementation: (Alertmanager) Implementation of Alertmanager. Either 'cortex' or 'prometheus'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#implementation DataSource#implementation}
        :param interval: (Elasticsearch) Index date time format. nil(No Pattern), 'Hourly', 'Daily', 'Weekly', 'Monthly' or 'Yearly'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#interval DataSource#interval}
        :param log_level_field: (Elasticsearch) Which field should be used to indicate the priority of the log message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#log_level_field DataSource#log_level_field}
        :param log_message_field: (Elasticsearch) Which field should be used as the log message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#log_message_field DataSource#log_message_field}
        :param manage_alerts: (Prometheus) Manage alerts. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#manage_alerts DataSource#manage_alerts}
        :param max_concurrent_shard_requests: (Elasticsearch) Maximum number of concurrent shard requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_concurrent_shard_requests DataSource#max_concurrent_shard_requests}
        :param max_idle_conns: (MySQL, PostgreSQL and MSSQL) Maximum number of connections in the idle connection pool (Grafana v5.4+). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_idle_conns DataSource#max_idle_conns}
        :param max_lines: (Loki) Upper limit for the number of log lines returned by Loki. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_lines DataSource#max_lines}
        :param max_open_conns: (MySQL, PostgreSQL and MSSQL) Maximum number of open connections to the database (Grafana v5.4+). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_open_conns DataSource#max_open_conns}
        :param organization: (InfluxDB) An organization is a workspace for a group of users. All dashboards, tasks, buckets, members, etc., belong to an organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#organization DataSource#organization}
        :param org_slug: (Sentry) Organization slug. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#org_slug DataSource#org_slug}
        :param output_location: (Athena) AWS S3 bucket to store execution outputs. If not specified, the default query result location from the Workgroup configuration will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#output_location DataSource#output_location}
        :param postgres_version: (PostgreSQL) Postgres version as a number (903/904/905/906/1000) meaning v9.3, v9.4, etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#postgres_version DataSource#postgres_version}
        :param profile: (CloudWatch, Athena) The credentials profile name to use when authentication type is set as 'Credentials file'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#profile DataSource#profile}
        :param query_timeout: (Prometheus) Timeout for queries made to the Prometheus data source in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#query_timeout DataSource#query_timeout}
        :param sigv4_assume_role_arn: (Elasticsearch and Prometheus) Specifies the ARN of an IAM role to assume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_assume_role_arn DataSource#sigv4_assume_role_arn}
        :param sigv4_auth: (Elasticsearch and Prometheus) Enable usage of SigV4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_auth DataSource#sigv4_auth}
        :param sigv4_auth_type: (Elasticsearch and Prometheus) The Sigv4 authentication provider to use: 'default', 'credentials' or 'keys' (AMG: 'workspace-iam-role'). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_auth_type DataSource#sigv4_auth_type}
        :param sigv4_external_id: (Elasticsearch and Prometheus) When assuming a role in another account use this external ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_external_id DataSource#sigv4_external_id}
        :param sigv4_profile: (Elasticsearch and Prometheus) Credentials profile name, leave blank for default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_profile DataSource#sigv4_profile}
        :param sigv4_region: (Elasticsearch and Prometheus) AWS region to use for Sigv4. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_region DataSource#sigv4_region}
        :param ssl_mode: (PostgreSQL) SSLmode. 'disable', 'require', 'verify-ca' or 'verify-full'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#ssl_mode DataSource#ssl_mode}
        :param subscription_id: (Azure Monitor) The subscription id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#subscription_id DataSource#subscription_id}
        :param tenant_id: (Azure Monitor) Service account tenant ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tenant_id DataSource#tenant_id}
        :param time_field: (Elasticsearch) Which field that should be used as timestamp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#time_field DataSource#time_field}
        :param time_interval: (Prometheus, Elasticsearch, InfluxDB, MySQL, PostgreSQL, and MSSQL) Lowest interval/step value that should be used for this data source. Sometimes called "Scrape Interval" in the Grafana UI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#time_interval DataSource#time_interval}
        :param timescaledb: (PostgreSQL) Enable usage of TimescaleDB extension. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#timescaledb DataSource#timescaledb}
        :param tls_auth: (All) Enable TLS authentication using client cert configured in secure json data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_auth DataSource#tls_auth}
        :param tls_auth_with_ca_cert: (All) Enable TLS authentication using CA cert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_auth_with_ca_cert DataSource#tls_auth_with_ca_cert}
        :param tls_configuration_method: (All) SSL Certificate configuration, either by ‘file-path’ or ‘file-content’. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_configuration_method DataSource#tls_configuration_method}
        :param tls_skip_verify: (All) Controls whether a client verifies the server’s certificate chain and host name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_skip_verify DataSource#tls_skip_verify}
        :param token_uri: (Stackdriver) The token URI used, provided in the service account key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#token_uri DataSource#token_uri}
        :param tracing_datasource_uid: (Cloudwatch) The X-Ray datasource uid to associate to this Cloudwatch datasource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tracing_datasource_uid DataSource#tracing_datasource_uid}
        :param tsdb_resolution: (OpenTSDB) Resolution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tsdb_resolution DataSource#tsdb_resolution}
        :param tsdb_version: (OpenTSDB) Version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tsdb_version DataSource#tsdb_version}
        :param version: (InfluxDB) InfluxQL or Flux. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#version DataSource#version}
        :param workgroup: (Athena) Workgroup to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#workgroup DataSource#workgroup}
        :param xpack_enabled: (Elasticsearch) Enable X-Pack support. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#xpack_enabled DataSource#xpack_enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__702c59a2bdc59e17d2c74713a4429c03889bf73250f72b44842604f93a960bdd)
            check_type(argname="argument alertmanager_uid", value=alertmanager_uid, expected_type=type_hints["alertmanager_uid"])
            check_type(argname="argument assume_role_arn", value=assume_role_arn, expected_type=type_hints["assume_role_arn"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument catalog", value=catalog, expected_type=type_hints["catalog"])
            check_type(argname="argument client_email", value=client_email, expected_type=type_hints["client_email"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument cloud_name", value=cloud_name, expected_type=type_hints["cloud_name"])
            check_type(argname="argument conn_max_lifetime", value=conn_max_lifetime, expected_type=type_hints["conn_max_lifetime"])
            check_type(argname="argument custom_metrics_namespaces", value=custom_metrics_namespaces, expected_type=type_hints["custom_metrics_namespaces"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument default_bucket", value=default_bucket, expected_type=type_hints["default_bucket"])
            check_type(argname="argument default_project", value=default_project, expected_type=type_hints["default_project"])
            check_type(argname="argument default_region", value=default_region, expected_type=type_hints["default_region"])
            check_type(argname="argument derived_field", value=derived_field, expected_type=type_hints["derived_field"])
            check_type(argname="argument encrypt", value=encrypt, expected_type=type_hints["encrypt"])
            check_type(argname="argument es_version", value=es_version, expected_type=type_hints["es_version"])
            check_type(argname="argument external_id", value=external_id, expected_type=type_hints["external_id"])
            check_type(argname="argument github_url", value=github_url, expected_type=type_hints["github_url"])
            check_type(argname="argument graphite_version", value=graphite_version, expected_type=type_hints["graphite_version"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument implementation", value=implementation, expected_type=type_hints["implementation"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument log_level_field", value=log_level_field, expected_type=type_hints["log_level_field"])
            check_type(argname="argument log_message_field", value=log_message_field, expected_type=type_hints["log_message_field"])
            check_type(argname="argument manage_alerts", value=manage_alerts, expected_type=type_hints["manage_alerts"])
            check_type(argname="argument max_concurrent_shard_requests", value=max_concurrent_shard_requests, expected_type=type_hints["max_concurrent_shard_requests"])
            check_type(argname="argument max_idle_conns", value=max_idle_conns, expected_type=type_hints["max_idle_conns"])
            check_type(argname="argument max_lines", value=max_lines, expected_type=type_hints["max_lines"])
            check_type(argname="argument max_open_conns", value=max_open_conns, expected_type=type_hints["max_open_conns"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument org_slug", value=org_slug, expected_type=type_hints["org_slug"])
            check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
            check_type(argname="argument postgres_version", value=postgres_version, expected_type=type_hints["postgres_version"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument query_timeout", value=query_timeout, expected_type=type_hints["query_timeout"])
            check_type(argname="argument sigv4_assume_role_arn", value=sigv4_assume_role_arn, expected_type=type_hints["sigv4_assume_role_arn"])
            check_type(argname="argument sigv4_auth", value=sigv4_auth, expected_type=type_hints["sigv4_auth"])
            check_type(argname="argument sigv4_auth_type", value=sigv4_auth_type, expected_type=type_hints["sigv4_auth_type"])
            check_type(argname="argument sigv4_external_id", value=sigv4_external_id, expected_type=type_hints["sigv4_external_id"])
            check_type(argname="argument sigv4_profile", value=sigv4_profile, expected_type=type_hints["sigv4_profile"])
            check_type(argname="argument sigv4_region", value=sigv4_region, expected_type=type_hints["sigv4_region"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument subscription_id", value=subscription_id, expected_type=type_hints["subscription_id"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument time_field", value=time_field, expected_type=type_hints["time_field"])
            check_type(argname="argument time_interval", value=time_interval, expected_type=type_hints["time_interval"])
            check_type(argname="argument timescaledb", value=timescaledb, expected_type=type_hints["timescaledb"])
            check_type(argname="argument tls_auth", value=tls_auth, expected_type=type_hints["tls_auth"])
            check_type(argname="argument tls_auth_with_ca_cert", value=tls_auth_with_ca_cert, expected_type=type_hints["tls_auth_with_ca_cert"])
            check_type(argname="argument tls_configuration_method", value=tls_configuration_method, expected_type=type_hints["tls_configuration_method"])
            check_type(argname="argument tls_skip_verify", value=tls_skip_verify, expected_type=type_hints["tls_skip_verify"])
            check_type(argname="argument token_uri", value=token_uri, expected_type=type_hints["token_uri"])
            check_type(argname="argument tracing_datasource_uid", value=tracing_datasource_uid, expected_type=type_hints["tracing_datasource_uid"])
            check_type(argname="argument tsdb_resolution", value=tsdb_resolution, expected_type=type_hints["tsdb_resolution"])
            check_type(argname="argument tsdb_version", value=tsdb_version, expected_type=type_hints["tsdb_version"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument workgroup", value=workgroup, expected_type=type_hints["workgroup"])
            check_type(argname="argument xpack_enabled", value=xpack_enabled, expected_type=type_hints["xpack_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alertmanager_uid is not None:
            self._values["alertmanager_uid"] = alertmanager_uid
        if assume_role_arn is not None:
            self._values["assume_role_arn"] = assume_role_arn
        if authentication_type is not None:
            self._values["authentication_type"] = authentication_type
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if catalog is not None:
            self._values["catalog"] = catalog
        if client_email is not None:
            self._values["client_email"] = client_email
        if client_id is not None:
            self._values["client_id"] = client_id
        if cloud_name is not None:
            self._values["cloud_name"] = cloud_name
        if conn_max_lifetime is not None:
            self._values["conn_max_lifetime"] = conn_max_lifetime
        if custom_metrics_namespaces is not None:
            self._values["custom_metrics_namespaces"] = custom_metrics_namespaces
        if database is not None:
            self._values["database"] = database
        if default_bucket is not None:
            self._values["default_bucket"] = default_bucket
        if default_project is not None:
            self._values["default_project"] = default_project
        if default_region is not None:
            self._values["default_region"] = default_region
        if derived_field is not None:
            self._values["derived_field"] = derived_field
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if es_version is not None:
            self._values["es_version"] = es_version
        if external_id is not None:
            self._values["external_id"] = external_id
        if github_url is not None:
            self._values["github_url"] = github_url
        if graphite_version is not None:
            self._values["graphite_version"] = graphite_version
        if http_method is not None:
            self._values["http_method"] = http_method
        if implementation is not None:
            self._values["implementation"] = implementation
        if interval is not None:
            self._values["interval"] = interval
        if log_level_field is not None:
            self._values["log_level_field"] = log_level_field
        if log_message_field is not None:
            self._values["log_message_field"] = log_message_field
        if manage_alerts is not None:
            self._values["manage_alerts"] = manage_alerts
        if max_concurrent_shard_requests is not None:
            self._values["max_concurrent_shard_requests"] = max_concurrent_shard_requests
        if max_idle_conns is not None:
            self._values["max_idle_conns"] = max_idle_conns
        if max_lines is not None:
            self._values["max_lines"] = max_lines
        if max_open_conns is not None:
            self._values["max_open_conns"] = max_open_conns
        if organization is not None:
            self._values["organization"] = organization
        if org_slug is not None:
            self._values["org_slug"] = org_slug
        if output_location is not None:
            self._values["output_location"] = output_location
        if postgres_version is not None:
            self._values["postgres_version"] = postgres_version
        if profile is not None:
            self._values["profile"] = profile
        if query_timeout is not None:
            self._values["query_timeout"] = query_timeout
        if sigv4_assume_role_arn is not None:
            self._values["sigv4_assume_role_arn"] = sigv4_assume_role_arn
        if sigv4_auth is not None:
            self._values["sigv4_auth"] = sigv4_auth
        if sigv4_auth_type is not None:
            self._values["sigv4_auth_type"] = sigv4_auth_type
        if sigv4_external_id is not None:
            self._values["sigv4_external_id"] = sigv4_external_id
        if sigv4_profile is not None:
            self._values["sigv4_profile"] = sigv4_profile
        if sigv4_region is not None:
            self._values["sigv4_region"] = sigv4_region
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if subscription_id is not None:
            self._values["subscription_id"] = subscription_id
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id
        if time_field is not None:
            self._values["time_field"] = time_field
        if time_interval is not None:
            self._values["time_interval"] = time_interval
        if timescaledb is not None:
            self._values["timescaledb"] = timescaledb
        if tls_auth is not None:
            self._values["tls_auth"] = tls_auth
        if tls_auth_with_ca_cert is not None:
            self._values["tls_auth_with_ca_cert"] = tls_auth_with_ca_cert
        if tls_configuration_method is not None:
            self._values["tls_configuration_method"] = tls_configuration_method
        if tls_skip_verify is not None:
            self._values["tls_skip_verify"] = tls_skip_verify
        if token_uri is not None:
            self._values["token_uri"] = token_uri
        if tracing_datasource_uid is not None:
            self._values["tracing_datasource_uid"] = tracing_datasource_uid
        if tsdb_resolution is not None:
            self._values["tsdb_resolution"] = tsdb_resolution
        if tsdb_version is not None:
            self._values["tsdb_version"] = tsdb_version
        if version is not None:
            self._values["version"] = version
        if workgroup is not None:
            self._values["workgroup"] = workgroup
        if xpack_enabled is not None:
            self._values["xpack_enabled"] = xpack_enabled

    @builtins.property
    def alertmanager_uid(self) -> typing.Optional[builtins.str]:
        '''(Prometheus) The name of the Alertmanager datasource to manage alerts via UI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#alertmanager_uid DataSource#alertmanager_uid}
        '''
        result = self._values.get("alertmanager_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) The ARN of the role to be assumed by Grafana when using the CloudWatch or Athena data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#assume_role_arn DataSource#assume_role_arn}
        '''
        result = self._values.get("assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authentication_type(self) -> typing.Optional[builtins.str]:
        '''(Stackdriver) The authentication type: ``jwt`` or ``gce``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#authentication_type DataSource#authentication_type}
        '''
        result = self._values.get("authentication_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) The authentication type used to access the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#auth_type DataSource#auth_type}
        '''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catalog(self) -> typing.Optional[builtins.str]:
        '''(Athena) Athena catalog.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#catalog DataSource#catalog}
        '''
        result = self._values.get("catalog")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_email(self) -> typing.Optional[builtins.str]:
        '''(Stackdriver) Service account email address.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#client_email DataSource#client_email}
        '''
        result = self._values.get("client_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''(Azure Monitor) The service account client id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#client_id DataSource#client_id}
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cloud_name(self) -> typing.Optional[builtins.str]:
        '''(Azure Monitor) The cloud name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#cloud_name DataSource#cloud_name}
        '''
        result = self._values.get("cloud_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conn_max_lifetime(self) -> typing.Optional[jsii.Number]:
        '''(MySQL, PostgreSQL, and MSSQL) Maximum amount of time in seconds a connection may be reused (Grafana v5.4+).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#conn_max_lifetime DataSource#conn_max_lifetime}
        '''
        result = self._values.get("conn_max_lifetime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def custom_metrics_namespaces(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch) A comma-separated list of custom namespaces to be queried by the CloudWatch data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#custom_metrics_namespaces DataSource#custom_metrics_namespaces}
        '''
        result = self._values.get("custom_metrics_namespaces")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database(self) -> typing.Optional[builtins.str]:
        '''(Athena) Name of the database within the catalog.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#database DataSource#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_bucket(self) -> typing.Optional[builtins.str]:
        '''(InfluxDB) The default bucket for the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#default_bucket DataSource#default_bucket}
        '''
        result = self._values.get("default_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_project(self) -> typing.Optional[builtins.str]:
        '''(Stackdriver) The default project for the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#default_project DataSource#default_project}
        '''
        result = self._values.get("default_project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_region(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) The default region for the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#default_region DataSource#default_region}
        '''
        result = self._values.get("default_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def derived_field(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceJsonDataDerivedField"]]]:
        '''derived_field block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#derived_field DataSource#derived_field}
        '''
        result = self._values.get("derived_field")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataSourceJsonDataDerivedField"]]], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.str]:
        '''(MSSQL) Connection SSL encryption handling: 'disable', 'false' or 'true'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#encrypt DataSource#encrypt}
        '''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def es_version(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch) Elasticsearch semantic version (Grafana v8.0+).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#es_version DataSource#es_version}
        '''
        result = self._values.get("es_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_id(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) If you are assuming a role in another account, that has been created with an external ID, specify the external ID here.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#external_id DataSource#external_id}
        '''
        result = self._values.get("external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def github_url(self) -> typing.Optional[builtins.str]:
        '''(Github) Github URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#github_url DataSource#github_url}
        '''
        result = self._values.get("github_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def graphite_version(self) -> typing.Optional[builtins.str]:
        '''(Graphite) Graphite version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#graphite_version DataSource#graphite_version}
        '''
        result = self._values.get("graphite_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''(Prometheus) HTTP method to use for making requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#http_method DataSource#http_method}
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def implementation(self) -> typing.Optional[builtins.str]:
        '''(Alertmanager) Implementation of Alertmanager. Either 'cortex' or 'prometheus'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#implementation DataSource#implementation}
        '''
        result = self._values.get("implementation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch) Index date time format. nil(No Pattern), 'Hourly', 'Daily', 'Weekly', 'Monthly' or 'Yearly'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#interval DataSource#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_level_field(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch) Which field should be used to indicate the priority of the log message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#log_level_field DataSource#log_level_field}
        '''
        result = self._values.get("log_level_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_message_field(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch) Which field should be used as the log message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#log_message_field DataSource#log_message_field}
        '''
        result = self._values.get("log_message_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def manage_alerts(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(Prometheus) Manage alerts.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#manage_alerts DataSource#manage_alerts}
        '''
        result = self._values.get("manage_alerts")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def max_concurrent_shard_requests(self) -> typing.Optional[jsii.Number]:
        '''(Elasticsearch) Maximum number of concurrent shard requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_concurrent_shard_requests DataSource#max_concurrent_shard_requests}
        '''
        result = self._values.get("max_concurrent_shard_requests")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_idle_conns(self) -> typing.Optional[jsii.Number]:
        '''(MySQL, PostgreSQL and MSSQL) Maximum number of connections in the idle connection pool (Grafana v5.4+).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_idle_conns DataSource#max_idle_conns}
        '''
        result = self._values.get("max_idle_conns")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_lines(self) -> typing.Optional[jsii.Number]:
        '''(Loki) Upper limit for the number of log lines returned by Loki.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_lines DataSource#max_lines}
        '''
        result = self._values.get("max_lines")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_open_conns(self) -> typing.Optional[jsii.Number]:
        '''(MySQL, PostgreSQL and MSSQL) Maximum number of open connections to the database (Grafana v5.4+).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#max_open_conns DataSource#max_open_conns}
        '''
        result = self._values.get("max_open_conns")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''(InfluxDB) An organization is a workspace for a group of users.

        All dashboards, tasks, buckets, members, etc., belong to an organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#organization DataSource#organization}
        '''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def org_slug(self) -> typing.Optional[builtins.str]:
        '''(Sentry) Organization slug.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#org_slug DataSource#org_slug}
        '''
        result = self._values.get("org_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_location(self) -> typing.Optional[builtins.str]:
        '''(Athena) AWS S3 bucket to store execution outputs.

        If not specified, the default query result location from the Workgroup configuration will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#output_location DataSource#output_location}
        '''
        result = self._values.get("output_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def postgres_version(self) -> typing.Optional[jsii.Number]:
        '''(PostgreSQL) Postgres version as a number (903/904/905/906/1000) meaning v9.3, v9.4, etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#postgres_version DataSource#postgres_version}
        '''
        result = self._values.get("postgres_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) The credentials profile name to use when authentication type is set as 'Credentials file'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#profile DataSource#profile}
        '''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_timeout(self) -> typing.Optional[builtins.str]:
        '''(Prometheus) Timeout for queries made to the Prometheus data source in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#query_timeout DataSource#query_timeout}
        '''
        result = self._values.get("query_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_assume_role_arn(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) Specifies the ARN of an IAM role to assume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_assume_role_arn DataSource#sigv4_assume_role_arn}
        '''
        result = self._values.get("sigv4_assume_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(Elasticsearch and Prometheus) Enable usage of SigV4.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_auth DataSource#sigv4_auth}
        '''
        result = self._values.get("sigv4_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def sigv4_auth_type(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) The Sigv4 authentication provider to use: 'default', 'credentials' or 'keys' (AMG: 'workspace-iam-role').

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_auth_type DataSource#sigv4_auth_type}
        '''
        result = self._values.get("sigv4_auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_external_id(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) When assuming a role in another account use this external ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_external_id DataSource#sigv4_external_id}
        '''
        result = self._values.get("sigv4_external_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_profile(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) Credentials profile name, leave blank for default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_profile DataSource#sigv4_profile}
        '''
        result = self._values.get("sigv4_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_region(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) AWS region to use for Sigv4.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_region DataSource#sigv4_region}
        '''
        result = self._values.get("sigv4_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''(PostgreSQL) SSLmode. 'disable', 'require', 'verify-ca' or 'verify-full'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#ssl_mode DataSource#ssl_mode}
        '''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_id(self) -> typing.Optional[builtins.str]:
        '''(Azure Monitor) The subscription id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#subscription_id DataSource#subscription_id}
        '''
        result = self._values.get("subscription_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''(Azure Monitor) Service account tenant ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tenant_id DataSource#tenant_id}
        '''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_field(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch) Which field that should be used as timestamp.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#time_field DataSource#time_field}
        '''
        result = self._values.get("time_field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_interval(self) -> typing.Optional[builtins.str]:
        '''(Prometheus, Elasticsearch, InfluxDB, MySQL, PostgreSQL, and MSSQL) Lowest interval/step value that should be used for this data source.

        Sometimes called "Scrape Interval" in the Grafana UI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#time_interval DataSource#time_interval}
        '''
        result = self._values.get("time_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timescaledb(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(PostgreSQL) Enable usage of TimescaleDB extension.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#timescaledb DataSource#timescaledb}
        '''
        result = self._values.get("timescaledb")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_auth(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(All) Enable TLS authentication using client cert configured in secure json data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_auth DataSource#tls_auth}
        '''
        result = self._values.get("tls_auth")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_auth_with_ca_cert(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(All) Enable TLS authentication using CA cert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_auth_with_ca_cert DataSource#tls_auth_with_ca_cert}
        '''
        result = self._values.get("tls_auth_with_ca_cert")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def tls_configuration_method(self) -> typing.Optional[builtins.str]:
        '''(All) SSL Certificate configuration, either by ‘file-path’ or ‘file-content’.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_configuration_method DataSource#tls_configuration_method}
        '''
        result = self._values.get("tls_configuration_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_skip_verify(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(All) Controls whether a client verifies the server’s certificate chain and host name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_skip_verify DataSource#tls_skip_verify}
        '''
        result = self._values.get("tls_skip_verify")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def token_uri(self) -> typing.Optional[builtins.str]:
        '''(Stackdriver) The token URI used, provided in the service account key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#token_uri DataSource#token_uri}
        '''
        result = self._values.get("token_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tracing_datasource_uid(self) -> typing.Optional[builtins.str]:
        '''(Cloudwatch) The X-Ray datasource uid to associate to this Cloudwatch datasource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tracing_datasource_uid DataSource#tracing_datasource_uid}
        '''
        result = self._values.get("tracing_datasource_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tsdb_resolution(self) -> typing.Optional[jsii.Number]:
        '''(OpenTSDB) Resolution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tsdb_resolution DataSource#tsdb_resolution}
        '''
        result = self._values.get("tsdb_resolution")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tsdb_version(self) -> typing.Optional[jsii.Number]:
        '''(OpenTSDB) Version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tsdb_version DataSource#tsdb_version}
        '''
        result = self._values.get("tsdb_version")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''(InfluxDB) InfluxQL or Flux.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#version DataSource#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workgroup(self) -> typing.Optional[builtins.str]:
        '''(Athena) Workgroup to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#workgroup DataSource#workgroup}
        '''
        result = self._values.get("workgroup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def xpack_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''(Elasticsearch) Enable X-Pack support.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#xpack_enabled DataSource#xpack_enabled}
        '''
        result = self._values.get("xpack_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceJsonData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.dataSource.DataSourceJsonDataDerivedField",
    jsii_struct_bases=[],
    name_mapping={
        "datasource_uid": "datasourceUid",
        "matcher_regex": "matcherRegex",
        "name": "name",
        "url": "url",
    },
)
class DataSourceJsonDataDerivedField:
    def __init__(
        self,
        *,
        datasource_uid: typing.Optional[builtins.str] = None,
        matcher_regex: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param datasource_uid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#datasource_uid DataSource#datasource_uid}.
        :param matcher_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#matcher_regex DataSource#matcher_regex}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#name DataSource#name}.
        :param url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#url DataSource#url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e29bf14fe3b5576322ea2f8126d1c0d62d00d04eff2660ba28c9d0eb5e338c)
            check_type(argname="argument datasource_uid", value=datasource_uid, expected_type=type_hints["datasource_uid"])
            check_type(argname="argument matcher_regex", value=matcher_regex, expected_type=type_hints["matcher_regex"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if datasource_uid is not None:
            self._values["datasource_uid"] = datasource_uid
        if matcher_regex is not None:
            self._values["matcher_regex"] = matcher_regex
        if name is not None:
            self._values["name"] = name
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def datasource_uid(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#datasource_uid DataSource#datasource_uid}.'''
        result = self._values.get("datasource_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def matcher_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#matcher_regex DataSource#matcher_regex}.'''
        result = self._values.get("matcher_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#name DataSource#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#url DataSource#url}.'''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceJsonDataDerivedField(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSourceJsonDataDerivedFieldList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSourceJsonDataDerivedFieldList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__78254645448865a8c49384a90b17be4f83036ac1afcd544865580a82f2be3b94)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataSourceJsonDataDerivedFieldOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775e2aa66c881189e6f2cf527dfbe982854a60ddfa27fffdcdf6337dbfc38c7a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataSourceJsonDataDerivedFieldOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51b437577e5a815fd9599ea6877f0f752e1e1873d8ed0bb064e6115af2291a02)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b629ba4d3e3a1c5fa81e8b6e6f9e417f779e19e9fb14a30c948594b9a586821)
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
            type_hints = typing.get_type_hints(_typecheckingstub__807faf0f7e44d1154ea92b2975e78eaf2a523bb513e3b12655c34b736374c33c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonDataDerivedField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonDataDerivedField]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonDataDerivedField]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2f3b5c8a99e010dd3303dd2295389ef2fd3fd33650e0ebbeaa27c4176090e53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataSourceJsonDataDerivedFieldOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSourceJsonDataDerivedFieldOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9de194be24dd30ade56c959e52dafd4661aa9621b9e9d6fc588ddec6c8cd8f7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDatasourceUid")
    def reset_datasource_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasourceUid", []))

    @jsii.member(jsii_name="resetMatcherRegex")
    def reset_matcher_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatcherRegex", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="datasourceUidInput")
    def datasource_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasourceUidInput"))

    @builtins.property
    @jsii.member(jsii_name="matcherRegexInput")
    def matcher_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matcherRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="datasourceUid")
    def datasource_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasourceUid"))

    @datasource_uid.setter
    def datasource_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58cd515fa4c3e901e182866df1d423f6a35f7dd847605ca39aac3c819482a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasourceUid", value)

    @builtins.property
    @jsii.member(jsii_name="matcherRegex")
    def matcher_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matcherRegex"))

    @matcher_regex.setter
    def matcher_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad66adeb875d79cd1d0bda3f343bb04c3ef5e5eef3ebb5727f815c024b99d7e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matcherRegex", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c36df6805b9a772f0eedb5f282b8bed6839eee556df9e42bb985df90dfaab13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd95e88c901be08519390a22becfa5efec5236541d098300670f43daa000d589)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataSourceJsonDataDerivedField, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataSourceJsonDataDerivedField, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataSourceJsonDataDerivedField, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce03fedd8b1cfe230445238ab82a2580a4a9b3d9b66b629c58bc2eddf53427f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataSourceJsonDataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSourceJsonDataList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b954caafcd947ef0af39d74d6785c007c3749472c560b016a7be0d159f773705)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataSourceJsonDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51385ddf02665b2670eef69aea6188473b4087b7fafe0dfa1fc59c05202021ea)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataSourceJsonDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12b1cfb6d0a6d25bb2a26268a111a1dc0d6e2ed5e6c215c5c94045825b8939c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__452eda43dfe9126a60799aac4289bf04f9591ea212eac95a2423d8cc23f3b85e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__43ba55a3a844eea02d31cd4d5662bc45e67373d266e8b051ba63eb673ad84f2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonData]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonData]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95a0988e48b8ae0175306e6953d6f6af83893b3cd31bcd0f66c5e074a0e641a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataSourceJsonDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSourceJsonDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c79905866b1a80291cdc37dcad2cf02ad96546104a71cd325ea86e2be713140)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDerivedField")
    def put_derived_field(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceJsonDataDerivedField, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96ff891e838e8cca2315b885f5d626fffd2418251b7a3ab04d39abd1a2de3f77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDerivedField", [value]))

    @jsii.member(jsii_name="resetAlertmanagerUid")
    def reset_alertmanager_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertmanagerUid", []))

    @jsii.member(jsii_name="resetAssumeRoleArn")
    def reset_assume_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssumeRoleArn", []))

    @jsii.member(jsii_name="resetAuthenticationType")
    def reset_authentication_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationType", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetCatalog")
    def reset_catalog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatalog", []))

    @jsii.member(jsii_name="resetClientEmail")
    def reset_client_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientEmail", []))

    @jsii.member(jsii_name="resetClientId")
    def reset_client_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientId", []))

    @jsii.member(jsii_name="resetCloudName")
    def reset_cloud_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudName", []))

    @jsii.member(jsii_name="resetConnMaxLifetime")
    def reset_conn_max_lifetime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnMaxLifetime", []))

    @jsii.member(jsii_name="resetCustomMetricsNamespaces")
    def reset_custom_metrics_namespaces(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomMetricsNamespaces", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetDefaultBucket")
    def reset_default_bucket(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultBucket", []))

    @jsii.member(jsii_name="resetDefaultProject")
    def reset_default_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultProject", []))

    @jsii.member(jsii_name="resetDefaultRegion")
    def reset_default_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultRegion", []))

    @jsii.member(jsii_name="resetDerivedField")
    def reset_derived_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDerivedField", []))

    @jsii.member(jsii_name="resetEncrypt")
    def reset_encrypt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypt", []))

    @jsii.member(jsii_name="resetEsVersion")
    def reset_es_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEsVersion", []))

    @jsii.member(jsii_name="resetExternalId")
    def reset_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalId", []))

    @jsii.member(jsii_name="resetGithubUrl")
    def reset_github_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithubUrl", []))

    @jsii.member(jsii_name="resetGraphiteVersion")
    def reset_graphite_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGraphiteVersion", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetImplementation")
    def reset_implementation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImplementation", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetLogLevelField")
    def reset_log_level_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogLevelField", []))

    @jsii.member(jsii_name="resetLogMessageField")
    def reset_log_message_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogMessageField", []))

    @jsii.member(jsii_name="resetManageAlerts")
    def reset_manage_alerts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManageAlerts", []))

    @jsii.member(jsii_name="resetMaxConcurrentShardRequests")
    def reset_max_concurrent_shard_requests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxConcurrentShardRequests", []))

    @jsii.member(jsii_name="resetMaxIdleConns")
    def reset_max_idle_conns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleConns", []))

    @jsii.member(jsii_name="resetMaxLines")
    def reset_max_lines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxLines", []))

    @jsii.member(jsii_name="resetMaxOpenConns")
    def reset_max_open_conns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxOpenConns", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetOrgSlug")
    def reset_org_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrgSlug", []))

    @jsii.member(jsii_name="resetOutputLocation")
    def reset_output_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputLocation", []))

    @jsii.member(jsii_name="resetPostgresVersion")
    def reset_postgres_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPostgresVersion", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetQueryTimeout")
    def reset_query_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryTimeout", []))

    @jsii.member(jsii_name="resetSigv4AssumeRoleArn")
    def reset_sigv4_assume_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4AssumeRoleArn", []))

    @jsii.member(jsii_name="resetSigv4Auth")
    def reset_sigv4_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4Auth", []))

    @jsii.member(jsii_name="resetSigv4AuthType")
    def reset_sigv4_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4AuthType", []))

    @jsii.member(jsii_name="resetSigv4ExternalId")
    def reset_sigv4_external_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4ExternalId", []))

    @jsii.member(jsii_name="resetSigv4Profile")
    def reset_sigv4_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4Profile", []))

    @jsii.member(jsii_name="resetSigv4Region")
    def reset_sigv4_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4Region", []))

    @jsii.member(jsii_name="resetSslMode")
    def reset_ssl_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslMode", []))

    @jsii.member(jsii_name="resetSubscriptionId")
    def reset_subscription_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionId", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @jsii.member(jsii_name="resetTimeField")
    def reset_time_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeField", []))

    @jsii.member(jsii_name="resetTimeInterval")
    def reset_time_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeInterval", []))

    @jsii.member(jsii_name="resetTimescaledb")
    def reset_timescaledb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimescaledb", []))

    @jsii.member(jsii_name="resetTlsAuth")
    def reset_tls_auth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsAuth", []))

    @jsii.member(jsii_name="resetTlsAuthWithCaCert")
    def reset_tls_auth_with_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsAuthWithCaCert", []))

    @jsii.member(jsii_name="resetTlsConfigurationMethod")
    def reset_tls_configuration_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsConfigurationMethod", []))

    @jsii.member(jsii_name="resetTlsSkipVerify")
    def reset_tls_skip_verify(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsSkipVerify", []))

    @jsii.member(jsii_name="resetTokenUri")
    def reset_token_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenUri", []))

    @jsii.member(jsii_name="resetTracingDatasourceUid")
    def reset_tracing_datasource_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTracingDatasourceUid", []))

    @jsii.member(jsii_name="resetTsdbResolution")
    def reset_tsdb_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTsdbResolution", []))

    @jsii.member(jsii_name="resetTsdbVersion")
    def reset_tsdb_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTsdbVersion", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @jsii.member(jsii_name="resetWorkgroup")
    def reset_workgroup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkgroup", []))

    @jsii.member(jsii_name="resetXpackEnabled")
    def reset_xpack_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXpackEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="derivedField")
    def derived_field(self) -> DataSourceJsonDataDerivedFieldList:
        return typing.cast(DataSourceJsonDataDerivedFieldList, jsii.get(self, "derivedField"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerUidInput")
    def alertmanager_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertmanagerUidInput"))

    @builtins.property
    @jsii.member(jsii_name="assumeRoleArnInput")
    def assume_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assumeRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationTypeInput")
    def authentication_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="catalogInput")
    def catalog_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catalogInput"))

    @builtins.property
    @jsii.member(jsii_name="clientEmailInput")
    def client_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudNameInput")
    def cloud_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cloudNameInput"))

    @builtins.property
    @jsii.member(jsii_name="connMaxLifetimeInput")
    def conn_max_lifetime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "connMaxLifetimeInput"))

    @builtins.property
    @jsii.member(jsii_name="customMetricsNamespacesInput")
    def custom_metrics_namespaces_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customMetricsNamespacesInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultBucketInput")
    def default_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultProjectInput")
    def default_project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultProjectInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultRegionInput")
    def default_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="derivedFieldInput")
    def derived_field_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonDataDerivedField]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonDataDerivedField]]], jsii.get(self, "derivedFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptInput")
    def encrypt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptInput"))

    @builtins.property
    @jsii.member(jsii_name="esVersionInput")
    def es_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "esVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="externalIdInput")
    def external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "externalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="githubUrlInput")
    def github_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "githubUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="graphiteVersionInput")
    def graphite_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "graphiteVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="implementationInput")
    def implementation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "implementationInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="logLevelFieldInput")
    def log_level_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logLevelFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="logMessageFieldInput")
    def log_message_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logMessageFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="manageAlertsInput")
    def manage_alerts_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "manageAlertsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentShardRequestsInput")
    def max_concurrent_shard_requests_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentShardRequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleConnsInput")
    def max_idle_conns_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleConnsInput"))

    @builtins.property
    @jsii.member(jsii_name="maxLinesInput")
    def max_lines_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLinesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxOpenConnsInput")
    def max_open_conns_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxOpenConnsInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="orgSlugInput")
    def org_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orgSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="outputLocationInput")
    def output_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="postgresVersionInput")
    def postgres_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "postgresVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="queryTimeoutInput")
    def query_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4AssumeRoleArnInput")
    def sigv4_assume_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4AssumeRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4AuthInput")
    def sigv4_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sigv4AuthInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4AuthTypeInput")
    def sigv4_auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4AuthTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4ExternalIdInput")
    def sigv4_external_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4ExternalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4ProfileInput")
    def sigv4_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4ProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4RegionInput")
    def sigv4_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4RegionInput"))

    @builtins.property
    @jsii.member(jsii_name="sslModeInput")
    def ssl_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslModeInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionIdInput")
    def subscription_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeFieldInput")
    def time_field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeFieldInput"))

    @builtins.property
    @jsii.member(jsii_name="timeIntervalInput")
    def time_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="timescaledbInput")
    def timescaledb_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "timescaledbInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsAuthInput")
    def tls_auth_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tlsAuthInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsAuthWithCaCertInput")
    def tls_auth_with_ca_cert_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tlsAuthWithCaCertInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsConfigurationMethodInput")
    def tls_configuration_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsConfigurationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsSkipVerifyInput")
    def tls_skip_verify_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "tlsSkipVerifyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenUriInput")
    def token_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenUriInput"))

    @builtins.property
    @jsii.member(jsii_name="tracingDatasourceUidInput")
    def tracing_datasource_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tracingDatasourceUidInput"))

    @builtins.property
    @jsii.member(jsii_name="tsdbResolutionInput")
    def tsdb_resolution_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tsdbResolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="tsdbVersionInput")
    def tsdb_version_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tsdbVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="workgroupInput")
    def workgroup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workgroupInput"))

    @builtins.property
    @jsii.member(jsii_name="xpackEnabledInput")
    def xpack_enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "xpackEnabledInput"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerUid")
    def alertmanager_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "alertmanagerUid"))

    @alertmanager_uid.setter
    def alertmanager_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b18aadb9a3f6964353d37013215bcfd87eaa1b6d9e216659362971bb53a8e1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertmanagerUid", value)

    @builtins.property
    @jsii.member(jsii_name="assumeRoleArn")
    def assume_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "assumeRoleArn"))

    @assume_role_arn.setter
    def assume_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a2c179a23105278a9a5db44634ecdb256afe8da4ca827b53ddd4a445c9f2118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumeRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__132bf8483bb75846c83dfbc6848630d0550c19610fb40fde62d787d62a90f447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22d70bc716b7148d5a4de2615ba6a31d815ffbd0dbfd9da01da1b0ccf38ff46b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="catalog")
    def catalog(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catalog"))

    @catalog.setter
    def catalog(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d6a057224ce983445f0d0e59aa575af4d211dddfd5ef150ff4fb6d2ccadf64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catalog", value)

    @builtins.property
    @jsii.member(jsii_name="clientEmail")
    def client_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientEmail"))

    @client_email.setter
    def client_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e8154e1d57b9a04f47fcd216a7a97c93623340df28e9c72f204db159674fd36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientEmail", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3810b8b0594e5cb9be9b1c55e62b67f31867e4b713b1c6a3169d55836420f318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="cloudName")
    def cloud_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudName"))

    @cloud_name.setter
    def cloud_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74e7318be912a13624103c193766ebe1e63f7b7687088de440bd1998c77639f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudName", value)

    @builtins.property
    @jsii.member(jsii_name="connMaxLifetime")
    def conn_max_lifetime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "connMaxLifetime"))

    @conn_max_lifetime.setter
    def conn_max_lifetime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__828e99baef044cffd115400d6fda428dfdb1a2e7e36fc7b963ede365ed60b953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connMaxLifetime", value)

    @builtins.property
    @jsii.member(jsii_name="customMetricsNamespaces")
    def custom_metrics_namespaces(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customMetricsNamespaces"))

    @custom_metrics_namespaces.setter
    def custom_metrics_namespaces(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18a4605bab570a7c0a8734aa299d59bd018424cc1461270b8d8ce5c3aac1e89f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customMetricsNamespaces", value)

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bae646002615731dd0e39e021a8377730a796aaaf6a6ca9f56aa8f70e4e7781e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="defaultBucket")
    def default_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBucket"))

    @default_bucket.setter
    def default_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4e097403159704bf1e1870d10194bbf51f4814f724aa90ff9976d46511bdc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultBucket", value)

    @builtins.property
    @jsii.member(jsii_name="defaultProject")
    def default_project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultProject"))

    @default_project.setter
    def default_project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87102530a10701567d490f1d930681ac9d93861fc8aba99bbebe45c87465c121)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultProject", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRegion")
    def default_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultRegion"))

    @default_region.setter
    def default_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d2732412ff672bfd46aa455f225e5d850061c7186ea64ad2d4afd2df7624c0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRegion", value)

    @builtins.property
    @jsii.member(jsii_name="encrypt")
    def encrypt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encrypt"))

    @encrypt.setter
    def encrypt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe5bc662e70e823900526d4f1b574f8b33886ec6c77e0f539ee7e329545ebef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypt", value)

    @builtins.property
    @jsii.member(jsii_name="esVersion")
    def es_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "esVersion"))

    @es_version.setter
    def es_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecaa0476716aef62950a5903282e4b1e2096360bf1cbbecd5e5247a6e134f47e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "esVersion", value)

    @builtins.property
    @jsii.member(jsii_name="externalId")
    def external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalId"))

    @external_id.setter
    def external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e3d91830407cf7a34ce9aacff5e86b60712ebe17b2ab88a7ca24b91d1fab9e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalId", value)

    @builtins.property
    @jsii.member(jsii_name="githubUrl")
    def github_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "githubUrl"))

    @github_url.setter
    def github_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94db0c49fb589ee4d5432084f8babdc75bab9a87e9550f46d16981758a83ba4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "githubUrl", value)

    @builtins.property
    @jsii.member(jsii_name="graphiteVersion")
    def graphite_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "graphiteVersion"))

    @graphite_version.setter
    def graphite_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187d014672dd26ed694b53e98275bfa7f21cda2500f842f878b39118b831aefc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "graphiteVersion", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b1b533dd8741a6c31b3e803ff3e0fa78ebf4b7a4955182235de9774b19d73b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="implementation")
    def implementation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "implementation"))

    @implementation.setter
    def implementation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f1f7a1f410e57420a0b3f5fdf9fa3636e6b36d3579f11465195787994858692)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "implementation", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfa5a0873a2795f6e5e2ff18e5289b4b0559f9b662efe83b6b86dc73e301cded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="logLevelField")
    def log_level_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logLevelField"))

    @log_level_field.setter
    def log_level_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d04aba409c5671715eb9bd35cec490bc0f84cc1bb32af27226ed9b7443c6af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logLevelField", value)

    @builtins.property
    @jsii.member(jsii_name="logMessageField")
    def log_message_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logMessageField"))

    @log_message_field.setter
    def log_message_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4df3cc94abbd523ca4ce7a05d5fb6bb6a5c124eb23c1714e5a62e9325aaaf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logMessageField", value)

    @builtins.property
    @jsii.member(jsii_name="manageAlerts")
    def manage_alerts(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "manageAlerts"))

    @manage_alerts.setter
    def manage_alerts(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9862eab1a7accd6d6cda8b8cda9fb451b085ac73c187db35165532bbe86bad6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manageAlerts", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentShardRequests")
    def max_concurrent_shard_requests(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxConcurrentShardRequests"))

    @max_concurrent_shard_requests.setter
    def max_concurrent_shard_requests(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9bc9ab2d5a6e3af3851c8cb7a7682e63c7146cd8ded51de116cc5de91b66332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentShardRequests", value)

    @builtins.property
    @jsii.member(jsii_name="maxIdleConns")
    def max_idle_conns(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleConns"))

    @max_idle_conns.setter
    def max_idle_conns(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e90ff87d0d5aaf398432c3f5fab85aa41b2f994bc9e97a9fb09dea3711a01e78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleConns", value)

    @builtins.property
    @jsii.member(jsii_name="maxLines")
    def max_lines(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxLines"))

    @max_lines.setter
    def max_lines(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca3d47e9961e2a34ed4c21149ba72b14c1704c5faa4eb374ba2bf6bdd801a1a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLines", value)

    @builtins.property
    @jsii.member(jsii_name="maxOpenConns")
    def max_open_conns(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxOpenConns"))

    @max_open_conns.setter
    def max_open_conns(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88b093045d785bc33d75d0a8e40bb57a69ce685a3404b2ea91c153d451ecb56f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxOpenConns", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e7fed34c7f668f08bcf212d7a1eb480e49d5688e281849bbaaee347510a005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="orgSlug")
    def org_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgSlug"))

    @org_slug.setter
    def org_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c97b645871baa4f3cf004f24d8d6d6b532472a52bf9eda2d47d7473b00b133)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orgSlug", value)

    @builtins.property
    @jsii.member(jsii_name="outputLocation")
    def output_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputLocation"))

    @output_location.setter
    def output_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c3d3d8a89b8cf23f39c400c997f8c783d04edac5315e1d9707e82ad84082376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputLocation", value)

    @builtins.property
    @jsii.member(jsii_name="postgresVersion")
    def postgres_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "postgresVersion"))

    @postgres_version.setter
    def postgres_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3d6ad294ea6a2b590e0fad362f695b12c17cb0ff447276dc46394b33f355228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postgresVersion", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3177a461d641fd46037d1b5c35ceac605b3aa7b3ea0b2de0440d7c80e9eaeb35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="queryTimeout")
    def query_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryTimeout"))

    @query_timeout.setter
    def query_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__639fd4587cd3cfd80a51af886c7fa238132949a2bfa7161330ba7ec984282065)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4AssumeRoleArn")
    def sigv4_assume_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4AssumeRoleArn"))

    @sigv4_assume_role_arn.setter
    def sigv4_assume_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__746a4d389cdc78015767a74510e56f036f6f107159d75b67f74e2cc2c296d29f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4AssumeRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4Auth")
    def sigv4_auth(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sigv4Auth"))

    @sigv4_auth.setter
    def sigv4_auth(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__799664088f202536aae36f37985fb446aaba8fc7a172d3838c7b4abfacd88da1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4Auth", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4AuthType")
    def sigv4_auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4AuthType"))

    @sigv4_auth_type.setter
    def sigv4_auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaab3b669978c53e3dc6b6b6df4f5b9352e87df786a00413170db823007736d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4AuthType", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4ExternalId")
    def sigv4_external_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4ExternalId"))

    @sigv4_external_id.setter
    def sigv4_external_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7168a383dd34ea698e6885c3f98317319d0bc58d7e70e19978683ed6701e948a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4ExternalId", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4Profile")
    def sigv4_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4Profile"))

    @sigv4_profile.setter
    def sigv4_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011005db8407c7855e62c6c7eb9f1d42cb150a5d9a3d87a127e69ab28e845477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4Profile", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4Region")
    def sigv4_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4Region"))

    @sigv4_region.setter
    def sigv4_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbc18dd8336ae57f252a01f4a5712de259fab2765ddd0b9f5c5ca8944765c80d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4Region", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6820278461e3306f11693beb865a105fdbb26e77d499565443b9117238275aaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionId")
    def subscription_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionId"))

    @subscription_id.setter
    def subscription_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbccea76dc90db3bd861ec42c3d16bcb31d18ad6d8466aac497e8d4087bfddc9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionId", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65c3c80957aa1fae0916c1bf46af1443a1080c9a35bab787a53780eec3b5960b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="timeField")
    def time_field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeField"))

    @time_field.setter
    def time_field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51b69eb6c5e2aa406f54f554ee0911182d9cabe0c059ccb71d71f3118c3a2d05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeField", value)

    @builtins.property
    @jsii.member(jsii_name="timeInterval")
    def time_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeInterval"))

    @time_interval.setter
    def time_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ee6b5d9aad4c6d0ae1b3f8862b2d1c4e41273cf37cb43ae2e6bc945c1611bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeInterval", value)

    @builtins.property
    @jsii.member(jsii_name="timescaledb")
    def timescaledb(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "timescaledb"))

    @timescaledb.setter
    def timescaledb(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0da3d4380b9996c3e25821ecb37ca9e40caff77898749fe55ebf23d1a00a1a66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timescaledb", value)

    @builtins.property
    @jsii.member(jsii_name="tlsAuth")
    def tls_auth(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tlsAuth"))

    @tls_auth.setter
    def tls_auth(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d657370c79e4015634d9752dbf5c830879fea9873e071b066f6cf1af6544fe01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsAuth", value)

    @builtins.property
    @jsii.member(jsii_name="tlsAuthWithCaCert")
    def tls_auth_with_ca_cert(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tlsAuthWithCaCert"))

    @tls_auth_with_ca_cert.setter
    def tls_auth_with_ca_cert(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4373b9f7bfacd9da4735ab03dca62f75efa221ce877eda3aa4cfc29b01467ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsAuthWithCaCert", value)

    @builtins.property
    @jsii.member(jsii_name="tlsConfigurationMethod")
    def tls_configuration_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsConfigurationMethod"))

    @tls_configuration_method.setter
    def tls_configuration_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49449671a2ae71a344c73f0d7cf9bf532df0faeedba6dc612346ee7683f2d83b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsConfigurationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="tlsSkipVerify")
    def tls_skip_verify(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "tlsSkipVerify"))

    @tls_skip_verify.setter
    def tls_skip_verify(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b212b62b697c06a1c996437d825c4893399192747cda25742f9cd010729af785)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsSkipVerify", value)

    @builtins.property
    @jsii.member(jsii_name="tokenUri")
    def token_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenUri"))

    @token_uri.setter
    def token_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a201bf3936a9dba2a534d92343fe5c866029cab349cff1f07633a15577fc9d26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenUri", value)

    @builtins.property
    @jsii.member(jsii_name="tracingDatasourceUid")
    def tracing_datasource_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tracingDatasourceUid"))

    @tracing_datasource_uid.setter
    def tracing_datasource_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84f49a6fa0e34f6158dd988297d3df767d211b22a11463c40206c05a30b9dab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tracingDatasourceUid", value)

    @builtins.property
    @jsii.member(jsii_name="tsdbResolution")
    def tsdb_resolution(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tsdbResolution"))

    @tsdb_resolution.setter
    def tsdb_resolution(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b0125d82f31c659a6b682bde5746d92021c7cd6e331e4089ede047fa11a3a5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tsdbResolution", value)

    @builtins.property
    @jsii.member(jsii_name="tsdbVersion")
    def tsdb_version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tsdbVersion"))

    @tsdb_version.setter
    def tsdb_version(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__085a85e0c63679d7a4955c5d22399124bb307ccfa6154a2a62f4b8f1562eb967)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tsdbVersion", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad87e896f3594112be6675e19aabcf33f3fa13bd5ea0595fb72ec00966d9012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="workgroup")
    def workgroup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workgroup"))

    @workgroup.setter
    def workgroup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21a550303b0dec941eaf6067034a0f97565142a45c9d703b0586a471f3f00205)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workgroup", value)

    @builtins.property
    @jsii.member(jsii_name="xpackEnabled")
    def xpack_enabled(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "xpackEnabled"))

    @xpack_enabled.setter
    def xpack_enabled(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c0570666329c0fb591d743c51e22fa91c30e3fdc502c0c683fbb0a7de0e595a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "xpackEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataSourceJsonData, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataSourceJsonData, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataSourceJsonData, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa9d374424fd2d493a391def4c3630e1239c1edb9f32fb1d9808f3604e1f7da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.dataSource.DataSourceSecureJsonData",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "access_token": "accessToken",
        "auth_token": "authToken",
        "basic_auth_password": "basicAuthPassword",
        "client_secret": "clientSecret",
        "password": "password",
        "private_key": "privateKey",
        "secret_key": "secretKey",
        "sigv4_access_key": "sigv4AccessKey",
        "sigv4_secret_key": "sigv4SecretKey",
        "tls_ca_cert": "tlsCaCert",
        "tls_client_cert": "tlsClientCert",
        "tls_client_key": "tlsClientKey",
    },
)
class DataSourceSecureJsonData:
    def __init__(
        self,
        *,
        access_key: typing.Optional[builtins.str] = None,
        access_token: typing.Optional[builtins.str] = None,
        auth_token: typing.Optional[builtins.str] = None,
        basic_auth_password: typing.Optional[builtins.str] = None,
        client_secret: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        secret_key: typing.Optional[builtins.str] = None,
        sigv4_access_key: typing.Optional[builtins.str] = None,
        sigv4_secret_key: typing.Optional[builtins.str] = None,
        tls_ca_cert: typing.Optional[builtins.str] = None,
        tls_client_cert: typing.Optional[builtins.str] = None,
        tls_client_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: (CloudWatch, Athena) The access key used to access the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_key DataSource#access_key}
        :param access_token: (Github) The access token used to access the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_token DataSource#access_token}
        :param auth_token: (Sentry) Authorization token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#auth_token DataSource#auth_token}
        :param basic_auth_password: (All) Password to use for basic authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_password DataSource#basic_auth_password}
        :param client_secret: (Azure Monitor) Client secret for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#client_secret DataSource#client_secret}
        :param password: (All) Password to use for authentication. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#password DataSource#password}
        :param private_key: (Stackdriver) The service account key ``private_key`` to use to access the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#private_key DataSource#private_key}
        :param secret_key: (CloudWatch, Athena) The secret key to use to access the data source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secret_key DataSource#secret_key}
        :param sigv4_access_key: (Elasticsearch and Prometheus) SigV4 access key. Required when using 'keys' auth provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_access_key DataSource#sigv4_access_key}
        :param sigv4_secret_key: (Elasticsearch and Prometheus) SigV4 secret key. Required when using 'keys' auth provider. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_secret_key DataSource#sigv4_secret_key}
        :param tls_ca_cert: (All) CA cert for out going requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_ca_cert DataSource#tls_ca_cert}
        :param tls_client_cert: (All) TLS Client cert for outgoing requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_client_cert DataSource#tls_client_cert}
        :param tls_client_key: (All) TLS Client key for outgoing requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_client_key DataSource#tls_client_key}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4134817debfac37e0ce55709a21036a1767a625c76de347d8764b579683944d)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument auth_token", value=auth_token, expected_type=type_hints["auth_token"])
            check_type(argname="argument basic_auth_password", value=basic_auth_password, expected_type=type_hints["basic_auth_password"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument sigv4_access_key", value=sigv4_access_key, expected_type=type_hints["sigv4_access_key"])
            check_type(argname="argument sigv4_secret_key", value=sigv4_secret_key, expected_type=type_hints["sigv4_secret_key"])
            check_type(argname="argument tls_ca_cert", value=tls_ca_cert, expected_type=type_hints["tls_ca_cert"])
            check_type(argname="argument tls_client_cert", value=tls_client_cert, expected_type=type_hints["tls_client_cert"])
            check_type(argname="argument tls_client_key", value=tls_client_key, expected_type=type_hints["tls_client_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_key is not None:
            self._values["access_key"] = access_key
        if access_token is not None:
            self._values["access_token"] = access_token
        if auth_token is not None:
            self._values["auth_token"] = auth_token
        if basic_auth_password is not None:
            self._values["basic_auth_password"] = basic_auth_password
        if client_secret is not None:
            self._values["client_secret"] = client_secret
        if password is not None:
            self._values["password"] = password
        if private_key is not None:
            self._values["private_key"] = private_key
        if secret_key is not None:
            self._values["secret_key"] = secret_key
        if sigv4_access_key is not None:
            self._values["sigv4_access_key"] = sigv4_access_key
        if sigv4_secret_key is not None:
            self._values["sigv4_secret_key"] = sigv4_secret_key
        if tls_ca_cert is not None:
            self._values["tls_ca_cert"] = tls_ca_cert
        if tls_client_cert is not None:
            self._values["tls_client_cert"] = tls_client_cert
        if tls_client_key is not None:
            self._values["tls_client_key"] = tls_client_key

    @builtins.property
    def access_key(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) The access key used to access the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_key DataSource#access_key}
        '''
        result = self._values.get("access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''(Github) The access token used to access the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#access_token DataSource#access_token}
        '''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auth_token(self) -> typing.Optional[builtins.str]:
        '''(Sentry) Authorization token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#auth_token DataSource#auth_token}
        '''
        result = self._values.get("auth_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_auth_password(self) -> typing.Optional[builtins.str]:
        '''(All) Password to use for basic authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#basic_auth_password DataSource#basic_auth_password}
        '''
        result = self._values.get("basic_auth_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def client_secret(self) -> typing.Optional[builtins.str]:
        '''(Azure Monitor) Client secret for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#client_secret DataSource#client_secret}
        '''
        result = self._values.get("client_secret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''(All) Password to use for authentication.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#password DataSource#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''(Stackdriver) The service account key ``private_key`` to use to access the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#private_key DataSource#private_key}
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_key(self) -> typing.Optional[builtins.str]:
        '''(CloudWatch, Athena) The secret key to use to access the data source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#secret_key DataSource#secret_key}
        '''
        result = self._values.get("secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_access_key(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) SigV4 access key. Required when using 'keys' auth provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_access_key DataSource#sigv4_access_key}
        '''
        result = self._values.get("sigv4_access_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sigv4_secret_key(self) -> typing.Optional[builtins.str]:
        '''(Elasticsearch and Prometheus) SigV4 secret key. Required when using 'keys' auth provider.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#sigv4_secret_key DataSource#sigv4_secret_key}
        '''
        result = self._values.get("sigv4_secret_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_ca_cert(self) -> typing.Optional[builtins.str]:
        '''(All) CA cert for out going requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_ca_cert DataSource#tls_ca_cert}
        '''
        result = self._values.get("tls_ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_cert(self) -> typing.Optional[builtins.str]:
        '''(All) TLS Client cert for outgoing requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_client_cert DataSource#tls_client_cert}
        '''
        result = self._values.get("tls_client_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tls_client_key(self) -> typing.Optional[builtins.str]:
        '''(All) TLS Client key for outgoing requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/data_source#tls_client_key DataSource#tls_client_key}
        '''
        result = self._values.get("tls_client_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceSecureJsonData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataSourceSecureJsonDataList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSourceSecureJsonDataList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__79119e80e569272e0000d7b750add4e6268e45d18975b298adb5f7cbe85e25a8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataSourceSecureJsonDataOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d0bc5b5b21544427a8690345490ff679c50b156968a567ec1a25b22f68aa6ec)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataSourceSecureJsonDataOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c9949ed81ac486b18167727c6ec6f9c4837b3cec0043abb68dbf1545d262c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1223c20abdb65f1b38068a1a052ec6ad3cce2c4ceae66c2741283cf166a25708)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72915573461c303b0fb7607279d86bec1663548fc891f1b466c3f7f5a970e8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceSecureJsonData]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceSecureJsonData]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceSecureJsonData]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c726a7ebbea6d11b449c4165bd0d6392f1f4ff3ca147c9405c09749180875a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DataSourceSecureJsonDataOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.dataSource.DataSourceSecureJsonDataOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__416097c91baaeb6771f68f0a3cafcd6e1d531de92c708852a8acc80e6f323f97)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAccessKey")
    def reset_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessKey", []))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAuthToken")
    def reset_auth_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthToken", []))

    @jsii.member(jsii_name="resetBasicAuthPassword")
    def reset_basic_auth_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthPassword", []))

    @jsii.member(jsii_name="resetClientSecret")
    def reset_client_secret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientSecret", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPrivateKey")
    def reset_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKey", []))

    @jsii.member(jsii_name="resetSecretKey")
    def reset_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretKey", []))

    @jsii.member(jsii_name="resetSigv4AccessKey")
    def reset_sigv4_access_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4AccessKey", []))

    @jsii.member(jsii_name="resetSigv4SecretKey")
    def reset_sigv4_secret_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigv4SecretKey", []))

    @jsii.member(jsii_name="resetTlsCaCert")
    def reset_tls_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsCaCert", []))

    @jsii.member(jsii_name="resetTlsClientCert")
    def reset_tls_client_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientCert", []))

    @jsii.member(jsii_name="resetTlsClientKey")
    def reset_tls_client_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTlsClientKey", []))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="authTokenInput")
    def auth_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthPasswordInput")
    def basic_auth_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4AccessKeyInput")
    def sigv4_access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4AccessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="sigv4SecretKeyInput")
    def sigv4_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sigv4SecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsCaCertInput")
    def tls_ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsCaCertInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientCertInput")
    def tls_client_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsClientCertInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsClientKeyInput")
    def tls_client_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tlsClientKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__963872f3b4566d9c4b7226f8948c1df900ccd72a99ba83602c5022f089510259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36e84235b8944b0f5fa872a079d4f378796dd1d344a70dd848a133dc21268ca7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="authToken")
    def auth_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authToken"))

    @auth_token.setter
    def auth_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7818555454ebd783674f5c9f39b4cc96f7b69eeefd32ce84c0f7a9b20770493b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authToken", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthPassword")
    def basic_auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthPassword"))

    @basic_auth_password.setter
    def basic_auth_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0877cf559ceb6dd3071b67d6d0e133998e9199796e4d302e8a452b3797b29799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthPassword", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56c43f7e541ef5397cf761af229c17b36eb17def8b1a1ec522a0d0a14bb6a0ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa25364d343192e0872a26bb0180fe66473bf1fc811c8a1461653dbca486a1f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1a275b8a03eb4793dc594bafc2fd177f58778b456ef262f802837d1b266f657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9408932e5f8f759a0f77ef6944ae123fc9bb21500d8533ca4296cb9152c38f8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4AccessKey")
    def sigv4_access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4AccessKey"))

    @sigv4_access_key.setter
    def sigv4_access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa07442f63b4d4f0b06749b8b67f1402e9bef058fba6563432aca26e40b99b28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4AccessKey", value)

    @builtins.property
    @jsii.member(jsii_name="sigv4SecretKey")
    def sigv4_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sigv4SecretKey"))

    @sigv4_secret_key.setter
    def sigv4_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24ebed5c57e5197131937ae25c892b2855cea249c79253ea13615cb18b2b255d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sigv4SecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="tlsCaCert")
    def tls_ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsCaCert"))

    @tls_ca_cert.setter
    def tls_ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f016cd386699c1c25e59422b49d8aa830d7bbe70d0ae421852dbb7a3222d714)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsCaCert", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientCert")
    def tls_client_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientCert"))

    @tls_client_cert.setter
    def tls_client_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a5097c43a820ec87d6d78ee69c40f6ea16dc79e7379d0062f5c96b43cb72ca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientCert", value)

    @builtins.property
    @jsii.member(jsii_name="tlsClientKey")
    def tls_client_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tlsClientKey"))

    @tls_client_key.setter
    def tls_client_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f6f4ab89573b009db1b2a57165406548d0160faf899a25324eac7df5408013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsClientKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataSourceSecureJsonData, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataSourceSecureJsonData, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataSourceSecureJsonData, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a588d7c859770e856d8c24dd9f6eee4bdb97091d4dacad34bc420aaef0e6aeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataSource",
    "DataSourceConfig",
    "DataSourceJsonData",
    "DataSourceJsonDataDerivedField",
    "DataSourceJsonDataDerivedFieldList",
    "DataSourceJsonDataDerivedFieldOutputReference",
    "DataSourceJsonDataList",
    "DataSourceJsonDataOutputReference",
    "DataSourceSecureJsonData",
    "DataSourceSecureJsonDataList",
    "DataSourceSecureJsonDataOutputReference",
]

publication.publish()

def _typecheckingstub__d4b8dec4b48d7119e7578e5f174056cdb59f1c04c2b0697a78287c6e6206a815(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    access_mode: typing.Optional[builtins.str] = None,
    basic_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    basic_auth_password: typing.Optional[builtins.str] = None,
    basic_auth_username: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceJsonData, typing.Dict[builtins.str, typing.Any]]]]] = None,
    json_data_encoded: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    secure_json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceSecureJsonData, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secure_json_data_encoded: typing.Optional[builtins.str] = None,
    uid: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__7120ce6719f2019de75de8012b5a544302c7a8d7d0c255579c0622a6776dfa2a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceJsonData, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1603318e5a629e9795bc96703b533bd23dabd53b19ade144dde77b60bf07244(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceSecureJsonData, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__734c391bb5835007a6c3c859845fec868baa66beac8d7358e60bb8881b76641c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51fcbe00ae3fe694dbd9fef8686d66740adb691dc1e3d19fbe14201df14998a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df44787d1d3ca335850f181fc9bdab687cffe9e994f9bde17037df03b4f128f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89db1f21e30975157b4d964120833a900b96d7957b975df1fa840111285045b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__864d1f88dd58d3e06048170a0569a782f97a6d9d629632938a3372bc822249ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c527cb764c8792228f69ed81ea4c1cb2b685b709ccc38375377aa6e39056cecd(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75312fec482c3d8141b59691b0d6a274d55e63d5f29229e2e6ab10ee0a5912f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4bc7bc9fc8968727bfa977d4e521062a5adbfac88316d493f1c7b147f54dfe(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1337e6ad9b7a3e0c9463a95f27edc010f4a4a14f7500adc98b0bc39c393fc65b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fe948bd39650f414260dd2b3b75e27fd738ca1e0194198ee2963ae1c1e99dbf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f637e76b24dfe237a5ea116fb85d53b00c1d93545c474eb349acffa47ecaefa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c0234e4d7ad783729ae57ae2bfe2ed0e51ba3d5ddc67df4513214a916dd114(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8e1797e5439540d412281d456f8126070487d1f89687bdd71f5611b25df21d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3911837ba8e539883990d29874e784bfb72d4244f43f6d7dd1f00260649346(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d834bec290bb01ba66aea76c7c74bdf1f4b32b5ab739f8b6db393115277842f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42d5a32c2285f82ec5f6939c75a923c2642be7e51136f3f66d316f36282355fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cecf55e8dd515cf51605327eb35b25f495dae0ac159c3ad09d0c27ff93c8177(
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
    access_mode: typing.Optional[builtins.str] = None,
    basic_auth_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    basic_auth_password: typing.Optional[builtins.str] = None,
    basic_auth_username: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    http_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    id: typing.Optional[builtins.str] = None,
    is_default: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceJsonData, typing.Dict[builtins.str, typing.Any]]]]] = None,
    json_data_encoded: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    secure_json_data: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceSecureJsonData, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secure_json_data_encoded: typing.Optional[builtins.str] = None,
    uid: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__702c59a2bdc59e17d2c74713a4429c03889bf73250f72b44842604f93a960bdd(
    *,
    alertmanager_uid: typing.Optional[builtins.str] = None,
    assume_role_arn: typing.Optional[builtins.str] = None,
    authentication_type: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    catalog: typing.Optional[builtins.str] = None,
    client_email: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    cloud_name: typing.Optional[builtins.str] = None,
    conn_max_lifetime: typing.Optional[jsii.Number] = None,
    custom_metrics_namespaces: typing.Optional[builtins.str] = None,
    database: typing.Optional[builtins.str] = None,
    default_bucket: typing.Optional[builtins.str] = None,
    default_project: typing.Optional[builtins.str] = None,
    default_region: typing.Optional[builtins.str] = None,
    derived_field: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceJsonDataDerivedField, typing.Dict[builtins.str, typing.Any]]]]] = None,
    encrypt: typing.Optional[builtins.str] = None,
    es_version: typing.Optional[builtins.str] = None,
    external_id: typing.Optional[builtins.str] = None,
    github_url: typing.Optional[builtins.str] = None,
    graphite_version: typing.Optional[builtins.str] = None,
    http_method: typing.Optional[builtins.str] = None,
    implementation: typing.Optional[builtins.str] = None,
    interval: typing.Optional[builtins.str] = None,
    log_level_field: typing.Optional[builtins.str] = None,
    log_message_field: typing.Optional[builtins.str] = None,
    manage_alerts: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    max_concurrent_shard_requests: typing.Optional[jsii.Number] = None,
    max_idle_conns: typing.Optional[jsii.Number] = None,
    max_lines: typing.Optional[jsii.Number] = None,
    max_open_conns: typing.Optional[jsii.Number] = None,
    organization: typing.Optional[builtins.str] = None,
    org_slug: typing.Optional[builtins.str] = None,
    output_location: typing.Optional[builtins.str] = None,
    postgres_version: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    query_timeout: typing.Optional[builtins.str] = None,
    sigv4_assume_role_arn: typing.Optional[builtins.str] = None,
    sigv4_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    sigv4_auth_type: typing.Optional[builtins.str] = None,
    sigv4_external_id: typing.Optional[builtins.str] = None,
    sigv4_profile: typing.Optional[builtins.str] = None,
    sigv4_region: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    subscription_id: typing.Optional[builtins.str] = None,
    tenant_id: typing.Optional[builtins.str] = None,
    time_field: typing.Optional[builtins.str] = None,
    time_interval: typing.Optional[builtins.str] = None,
    timescaledb: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_auth: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_auth_with_ca_cert: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    tls_configuration_method: typing.Optional[builtins.str] = None,
    tls_skip_verify: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    token_uri: typing.Optional[builtins.str] = None,
    tracing_datasource_uid: typing.Optional[builtins.str] = None,
    tsdb_resolution: typing.Optional[jsii.Number] = None,
    tsdb_version: typing.Optional[jsii.Number] = None,
    version: typing.Optional[builtins.str] = None,
    workgroup: typing.Optional[builtins.str] = None,
    xpack_enabled: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e29bf14fe3b5576322ea2f8126d1c0d62d00d04eff2660ba28c9d0eb5e338c(
    *,
    datasource_uid: typing.Optional[builtins.str] = None,
    matcher_regex: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78254645448865a8c49384a90b17be4f83036ac1afcd544865580a82f2be3b94(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775e2aa66c881189e6f2cf527dfbe982854a60ddfa27fffdcdf6337dbfc38c7a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b437577e5a815fd9599ea6877f0f752e1e1873d8ed0bb064e6115af2291a02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b629ba4d3e3a1c5fa81e8b6e6f9e417f779e19e9fb14a30c948594b9a586821(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807faf0f7e44d1154ea92b2975e78eaf2a523bb513e3b12655c34b736374c33c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f3b5c8a99e010dd3303dd2295389ef2fd3fd33650e0ebbeaa27c4176090e53(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonDataDerivedField]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9de194be24dd30ade56c959e52dafd4661aa9621b9e9d6fc588ddec6c8cd8f7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58cd515fa4c3e901e182866df1d423f6a35f7dd847605ca39aac3c819482a4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad66adeb875d79cd1d0bda3f343bb04c3ef5e5eef3ebb5727f815c024b99d7e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c36df6805b9a772f0eedb5f282b8bed6839eee556df9e42bb985df90dfaab13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd95e88c901be08519390a22becfa5efec5236541d098300670f43daa000d589(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce03fedd8b1cfe230445238ab82a2580a4a9b3d9b66b629c58bc2eddf53427f4(
    value: typing.Optional[typing.Union[DataSourceJsonDataDerivedField, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b954caafcd947ef0af39d74d6785c007c3749472c560b016a7be0d159f773705(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51385ddf02665b2670eef69aea6188473b4087b7fafe0dfa1fc59c05202021ea(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b1cfb6d0a6d25bb2a26268a111a1dc0d6e2ed5e6c215c5c94045825b8939c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452eda43dfe9126a60799aac4289bf04f9591ea212eac95a2423d8cc23f3b85e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43ba55a3a844eea02d31cd4d5662bc45e67373d266e8b051ba63eb673ad84f2c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95a0988e48b8ae0175306e6953d6f6af83893b3cd31bcd0f66c5e074a0e641a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceJsonData]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c79905866b1a80291cdc37dcad2cf02ad96546104a71cd325ea86e2be713140(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ff891e838e8cca2315b885f5d626fffd2418251b7a3ab04d39abd1a2de3f77(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataSourceJsonDataDerivedField, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b18aadb9a3f6964353d37013215bcfd87eaa1b6d9e216659362971bb53a8e1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2c179a23105278a9a5db44634ecdb256afe8da4ca827b53ddd4a445c9f2118(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__132bf8483bb75846c83dfbc6848630d0550c19610fb40fde62d787d62a90f447(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22d70bc716b7148d5a4de2615ba6a31d815ffbd0dbfd9da01da1b0ccf38ff46b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d6a057224ce983445f0d0e59aa575af4d211dddfd5ef150ff4fb6d2ccadf64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8154e1d57b9a04f47fcd216a7a97c93623340df28e9c72f204db159674fd36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3810b8b0594e5cb9be9b1c55e62b67f31867e4b713b1c6a3169d55836420f318(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e7318be912a13624103c193766ebe1e63f7b7687088de440bd1998c77639f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__828e99baef044cffd115400d6fda428dfdb1a2e7e36fc7b963ede365ed60b953(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a4605bab570a7c0a8734aa299d59bd018424cc1461270b8d8ce5c3aac1e89f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae646002615731dd0e39e021a8377730a796aaaf6a6ca9f56aa8f70e4e7781e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4e097403159704bf1e1870d10194bbf51f4814f724aa90ff9976d46511bdc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87102530a10701567d490f1d930681ac9d93861fc8aba99bbebe45c87465c121(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2732412ff672bfd46aa455f225e5d850061c7186ea64ad2d4afd2df7624c0d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe5bc662e70e823900526d4f1b574f8b33886ec6c77e0f539ee7e329545ebef6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecaa0476716aef62950a5903282e4b1e2096360bf1cbbecd5e5247a6e134f47e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3d91830407cf7a34ce9aacff5e86b60712ebe17b2ab88a7ca24b91d1fab9e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94db0c49fb589ee4d5432084f8babdc75bab9a87e9550f46d16981758a83ba4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187d014672dd26ed694b53e98275bfa7f21cda2500f842f878b39118b831aefc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b1b533dd8741a6c31b3e803ff3e0fa78ebf4b7a4955182235de9774b19d73b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f1f7a1f410e57420a0b3f5fdf9fa3636e6b36d3579f11465195787994858692(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa5a0873a2795f6e5e2ff18e5289b4b0559f9b662efe83b6b86dc73e301cded(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d04aba409c5671715eb9bd35cec490bc0f84cc1bb32af27226ed9b7443c6af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4df3cc94abbd523ca4ce7a05d5fb6bb6a5c124eb23c1714e5a62e9325aaaf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9862eab1a7accd6d6cda8b8cda9fb451b085ac73c187db35165532bbe86bad6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9bc9ab2d5a6e3af3851c8cb7a7682e63c7146cd8ded51de116cc5de91b66332(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e90ff87d0d5aaf398432c3f5fab85aa41b2f994bc9e97a9fb09dea3711a01e78(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca3d47e9961e2a34ed4c21149ba72b14c1704c5faa4eb374ba2bf6bdd801a1a3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88b093045d785bc33d75d0a8e40bb57a69ce685a3404b2ea91c153d451ecb56f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e7fed34c7f668f08bcf212d7a1eb480e49d5688e281849bbaaee347510a005(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c97b645871baa4f3cf004f24d8d6d6b532472a52bf9eda2d47d7473b00b133(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c3d3d8a89b8cf23f39c400c997f8c783d04edac5315e1d9707e82ad84082376(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d6ad294ea6a2b590e0fad362f695b12c17cb0ff447276dc46394b33f355228(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3177a461d641fd46037d1b5c35ceac605b3aa7b3ea0b2de0440d7c80e9eaeb35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__639fd4587cd3cfd80a51af886c7fa238132949a2bfa7161330ba7ec984282065(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746a4d389cdc78015767a74510e56f036f6f107159d75b67f74e2cc2c296d29f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__799664088f202536aae36f37985fb446aaba8fc7a172d3838c7b4abfacd88da1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaab3b669978c53e3dc6b6b6df4f5b9352e87df786a00413170db823007736d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7168a383dd34ea698e6885c3f98317319d0bc58d7e70e19978683ed6701e948a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011005db8407c7855e62c6c7eb9f1d42cb150a5d9a3d87a127e69ab28e845477(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbc18dd8336ae57f252a01f4a5712de259fab2765ddd0b9f5c5ca8944765c80d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6820278461e3306f11693beb865a105fdbb26e77d499565443b9117238275aaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbccea76dc90db3bd861ec42c3d16bcb31d18ad6d8466aac497e8d4087bfddc9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65c3c80957aa1fae0916c1bf46af1443a1080c9a35bab787a53780eec3b5960b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51b69eb6c5e2aa406f54f554ee0911182d9cabe0c059ccb71d71f3118c3a2d05(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ee6b5d9aad4c6d0ae1b3f8862b2d1c4e41273cf37cb43ae2e6bc945c1611bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0da3d4380b9996c3e25821ecb37ca9e40caff77898749fe55ebf23d1a00a1a66(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d657370c79e4015634d9752dbf5c830879fea9873e071b066f6cf1af6544fe01(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4373b9f7bfacd9da4735ab03dca62f75efa221ce877eda3aa4cfc29b01467ae8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49449671a2ae71a344c73f0d7cf9bf532df0faeedba6dc612346ee7683f2d83b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b212b62b697c06a1c996437d825c4893399192747cda25742f9cd010729af785(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a201bf3936a9dba2a534d92343fe5c866029cab349cff1f07633a15577fc9d26(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84f49a6fa0e34f6158dd988297d3df767d211b22a11463c40206c05a30b9dab3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0125d82f31c659a6b682bde5746d92021c7cd6e331e4089ede047fa11a3a5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__085a85e0c63679d7a4955c5d22399124bb307ccfa6154a2a62f4b8f1562eb967(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad87e896f3594112be6675e19aabcf33f3fa13bd5ea0595fb72ec00966d9012(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21a550303b0dec941eaf6067034a0f97565142a45c9d703b0586a471f3f00205(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c0570666329c0fb591d743c51e22fa91c30e3fdc502c0c683fbb0a7de0e595a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa9d374424fd2d493a391def4c3630e1239c1edb9f32fb1d9808f3604e1f7da(
    value: typing.Optional[typing.Union[DataSourceJsonData, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4134817debfac37e0ce55709a21036a1767a625c76de347d8764b579683944d(
    *,
    access_key: typing.Optional[builtins.str] = None,
    access_token: typing.Optional[builtins.str] = None,
    auth_token: typing.Optional[builtins.str] = None,
    basic_auth_password: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    secret_key: typing.Optional[builtins.str] = None,
    sigv4_access_key: typing.Optional[builtins.str] = None,
    sigv4_secret_key: typing.Optional[builtins.str] = None,
    tls_ca_cert: typing.Optional[builtins.str] = None,
    tls_client_cert: typing.Optional[builtins.str] = None,
    tls_client_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79119e80e569272e0000d7b750add4e6268e45d18975b298adb5f7cbe85e25a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0bc5b5b21544427a8690345490ff679c50b156968a567ec1a25b22f68aa6ec(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c9949ed81ac486b18167727c6ec6f9c4837b3cec0043abb68dbf1545d262c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1223c20abdb65f1b38068a1a052ec6ad3cce2c4ceae66c2741283cf166a25708(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72915573461c303b0fb7607279d86bec1663548fc891f1b466c3f7f5a970e8c2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c726a7ebbea6d11b449c4165bd0d6392f1f4ff3ca147c9405c09749180875a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataSourceSecureJsonData]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416097c91baaeb6771f68f0a3cafcd6e1d531de92c708852a8acc80e6f323f97(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__963872f3b4566d9c4b7226f8948c1df900ccd72a99ba83602c5022f089510259(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36e84235b8944b0f5fa872a079d4f378796dd1d344a70dd848a133dc21268ca7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7818555454ebd783674f5c9f39b4cc96f7b69eeefd32ce84c0f7a9b20770493b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0877cf559ceb6dd3071b67d6d0e133998e9199796e4d302e8a452b3797b29799(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56c43f7e541ef5397cf761af229c17b36eb17def8b1a1ec522a0d0a14bb6a0ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa25364d343192e0872a26bb0180fe66473bf1fc811c8a1461653dbca486a1f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a275b8a03eb4793dc594bafc2fd177f58778b456ef262f802837d1b266f657(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9408932e5f8f759a0f77ef6944ae123fc9bb21500d8533ca4296cb9152c38f8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa07442f63b4d4f0b06749b8b67f1402e9bef058fba6563432aca26e40b99b28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ebed5c57e5197131937ae25c892b2855cea249c79253ea13615cb18b2b255d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f016cd386699c1c25e59422b49d8aa830d7bbe70d0ae421852dbb7a3222d714(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a5097c43a820ec87d6d78ee69c40f6ea16dc79e7379d0062f5c96b43cb72ca2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f6f4ab89573b009db1b2a57165406548d0160faf899a25324eac7df5408013(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a588d7c859770e856d8c24dd9f6eee4bdb97091d4dacad34bc420aaef0e6aeb(
    value: typing.Optional[typing.Union[DataSourceSecureJsonData, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
