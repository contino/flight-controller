'''
# `grafana_report`

Refer to the Terraform Registory for docs: [`grafana_report`](https://www.terraform.io/docs/providers/grafana/r/report).
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


class Report(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.report.Report",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/report grafana_report}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        recipients: typing.Sequence[builtins.str],
        schedule: typing.Union["ReportSchedule", typing.Dict[builtins.str, typing.Any]],
        dashboard_id: typing.Optional[jsii.Number] = None,
        dashboard_uid: typing.Optional[builtins.str] = None,
        include_dashboard_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_table_csv: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        layout: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        orientation: typing.Optional[builtins.str] = None,
        reply_to: typing.Optional[builtins.str] = None,
        time_range: typing.Optional[typing.Union["ReportTimeRange", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/report grafana_report} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#name Report#name}
        :param recipients: List of recipients of the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#recipients Report#recipients}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#schedule Report#schedule}
        :param dashboard_id: Dashboard to be sent in the report. This field is deprecated, use ``dashboard_uid`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#dashboard_id Report#dashboard_id}
        :param dashboard_uid: Dashboard to be sent in the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#dashboard_uid Report#dashboard_uid}
        :param include_dashboard_link: Whether to include a link to the dashboard in the report. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#include_dashboard_link Report#include_dashboard_link}
        :param include_table_csv: Whether to include a CSV file of table panel data. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#include_table_csv Report#include_table_csv}
        :param layout: Layout of the report. Allowed values: ``simple``, ``grid``. Defaults to ``grid``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#layout Report#layout}
        :param message: Message to be sent in the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#message Report#message}
        :param orientation: Orientation of the report. Allowed values: ``landscape``, ``portrait``. Defaults to ``landscape``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#orientation Report#orientation}
        :param reply_to: Reply-to email address of the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#reply_to Report#reply_to}
        :param time_range: time_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#time_range Report#time_range}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b978e7f39519aaaee4b60bd4cbb9a03c0daf9f9cd76a8b7b8d7224cb4382ecc0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ReportConfig(
            name=name,
            recipients=recipients,
            schedule=schedule,
            dashboard_id=dashboard_id,
            dashboard_uid=dashboard_uid,
            include_dashboard_link=include_dashboard_link,
            include_table_csv=include_table_csv,
            layout=layout,
            message=message,
            orientation=orientation,
            reply_to=reply_to,
            time_range=time_range,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="putSchedule")
    def put_schedule(
        self,
        *,
        frequency: builtins.str,
        custom_interval: typing.Optional[builtins.str] = None,
        end_time: typing.Optional[builtins.str] = None,
        last_day_of_month: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        start_time: typing.Optional[builtins.str] = None,
        workdays_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param frequency: Frequency of the report. Allowed values: ``never``, ``once``, ``hourly``, ``daily``, ``weekly``, ``monthly``, ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#frequency Report#frequency}
        :param custom_interval: Custom interval of the report. *Note:** This field is only available when frequency is set to ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#custom_interval Report#custom_interval}
        :param end_time: End time of the report. If empty, the report will be sent indefinitely (according to frequency). Note that times will be saved as UTC in Grafana. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#end_time Report#end_time}
        :param last_day_of_month: Send the report on the last day of the month Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#last_day_of_month Report#last_day_of_month}
        :param start_time: Start time of the report. If empty, the start date will be set to the creation time. Note that times will be saved as UTC in Grafana. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#start_time Report#start_time}
        :param workdays_only: Whether to send the report only on work days. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#workdays_only Report#workdays_only}
        '''
        value = ReportSchedule(
            frequency=frequency,
            custom_interval=custom_interval,
            end_time=end_time,
            last_day_of_month=last_day_of_month,
            start_time=start_time,
            workdays_only=workdays_only,
        )

        return typing.cast(None, jsii.invoke(self, "putSchedule", [value]))

    @jsii.member(jsii_name="putTimeRange")
    def put_time_range(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Start of the time range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#from Report#from}
        :param to: End of the time range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#to Report#to}
        '''
        value = ReportTimeRange(from_=from_, to=to)

        return typing.cast(None, jsii.invoke(self, "putTimeRange", [value]))

    @jsii.member(jsii_name="resetDashboardId")
    def reset_dashboard_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDashboardId", []))

    @jsii.member(jsii_name="resetDashboardUid")
    def reset_dashboard_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDashboardUid", []))

    @jsii.member(jsii_name="resetIncludeDashboardLink")
    def reset_include_dashboard_link(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeDashboardLink", []))

    @jsii.member(jsii_name="resetIncludeTableCsv")
    def reset_include_table_csv(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIncludeTableCsv", []))

    @jsii.member(jsii_name="resetLayout")
    def reset_layout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLayout", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetOrientation")
    def reset_orientation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrientation", []))

    @jsii.member(jsii_name="resetReplyTo")
    def reset_reply_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplyTo", []))

    @jsii.member(jsii_name="resetTimeRange")
    def reset_time_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeRange", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> "ReportScheduleOutputReference":
        return typing.cast("ReportScheduleOutputReference", jsii.get(self, "schedule"))

    @builtins.property
    @jsii.member(jsii_name="timeRange")
    def time_range(self) -> "ReportTimeRangeOutputReference":
        return typing.cast("ReportTimeRangeOutputReference", jsii.get(self, "timeRange"))

    @builtins.property
    @jsii.member(jsii_name="dashboardIdInput")
    def dashboard_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dashboardIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardUidInput")
    def dashboard_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dashboardUidInput"))

    @builtins.property
    @jsii.member(jsii_name="includeDashboardLinkInput")
    def include_dashboard_link_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeDashboardLinkInput"))

    @builtins.property
    @jsii.member(jsii_name="includeTableCsvInput")
    def include_table_csv_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "includeTableCsvInput"))

    @builtins.property
    @jsii.member(jsii_name="layoutInput")
    def layout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "layoutInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orientationInput")
    def orientation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "orientationInput"))

    @builtins.property
    @jsii.member(jsii_name="recipientsInput")
    def recipients_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "recipientsInput"))

    @builtins.property
    @jsii.member(jsii_name="replyToInput")
    def reply_to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replyToInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional["ReportSchedule"]:
        return typing.cast(typing.Optional["ReportSchedule"], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="timeRangeInput")
    def time_range_input(self) -> typing.Optional["ReportTimeRange"]:
        return typing.cast(typing.Optional["ReportTimeRange"], jsii.get(self, "timeRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="dashboardId")
    def dashboard_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dashboardId"))

    @dashboard_id.setter
    def dashboard_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7203c5bc974fba11b4576518f8592102a75f5126e56696800c4a8c3e00d5f9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardId", value)

    @builtins.property
    @jsii.member(jsii_name="dashboardUid")
    def dashboard_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dashboardUid"))

    @dashboard_uid.setter
    def dashboard_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce1512f1525d1be9e9172fb3c6c22fe99cd5e0d40c90cebcaf4ee656571559b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardUid", value)

    @builtins.property
    @jsii.member(jsii_name="includeDashboardLink")
    def include_dashboard_link(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeDashboardLink"))

    @include_dashboard_link.setter
    def include_dashboard_link(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c09e08b1e62a0be0c169bdd01f33f131f0b3cc2d67363cf0b2d665e65ff72b9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeDashboardLink", value)

    @builtins.property
    @jsii.member(jsii_name="includeTableCsv")
    def include_table_csv(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "includeTableCsv"))

    @include_table_csv.setter
    def include_table_csv(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f113e7f5018a98de1e845388eca594579480c0e5004f21d242709034e9130a29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "includeTableCsv", value)

    @builtins.property
    @jsii.member(jsii_name="layout")
    def layout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "layout"))

    @layout.setter
    def layout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cc93e8cc796f80a4cd30faf072fed70d0182be77742db7c23b36e246427aeb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layout", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d1b08a40d9d8ed67211cd24589e4a094b9cc09d1c09a685833dc14b1f0bb1f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c986502eca8b590294a39ec5f0619bc5f29b365907144ff71496020c72de21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="orientation")
    def orientation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orientation"))

    @orientation.setter
    def orientation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e66d578e47ae4c73997f719f871ba7a0712a44dcc9204cd2292f9ef25db22ce6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "orientation", value)

    @builtins.property
    @jsii.member(jsii_name="recipients")
    def recipients(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "recipients"))

    @recipients.setter
    def recipients(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceda30e15847f451100c7294a6ef581f5aad385e9c13da4c3d1d5f2103d3637e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipients", value)

    @builtins.property
    @jsii.member(jsii_name="replyTo")
    def reply_to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replyTo"))

    @reply_to.setter
    def reply_to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2729f223fa60a14b2cbe5a81e119aa409ce1619335f2b7f121cc9ca91639056e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replyTo", value)


@jsii.data_type(
    jsii_type="grafana.report.ReportConfig",
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
        "recipients": "recipients",
        "schedule": "schedule",
        "dashboard_id": "dashboardId",
        "dashboard_uid": "dashboardUid",
        "include_dashboard_link": "includeDashboardLink",
        "include_table_csv": "includeTableCsv",
        "layout": "layout",
        "message": "message",
        "orientation": "orientation",
        "reply_to": "replyTo",
        "time_range": "timeRange",
    },
)
class ReportConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        recipients: typing.Sequence[builtins.str],
        schedule: typing.Union["ReportSchedule", typing.Dict[builtins.str, typing.Any]],
        dashboard_id: typing.Optional[jsii.Number] = None,
        dashboard_uid: typing.Optional[builtins.str] = None,
        include_dashboard_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        include_table_csv: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        layout: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        orientation: typing.Optional[builtins.str] = None,
        reply_to: typing.Optional[builtins.str] = None,
        time_range: typing.Optional[typing.Union["ReportTimeRange", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#name Report#name}
        :param recipients: List of recipients of the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#recipients Report#recipients}
        :param schedule: schedule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#schedule Report#schedule}
        :param dashboard_id: Dashboard to be sent in the report. This field is deprecated, use ``dashboard_uid`` instead. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#dashboard_id Report#dashboard_id}
        :param dashboard_uid: Dashboard to be sent in the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#dashboard_uid Report#dashboard_uid}
        :param include_dashboard_link: Whether to include a link to the dashboard in the report. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#include_dashboard_link Report#include_dashboard_link}
        :param include_table_csv: Whether to include a CSV file of table panel data. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#include_table_csv Report#include_table_csv}
        :param layout: Layout of the report. Allowed values: ``simple``, ``grid``. Defaults to ``grid``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#layout Report#layout}
        :param message: Message to be sent in the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#message Report#message}
        :param orientation: Orientation of the report. Allowed values: ``landscape``, ``portrait``. Defaults to ``landscape``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#orientation Report#orientation}
        :param reply_to: Reply-to email address of the report. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#reply_to Report#reply_to}
        :param time_range: time_range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#time_range Report#time_range}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(schedule, dict):
            schedule = ReportSchedule(**schedule)
        if isinstance(time_range, dict):
            time_range = ReportTimeRange(**time_range)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e6bee9264c5a5512b825be9e1e23e08a2931fdec79f6dec6712d5edf51537f)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
            check_type(argname="argument dashboard_uid", value=dashboard_uid, expected_type=type_hints["dashboard_uid"])
            check_type(argname="argument include_dashboard_link", value=include_dashboard_link, expected_type=type_hints["include_dashboard_link"])
            check_type(argname="argument include_table_csv", value=include_table_csv, expected_type=type_hints["include_table_csv"])
            check_type(argname="argument layout", value=layout, expected_type=type_hints["layout"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument orientation", value=orientation, expected_type=type_hints["orientation"])
            check_type(argname="argument reply_to", value=reply_to, expected_type=type_hints["reply_to"])
            check_type(argname="argument time_range", value=time_range, expected_type=type_hints["time_range"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "recipients": recipients,
            "schedule": schedule,
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
        if include_dashboard_link is not None:
            self._values["include_dashboard_link"] = include_dashboard_link
        if include_table_csv is not None:
            self._values["include_table_csv"] = include_table_csv
        if layout is not None:
            self._values["layout"] = layout
        if message is not None:
            self._values["message"] = message
        if orientation is not None:
            self._values["orientation"] = orientation
        if reply_to is not None:
            self._values["reply_to"] = reply_to
        if time_range is not None:
            self._values["time_range"] = time_range

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
        '''Name of the report.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#name Report#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recipients(self) -> typing.List[builtins.str]:
        '''List of recipients of the report.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#recipients Report#recipients}
        '''
        result = self._values.get("recipients")
        assert result is not None, "Required property 'recipients' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def schedule(self) -> "ReportSchedule":
        '''schedule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#schedule Report#schedule}
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast("ReportSchedule", result)

    @builtins.property
    def dashboard_id(self) -> typing.Optional[jsii.Number]:
        '''Dashboard to be sent in the report. This field is deprecated, use ``dashboard_uid`` instead.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#dashboard_id Report#dashboard_id}
        '''
        result = self._values.get("dashboard_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dashboard_uid(self) -> typing.Optional[builtins.str]:
        '''Dashboard to be sent in the report.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#dashboard_uid Report#dashboard_uid}
        '''
        result = self._values.get("dashboard_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def include_dashboard_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to include a link to the dashboard in the report. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#include_dashboard_link Report#include_dashboard_link}
        '''
        result = self._values.get("include_dashboard_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def include_table_csv(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to include a CSV file of table panel data. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#include_table_csv Report#include_table_csv}
        '''
        result = self._values.get("include_table_csv")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def layout(self) -> typing.Optional[builtins.str]:
        '''Layout of the report. Allowed values: ``simple``, ``grid``. Defaults to ``grid``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#layout Report#layout}
        '''
        result = self._values.get("layout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Message to be sent in the report.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#message Report#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def orientation(self) -> typing.Optional[builtins.str]:
        '''Orientation of the report. Allowed values: ``landscape``, ``portrait``. Defaults to ``landscape``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#orientation Report#orientation}
        '''
        result = self._values.get("orientation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reply_to(self) -> typing.Optional[builtins.str]:
        '''Reply-to email address of the report.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#reply_to Report#reply_to}
        '''
        result = self._values.get("reply_to")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_range(self) -> typing.Optional["ReportTimeRange"]:
        '''time_range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#time_range Report#time_range}
        '''
        result = self._values.get("time_range")
        return typing.cast(typing.Optional["ReportTimeRange"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReportConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.report.ReportSchedule",
    jsii_struct_bases=[],
    name_mapping={
        "frequency": "frequency",
        "custom_interval": "customInterval",
        "end_time": "endTime",
        "last_day_of_month": "lastDayOfMonth",
        "start_time": "startTime",
        "workdays_only": "workdaysOnly",
    },
)
class ReportSchedule:
    def __init__(
        self,
        *,
        frequency: builtins.str,
        custom_interval: typing.Optional[builtins.str] = None,
        end_time: typing.Optional[builtins.str] = None,
        last_day_of_month: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        start_time: typing.Optional[builtins.str] = None,
        workdays_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param frequency: Frequency of the report. Allowed values: ``never``, ``once``, ``hourly``, ``daily``, ``weekly``, ``monthly``, ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#frequency Report#frequency}
        :param custom_interval: Custom interval of the report. *Note:** This field is only available when frequency is set to ``custom``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#custom_interval Report#custom_interval}
        :param end_time: End time of the report. If empty, the report will be sent indefinitely (according to frequency). Note that times will be saved as UTC in Grafana. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#end_time Report#end_time}
        :param last_day_of_month: Send the report on the last day of the month Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#last_day_of_month Report#last_day_of_month}
        :param start_time: Start time of the report. If empty, the start date will be set to the creation time. Note that times will be saved as UTC in Grafana. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#start_time Report#start_time}
        :param workdays_only: Whether to send the report only on work days. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#workdays_only Report#workdays_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f90c56bdaf205d3bcc1dab8bfb218a0802ac0763db9bc405a99f6751e90e287a)
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument custom_interval", value=custom_interval, expected_type=type_hints["custom_interval"])
            check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
            check_type(argname="argument last_day_of_month", value=last_day_of_month, expected_type=type_hints["last_day_of_month"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument workdays_only", value=workdays_only, expected_type=type_hints["workdays_only"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "frequency": frequency,
        }
        if custom_interval is not None:
            self._values["custom_interval"] = custom_interval
        if end_time is not None:
            self._values["end_time"] = end_time
        if last_day_of_month is not None:
            self._values["last_day_of_month"] = last_day_of_month
        if start_time is not None:
            self._values["start_time"] = start_time
        if workdays_only is not None:
            self._values["workdays_only"] = workdays_only

    @builtins.property
    def frequency(self) -> builtins.str:
        '''Frequency of the report. Allowed values: ``never``, ``once``, ``hourly``, ``daily``, ``weekly``, ``monthly``, ``custom``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#frequency Report#frequency}
        '''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_interval(self) -> typing.Optional[builtins.str]:
        '''Custom interval of the report. *Note:** This field is only available when frequency is set to ``custom``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#custom_interval Report#custom_interval}
        '''
        result = self._values.get("custom_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_time(self) -> typing.Optional[builtins.str]:
        '''End time of the report.

        If empty, the report will be sent indefinitely (according to frequency). Note that times will be saved as UTC in Grafana.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#end_time Report#end_time}
        '''
        result = self._values.get("end_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def last_day_of_month(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Send the report on the last day of the month Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#last_day_of_month Report#last_day_of_month}
        '''
        result = self._values.get("last_day_of_month")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''Start time of the report.

        If empty, the start date will be set to the creation time. Note that times will be saved as UTC in Grafana.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#start_time Report#start_time}
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workdays_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to send the report only on work days. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#workdays_only Report#workdays_only}
        '''
        result = self._values.get("workdays_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReportSchedule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ReportScheduleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.report.ReportScheduleOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c4760ae066a78243465234dd020bf58a03ae4ca16b34dc120cd8b2a65b7c1f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomInterval")
    def reset_custom_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomInterval", []))

    @jsii.member(jsii_name="resetEndTime")
    def reset_end_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndTime", []))

    @jsii.member(jsii_name="resetLastDayOfMonth")
    def reset_last_day_of_month(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLastDayOfMonth", []))

    @jsii.member(jsii_name="resetStartTime")
    def reset_start_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTime", []))

    @jsii.member(jsii_name="resetWorkdaysOnly")
    def reset_workdays_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkdaysOnly", []))

    @builtins.property
    @jsii.member(jsii_name="customIntervalInput")
    def custom_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="endTimeInput")
    def end_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="lastDayOfMonthInput")
    def last_day_of_month_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "lastDayOfMonthInput"))

    @builtins.property
    @jsii.member(jsii_name="startTimeInput")
    def start_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="workdaysOnlyInput")
    def workdays_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "workdaysOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="customInterval")
    def custom_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customInterval"))

    @custom_interval.setter
    def custom_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e0b1c136cd8cda7c6800e7cb6796c8521392e8d54d488bc8403a0e78bb6194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customInterval", value)

    @builtins.property
    @jsii.member(jsii_name="endTime")
    def end_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endTime"))

    @end_time.setter
    def end_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44793f44d41dfeed3f7793465a2c804e10ca8e05031315c74df13a22516f1df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endTime", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__538254bcf017dd2af23efc15dcf0fcbd862c0e5dcf851ce7cc3958819c6260a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="lastDayOfMonth")
    def last_day_of_month(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "lastDayOfMonth"))

    @last_day_of_month.setter
    def last_day_of_month(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70fbfc6ea913fd72c8208e25ff33a685b5d94794fa4b4e9f2825044deaee031b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastDayOfMonth", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047960c6462c472ef58544434f0edb37317609494b80323385a9269c316f51f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="workdaysOnly")
    def workdays_only(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "workdaysOnly"))

    @workdays_only.setter
    def workdays_only(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b87885931e9ba4476294150352009a8cfef5c0c66e37c32c2d92861453b7f004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workdaysOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ReportSchedule]:
        return typing.cast(typing.Optional[ReportSchedule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ReportSchedule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6490df54c3b3223d01cb319c5f5f184f22689a11d97cd475610503e88f43161)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.report.ReportTimeRange",
    jsii_struct_bases=[],
    name_mapping={"from_": "from", "to": "to"},
)
class ReportTimeRange:
    def __init__(
        self,
        *,
        from_: typing.Optional[builtins.str] = None,
        to: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param from_: Start of the time range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#from Report#from}
        :param to: End of the time range. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#to Report#to}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57a14705174e3d37c8d9dff9d39c66cd84145c4e1235ae5b7c9ce2fd2ebd9a44)
            check_type(argname="argument from_", value=from_, expected_type=type_hints["from_"])
            check_type(argname="argument to", value=to, expected_type=type_hints["to"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if from_ is not None:
            self._values["from_"] = from_
        if to is not None:
            self._values["to"] = to

    @builtins.property
    def from_(self) -> typing.Optional[builtins.str]:
        '''Start of the time range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#from Report#from}
        '''
        result = self._values.get("from_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def to(self) -> typing.Optional[builtins.str]:
        '''End of the time range.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/report#to Report#to}
        '''
        result = self._values.get("to")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReportTimeRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ReportTimeRangeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.report.ReportTimeRangeOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__448f920207328cd199bb78b84cd9eb21aa3f9e73b3153be24b62c87f56a4a05d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFrom")
    def reset_from(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrom", []))

    @jsii.member(jsii_name="resetTo")
    def reset_to(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTo", []))

    @builtins.property
    @jsii.member(jsii_name="fromInput")
    def from_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromInput"))

    @builtins.property
    @jsii.member(jsii_name="toInput")
    def to_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "toInput"))

    @builtins.property
    @jsii.member(jsii_name="from")
    def from_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "from"))

    @from_.setter
    def from_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb51e12b00087d93d62be08f9fb996d8ffa4f22bd9aa87ddc07d36132498a4f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "from", value)

    @builtins.property
    @jsii.member(jsii_name="to")
    def to(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "to"))

    @to.setter
    def to(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db8659cddfbaf0f434f781b97d636662e301d8b0c3efc96b742f2b9d188c695c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "to", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ReportTimeRange]:
        return typing.cast(typing.Optional[ReportTimeRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ReportTimeRange]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32aff2279160ad277d994501074439369dfa5d3878d7985957dfb46080ec6509)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Report",
    "ReportConfig",
    "ReportSchedule",
    "ReportScheduleOutputReference",
    "ReportTimeRange",
    "ReportTimeRangeOutputReference",
]

publication.publish()

def _typecheckingstub__b978e7f39519aaaee4b60bd4cbb9a03c0daf9f9cd76a8b7b8d7224cb4382ecc0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    recipients: typing.Sequence[builtins.str],
    schedule: typing.Union[ReportSchedule, typing.Dict[builtins.str, typing.Any]],
    dashboard_id: typing.Optional[jsii.Number] = None,
    dashboard_uid: typing.Optional[builtins.str] = None,
    include_dashboard_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_table_csv: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    layout: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
    orientation: typing.Optional[builtins.str] = None,
    reply_to: typing.Optional[builtins.str] = None,
    time_range: typing.Optional[typing.Union[ReportTimeRange, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__e7203c5bc974fba11b4576518f8592102a75f5126e56696800c4a8c3e00d5f9b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce1512f1525d1be9e9172fb3c6c22fe99cd5e0d40c90cebcaf4ee656571559b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09e08b1e62a0be0c169bdd01f33f131f0b3cc2d67363cf0b2d665e65ff72b9f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f113e7f5018a98de1e845388eca594579480c0e5004f21d242709034e9130a29(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc93e8cc796f80a4cd30faf072fed70d0182be77742db7c23b36e246427aeb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d1b08a40d9d8ed67211cd24589e4a094b9cc09d1c09a685833dc14b1f0bb1f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c986502eca8b590294a39ec5f0619bc5f29b365907144ff71496020c72de21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e66d578e47ae4c73997f719f871ba7a0712a44dcc9204cd2292f9ef25db22ce6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceda30e15847f451100c7294a6ef581f5aad385e9c13da4c3d1d5f2103d3637e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2729f223fa60a14b2cbe5a81e119aa409ce1619335f2b7f121cc9ca91639056e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e6bee9264c5a5512b825be9e1e23e08a2931fdec79f6dec6712d5edf51537f(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    recipients: typing.Sequence[builtins.str],
    schedule: typing.Union[ReportSchedule, typing.Dict[builtins.str, typing.Any]],
    dashboard_id: typing.Optional[jsii.Number] = None,
    dashboard_uid: typing.Optional[builtins.str] = None,
    include_dashboard_link: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    include_table_csv: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    layout: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
    orientation: typing.Optional[builtins.str] = None,
    reply_to: typing.Optional[builtins.str] = None,
    time_range: typing.Optional[typing.Union[ReportTimeRange, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f90c56bdaf205d3bcc1dab8bfb218a0802ac0763db9bc405a99f6751e90e287a(
    *,
    frequency: builtins.str,
    custom_interval: typing.Optional[builtins.str] = None,
    end_time: typing.Optional[builtins.str] = None,
    last_day_of_month: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    start_time: typing.Optional[builtins.str] = None,
    workdays_only: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4760ae066a78243465234dd020bf58a03ae4ca16b34dc120cd8b2a65b7c1f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e0b1c136cd8cda7c6800e7cb6796c8521392e8d54d488bc8403a0e78bb6194(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44793f44d41dfeed3f7793465a2c804e10ca8e05031315c74df13a22516f1df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__538254bcf017dd2af23efc15dcf0fcbd862c0e5dcf851ce7cc3958819c6260a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70fbfc6ea913fd72c8208e25ff33a685b5d94794fa4b4e9f2825044deaee031b(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047960c6462c472ef58544434f0edb37317609494b80323385a9269c316f51f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b87885931e9ba4476294150352009a8cfef5c0c66e37c32c2d92861453b7f004(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6490df54c3b3223d01cb319c5f5f184f22689a11d97cd475610503e88f43161(
    value: typing.Optional[ReportSchedule],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a14705174e3d37c8d9dff9d39c66cd84145c4e1235ae5b7c9ce2fd2ebd9a44(
    *,
    from_: typing.Optional[builtins.str] = None,
    to: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__448f920207328cd199bb78b84cd9eb21aa3f9e73b3153be24b62c87f56a4a05d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb51e12b00087d93d62be08f9fb996d8ffa4f22bd9aa87ddc07d36132498a4f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8659cddfbaf0f434f781b97d636662e301d8b0c3efc96b742f2b9d188c695c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32aff2279160ad277d994501074439369dfa5d3878d7985957dfb46080ec6509(
    value: typing.Optional[ReportTimeRange],
) -> None:
    """Type checking stubs"""
    pass
