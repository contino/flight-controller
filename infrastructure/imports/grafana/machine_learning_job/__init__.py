'''
# `grafana_machine_learning_job`

Refer to the Terraform Registory for docs: [`grafana_machine_learning_job`](https://www.terraform.io/docs/providers/grafana/r/machine_learning_job).
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


class MachineLearningJob(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.machineLearningJob.MachineLearningJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job grafana_machine_learning_job}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        datasource_type: builtins.str,
        metric: builtins.str,
        name: builtins.str,
        query_params: typing.Mapping[builtins.str, builtins.str],
        datasource_id: typing.Optional[jsii.Number] = None,
        datasource_uid: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        holidays: typing.Optional[typing.Sequence[builtins.str]] = None,
        hyper_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        interval: typing.Optional[jsii.Number] = None,
        training_window: typing.Optional[jsii.Number] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job grafana_machine_learning_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datasource_type: The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_type MachineLearningJob#datasource_type}
        :param metric: The metric used to query the job results. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#metric MachineLearningJob#metric}
        :param name: The name of the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#name MachineLearningJob#name}
        :param query_params: An object representing the query params to query Grafana with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#query_params MachineLearningJob#query_params}
        :param datasource_id: The id of the datasource to query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_id MachineLearningJob#datasource_id}
        :param datasource_uid: The uid of the datasource to query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_uid MachineLearningJob#datasource_uid}
        :param description: A description of the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#description MachineLearningJob#description}
        :param holidays: A list of holiday IDs or names to take into account when training the model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#holidays MachineLearningJob#holidays}
        :param hyper_params: The hyperparameters used to fine tune the algorithm. See https://grafana.com/docs/grafana-cloud/machine-learning/models/ for the full list of available hyperparameters. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#hyper_params MachineLearningJob#hyper_params}
        :param interval: The data interval in seconds to train the data on. Defaults to ``300``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#interval MachineLearningJob#interval}
        :param training_window: The data interval in seconds to train the data on. Defaults to ``7776000``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#training_window MachineLearningJob#training_window}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83fd421b47bf69b3f670a44ac886282b5c4c2ac7716c310b725eace1fc0030b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = MachineLearningJobConfig(
            datasource_type=datasource_type,
            metric=metric,
            name=name,
            query_params=query_params,
            datasource_id=datasource_id,
            datasource_uid=datasource_uid,
            description=description,
            holidays=holidays,
            hyper_params=hyper_params,
            interval=interval,
            training_window=training_window,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetDatasourceId")
    def reset_datasource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasourceId", []))

    @jsii.member(jsii_name="resetDatasourceUid")
    def reset_datasource_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasourceUid", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetHolidays")
    def reset_holidays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHolidays", []))

    @jsii.member(jsii_name="resetHyperParams")
    def reset_hyper_params(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHyperParams", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetTrainingWindow")
    def reset_training_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrainingWindow", []))

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
    @jsii.member(jsii_name="datasourceIdInput")
    def datasource_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "datasourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasourceTypeInput")
    def datasource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="datasourceUidInput")
    def datasource_uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasourceUidInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="holidaysInput")
    def holidays_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "holidaysInput"))

    @builtins.property
    @jsii.member(jsii_name="hyperParamsInput")
    def hyper_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "hyperParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="queryParamsInput")
    def query_params_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "queryParamsInput"))

    @builtins.property
    @jsii.member(jsii_name="trainingWindowInput")
    def training_window_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "trainingWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="datasourceId")
    def datasource_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "datasourceId"))

    @datasource_id.setter
    def datasource_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6926fc671414866af06fd3122729d14dc1563d07960312035af980c2df9774c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasourceId", value)

    @builtins.property
    @jsii.member(jsii_name="datasourceType")
    def datasource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasourceType"))

    @datasource_type.setter
    def datasource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50d850e8b67ca8b950a9738160a8acf67c3bf8755099abbb2c4303d3be5fe389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasourceType", value)

    @builtins.property
    @jsii.member(jsii_name="datasourceUid")
    def datasource_uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasourceUid"))

    @datasource_uid.setter
    def datasource_uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ce6ca368c4e683f994d727fea2ad338d74761e88dda14454318667673c6bb6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasourceUid", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca73ab2f04f2eb381924c1350da1d4244db83adad85cba8bf33ec20c818589e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="holidays")
    def holidays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "holidays"))

    @holidays.setter
    def holidays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__957c6c7d7f35a6764ad7d03fb291a13c3e5f1198e7f978b41712859c4074875b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "holidays", value)

    @builtins.property
    @jsii.member(jsii_name="hyperParams")
    def hyper_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "hyperParams"))

    @hyper_params.setter
    def hyper_params(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9514e85ea91e65b30386d6550df660e9aa8d1bdbb8789bab8b5e3e1cabd562f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hyperParams", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf74856668bd913d093699355bb62897c245b73aed89b8a7ec4dd448d748692d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metric"))

    @metric.setter
    def metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c696c619371201a41bf36318cc4e78fb4db8a98e4780427ae19d59c6f7bc0d27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metric", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3302b31f99aafd72b9019a4c1701b8adef0bbb134cb7af49c14fe6f4feed088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryParams")
    def query_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "queryParams"))

    @query_params.setter
    def query_params(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94a3ac4ceeba196996dec00a2537bf0c017fc451964f1d9b9e8b3e4b83b2c6ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryParams", value)

    @builtins.property
    @jsii.member(jsii_name="trainingWindow")
    def training_window(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "trainingWindow"))

    @training_window.setter
    def training_window(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad95437ac4fcc2670c5ee2b9c0cae5334b7264ba80f10b3f60a5750470c93284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trainingWindow", value)


@jsii.data_type(
    jsii_type="grafana.machineLearningJob.MachineLearningJobConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datasource_type": "datasourceType",
        "metric": "metric",
        "name": "name",
        "query_params": "queryParams",
        "datasource_id": "datasourceId",
        "datasource_uid": "datasourceUid",
        "description": "description",
        "holidays": "holidays",
        "hyper_params": "hyperParams",
        "interval": "interval",
        "training_window": "trainingWindow",
    },
)
class MachineLearningJobConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        datasource_type: builtins.str,
        metric: builtins.str,
        name: builtins.str,
        query_params: typing.Mapping[builtins.str, builtins.str],
        datasource_id: typing.Optional[jsii.Number] = None,
        datasource_uid: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        holidays: typing.Optional[typing.Sequence[builtins.str]] = None,
        hyper_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        interval: typing.Optional[jsii.Number] = None,
        training_window: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datasource_type: The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_type MachineLearningJob#datasource_type}
        :param metric: The metric used to query the job results. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#metric MachineLearningJob#metric}
        :param name: The name of the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#name MachineLearningJob#name}
        :param query_params: An object representing the query params to query Grafana with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#query_params MachineLearningJob#query_params}
        :param datasource_id: The id of the datasource to query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_id MachineLearningJob#datasource_id}
        :param datasource_uid: The uid of the datasource to query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_uid MachineLearningJob#datasource_uid}
        :param description: A description of the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#description MachineLearningJob#description}
        :param holidays: A list of holiday IDs or names to take into account when training the model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#holidays MachineLearningJob#holidays}
        :param hyper_params: The hyperparameters used to fine tune the algorithm. See https://grafana.com/docs/grafana-cloud/machine-learning/models/ for the full list of available hyperparameters. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#hyper_params MachineLearningJob#hyper_params}
        :param interval: The data interval in seconds to train the data on. Defaults to ``300``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#interval MachineLearningJob#interval}
        :param training_window: The data interval in seconds to train the data on. Defaults to ``7776000``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#training_window MachineLearningJob#training_window}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__907ca0a8b6bbe23c62da1103e8660dad0ce7441c649476bb282df89ea8a64994)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datasource_type", value=datasource_type, expected_type=type_hints["datasource_type"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_params", value=query_params, expected_type=type_hints["query_params"])
            check_type(argname="argument datasource_id", value=datasource_id, expected_type=type_hints["datasource_id"])
            check_type(argname="argument datasource_uid", value=datasource_uid, expected_type=type_hints["datasource_uid"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument holidays", value=holidays, expected_type=type_hints["holidays"])
            check_type(argname="argument hyper_params", value=hyper_params, expected_type=type_hints["hyper_params"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument training_window", value=training_window, expected_type=type_hints["training_window"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datasource_type": datasource_type,
            "metric": metric,
            "name": name,
            "query_params": query_params,
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
        if datasource_id is not None:
            self._values["datasource_id"] = datasource_id
        if datasource_uid is not None:
            self._values["datasource_uid"] = datasource_uid
        if description is not None:
            self._values["description"] = description
        if holidays is not None:
            self._values["holidays"] = holidays
        if hyper_params is not None:
            self._values["hyper_params"] = hyper_params
        if interval is not None:
            self._values["interval"] = interval
        if training_window is not None:
            self._values["training_window"] = training_window

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
    def datasource_type(self) -> builtins.str:
        '''The type of datasource being queried. Currently allowed values are prometheus, graphite, loki, postgres, and datadog.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_type MachineLearningJob#datasource_type}
        '''
        result = self._values.get("datasource_type")
        assert result is not None, "Required property 'datasource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric(self) -> builtins.str:
        '''The metric used to query the job results.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#metric MachineLearningJob#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#name MachineLearningJob#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_params(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''An object representing the query params to query Grafana with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#query_params MachineLearningJob#query_params}
        '''
        result = self._values.get("query_params")
        assert result is not None, "Required property 'query_params' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def datasource_id(self) -> typing.Optional[jsii.Number]:
        '''The id of the datasource to query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_id MachineLearningJob#datasource_id}
        '''
        result = self._values.get("datasource_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def datasource_uid(self) -> typing.Optional[builtins.str]:
        '''The uid of the datasource to query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#datasource_uid MachineLearningJob#datasource_uid}
        '''
        result = self._values.get("datasource_uid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#description MachineLearningJob#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def holidays(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of holiday IDs or names to take into account when training the model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#holidays MachineLearningJob#holidays}
        '''
        result = self._values.get("holidays")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hyper_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The hyperparameters used to fine tune the algorithm.

        See https://grafana.com/docs/grafana-cloud/machine-learning/models/ for the full list of available hyperparameters. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#hyper_params MachineLearningJob#hyper_params}
        '''
        result = self._values.get("hyper_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def interval(self) -> typing.Optional[jsii.Number]:
        '''The data interval in seconds to train the data on. Defaults to ``300``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#interval MachineLearningJob#interval}
        '''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def training_window(self) -> typing.Optional[jsii.Number]:
        '''The data interval in seconds to train the data on. Defaults to ``7776000``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/machine_learning_job#training_window MachineLearningJob#training_window}
        '''
        result = self._values.get("training_window")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MachineLearningJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MachineLearningJob",
    "MachineLearningJobConfig",
]

publication.publish()

def _typecheckingstub__b83fd421b47bf69b3f670a44ac886282b5c4c2ac7716c310b725eace1fc0030b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    datasource_type: builtins.str,
    metric: builtins.str,
    name: builtins.str,
    query_params: typing.Mapping[builtins.str, builtins.str],
    datasource_id: typing.Optional[jsii.Number] = None,
    datasource_uid: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    holidays: typing.Optional[typing.Sequence[builtins.str]] = None,
    hyper_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    interval: typing.Optional[jsii.Number] = None,
    training_window: typing.Optional[jsii.Number] = None,
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

def _typecheckingstub__6926fc671414866af06fd3122729d14dc1563d07960312035af980c2df9774c7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50d850e8b67ca8b950a9738160a8acf67c3bf8755099abbb2c4303d3be5fe389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ce6ca368c4e683f994d727fea2ad338d74761e88dda14454318667673c6bb6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca73ab2f04f2eb381924c1350da1d4244db83adad85cba8bf33ec20c818589e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__957c6c7d7f35a6764ad7d03fb291a13c3e5f1198e7f978b41712859c4074875b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9514e85ea91e65b30386d6550df660e9aa8d1bdbb8789bab8b5e3e1cabd562f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf74856668bd913d093699355bb62897c245b73aed89b8a7ec4dd448d748692d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c696c619371201a41bf36318cc4e78fb4db8a98e4780427ae19d59c6f7bc0d27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3302b31f99aafd72b9019a4c1701b8adef0bbb134cb7af49c14fe6f4feed088(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a3ac4ceeba196996dec00a2537bf0c017fc451964f1d9b9e8b3e4b83b2c6ac(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad95437ac4fcc2670c5ee2b9c0cae5334b7264ba80f10b3f60a5750470c93284(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__907ca0a8b6bbe23c62da1103e8660dad0ce7441c649476bb282df89ea8a64994(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    datasource_type: builtins.str,
    metric: builtins.str,
    name: builtins.str,
    query_params: typing.Mapping[builtins.str, builtins.str],
    datasource_id: typing.Optional[jsii.Number] = None,
    datasource_uid: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    holidays: typing.Optional[typing.Sequence[builtins.str]] = None,
    hyper_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    interval: typing.Optional[jsii.Number] = None,
    training_window: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
