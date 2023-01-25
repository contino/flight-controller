'''
# `grafana_machine_learning_holiday`

Refer to the Terraform Registory for docs: [`grafana_machine_learning_holiday`](https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday).
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


class MachineLearningHoliday(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.machineLearningHoliday.MachineLearningHoliday",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday grafana_machine_learning_holiday}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        custom_periods: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MachineLearningHolidayCustomPeriods", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        ical_timezone: typing.Optional[builtins.str] = None,
        ical_url: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday grafana_machine_learning_holiday} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the holiday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#name MachineLearningHoliday#name}
        :param custom_periods: custom_periods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#custom_periods MachineLearningHoliday#custom_periods}
        :param description: A description of the holiday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#description MachineLearningHoliday#description}
        :param ical_timezone: The timezone to use for events in the iCal file pointed to by ical_url. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#ical_timezone MachineLearningHoliday#ical_timezone}
        :param ical_url: A URL to an iCal file containing all occurrences of the holiday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#ical_url MachineLearningHoliday#ical_url}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704beca00c78ae5b6e9ed55803db76f1e11f0556a35c9be860f23c0cbf2f89a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = MachineLearningHolidayConfig(
            name=name,
            custom_periods=custom_periods,
            description=description,
            ical_timezone=ical_timezone,
            ical_url=ical_url,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putCustomPeriods")
    def put_custom_periods(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MachineLearningHolidayCustomPeriods", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4013c7db1073b32901003ebdc69e70b0296b1f374ee67bbff4de2be05d248922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomPeriods", [value]))

    @jsii.member(jsii_name="resetCustomPeriods")
    def reset_custom_periods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPeriods", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetIcalTimezone")
    def reset_ical_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcalTimezone", []))

    @jsii.member(jsii_name="resetIcalUrl")
    def reset_ical_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIcalUrl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="customPeriods")
    def custom_periods(self) -> "MachineLearningHolidayCustomPeriodsList":
        return typing.cast("MachineLearningHolidayCustomPeriodsList", jsii.get(self, "customPeriods"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="customPeriodsInput")
    def custom_periods_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MachineLearningHolidayCustomPeriods"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MachineLearningHolidayCustomPeriods"]]], jsii.get(self, "customPeriodsInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="icalTimezoneInput")
    def ical_timezone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icalTimezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="icalUrlInput")
    def ical_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "icalUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db7ef7547b6045c0b9d4e3162d4aa20892e18c2453bd91a955e29ab99c3c3488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="icalTimezone")
    def ical_timezone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icalTimezone"))

    @ical_timezone.setter
    def ical_timezone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ef1e9d2a5447b531c7852197435bf52e0f32986df82c5e1244a9d370fa217b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icalTimezone", value)

    @builtins.property
    @jsii.member(jsii_name="icalUrl")
    def ical_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "icalUrl"))

    @ical_url.setter
    def ical_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa61530dd4c1aa64ec22f067cf3c0bff9457f08c4a0aa0bd4a1acf03c9530eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "icalUrl", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f0ccf1913cfc9e7ae2129d48ad7e9bc81418536d61d5998b096acd8baed4c86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="grafana.machineLearningHoliday.MachineLearningHolidayConfig",
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
        "custom_periods": "customPeriods",
        "description": "description",
        "ical_timezone": "icalTimezone",
        "ical_url": "icalUrl",
    },
)
class MachineLearningHolidayConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        custom_periods: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["MachineLearningHolidayCustomPeriods", typing.Dict[builtins.str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        ical_timezone: typing.Optional[builtins.str] = None,
        ical_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the holiday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#name MachineLearningHoliday#name}
        :param custom_periods: custom_periods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#custom_periods MachineLearningHoliday#custom_periods}
        :param description: A description of the holiday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#description MachineLearningHoliday#description}
        :param ical_timezone: The timezone to use for events in the iCal file pointed to by ical_url. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#ical_timezone MachineLearningHoliday#ical_timezone}
        :param ical_url: A URL to an iCal file containing all occurrences of the holiday. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#ical_url MachineLearningHoliday#ical_url}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aab7c1a3cb2827dc0bc9a70dc925072ec794c3842e3bfd7e4ea76f55e60fed3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument custom_periods", value=custom_periods, expected_type=type_hints["custom_periods"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument ical_timezone", value=ical_timezone, expected_type=type_hints["ical_timezone"])
            check_type(argname="argument ical_url", value=ical_url, expected_type=type_hints["ical_url"])
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
        if custom_periods is not None:
            self._values["custom_periods"] = custom_periods
        if description is not None:
            self._values["description"] = description
        if ical_timezone is not None:
            self._values["ical_timezone"] = ical_timezone
        if ical_url is not None:
            self._values["ical_url"] = ical_url

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
        '''The name of the holiday.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#name MachineLearningHoliday#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_periods(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MachineLearningHolidayCustomPeriods"]]]:
        '''custom_periods block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#custom_periods MachineLearningHoliday#custom_periods}
        '''
        result = self._values.get("custom_periods")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["MachineLearningHolidayCustomPeriods"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the holiday.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#description MachineLearningHoliday#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ical_timezone(self) -> typing.Optional[builtins.str]:
        '''The timezone to use for events in the iCal file pointed to by ical_url.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#ical_timezone MachineLearningHoliday#ical_timezone}
        '''
        result = self._values.get("ical_timezone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ical_url(self) -> typing.Optional[builtins.str]:
        '''A URL to an iCal file containing all occurrences of the holiday.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#ical_url MachineLearningHoliday#ical_url}
        '''
        result = self._values.get("ical_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningHolidayConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.machineLearningHoliday.MachineLearningHolidayCustomPeriods",
    jsii_struct_bases=[],
    name_mapping={"end_time": "endTime", "start_time": "startTime", "name": "name"},
)
class MachineLearningHolidayCustomPeriods:
    def __init__(
        self,
        *,
        end_time: builtins.str,
        start_time: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param end_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#end_time MachineLearningHoliday#end_time}.
        :param start_time: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#start_time MachineLearningHoliday#start_time}.
        :param name: The name of the custom period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#name MachineLearningHoliday#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__348993db7065e45e0ae2c68a9a23b97ad51cc5475b8a41cdcdc89ad65ce872fb)
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "end_time": end_time,
            "start_time": start_time,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def end_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#end_time MachineLearningHoliday#end_time}.'''
        result = self._values.get("end_time")
        assert result is not None, "Required property 'end_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def start_time(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#start_time MachineLearningHoliday#start_time}.'''
        result = self._values.get("start_time")
        assert result is not None, "Required property 'start_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the custom period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_holiday#name MachineLearningHoliday#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningHolidayCustomPeriods(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MachineLearningHolidayCustomPeriodsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.machineLearningHoliday.MachineLearningHolidayCustomPeriodsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__38e2110de2e73ccd70954f43fa03a120a6411f796d6304037c286cf7ee3f84e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "MachineLearningHolidayCustomPeriodsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__672d812dfa0177dbd3754adc4b2c47c1fe71015c433d378e303c946ff7e8e27a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("MachineLearningHolidayCustomPeriodsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cbb65a35314f1e6cce5420c37e9f627a293c9b63d7e7a9b788e561a7fb58cb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97716567ad444e72782c90d12643e1e51959c37cd9a13597be8ba437bf1097ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a74beee0bad884c91f89185eef32e63e3ddd1241e9bf754349b03eaa3f832da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MachineLearningHolidayCustomPeriods]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MachineLearningHolidayCustomPeriods]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MachineLearningHolidayCustomPeriods]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3aca61292ec48ca2f0b073f49637ea2a1d224152b1792d0ddbb531aade0e3f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class MachineLearningHolidayCustomPeriodsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.machineLearningHoliday.MachineLearningHolidayCustomPeriodsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__339cbf52a29e114a3c286930d10adb37ad85b173809572b7f54516363de488d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308a4542485353560c13753750d951f2f18346e3b80f3c2def3e2d1473783529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e63c117e09acac8f7962553d971e89a687b60960d967d121669c453376969e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f1b0df7fea52022d5d72e88bf0ae97ddbdaa72f87475d76949d95a1a1de8d96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MachineLearningHolidayCustomPeriods, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MachineLearningHolidayCustomPeriods, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MachineLearningHolidayCustomPeriods, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14cd0e0d6235ec3146f6f6dcaa57455dc9d105923f386c778eafa464a8078705)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "MachineLearningHoliday",
    "MachineLearningHolidayConfig",
    "MachineLearningHolidayCustomPeriods",
    "MachineLearningHolidayCustomPeriodsList",
    "MachineLearningHolidayCustomPeriodsOutputReference",
]

publication.publish()

def _typecheckingstub__704beca00c78ae5b6e9ed55803db76f1e11f0556a35c9be860f23c0cbf2f89a5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    custom_periods: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MachineLearningHolidayCustomPeriods, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    ical_timezone: typing.Optional[builtins.str] = None,
    ical_url: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__4013c7db1073b32901003ebdc69e70b0296b1f374ee67bbff4de2be05d248922(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MachineLearningHolidayCustomPeriods, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db7ef7547b6045c0b9d4e3162d4aa20892e18c2453bd91a955e29ab99c3c3488(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef1e9d2a5447b531c7852197435bf52e0f32986df82c5e1244a9d370fa217b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa61530dd4c1aa64ec22f067cf3c0bff9457f08c4a0aa0bd4a1acf03c9530eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0ccf1913cfc9e7ae2129d48ad7e9bc81418536d61d5998b096acd8baed4c86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aab7c1a3cb2827dc0bc9a70dc925072ec794c3842e3bfd7e4ea76f55e60fed3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    custom_periods: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[MachineLearningHolidayCustomPeriods, typing.Dict[builtins.str, typing.Any]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    ical_timezone: typing.Optional[builtins.str] = None,
    ical_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__348993db7065e45e0ae2c68a9a23b97ad51cc5475b8a41cdcdc89ad65ce872fb(
    *,
    end_time: builtins.str,
    start_time: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38e2110de2e73ccd70954f43fa03a120a6411f796d6304037c286cf7ee3f84e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__672d812dfa0177dbd3754adc4b2c47c1fe71015c433d378e303c946ff7e8e27a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cbb65a35314f1e6cce5420c37e9f627a293c9b63d7e7a9b788e561a7fb58cb7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97716567ad444e72782c90d12643e1e51959c37cd9a13597be8ba437bf1097ec(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74beee0bad884c91f89185eef32e63e3ddd1241e9bf754349b03eaa3f832da2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3aca61292ec48ca2f0b073f49637ea2a1d224152b1792d0ddbb531aade0e3f1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[MachineLearningHolidayCustomPeriods]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__339cbf52a29e114a3c286930d10adb37ad85b173809572b7f54516363de488d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308a4542485353560c13753750d951f2f18346e3b80f3c2def3e2d1473783529(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e63c117e09acac8f7962553d971e89a687b60960d967d121669c453376969e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f1b0df7fea52022d5d72e88bf0ae97ddbdaa72f87475d76949d95a1a1de8d96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14cd0e0d6235ec3146f6f6dcaa57455dc9d105923f386c778eafa464a8078705(
    value: typing.Optional[typing.Union[MachineLearningHolidayCustomPeriods, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
