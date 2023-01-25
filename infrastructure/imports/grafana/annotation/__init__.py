'''
# `grafana_annotation`

Refer to the Terraform Registory for docs: [`grafana_annotation`](https://www.terraform.io/docs/providers/grafana/r/annotation).
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


class Annotation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.annotation.Annotation",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/annotation grafana_annotation}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        text: builtins.str,
        dashboard_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        panel_id: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        time: typing.Optional[builtins.str] = None,
        time_end: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/annotation grafana_annotation} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param text: The text to associate with the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#text Annotation#text}
        :param dashboard_id: The ID of the dashboard on which to create the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#dashboard_id Annotation#dashboard_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#id Annotation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param panel_id: The ID of the dashboard panel on which to create the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#panel_id Annotation#panel_id}
        :param tags: The tags to associate with the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#tags Annotation#tags}
        :param time: The RFC 3339-formatted time string indicating the annotation's time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#time Annotation#time}
        :param time_end: The RFC 3339-formatted time string indicating the annotation's end time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#time_end Annotation#time_end}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e6ae2dc5fb7a709759eb81f96bd7a6ac0faf3927fe04a7ebaf34c70062c48ac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AnnotationConfig(
            text=text,
            dashboard_id=dashboard_id,
            id=id,
            panel_id=panel_id,
            tags=tags,
            time=time,
            time_end=time_end,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDashboardId")
    def reset_dashboard_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDashboardId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPanelId")
    def reset_panel_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPanelId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTime")
    def reset_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTime", []))

    @jsii.member(jsii_name="resetTimeEnd")
    def reset_time_end(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeEnd", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dashboardIdInput")
    def dashboard_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="panelIdInput")
    def panel_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "panelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="timeEndInput")
    def time_end_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeEndInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dashboardId"))

    @dashboard_id.setter
    def dashboard_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aac17a189273752849268c64fb62f3795a0500f61e822a9c8d28a915b659012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ef3cade4a10060f529a4ecdd3ae845a16d3a36156ea819a3e63c609389b5f15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="panelId")
    def panel_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "panelId"))

    @panel_id.setter
    def panel_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2428437de9ca0fa00e7d612f780fe1b83dcf56ee7dc07d8c06490f527fa72267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "panelId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb567db44db4d1e2e2beb8136fc3e53849731af4473d12440d71e26fef57088c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d480d05e9d65f7894241b1c9afe7a53ecfe4a9ef01969bb19a374ee4722d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__affca23d08c766b26469dccb33fce12b840458579424d6f162106d98e944c67d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="timeEnd")
    def time_end(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timeEnd"))

    @time_end.setter
    def time_end(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8889304dbafd08ffa5bee601888e50543d149e7fca9425ba4f85970779fbb7ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeEnd", value)


@jsii.data_type(
    jsii_type="grafana.annotation.AnnotationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "text": "text",
        "dashboard_id": "dashboardId",
        "id": "id",
        "panel_id": "panelId",
        "tags": "tags",
        "time": "time",
        "time_end": "timeEnd",
    },
)
class AnnotationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        text: builtins.str,
        dashboard_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        panel_id: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        time: typing.Optional[builtins.str] = None,
        time_end: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param text: The text to associate with the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#text Annotation#text}
        :param dashboard_id: The ID of the dashboard on which to create the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#dashboard_id Annotation#dashboard_id}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#id Annotation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param panel_id: The ID of the dashboard panel on which to create the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#panel_id Annotation#panel_id}
        :param tags: The tags to associate with the annotation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#tags Annotation#tags}
        :param time: The RFC 3339-formatted time string indicating the annotation's time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#time Annotation#time}
        :param time_end: The RFC 3339-formatted time string indicating the annotation's end time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#time_end Annotation#time_end}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__753c715536d6a7cde43e099dc2fd5d3a527f63aac19c35c22da67234e11e9831)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument panel_id", value=panel_id, expected_type=type_hints["panel_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            check_type(argname="argument time_end", value=time_end, expected_type=type_hints["time_end"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "text": text,
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
        if id is not None:
            self._values["id"] = id
        if panel_id is not None:
            self._values["panel_id"] = panel_id
        if tags is not None:
            self._values["tags"] = tags
        if time is not None:
            self._values["time"] = time
        if time_end is not None:
            self._values["time_end"] = time_end

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
    def text(self) -> builtins.str:
        '''The text to associate with the annotation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#text Annotation#text}
        '''
        result = self._values.get("text")
        assert result is not None, "Required property 'text' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the dashboard on which to create the annotation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#dashboard_id Annotation#dashboard_id}
        '''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#id Annotation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def panel_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the dashboard panel on which to create the annotation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#panel_id Annotation#panel_id}
        '''
        result = self._values.get("panel_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The tags to associate with the annotation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#tags Annotation#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def time(self) -> typing.Optional[builtins.str]:
        '''The RFC 3339-formatted time string indicating the annotation's time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#time Annotation#time}
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_end(self) -> typing.Optional[builtins.str]:
        '''The RFC 3339-formatted time string indicating the annotation's end time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/annotation#time_end Annotation#time_end}
        '''
        result = self._values.get("time_end")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnnotationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Annotation",
    "AnnotationConfig",
]

publication.publish()

def _typecheckingstub__7e6ae2dc5fb7a709759eb81f96bd7a6ac0faf3927fe04a7ebaf34c70062c48ac(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    text: builtins.str,
    dashboard_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    panel_id: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    time: typing.Optional[builtins.str] = None,
    time_end: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__3aac17a189273752849268c64fb62f3795a0500f61e822a9c8d28a915b659012(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef3cade4a10060f529a4ecdd3ae845a16d3a36156ea819a3e63c609389b5f15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2428437de9ca0fa00e7d612f780fe1b83dcf56ee7dc07d8c06490f527fa72267(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb567db44db4d1e2e2beb8136fc3e53849731af4473d12440d71e26fef57088c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d480d05e9d65f7894241b1c9afe7a53ecfe4a9ef01969bb19a374ee4722d52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__affca23d08c766b26469dccb33fce12b840458579424d6f162106d98e944c67d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8889304dbafd08ffa5bee601888e50543d149e7fca9425ba4f85970779fbb7ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753c715536d6a7cde43e099dc2fd5d3a527f63aac19c35c22da67234e11e9831(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    text: builtins.str,
    dashboard_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    panel_id: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    time: typing.Optional[builtins.str] = None,
    time_end: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
