'''
# `grafana_contact_point`

Refer to the Terraform Registory for docs: [`grafana_contact_point`](https://www.terraform.io/docs/providers/grafana/r/contact_point).
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


class ContactPoint(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPoint",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/contact_point grafana_contact_point}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        alertmanager: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointAlertmanager", typing.Dict[builtins.str, typing.Any]]]]] = None,
        dingding: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointDingding", typing.Dict[builtins.str, typing.Any]]]]] = None,
        discord: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointDiscord", typing.Dict[builtins.str, typing.Any]]]]] = None,
        email: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointEmail", typing.Dict[builtins.str, typing.Any]]]]] = None,
        googlechat: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointGooglechat", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointKafka", typing.Dict[builtins.str, typing.Any]]]]] = None,
        opsgenie: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointOpsgenie", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pagerduty: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointPagerduty", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pushover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointPushover", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sensugo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointSensugo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointSlack", typing.Dict[builtins.str, typing.Any]]]]] = None,
        teams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointTeams", typing.Dict[builtins.str, typing.Any]]]]] = None,
        telegram: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointTelegram", typing.Dict[builtins.str, typing.Any]]]]] = None,
        threema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointThreema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        victorops: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointVictorops", typing.Dict[builtins.str, typing.Any]]]]] = None,
        webhook: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointWebhook", typing.Dict[builtins.str, typing.Any]]]]] = None,
        wecom: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointWecom", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/contact_point grafana_contact_point} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the contact point. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#name ContactPoint#name}
        :param alertmanager: alertmanager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#alertmanager ContactPoint#alertmanager}
        :param dingding: dingding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#dingding ContactPoint#dingding}
        :param discord: discord block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#discord ContactPoint#discord}
        :param email: email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#email ContactPoint#email}
        :param googlechat: googlechat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#googlechat ContactPoint#googlechat}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#id ContactPoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka: kafka block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#kafka ContactPoint#kafka}
        :param opsgenie: opsgenie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#opsgenie ContactPoint#opsgenie}
        :param pagerduty: pagerduty block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#pagerduty ContactPoint#pagerduty}
        :param pushover: pushover block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#pushover ContactPoint#pushover}
        :param sensugo: sensugo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#sensugo ContactPoint#sensugo}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#slack ContactPoint#slack}
        :param teams: teams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#teams ContactPoint#teams}
        :param telegram: telegram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#telegram ContactPoint#telegram}
        :param threema: threema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#threema ContactPoint#threema}
        :param victorops: victorops block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#victorops ContactPoint#victorops}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#webhook ContactPoint#webhook}
        :param wecom: wecom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#wecom ContactPoint#wecom}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc80a278584220f835a99bc85f94cf459424ad6764b82be466c0c73f6188141)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContactPointConfig(
            name=name,
            alertmanager=alertmanager,
            dingding=dingding,
            discord=discord,
            email=email,
            googlechat=googlechat,
            id=id,
            kafka=kafka,
            opsgenie=opsgenie,
            pagerduty=pagerduty,
            pushover=pushover,
            sensugo=sensugo,
            slack=slack,
            teams=teams,
            telegram=telegram,
            threema=threema,
            victorops=victorops,
            webhook=webhook,
            wecom=wecom,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlertmanager")
    def put_alertmanager(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointAlertmanager", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ea99c45a08226c084235dd59d275eef28bf09cc6b967a7de354963ec187af4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlertmanager", [value]))

    @jsii.member(jsii_name="putDingding")
    def put_dingding(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointDingding", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b33e7150102067ecc09e2ae98297edb45b1489dd536aff0dfe9a9cef0ebdded2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDingding", [value]))

    @jsii.member(jsii_name="putDiscord")
    def put_discord(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointDiscord", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ed28e02536b2823d3866f10a36ddb70d73c0c7f750f31d0562f22eb77d0c23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDiscord", [value]))

    @jsii.member(jsii_name="putEmail")
    def put_email(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointEmail", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc27e2f0bbb735a944dd870351565aae4f2d2e297b6e4573beb8e404e681f85e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmail", [value]))

    @jsii.member(jsii_name="putGooglechat")
    def put_googlechat(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointGooglechat", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7083efbc23bc53b9088417a12ada89b64d7f96374199e200739a5a3a6ef9749)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGooglechat", [value]))

    @jsii.member(jsii_name="putKafka")
    def put_kafka(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointKafka", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b2c9d273ade5d88a5e720e81147878712602765ea1bfac1fcfcad1830d66919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKafka", [value]))

    @jsii.member(jsii_name="putOpsgenie")
    def put_opsgenie(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointOpsgenie", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed7a65acc24519808577034d4cdfbc14b3097a2be985a2e010f552e5d63f5124)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOpsgenie", [value]))

    @jsii.member(jsii_name="putPagerduty")
    def put_pagerduty(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointPagerduty", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a11f89a0d4f0ffdb4ef243c8b9ad2c3dcc51a513c130e7020900c48a14af1ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPagerduty", [value]))

    @jsii.member(jsii_name="putPushover")
    def put_pushover(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointPushover", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ca1d086dd3137464e5be1e9f48c77bb9fd6e3f4641588d1b4a6a5584421245d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPushover", [value]))

    @jsii.member(jsii_name="putSensugo")
    def put_sensugo(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointSensugo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6ca755cbd0c328d0ac7ed428b82bb8711247be30c01f826e7e7273f2ab28f82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSensugo", [value]))

    @jsii.member(jsii_name="putSlack")
    def put_slack(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointSlack", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0133b1ee9714baa647af3a78da9fde3d0805a3005fa273d89a416b41a3eb77a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSlack", [value]))

    @jsii.member(jsii_name="putTeams")
    def put_teams(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointTeams", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b7c90bd438497d1da51e4e0ccccc08f305690f979bda49957c8989c9f1c78e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTeams", [value]))

    @jsii.member(jsii_name="putTelegram")
    def put_telegram(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointTelegram", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2e43c74ea7453d857dbbcaffb8b4435590e34546de40655abdd019a21147f31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTelegram", [value]))

    @jsii.member(jsii_name="putThreema")
    def put_threema(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointThreema", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__351f62c78ba3cb8e420931ae7bad38740eaadf5c5feb3f8765c91823efa1614c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThreema", [value]))

    @jsii.member(jsii_name="putVictorops")
    def put_victorops(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointVictorops", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caad4350a0366229f4ba9fd33a49d39011ab1e2f4ffa344b4a6e348b36738c83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVictorops", [value]))

    @jsii.member(jsii_name="putWebhook")
    def put_webhook(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointWebhook", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f73486e4d3b39d524d216fbbd11b45ec0e1b05f09aa9ed4e70f47669f0fb81dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebhook", [value]))

    @jsii.member(jsii_name="putWecom")
    def put_wecom(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointWecom", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f8bc15393c591689eb184be0da383312d7931241511449e93e4a42cecfe3ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWecom", [value]))

    @jsii.member(jsii_name="resetAlertmanager")
    def reset_alertmanager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlertmanager", []))

    @jsii.member(jsii_name="resetDingding")
    def reset_dingding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDingding", []))

    @jsii.member(jsii_name="resetDiscord")
    def reset_discord(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiscord", []))

    @jsii.member(jsii_name="resetEmail")
    def reset_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmail", []))

    @jsii.member(jsii_name="resetGooglechat")
    def reset_googlechat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGooglechat", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKafka")
    def reset_kafka(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKafka", []))

    @jsii.member(jsii_name="resetOpsgenie")
    def reset_opsgenie(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpsgenie", []))

    @jsii.member(jsii_name="resetPagerduty")
    def reset_pagerduty(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPagerduty", []))

    @jsii.member(jsii_name="resetPushover")
    def reset_pushover(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPushover", []))

    @jsii.member(jsii_name="resetSensugo")
    def reset_sensugo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSensugo", []))

    @jsii.member(jsii_name="resetSlack")
    def reset_slack(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlack", []))

    @jsii.member(jsii_name="resetTeams")
    def reset_teams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTeams", []))

    @jsii.member(jsii_name="resetTelegram")
    def reset_telegram(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTelegram", []))

    @jsii.member(jsii_name="resetThreema")
    def reset_threema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThreema", []))

    @jsii.member(jsii_name="resetVictorops")
    def reset_victorops(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVictorops", []))

    @jsii.member(jsii_name="resetWebhook")
    def reset_webhook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebhook", []))

    @jsii.member(jsii_name="resetWecom")
    def reset_wecom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWecom", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alertmanager")
    def alertmanager(self) -> "ContactPointAlertmanagerList":
        return typing.cast("ContactPointAlertmanagerList", jsii.get(self, "alertmanager"))

    @builtins.property
    @jsii.member(jsii_name="dingding")
    def dingding(self) -> "ContactPointDingdingList":
        return typing.cast("ContactPointDingdingList", jsii.get(self, "dingding"))

    @builtins.property
    @jsii.member(jsii_name="discord")
    def discord(self) -> "ContactPointDiscordList":
        return typing.cast("ContactPointDiscordList", jsii.get(self, "discord"))

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> "ContactPointEmailList":
        return typing.cast("ContactPointEmailList", jsii.get(self, "email"))

    @builtins.property
    @jsii.member(jsii_name="googlechat")
    def googlechat(self) -> "ContactPointGooglechatList":
        return typing.cast("ContactPointGooglechatList", jsii.get(self, "googlechat"))

    @builtins.property
    @jsii.member(jsii_name="kafka")
    def kafka(self) -> "ContactPointKafkaList":
        return typing.cast("ContactPointKafkaList", jsii.get(self, "kafka"))

    @builtins.property
    @jsii.member(jsii_name="opsgenie")
    def opsgenie(self) -> "ContactPointOpsgenieList":
        return typing.cast("ContactPointOpsgenieList", jsii.get(self, "opsgenie"))

    @builtins.property
    @jsii.member(jsii_name="pagerduty")
    def pagerduty(self) -> "ContactPointPagerdutyList":
        return typing.cast("ContactPointPagerdutyList", jsii.get(self, "pagerduty"))

    @builtins.property
    @jsii.member(jsii_name="pushover")
    def pushover(self) -> "ContactPointPushoverList":
        return typing.cast("ContactPointPushoverList", jsii.get(self, "pushover"))

    @builtins.property
    @jsii.member(jsii_name="sensugo")
    def sensugo(self) -> "ContactPointSensugoList":
        return typing.cast("ContactPointSensugoList", jsii.get(self, "sensugo"))

    @builtins.property
    @jsii.member(jsii_name="slack")
    def slack(self) -> "ContactPointSlackList":
        return typing.cast("ContactPointSlackList", jsii.get(self, "slack"))

    @builtins.property
    @jsii.member(jsii_name="teams")
    def teams(self) -> "ContactPointTeamsList":
        return typing.cast("ContactPointTeamsList", jsii.get(self, "teams"))

    @builtins.property
    @jsii.member(jsii_name="telegram")
    def telegram(self) -> "ContactPointTelegramList":
        return typing.cast("ContactPointTelegramList", jsii.get(self, "telegram"))

    @builtins.property
    @jsii.member(jsii_name="threema")
    def threema(self) -> "ContactPointThreemaList":
        return typing.cast("ContactPointThreemaList", jsii.get(self, "threema"))

    @builtins.property
    @jsii.member(jsii_name="victorops")
    def victorops(self) -> "ContactPointVictoropsList":
        return typing.cast("ContactPointVictoropsList", jsii.get(self, "victorops"))

    @builtins.property
    @jsii.member(jsii_name="webhook")
    def webhook(self) -> "ContactPointWebhookList":
        return typing.cast("ContactPointWebhookList", jsii.get(self, "webhook"))

    @builtins.property
    @jsii.member(jsii_name="wecom")
    def wecom(self) -> "ContactPointWecomList":
        return typing.cast("ContactPointWecomList", jsii.get(self, "wecom"))

    @builtins.property
    @jsii.member(jsii_name="alertmanagerInput")
    def alertmanager_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointAlertmanager"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointAlertmanager"]]], jsii.get(self, "alertmanagerInput"))

    @builtins.property
    @jsii.member(jsii_name="dingdingInput")
    def dingding_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDingding"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDingding"]]], jsii.get(self, "dingdingInput"))

    @builtins.property
    @jsii.member(jsii_name="discordInput")
    def discord_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDiscord"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDiscord"]]], jsii.get(self, "discordInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointEmail"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointEmail"]]], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="googlechatInput")
    def googlechat_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointGooglechat"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointGooglechat"]]], jsii.get(self, "googlechatInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaInput")
    def kafka_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointKafka"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointKafka"]]], jsii.get(self, "kafkaInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="opsgenieInput")
    def opsgenie_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointOpsgenie"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointOpsgenie"]]], jsii.get(self, "opsgenieInput"))

    @builtins.property
    @jsii.member(jsii_name="pagerdutyInput")
    def pagerduty_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPagerduty"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPagerduty"]]], jsii.get(self, "pagerdutyInput"))

    @builtins.property
    @jsii.member(jsii_name="pushoverInput")
    def pushover_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPushover"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPushover"]]], jsii.get(self, "pushoverInput"))

    @builtins.property
    @jsii.member(jsii_name="sensugoInput")
    def sensugo_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSensugo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSensugo"]]], jsii.get(self, "sensugoInput"))

    @builtins.property
    @jsii.member(jsii_name="slackInput")
    def slack_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSlack"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSlack"]]], jsii.get(self, "slackInput"))

    @builtins.property
    @jsii.member(jsii_name="teamsInput")
    def teams_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTeams"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTeams"]]], jsii.get(self, "teamsInput"))

    @builtins.property
    @jsii.member(jsii_name="telegramInput")
    def telegram_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTelegram"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTelegram"]]], jsii.get(self, "telegramInput"))

    @builtins.property
    @jsii.member(jsii_name="threemaInput")
    def threema_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointThreema"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointThreema"]]], jsii.get(self, "threemaInput"))

    @builtins.property
    @jsii.member(jsii_name="victoropsInput")
    def victorops_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointVictorops"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointVictorops"]]], jsii.get(self, "victoropsInput"))

    @builtins.property
    @jsii.member(jsii_name="webhookInput")
    def webhook_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWebhook"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWebhook"]]], jsii.get(self, "webhookInput"))

    @builtins.property
    @jsii.member(jsii_name="wecomInput")
    def wecom_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWecom"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWecom"]]], jsii.get(self, "wecomInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b8de0c515f98a91b1e5e7691e8bf219173ccfd643f387ec540b8c8bdcabf3ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dec3fb2b5421a1a161b4bc6ed518741c32fa8514c16e8e9c75675c668f5ff22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointAlertmanager",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "basic_auth_password": "basicAuthPassword",
        "basic_auth_user": "basicAuthUser",
        "disable_resolve_message": "disableResolveMessage",
        "settings": "settings",
    },
)
class ContactPointAlertmanager:
    def __init__(
        self,
        *,
        url: builtins.str,
        basic_auth_password: typing.Optional[builtins.str] = None,
        basic_auth_user: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: The URL of the Alertmanager instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param basic_auth_password: The password component of the basic auth credentials to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_password ContactPoint#basic_auth_password}
        :param basic_auth_user: The username component of the basic auth credentials to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_user ContactPoint#basic_auth_user}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a55bcd5375b4ee9e72866c4580e189b78b7c8c0ab82e321b1df0614a2676bbf)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument basic_auth_password", value=basic_auth_password, expected_type=type_hints["basic_auth_password"])
            check_type(argname="argument basic_auth_user", value=basic_auth_user, expected_type=type_hints["basic_auth_user"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if basic_auth_password is not None:
            self._values["basic_auth_password"] = basic_auth_password
        if basic_auth_user is not None:
            self._values["basic_auth_user"] = basic_auth_user
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL of the Alertmanager instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic_auth_password(self) -> typing.Optional[builtins.str]:
        '''The password component of the basic auth credentials to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_password ContactPoint#basic_auth_password}
        '''
        result = self._values.get("basic_auth_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_auth_user(self) -> typing.Optional[builtins.str]:
        '''The username component of the basic auth credentials to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_user ContactPoint#basic_auth_user}
        '''
        result = self._values.get("basic_auth_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointAlertmanager(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointAlertmanagerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointAlertmanagerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__787a4cbd1c0469cd309ddb7462830d9c358b20bd7c95a6164e33e81fb0177ded)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointAlertmanagerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1424d08f7c770acfc30e5c5c416b79a185fba88f160d0265ca321d367e37b5c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointAlertmanagerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9281650a84e647e4acd3a6efab6f717fad969715e1d85996a6f57bf2e0a9bc94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a58a4a5802eae1692fbb76d1612767c7ce4e5b1ac4bb334bf788b917597e482a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7f3a9d18c41ca701da1e74e9a95cd5f4a9d17cb050da41beb2f9023338c46d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointAlertmanager]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointAlertmanager]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointAlertmanager]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8ec8a4d4a584ee15553a48c171852f0d5d6af4b548e362c69187cbbf79444c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointAlertmanagerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointAlertmanagerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__712dc88141e23acea4244721f2435ef95adb2c61962240cc8d5526af6415c50f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBasicAuthPassword")
    def reset_basic_auth_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthPassword", []))

    @jsii.member(jsii_name="resetBasicAuthUser")
    def reset_basic_auth_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthUser", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthPasswordInput")
    def basic_auth_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthUserInput")
    def basic_auth_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthUserInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthPassword")
    def basic_auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthPassword"))

    @basic_auth_password.setter
    def basic_auth_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77b39767906afe43281da628c4a9557525b572b0011907f5f66b98daadaca958)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthPassword", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthUser")
    def basic_auth_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthUser"))

    @basic_auth_user.setter
    def basic_auth_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f443a6c7183bd7dab1b3a0e5ba38c395fb4da1654736e2e46e8ee3357ac1134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthUser", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b63c0ba15c07fa75bc0417f0119d773c2e6da5e8980223b5b0252e826ee8f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ab101edd6e2518a44d2d0cfc140033ed3aaf97a6ce3a4d6d2501fe5ffa11b98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a2fb4a6bdc7b13dc683f58fd06af57a2b719a0b4ab61953ac6f3467d549bd99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointAlertmanager, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointAlertmanager, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointAlertmanager, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecd8f02d4317bad2d39c1ff66ac2544cfc8b5368db83f2d08cfbeba85db33895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointConfig",
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
        "alertmanager": "alertmanager",
        "dingding": "dingding",
        "discord": "discord",
        "email": "email",
        "googlechat": "googlechat",
        "id": "id",
        "kafka": "kafka",
        "opsgenie": "opsgenie",
        "pagerduty": "pagerduty",
        "pushover": "pushover",
        "sensugo": "sensugo",
        "slack": "slack",
        "teams": "teams",
        "telegram": "telegram",
        "threema": "threema",
        "victorops": "victorops",
        "webhook": "webhook",
        "wecom": "wecom",
    },
)
class ContactPointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        alertmanager: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointAlertmanager, typing.Dict[builtins.str, typing.Any]]]]] = None,
        dingding: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointDingding", typing.Dict[builtins.str, typing.Any]]]]] = None,
        discord: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointDiscord", typing.Dict[builtins.str, typing.Any]]]]] = None,
        email: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointEmail", typing.Dict[builtins.str, typing.Any]]]]] = None,
        googlechat: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointGooglechat", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointKafka", typing.Dict[builtins.str, typing.Any]]]]] = None,
        opsgenie: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointOpsgenie", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pagerduty: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointPagerduty", typing.Dict[builtins.str, typing.Any]]]]] = None,
        pushover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointPushover", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sensugo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointSensugo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointSlack", typing.Dict[builtins.str, typing.Any]]]]] = None,
        teams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointTeams", typing.Dict[builtins.str, typing.Any]]]]] = None,
        telegram: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointTelegram", typing.Dict[builtins.str, typing.Any]]]]] = None,
        threema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointThreema", typing.Dict[builtins.str, typing.Any]]]]] = None,
        victorops: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointVictorops", typing.Dict[builtins.str, typing.Any]]]]] = None,
        webhook: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointWebhook", typing.Dict[builtins.str, typing.Any]]]]] = None,
        wecom: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["ContactPointWecom", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the contact point. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#name ContactPoint#name}
        :param alertmanager: alertmanager block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#alertmanager ContactPoint#alertmanager}
        :param dingding: dingding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#dingding ContactPoint#dingding}
        :param discord: discord block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#discord ContactPoint#discord}
        :param email: email block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#email ContactPoint#email}
        :param googlechat: googlechat block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#googlechat ContactPoint#googlechat}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#id ContactPoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka: kafka block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#kafka ContactPoint#kafka}
        :param opsgenie: opsgenie block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#opsgenie ContactPoint#opsgenie}
        :param pagerduty: pagerduty block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#pagerduty ContactPoint#pagerduty}
        :param pushover: pushover block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#pushover ContactPoint#pushover}
        :param sensugo: sensugo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#sensugo ContactPoint#sensugo}
        :param slack: slack block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#slack ContactPoint#slack}
        :param teams: teams block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#teams ContactPoint#teams}
        :param telegram: telegram block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#telegram ContactPoint#telegram}
        :param threema: threema block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#threema ContactPoint#threema}
        :param victorops: victorops block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#victorops ContactPoint#victorops}
        :param webhook: webhook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#webhook ContactPoint#webhook}
        :param wecom: wecom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#wecom ContactPoint#wecom}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fc238d2d24ae713a63a82f534398dd72797dd983125d560c8132cee41237621)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alertmanager", value=alertmanager, expected_type=type_hints["alertmanager"])
            check_type(argname="argument dingding", value=dingding, expected_type=type_hints["dingding"])
            check_type(argname="argument discord", value=discord, expected_type=type_hints["discord"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument googlechat", value=googlechat, expected_type=type_hints["googlechat"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kafka", value=kafka, expected_type=type_hints["kafka"])
            check_type(argname="argument opsgenie", value=opsgenie, expected_type=type_hints["opsgenie"])
            check_type(argname="argument pagerduty", value=pagerduty, expected_type=type_hints["pagerduty"])
            check_type(argname="argument pushover", value=pushover, expected_type=type_hints["pushover"])
            check_type(argname="argument sensugo", value=sensugo, expected_type=type_hints["sensugo"])
            check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
            check_type(argname="argument teams", value=teams, expected_type=type_hints["teams"])
            check_type(argname="argument telegram", value=telegram, expected_type=type_hints["telegram"])
            check_type(argname="argument threema", value=threema, expected_type=type_hints["threema"])
            check_type(argname="argument victorops", value=victorops, expected_type=type_hints["victorops"])
            check_type(argname="argument webhook", value=webhook, expected_type=type_hints["webhook"])
            check_type(argname="argument wecom", value=wecom, expected_type=type_hints["wecom"])
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
        if alertmanager is not None:
            self._values["alertmanager"] = alertmanager
        if dingding is not None:
            self._values["dingding"] = dingding
        if discord is not None:
            self._values["discord"] = discord
        if email is not None:
            self._values["email"] = email
        if googlechat is not None:
            self._values["googlechat"] = googlechat
        if id is not None:
            self._values["id"] = id
        if kafka is not None:
            self._values["kafka"] = kafka
        if opsgenie is not None:
            self._values["opsgenie"] = opsgenie
        if pagerduty is not None:
            self._values["pagerduty"] = pagerduty
        if pushover is not None:
            self._values["pushover"] = pushover
        if sensugo is not None:
            self._values["sensugo"] = sensugo
        if slack is not None:
            self._values["slack"] = slack
        if teams is not None:
            self._values["teams"] = teams
        if telegram is not None:
            self._values["telegram"] = telegram
        if threema is not None:
            self._values["threema"] = threema
        if victorops is not None:
            self._values["victorops"] = victorops
        if webhook is not None:
            self._values["webhook"] = webhook
        if wecom is not None:
            self._values["wecom"] = wecom

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
        '''The name of the contact point.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#name ContactPoint#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alertmanager(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointAlertmanager]]]:
        '''alertmanager block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#alertmanager ContactPoint#alertmanager}
        '''
        result = self._values.get("alertmanager")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointAlertmanager]]], result)

    @builtins.property
    def dingding(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDingding"]]]:
        '''dingding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#dingding ContactPoint#dingding}
        '''
        result = self._values.get("dingding")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDingding"]]], result)

    @builtins.property
    def discord(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDiscord"]]]:
        '''discord block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#discord ContactPoint#discord}
        '''
        result = self._values.get("discord")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointDiscord"]]], result)

    @builtins.property
    def email(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointEmail"]]]:
        '''email block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#email ContactPoint#email}
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointEmail"]]], result)

    @builtins.property
    def googlechat(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointGooglechat"]]]:
        '''googlechat block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#googlechat ContactPoint#googlechat}
        '''
        result = self._values.get("googlechat")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointGooglechat"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#id ContactPoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointKafka"]]]:
        '''kafka block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#kafka ContactPoint#kafka}
        '''
        result = self._values.get("kafka")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointKafka"]]], result)

    @builtins.property
    def opsgenie(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointOpsgenie"]]]:
        '''opsgenie block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#opsgenie ContactPoint#opsgenie}
        '''
        result = self._values.get("opsgenie")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointOpsgenie"]]], result)

    @builtins.property
    def pagerduty(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPagerduty"]]]:
        '''pagerduty block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#pagerduty ContactPoint#pagerduty}
        '''
        result = self._values.get("pagerduty")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPagerduty"]]], result)

    @builtins.property
    def pushover(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPushover"]]]:
        '''pushover block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#pushover ContactPoint#pushover}
        '''
        result = self._values.get("pushover")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointPushover"]]], result)

    @builtins.property
    def sensugo(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSensugo"]]]:
        '''sensugo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#sensugo ContactPoint#sensugo}
        '''
        result = self._values.get("sensugo")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSensugo"]]], result)

    @builtins.property
    def slack(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSlack"]]]:
        '''slack block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#slack ContactPoint#slack}
        '''
        result = self._values.get("slack")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointSlack"]]], result)

    @builtins.property
    def teams(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTeams"]]]:
        '''teams block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#teams ContactPoint#teams}
        '''
        result = self._values.get("teams")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTeams"]]], result)

    @builtins.property
    def telegram(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTelegram"]]]:
        '''telegram block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#telegram ContactPoint#telegram}
        '''
        result = self._values.get("telegram")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointTelegram"]]], result)

    @builtins.property
    def threema(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointThreema"]]]:
        '''threema block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#threema ContactPoint#threema}
        '''
        result = self._values.get("threema")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointThreema"]]], result)

    @builtins.property
    def victorops(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointVictorops"]]]:
        '''victorops block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#victorops ContactPoint#victorops}
        '''
        result = self._values.get("victorops")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointVictorops"]]], result)

    @builtins.property
    def webhook(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWebhook"]]]:
        '''webhook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#webhook ContactPoint#webhook}
        '''
        result = self._values.get("webhook")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWebhook"]]], result)

    @builtins.property
    def wecom(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWecom"]]]:
        '''wecom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#wecom ContactPoint#wecom}
        '''
        result = self._values.get("wecom")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["ContactPointWecom"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointDingding",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "message_type": "messageType",
        "settings": "settings",
    },
)
class ContactPointDingding:
    def __init__(
        self,
        *,
        url: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        message_type: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: The DingDing webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param message_type: The format of message to send - either 'link' or 'actionCard'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message_type ContactPoint#message_type}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce516f44549665b4315b456247d27c74345955251c56f3c2f04fc11970bb9976)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument message_type", value=message_type, expected_type=type_hints["message_type"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if message_type is not None:
            self._values["message_type"] = message_type
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def url(self) -> builtins.str:
        '''The DingDing webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message_type(self) -> typing.Optional[builtins.str]:
        '''The format of message to send - either 'link' or 'actionCard'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message_type ContactPoint#message_type}
        '''
        result = self._values.get("message_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointDingding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointDingdingList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointDingdingList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4555b6a362698f0e7adee54cb62a4630d2c426739c4fabe6d612977598f49b04)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointDingdingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd54b50489a894d71683302b297c14c29bd22f81e8579ecab555828ad84c92c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointDingdingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc2964c821eead79201d1a79222dd994e57b01ef6a65418e5167b27704077f40)
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
            type_hints = typing.get_type_hints(_typecheckingstub__541b64beb92df4544a04627bddab27033ca8440b3c0ed3996c57287aa89de6af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0ec16c5dc1c291c74d10878e470ce89be7b5faa9a8b40fb81b45b71c44c6687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDingding]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDingding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDingding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e769eea5ce88d293dae0d05f6636f4658b75171e79ca68b372d83c88bfd9916f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointDingdingOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointDingdingOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__53236e6a22d46894546c39dffcba89d7ce01a222f5b55b31e47c2dc8ac811840)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetMessageType")
    def reset_message_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageType", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageTypeInput")
    def message_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef68a5e71cf871f117b8a8348d801ea6a893fc1c8e1d9c46eebb4eaff3574310)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e45b40b760783d972687e36ace5dc1d17fd2f9947d72a8c03a5915539ea960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="messageType")
    def message_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageType"))

    @message_type.setter
    def message_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97be0bbcea4a294b133063d474a5dddcfeaba87235b1a2d9d489c60144fbb1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageType", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7917ed878ebb1b85e1c9012e401c97acfad81adac7b6e7df2ac80eb4af3cefa3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f015f9d8c31abac25dfd9c4844ba52a7fd170a9c4faa4e6e0ce13e70c8eaf5da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointDingding, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointDingding, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointDingding, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c5547e91268fa7e7688e8a3edc7a7f02e43a86ec4b0b6e60296844b080f26b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointDiscord",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "avatar_url": "avatarUrl",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "settings": "settings",
        "use_discord_username": "useDiscordUsername",
    },
)
class ContactPointDiscord:
    def __init__(
        self,
        *,
        url: builtins.str,
        avatar_url: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        use_discord_username: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param url: The discord webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param avatar_url: The URL of a custom avatar image to use. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#avatar_url ContactPoint#avatar_url}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the message. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param use_discord_username: Whether to use the bot account's plain username instead of "Grafana." Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#use_discord_username ContactPoint#use_discord_username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21671d67f40a466a84a2f3035ac79fc59e94093a011ff82c3acc28487a19183d)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument avatar_url", value=avatar_url, expected_type=type_hints["avatar_url"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument use_discord_username", value=use_discord_username, expected_type=type_hints["use_discord_username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if avatar_url is not None:
            self._values["avatar_url"] = avatar_url
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if settings is not None:
            self._values["settings"] = settings
        if use_discord_username is not None:
            self._values["use_discord_username"] = use_discord_username

    @builtins.property
    def url(self) -> builtins.str:
        '''The discord webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def avatar_url(self) -> typing.Optional[builtins.str]:
        '''The URL of a custom avatar image to use. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#avatar_url ContactPoint#avatar_url}
        '''
        result = self._values.get("avatar_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the message. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def use_discord_username(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to use the bot account's plain username instead of "Grafana." Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#use_discord_username ContactPoint#use_discord_username}
        '''
        result = self._values.get("use_discord_username")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointDiscord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointDiscordList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointDiscordList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__52e0838d90b0135d525487a8ba66b221efb53db3fee976e62b54761f4c1457f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointDiscordOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6d6bb8d4b21727448c36a0df50f70699e388418a3e3d7d011f2d463f2e224bd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointDiscordOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bfe74ca3674361c68320ef85f3f83cf58d143869736dbf0a3f07491ea46e2f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52e34f969a99854b93542c491a74f908384f7ee8542e0cd5a2f2e06283c06a4f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81bc7d622d67c5046cdda5b45fc049b345e11a8737a2bef00cebafe2e2bdfdf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDiscord]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDiscord]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDiscord]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b122d7cb966b212d1f702b3b77389fd28abd729926e30b6c657ca527558e5470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointDiscordOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointDiscordOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9801fe98239e0d4d5ae5c36b796b124da0969e04595dc43289c53db8e1850079)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAvatarUrl")
    def reset_avatar_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAvatarUrl", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetUseDiscordUsername")
    def reset_use_discord_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseDiscordUsername", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="avatarUrlInput")
    def avatar_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "avatarUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="useDiscordUsernameInput")
    def use_discord_username_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "useDiscordUsernameInput"))

    @builtins.property
    @jsii.member(jsii_name="avatarUrl")
    def avatar_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "avatarUrl"))

    @avatar_url.setter
    def avatar_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d39ade1b95bdbe2b2ce4619c7820047a2f842dadb992aef66851d45e7bdca0a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "avatarUrl", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45da6cbb0118057cf8b0af22d9f4d7bfb1ea86f35e389d7bdf29998dc043ff98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053e585030ff736dcfe2031792985c33a4cbcef48118034c6563fab3aebee888)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53dc28b1509caf61cd0296e927837786b4f9994c28ca0a2cc2f7becd7cc189f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f9f66b6aa071258206610439b1414e793e7ada9bda61ff3c07c177c7df7f887)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="useDiscordUsername")
    def use_discord_username(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "useDiscordUsername"))

    @use_discord_username.setter
    def use_discord_username(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dfeda7819bc84fa803c7dadfe9b6abfe19ddd99a538c550edd05b94a048edcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useDiscordUsername", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointDiscord, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointDiscord, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointDiscord, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab021e46a5c17ea868e14254a69a4e6155f014af13d439c46c1aa8298f959032)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointEmail",
    jsii_struct_bases=[],
    name_mapping={
        "addresses": "addresses",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "settings": "settings",
        "single_email": "singleEmail",
        "subject": "subject",
    },
)
class ContactPointEmail:
    def __init__(
        self,
        *,
        addresses: typing.Sequence[builtins.str],
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        single_email: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        subject: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param addresses: The addresses to send emails to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#addresses ContactPoint#addresses}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the email. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param single_email: Whether to send a single email CC'ing all addresses, rather than a separate email to each address. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#single_email ContactPoint#single_email}
        :param subject: The templated subject line of the email. Defaults to ``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#subject ContactPoint#subject}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4269019fc00f0de419e54f9a715b514093644a7445ae21e22c0fbc3d1af5d1cc)
            check_type(argname="argument addresses", value=addresses, expected_type=type_hints["addresses"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument single_email", value=single_email, expected_type=type_hints["single_email"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addresses": addresses,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if settings is not None:
            self._values["settings"] = settings
        if single_email is not None:
            self._values["single_email"] = single_email
        if subject is not None:
            self._values["subject"] = subject

    @builtins.property
    def addresses(self) -> typing.List[builtins.str]:
        '''The addresses to send emails to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#addresses ContactPoint#addresses}
        '''
        result = self._values.get("addresses")
        assert result is not None, "Required property 'addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the email. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def single_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to send a single email CC'ing all addresses, rather than a separate email to each address.

        Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#single_email ContactPoint#single_email}
        '''
        result = self._values.get("single_email")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def subject(self) -> typing.Optional[builtins.str]:
        '''The templated subject line of the email. Defaults to ``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#subject ContactPoint#subject}
        '''
        result = self._values.get("subject")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointEmail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointEmailList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointEmailList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6389b84a77ebc99d771bfbe60b505405344f7823b0ab8d3ec4a601f7d6c93704)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointEmailOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5942df88a19521f466a547daabfbdce46c311d1cd61e2712a4f0238b3cdb6839)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointEmailOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59ce5888ad0deaa2299f34a98e6f041b2ae5b75977809260d7ea65c6f9261992)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8052f2f499c3a1acde8e22d38468d032ab4a3d69c80311eabea71d56b760de4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f85109a5bb1cfc37fc87ca494343d61392793cfff76b6e8ce117fe95313e18b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointEmail]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointEmail]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointEmail]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0d1652dbd5319426e4bcc43b82c6ef9b1cbaaf39fb916d4340f6d4984e00ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointEmailOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointEmailOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30e6620f431920f894215c8ad8bd6552d7dae4612247ba0ca5dc8774e226b0ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetSingleEmail")
    def reset_single_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSingleEmail", []))

    @jsii.member(jsii_name="resetSubject")
    def reset_subject(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubject", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="addressesInput")
    def addresses_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "addressesInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="singleEmailInput")
    def single_email_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "singleEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="addresses")
    def addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "addresses"))

    @addresses.setter
    def addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d138327d63207d481aca0ed04997f493f13549da1052293b0bb3f2ac81543e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "addresses", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71fc7d595793c54532ef31f73f73a03bc4a04b7028f101af5c0e319a62e9cb8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66f614a22ddf5ee222fd8df3499f490721d096d8ea916bf9c83f57904209bec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac9a2e4d23c950fc00aeed0f1e5881cd608e30550b357b6359a6c5d624037203)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="singleEmail")
    def single_email(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "singleEmail"))

    @single_email.setter
    def single_email(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8887bc71fbb87e81f4ff5d87b53fe25f9bcae44326c51a2b2c6375a08c799e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "singleEmail", value)

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subject"))

    @subject.setter
    def subject(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e47e579b80dbf156fb0d38632bf56f717c6418887f894b27fd314c99c542c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subject", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointEmail, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointEmail, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointEmail, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fee4027ecb2f7aa9742f32c6b3733b5e4f0fcf0529b8f034e85bd680098019c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointGooglechat",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "settings": "settings",
    },
)
class ContactPointGooglechat:
    def __init__(
        self,
        *,
        url: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: The Google Chat webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fd10f897fb30618d8b2d7b28d757f43f7452a5e47e6c4df44e85cb171089597)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def url(self) -> builtins.str:
        '''The Google Chat webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointGooglechat(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointGooglechatList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointGooglechatList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__84741afa1cd63474c26359781d4f6762f8c087371ddce116e2cec2ab98ac79ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointGooglechatOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7d2e29e7c4790d34e650e32dc6714963efef968f820ca215c13cdbb916daad6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointGooglechatOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011fa6e2ef0119a4fedf7b82ac376ba2ddb20d6ef3ff94c5f28c8625abf140d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fad18e9c031df9e513bdbfad2fb62616c8b296dfaaddc81071e6ed1a212bb823)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb9eb4076e0948f54f90b11fb6f521429b87a48ab191ffa007aedc366f9dc25e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointGooglechat]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointGooglechat]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointGooglechat]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb56de7ee7f5819e6ab16f307a619ffd4124a2984231976eb594cb8caf09873f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointGooglechatOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointGooglechatOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__27da6acec29e1e9fd40ae3f8fd07c7645af5c96cd173f69fa63f89067ed495f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2985422d6fec16a47665cf52da581062f24dc222feb938dd91068385520e80dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9485dc1d2bed2f29e9331eb760f443f8796a585c62a79daf9413d087eb2fbde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58532e18eb2502cb1130bfa908f522f0628a7c875a89a23e0034695934fbb8fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a9645291af46aa99c0ef127530d701d788dd08525c77baea977e91e73d392e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointGooglechat, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointGooglechat, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointGooglechat, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bdfcfa9e714485b6207111397b2e47836bc326756710bcd4b240ecde99062aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointKafka",
    jsii_struct_bases=[],
    name_mapping={
        "rest_proxy_url": "restProxyUrl",
        "topic": "topic",
        "disable_resolve_message": "disableResolveMessage",
        "settings": "settings",
    },
)
class ContactPointKafka:
    def __init__(
        self,
        *,
        rest_proxy_url: builtins.str,
        topic: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param rest_proxy_url: The URL of the Kafka REST proxy to send requests to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#rest_proxy_url ContactPoint#rest_proxy_url}
        :param topic: The name of the Kafka topic to publish to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#topic ContactPoint#topic}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81c70d241204f0f72bc61170295bf9596aa8879f354ac1e5dd849686ad1d88d4)
            check_type(argname="argument rest_proxy_url", value=rest_proxy_url, expected_type=type_hints["rest_proxy_url"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rest_proxy_url": rest_proxy_url,
            "topic": topic,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def rest_proxy_url(self) -> builtins.str:
        '''The URL of the Kafka REST proxy to send requests to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#rest_proxy_url ContactPoint#rest_proxy_url}
        '''
        result = self._values.get("rest_proxy_url")
        assert result is not None, "Required property 'rest_proxy_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic(self) -> builtins.str:
        '''The name of the Kafka topic to publish to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#topic ContactPoint#topic}
        '''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointKafka(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointKafkaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointKafkaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74417e8aaee577fb3a84cd729d3c8bbc0a66958c9c08f62a1774dd6d062a2299)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointKafkaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2a230f94563884717d49d0dbd0b4976df10674ef4a4dc39d024bb9147960def)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointKafkaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88beb186ca3227615078cde0e2bc17b00bab0177b3c21b16cc0a345269be02be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e78b5d4d57e9695ab9f9ea98caa98d7ed7a29db268f87c4aa068da737f84d90d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__02b28a4469c762e11e28396ff7cee718b452e111c65d60c644b54d54f51baacf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointKafka]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointKafka]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointKafka]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef3b2882182ad6ba05eb600d98d64058a5c101ab5c9562816d4e75398eeb83c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointKafkaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointKafkaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07ceb7f6c511aea551e505345544fb2c8e366e9aff8292edc5de0d2d752d15aa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="restProxyUrlInput")
    def rest_proxy_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "restProxyUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="topicInput")
    def topic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "topicInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dbc20dd772d13ee89b26bc38d988d7950c0a2863f97290119c6d7de7ce2e335)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="restProxyUrl")
    def rest_proxy_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "restProxyUrl"))

    @rest_proxy_url.setter
    def rest_proxy_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aae7e3245797ecf7ff2015e87c6b577915a8215c1421c8d50f3cd4f1bba475d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "restProxyUrl", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d460755cb557f86e97fad8799dabee4d32d2539641269adfe55741cda4e143bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @topic.setter
    def topic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a607971cf377fff009e7d98541ea9d4ca5aceee3f7319ca9bc4998f7114c430c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topic", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointKafka, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointKafka, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointKafka, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0dd6d94776a6032362605642a66469fe6d2dd0a6acb41169f7f8ea7349b7aaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointOpsgenie",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "auto_close": "autoClose",
        "description": "description",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "override_priority": "overridePriority",
        "send_tags_as": "sendTagsAs",
        "settings": "settings",
        "url": "url",
    },
)
class ContactPointOpsgenie:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        auto_close: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        override_priority: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        send_tags_as: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: The OpsGenie API key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_key ContactPoint#api_key}
        :param auto_close: Whether to auto-close alerts in OpsGenie when they resolve in the Alertmanager. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#auto_close ContactPoint#auto_close}
        :param description: A templated high-level description to use for the alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#description ContactPoint#description}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param override_priority: Whether to allow the alert priority to be configured via the value of the ``og_priority`` annotation on the alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#override_priority ContactPoint#override_priority}
        :param send_tags_as: Whether to send annotations to OpsGenie as Tags, Details, or both. Supported values are ``tags``, ``details``, ``both``, or empty to use the default behavior of Tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#send_tags_as ContactPoint#send_tags_as}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param url: Allows customization of the OpsGenie API URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7103341ac45f3fad6897dd639017df76da2e6c2da1db6e0fcbe23d17399e1d26)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument auto_close", value=auto_close, expected_type=type_hints["auto_close"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument override_priority", value=override_priority, expected_type=type_hints["override_priority"])
            check_type(argname="argument send_tags_as", value=send_tags_as, expected_type=type_hints["send_tags_as"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
        }
        if auto_close is not None:
            self._values["auto_close"] = auto_close
        if description is not None:
            self._values["description"] = description
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if override_priority is not None:
            self._values["override_priority"] = override_priority
        if send_tags_as is not None:
            self._values["send_tags_as"] = send_tags_as
        if settings is not None:
            self._values["settings"] = settings
        if url is not None:
            self._values["url"] = url

    @builtins.property
    def api_key(self) -> builtins.str:
        '''The OpsGenie API key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_key ContactPoint#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_close(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to auto-close alerts in OpsGenie when they resolve in the Alertmanager.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#auto_close ContactPoint#auto_close}
        '''
        result = self._values.get("auto_close")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A templated high-level description to use for the alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#description ContactPoint#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_priority(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to allow the alert priority to be configured via the value of the ``og_priority`` annotation on the alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#override_priority ContactPoint#override_priority}
        '''
        result = self._values.get("override_priority")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def send_tags_as(self) -> typing.Optional[builtins.str]:
        '''Whether to send annotations to OpsGenie as Tags, Details, or both.

        Supported values are ``tags``, ``details``, ``both``, or empty to use the default behavior of Tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#send_tags_as ContactPoint#send_tags_as}
        '''
        result = self._values.get("send_tags_as")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''Allows customization of the OpsGenie API URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointOpsgenie(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointOpsgenieList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointOpsgenieList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__55530d0a694c8eec8a91adbcdd8b054d7d247050024a06903e5eb9c903a5687d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointOpsgenieOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbb2d507f6a9616fdd3893ea0c48b68bcb8aa6cde4226dccf6b6cb5185fbdf34)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointOpsgenieOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b963a08520687ba04763bfe77a88dc223898638effda3fc71f0a6267c8d634aa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8a7e7c7ec274b26aa3995c43f385f68c34464d78f7753c3f39f2cea9147fad32)
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
            type_hints = typing.get_type_hints(_typecheckingstub__83cd8b0faa1229c132a1dfbf850162e0da2a91607aa71fa5951a04c6748c8551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointOpsgenie]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointOpsgenie]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointOpsgenie]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7aaefb73a7595338c83d99b36e313689f04f2eb0e26049b770e26ae75596857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointOpsgenieOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointOpsgenieOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6937f109d6f5d77ba4f21204be9ca82229fe4947bba09b28e67af76ce856ba9b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutoClose")
    def reset_auto_close(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoClose", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetOverridePriority")
    def reset_override_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverridePriority", []))

    @jsii.member(jsii_name="resetSendTagsAs")
    def reset_send_tags_as(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendTagsAs", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="autoCloseInput")
    def auto_close_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "autoCloseInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="overridePriorityInput")
    def override_priority_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "overridePriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="sendTagsAsInput")
    def send_tags_as_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sendTagsAsInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7336114acd6ba4b57247ddf2779419c871e87291d431c3126a61087326bc3393)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="autoClose")
    def auto_close(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "autoClose"))

    @auto_close.setter
    def auto_close(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a297b48a2218e592cd5c289f560b9004f63d55b04ba623875a9cad4dbdcdf6f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoClose", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0499464080499e51bcad94a8ea992681fef8d3210904278565e37b680c8ce7b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e0076e85a0dac3d7c4cfbfd8057d58b7efc73780d76f2682b6844571096cdc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba13a14a4e4ee227aa96e33a73e68809e7bf2476af1b4e88ef1c92aae4ed31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="overridePriority")
    def override_priority(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "overridePriority"))

    @override_priority.setter
    def override_priority(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3e76dbcc654d636186ef6b150c0b81ff1fad89fa59aa7752a5cbd990f363588)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overridePriority", value)

    @builtins.property
    @jsii.member(jsii_name="sendTagsAs")
    def send_tags_as(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sendTagsAs"))

    @send_tags_as.setter
    def send_tags_as(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27d9bf75106d92411b2f90b47d8c17cfe029ada4a0e80210499620892b59db04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendTagsAs", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37d89ed2509906b9e58d3ead3eed6e6c36c2aa0aeac5d4cebffe0d083eb0b12f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81c75f6e795e555c90500b8da97f2cfa1a319c19e0bbfdb3866dee1fcd6a945e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointOpsgenie, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointOpsgenie, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointOpsgenie, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9e2edb7c451bfcdfb1eaa447f3735e90e99d37cbbeb921d61d37fc6c6b57fa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointPagerduty",
    jsii_struct_bases=[],
    name_mapping={
        "integration_key": "integrationKey",
        "class_": "class",
        "component": "component",
        "disable_resolve_message": "disableResolveMessage",
        "group": "group",
        "settings": "settings",
        "severity": "severity",
        "summary": "summary",
    },
)
class ContactPointPagerduty:
    def __init__(
        self,
        *,
        integration_key: builtins.str,
        class_: typing.Optional[builtins.str] = None,
        component: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        group: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        severity: typing.Optional[builtins.str] = None,
        summary: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param integration_key: The PagerDuty API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#integration_key ContactPoint#integration_key}
        :param class_: The class or type of event, for example ``ping failure``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#class ContactPoint#class}
        :param component: The component being affected by the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#component ContactPoint#component}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param group: The group to which the provided component belongs to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#group ContactPoint#group}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param severity: The PagerDuty event severity level. Default is ``critical``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#severity ContactPoint#severity}
        :param summary: The templated summary message of the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#summary ContactPoint#summary}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0176f8b2fc03154506059271a0c24b9adede7c02d3ee95f747548cbdf9d08710)
            check_type(argname="argument integration_key", value=integration_key, expected_type=type_hints["integration_key"])
            check_type(argname="argument class_", value=class_, expected_type=type_hints["class_"])
            check_type(argname="argument component", value=component, expected_type=type_hints["component"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument summary", value=summary, expected_type=type_hints["summary"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_key": integration_key,
        }
        if class_ is not None:
            self._values["class_"] = class_
        if component is not None:
            self._values["component"] = component
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if group is not None:
            self._values["group"] = group
        if settings is not None:
            self._values["settings"] = settings
        if severity is not None:
            self._values["severity"] = severity
        if summary is not None:
            self._values["summary"] = summary

    @builtins.property
    def integration_key(self) -> builtins.str:
        '''The PagerDuty API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#integration_key ContactPoint#integration_key}
        '''
        result = self._values.get("integration_key")
        assert result is not None, "Required property 'integration_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def class_(self) -> typing.Optional[builtins.str]:
        '''The class or type of event, for example ``ping failure``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#class ContactPoint#class}
        '''
        result = self._values.get("class_")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def component(self) -> typing.Optional[builtins.str]:
        '''The component being affected by the event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#component ContactPoint#component}
        '''
        result = self._values.get("component")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''The group to which the provided component belongs to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#group ContactPoint#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def severity(self) -> typing.Optional[builtins.str]:
        '''The PagerDuty event severity level. Default is ``critical``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#severity ContactPoint#severity}
        '''
        result = self._values.get("severity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def summary(self) -> typing.Optional[builtins.str]:
        '''The templated summary message of the event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#summary ContactPoint#summary}
        '''
        result = self._values.get("summary")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointPagerduty(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointPagerdutyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointPagerdutyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f11f6bc42c1a86d651f6e1859eee8e42c1fd3db0066cab44d369de376b836e99)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointPagerdutyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c3891ca9af075ebb3840abeff44eb48e3fb3c8192a5847f41503dbc512add0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointPagerdutyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a4e2a689ef79f8418a961490410fa66bf2c610144dba012534c68fd5dd8546)
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
            type_hints = typing.get_type_hints(_typecheckingstub__658efe29ea72e10fc44ed6d475de92125948150fb3a37c7e98255798b9bd70dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fdb74056f5f5554c5becde6808e170d0a0da8f7a96a9eb49bf3cda2563cb94a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPagerduty]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPagerduty]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPagerduty]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3978a7370606b06424ac5120d478e8b06c6d60ed7aa74876c3d26c002ec049d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointPagerdutyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointPagerdutyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__acd9b0de236147d06bb0630f154d5c0d90b3d6d0cc6ad194bf0547b45296df64)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetClass")
    def reset_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClass", []))

    @jsii.member(jsii_name="resetComponent")
    def reset_component(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComponent", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetSeverity")
    def reset_severity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeverity", []))

    @jsii.member(jsii_name="resetSummary")
    def reset_summary(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSummary", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="classInput")
    def class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "classInput"))

    @builtins.property
    @jsii.member(jsii_name="componentInput")
    def component_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "componentInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationKeyInput")
    def integration_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="severityInput")
    def severity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "severityInput"))

    @builtins.property
    @jsii.member(jsii_name="summaryInput")
    def summary_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "summaryInput"))

    @builtins.property
    @jsii.member(jsii_name="class")
    def class_(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "class"))

    @class_.setter
    def class_(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d79935a104db179cb945f4ca95c2f0568b31834f5dedaa9282d2e97bbdfaf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "class", value)

    @builtins.property
    @jsii.member(jsii_name="component")
    def component(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "component"))

    @component.setter
    def component(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ec3af39a017ead9cfef85396ebbac8da61f9942bdccac1b3ff448954cdccff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "component", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__044ee8c2a28d908d27537323655e3e655b421e6dcbe90001eec5815f37d68d35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ac11013f1693576885f06dbca7e4e5803ff48eabce03dda2fd80cd677267727)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="integrationKey")
    def integration_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationKey"))

    @integration_key.setter
    def integration_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adfd03c965db9577e9ea3149835b0740865637b36c4609b0867664c8b255fc0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationKey", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83be30ba4e29a2bce19fd5073b023a5ad916075d29c949761a93c4d73e65e678)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="severity")
    def severity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "severity"))

    @severity.setter
    def severity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3068d7ae210483da75b5905557235a0f393d4b31dfc200326e13db7f9c830dce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "severity", value)

    @builtins.property
    @jsii.member(jsii_name="summary")
    def summary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "summary"))

    @summary.setter
    def summary(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8dd12b6207572bcba47f974e66b19c64d90d7a9e6a2b77cd4a9ae98dde4d192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "summary", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointPagerduty, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointPagerduty, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointPagerduty, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d2cf4fb8cc24c8a8ff9eb64c01e72cb1b10721955026a0644b55b240128792)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointPushover",
    jsii_struct_bases=[],
    name_mapping={
        "api_token": "apiToken",
        "user_key": "userKey",
        "device": "device",
        "disable_resolve_message": "disableResolveMessage",
        "expire": "expire",
        "message": "message",
        "ok_priority": "okPriority",
        "ok_sound": "okSound",
        "priority": "priority",
        "retry": "retry",
        "settings": "settings",
        "sound": "sound",
    },
)
class ContactPointPushover:
    def __init__(
        self,
        *,
        api_token: builtins.str,
        user_key: builtins.str,
        device: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        expire: typing.Optional[jsii.Number] = None,
        message: typing.Optional[builtins.str] = None,
        ok_priority: typing.Optional[jsii.Number] = None,
        ok_sound: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        retry: typing.Optional[jsii.Number] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        sound: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_token: The Pushover API token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_token ContactPoint#api_token}
        :param user_key: The Pushover user key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#user_key ContactPoint#user_key}
        :param device: Comma-separated list of devices to which the event is associated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#device ContactPoint#device}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param expire: How many seconds for which the notification will continue to be retried by Pushover. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#expire ContactPoint#expire}
        :param message: The templated notification message content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param ok_priority: The priority level of the resolved event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#ok_priority ContactPoint#ok_priority}
        :param ok_sound: The sound associated with the resolved notification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#ok_sound ContactPoint#ok_sound}
        :param priority: The priority level of the event. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#priority ContactPoint#priority}
        :param retry: How often, in seconds, the Pushover servers will send the same notification to the user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#retry ContactPoint#retry}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param sound: The sound associated with the notification. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#sound ContactPoint#sound}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6430a3c5e4fa5822bfefa26379175c3418875010f05e6f14206d2635d71e17a0)
            check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            check_type(argname="argument user_key", value=user_key, expected_type=type_hints["user_key"])
            check_type(argname="argument device", value=device, expected_type=type_hints["device"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument expire", value=expire, expected_type=type_hints["expire"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument ok_priority", value=ok_priority, expected_type=type_hints["ok_priority"])
            check_type(argname="argument ok_sound", value=ok_sound, expected_type=type_hints["ok_sound"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument retry", value=retry, expected_type=type_hints["retry"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument sound", value=sound, expected_type=type_hints["sound"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_token": api_token,
            "user_key": user_key,
        }
        if device is not None:
            self._values["device"] = device
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if expire is not None:
            self._values["expire"] = expire
        if message is not None:
            self._values["message"] = message
        if ok_priority is not None:
            self._values["ok_priority"] = ok_priority
        if ok_sound is not None:
            self._values["ok_sound"] = ok_sound
        if priority is not None:
            self._values["priority"] = priority
        if retry is not None:
            self._values["retry"] = retry
        if settings is not None:
            self._values["settings"] = settings
        if sound is not None:
            self._values["sound"] = sound

    @builtins.property
    def api_token(self) -> builtins.str:
        '''The Pushover API token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_token ContactPoint#api_token}
        '''
        result = self._values.get("api_token")
        assert result is not None, "Required property 'api_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_key(self) -> builtins.str:
        '''The Pushover user key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#user_key ContactPoint#user_key}
        '''
        result = self._values.get("user_key")
        assert result is not None, "Required property 'user_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device(self) -> typing.Optional[builtins.str]:
        '''Comma-separated list of devices to which the event is associated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#device ContactPoint#device}
        '''
        result = self._values.get("device")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def expire(self) -> typing.Optional[jsii.Number]:
        '''How many seconds for which the notification will continue to be retried by Pushover.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#expire ContactPoint#expire}
        '''
        result = self._values.get("expire")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated notification message content.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ok_priority(self) -> typing.Optional[jsii.Number]:
        '''The priority level of the resolved event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#ok_priority ContactPoint#ok_priority}
        '''
        result = self._values.get("ok_priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ok_sound(self) -> typing.Optional[builtins.str]:
        '''The sound associated with the resolved notification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#ok_sound ContactPoint#ok_sound}
        '''
        result = self._values.get("ok_sound")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''The priority level of the event.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#priority ContactPoint#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retry(self) -> typing.Optional[jsii.Number]:
        '''How often, in seconds, the Pushover servers will send the same notification to the user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#retry ContactPoint#retry}
        '''
        result = self._values.get("retry")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def sound(self) -> typing.Optional[builtins.str]:
        '''The sound associated with the notification.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#sound ContactPoint#sound}
        '''
        result = self._values.get("sound")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointPushover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointPushoverList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointPushoverList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c638d278fed138cd89f7e8daf3439058b286933a6573cb67ec0c2fe68878e4ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointPushoverOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1331af03b6f597e8e2106366677074fb53d8cbdceddc58da6f3936d254348b84)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointPushoverOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b3c26161f9b5b763974b41416a23f3a01320791f9456ef8a07e96fcd4f44e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__685f694a16ea7643238d2f3b2cbd3c8f9778acff14b8f100311fa65bd5c0e36f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52b70baccbcfa29da1199e901930f01c4a4162088ec94285f27beb9a9b9177d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPushover]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPushover]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPushover]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c7ec2428becd8480f8fe76e8c37ba9ae0768c7067cc46c3b1ce47b2217cd4ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointPushoverOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointPushoverOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8a35501697c5aff5ee88c5543978e105ef376612c0a0bc0599bbe25e1df9ae6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDevice")
    def reset_device(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevice", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetExpire")
    def reset_expire(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpire", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetOkPriority")
    def reset_ok_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkPriority", []))

    @jsii.member(jsii_name="resetOkSound")
    def reset_ok_sound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOkSound", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetRetry")
    def reset_retry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetry", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetSound")
    def reset_sound(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSound", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="apiTokenInput")
    def api_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="deviceInput")
    def device_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="expireInput")
    def expire_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expireInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="okPriorityInput")
    def ok_priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "okPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="okSoundInput")
    def ok_sound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "okSoundInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="retryInput")
    def retry_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="soundInput")
    def sound_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "soundInput"))

    @builtins.property
    @jsii.member(jsii_name="userKeyInput")
    def user_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="apiToken")
    def api_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiToken"))

    @api_token.setter
    def api_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__563a1bb7192f8d572205b83ab7df0fc96188e64ecfc912fc3dcc5b0b7f4e1097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiToken", value)

    @builtins.property
    @jsii.member(jsii_name="device")
    def device(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "device"))

    @device.setter
    def device(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3614fa412342e8a690636865d2091cfa4c9c11ca9fd7502b45ddbb8583141088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "device", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9292fe09caac19ad3b47dca00f8058c83f0fc05c31efb3bd4037cfe993377f5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="expire")
    def expire(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expire"))

    @expire.setter
    def expire(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21f18c0030286a0942c17cb8e907fced4095e3e4acb8cd02eb23daf68ccf2c3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expire", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b97fbb8ca99ee02f3f3f765bcfc988783a8c37ee92c57a41f7e23a54fd35d75e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="okPriority")
    def ok_priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "okPriority"))

    @ok_priority.setter
    def ok_priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bb754b6c695a503ae785acbbfa73fa4405d55eefcb3ddf9fcadc56768d07eb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "okPriority", value)

    @builtins.property
    @jsii.member(jsii_name="okSound")
    def ok_sound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "okSound"))

    @ok_sound.setter
    def ok_sound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__687484980c9340f575437d79c94c2e475b8d06d39238e31221f93e561a058444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "okSound", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5554f33d2e262d1dbe743870ce6a65a530aa1545002e88958a86ecb863841ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="retry")
    def retry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retry"))

    @retry.setter
    def retry(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88a51044c0eac55733fcd91d61ea7bf277c4a0361b0dacc7b1253f582820ab5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retry", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef99295f6408b4824a7bf46c8147463104521409fc9e31690bdb3691e7a134a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="sound")
    def sound(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sound"))

    @sound.setter
    def sound(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f55d0c77c483d664d4b3d9ae7112e2363c9af688e5bf4c763d4ec344b0bc730e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sound", value)

    @builtins.property
    @jsii.member(jsii_name="userKey")
    def user_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userKey"))

    @user_key.setter
    def user_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0b71978e94515dffe037d4351c2f768318f3b12c4388c4b8fe8906f27f5db18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointPushover, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointPushover, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointPushover, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d1dcef806ae800816878c14a809f12b72e76125f0d0f95f8b0469fb4bf0d350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointSensugo",
    jsii_struct_bases=[],
    name_mapping={
        "api_key": "apiKey",
        "url": "url",
        "check": "check",
        "disable_resolve_message": "disableResolveMessage",
        "entity": "entity",
        "handler": "handler",
        "message": "message",
        "namespace": "namespace",
        "settings": "settings",
    },
)
class ContactPointSensugo:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        url: builtins.str,
        check: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        entity: typing.Optional[builtins.str] = None,
        handler: typing.Optional[builtins.str] = None,
        message: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param api_key: The SensuGo API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_key ContactPoint#api_key}
        :param url: The SensuGo URL to send requests to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param check: The SensuGo check to which the event should be routed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#check ContactPoint#check}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param entity: The entity being monitored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#entity ContactPoint#entity}
        :param handler: A custom handler to execute in addition to the check. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#handler ContactPoint#handler}
        :param message: Templated message content describing the alert. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param namespace: The namespace in which the check resides. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#namespace ContactPoint#namespace}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74d879225b6c3d742743e8aad6851e15881458543b034b9b82089ce7316daebb)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument check", value=check, expected_type=type_hints["check"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument entity", value=entity, expected_type=type_hints["entity"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key": api_key,
            "url": url,
        }
        if check is not None:
            self._values["check"] = check
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if entity is not None:
            self._values["entity"] = entity
        if handler is not None:
            self._values["handler"] = handler
        if message is not None:
            self._values["message"] = message
        if namespace is not None:
            self._values["namespace"] = namespace
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def api_key(self) -> builtins.str:
        '''The SensuGo API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_key ContactPoint#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The SensuGo URL to send requests to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def check(self) -> typing.Optional[builtins.str]:
        '''The SensuGo check to which the event should be routed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#check ContactPoint#check}
        '''
        result = self._values.get("check")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def entity(self) -> typing.Optional[builtins.str]:
        '''The entity being monitored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#entity ContactPoint#entity}
        '''
        result = self._values.get("entity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def handler(self) -> typing.Optional[builtins.str]:
        '''A custom handler to execute in addition to the check.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#handler ContactPoint#handler}
        '''
        result = self._values.get("handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''Templated message content describing the alert.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace in which the check resides.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#namespace ContactPoint#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointSensugo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointSensugoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointSensugoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de3f1c391b3d5420ad8bd5762bca5243bd7c50527862cc1db91ef088dca0b74e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointSensugoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4e889965feb2d7220f94a20349253cc420f441e58d58508f50d6ba89267b48)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointSensugoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b967917c8683557d626511ba15c60695545cfc59d3e687f20c40079352d14e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa8a94ea4532d8fe2c400cd963f69aee9d847bdb9a90a38bf0da7080a1e8917c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aea05fe351c2f0a394f94f58c4c474ac13f164a1b7bfbd6db74b649b15680949)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSensugo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSensugo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSensugo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d653cc177b7cab492b101c6f7efc502141ae939153730ccaf7d4b1c918c48130)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointSensugoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointSensugoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ff1cd3a26e42f6414032a265c1f4dbfb318e054db3b913686e9a8480f0b9c25d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCheck")
    def reset_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCheck", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetEntity")
    def reset_entity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEntity", []))

    @jsii.member(jsii_name="resetHandler")
    def reset_handler(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHandler", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="checkInput")
    def check_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "checkInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="entityInput")
    def entity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entityInput"))

    @builtins.property
    @jsii.member(jsii_name="handlerInput")
    def handler_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handlerInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cc8cc16e2ff35fe390a67e9ed98c5151dcfe2e9feb8fb9451e02f2650243c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="check")
    def check(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "check"))

    @check.setter
    def check(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8469db4827b94eca18b1115e14ed8b1c055ac112a8db255e1e13b3ad2094ecad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "check", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9f097e8de0e862a5946f8d21d28703ec79c4287a609509abe94702827540df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="entity")
    def entity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "entity"))

    @entity.setter
    def entity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcb034828a2c6724d859ad1fda4a2d5fe1f7d5e682ba2e04caa3528be906993a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entity", value)

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "handler"))

    @handler.setter
    def handler(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ed38b3323164947d35cc74feb2dda5e845508e8811a826c739c876c4e27446)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handler", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f595e4b3a948c8242a5c290a99b2cafc09f518d7b3a6c68d3265727877817b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be44f161e7f8e34e98f064f7a4b47b12f80c3481eedb3e17bca36f7926b6b7d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775c1b6ef8b4a494c3cee0837cbf1819a16b86d530910a608285e924bd1d6ea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d33962ac80abb061ec9bbc9965a23f5b657ae1955de4f91ff322927b6ffcbb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointSensugo, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointSensugo, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointSensugo, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429773d92bd5fe841043bc248d91ad499934ddba3edfcd30763aea07f4628093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointSlack",
    jsii_struct_bases=[],
    name_mapping={
        "disable_resolve_message": "disableResolveMessage",
        "endpoint_url": "endpointUrl",
        "icon_emoji": "iconEmoji",
        "icon_url": "iconUrl",
        "mention_channel": "mentionChannel",
        "mention_groups": "mentionGroups",
        "mention_users": "mentionUsers",
        "recipient": "recipient",
        "settings": "settings",
        "text": "text",
        "title": "title",
        "token": "token",
        "url": "url",
        "username": "username",
    },
)
class ContactPointSlack:
    def __init__(
        self,
        *,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        endpoint_url: typing.Optional[builtins.str] = None,
        icon_emoji: typing.Optional[builtins.str] = None,
        icon_url: typing.Optional[builtins.str] = None,
        mention_channel: typing.Optional[builtins.str] = None,
        mention_groups: typing.Optional[builtins.str] = None,
        mention_users: typing.Optional[builtins.str] = None,
        recipient: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        text: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
        token: typing.Optional[builtins.str] = None,
        url: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param endpoint_url: Use this to override the Slack API endpoint URL to send requests to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#endpoint_url ContactPoint#endpoint_url}
        :param icon_emoji: The name of a Slack workspace emoji to use as the bot icon. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#icon_emoji ContactPoint#icon_emoji}
        :param icon_url: A URL of an image to use as the bot icon. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#icon_url ContactPoint#icon_url}
        :param mention_channel: Describes how to ping the slack channel that messages are being sent to. Options are ``here`` for an @here ping, ``channel`` for @channel, or empty for no ping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#mention_channel ContactPoint#mention_channel}
        :param mention_groups: Comma-separated list of groups to mention in the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#mention_groups ContactPoint#mention_groups}
        :param mention_users: Comma-separated list of users to mention in the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#mention_users ContactPoint#mention_users}
        :param recipient: Channel, private group, or IM channel (can be an encoded ID or a name) to send messages to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#recipient ContactPoint#recipient}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param text: Templated content of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#text ContactPoint#text}
        :param title: Templated title of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#title ContactPoint#title}
        :param token: A Slack API token,for sending messages directly without the webhook method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#token ContactPoint#token}
        :param url: A Slack webhook URL,for sending messages via the webhook method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param username: Username for the bot to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#username ContactPoint#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7574723ee47f77f4da05ec2720b374b156c39e8c7b8a5bb5b9af8e0aee1ea843)
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument endpoint_url", value=endpoint_url, expected_type=type_hints["endpoint_url"])
            check_type(argname="argument icon_emoji", value=icon_emoji, expected_type=type_hints["icon_emoji"])
            check_type(argname="argument icon_url", value=icon_url, expected_type=type_hints["icon_url"])
            check_type(argname="argument mention_channel", value=mention_channel, expected_type=type_hints["mention_channel"])
            check_type(argname="argument mention_groups", value=mention_groups, expected_type=type_hints["mention_groups"])
            check_type(argname="argument mention_users", value=mention_users, expected_type=type_hints["mention_users"])
            check_type(argname="argument recipient", value=recipient, expected_type=type_hints["recipient"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if endpoint_url is not None:
            self._values["endpoint_url"] = endpoint_url
        if icon_emoji is not None:
            self._values["icon_emoji"] = icon_emoji
        if icon_url is not None:
            self._values["icon_url"] = icon_url
        if mention_channel is not None:
            self._values["mention_channel"] = mention_channel
        if mention_groups is not None:
            self._values["mention_groups"] = mention_groups
        if mention_users is not None:
            self._values["mention_users"] = mention_users
        if recipient is not None:
            self._values["recipient"] = recipient
        if settings is not None:
            self._values["settings"] = settings
        if text is not None:
            self._values["text"] = text
        if title is not None:
            self._values["title"] = title
        if token is not None:
            self._values["token"] = token
        if url is not None:
            self._values["url"] = url
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def endpoint_url(self) -> typing.Optional[builtins.str]:
        '''Use this to override the Slack API endpoint URL to send requests to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#endpoint_url ContactPoint#endpoint_url}
        '''
        result = self._values.get("endpoint_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icon_emoji(self) -> typing.Optional[builtins.str]:
        '''The name of a Slack workspace emoji to use as the bot icon.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#icon_emoji ContactPoint#icon_emoji}
        '''
        result = self._values.get("icon_emoji")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def icon_url(self) -> typing.Optional[builtins.str]:
        '''A URL of an image to use as the bot icon.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#icon_url ContactPoint#icon_url}
        '''
        result = self._values.get("icon_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mention_channel(self) -> typing.Optional[builtins.str]:
        '''Describes how to ping the slack channel that messages are being sent to.

        Options are ``here`` for an @here ping, ``channel`` for @channel, or empty for no ping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#mention_channel ContactPoint#mention_channel}
        '''
        result = self._values.get("mention_channel")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mention_groups(self) -> typing.Optional[builtins.str]:
        '''Comma-separated list of groups to mention in the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#mention_groups ContactPoint#mention_groups}
        '''
        result = self._values.get("mention_groups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mention_users(self) -> typing.Optional[builtins.str]:
        '''Comma-separated list of users to mention in the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#mention_users ContactPoint#mention_users}
        '''
        result = self._values.get("mention_users")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipient(self) -> typing.Optional[builtins.str]:
        '''Channel, private group, or IM channel (can be an encoded ID or a name) to send messages to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#recipient ContactPoint#recipient}
        '''
        result = self._values.get("recipient")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def text(self) -> typing.Optional[builtins.str]:
        '''Templated content of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#text ContactPoint#text}
        '''
        result = self._values.get("text")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Templated title of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#title ContactPoint#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''A Slack API token,for sending messages directly without the webhook method.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#token ContactPoint#token}
        '''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''A Slack webhook URL,for sending messages via the webhook method.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for the bot to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#username ContactPoint#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointSlack(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointSlackList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointSlackList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6532f72bc30f1e272942d92f2508decf96a2ad05b78a12a696c69edc9686893b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointSlackOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5166163e79af5e92381eb8e41bca67f4507eafba949180becac7509311e5ef6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointSlackOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be677b248fd57a57b7edfc348959c6b6e9d47fb048c12c795a526097f570608b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34b82d22c2a02823358c36335dd116b759a02a060460560a63f3e1e34ffa3af1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9dedebd2a40b51659b363916fc4e1bfd2b46f74bf17bed7be212ca27593e15e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSlack]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSlack]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSlack]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f60730c1bee7540491b06319bca64f1de11367f1fcaa9da811b8c3d61d4572c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointSlackOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointSlackOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50c2c3b7871d4219a8173c3c9fefd0acbf51218b3135a4f416b3687e16d36960)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetEndpointUrl")
    def reset_endpoint_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointUrl", []))

    @jsii.member(jsii_name="resetIconEmoji")
    def reset_icon_emoji(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIconEmoji", []))

    @jsii.member(jsii_name="resetIconUrl")
    def reset_icon_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIconUrl", []))

    @jsii.member(jsii_name="resetMentionChannel")
    def reset_mention_channel(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMentionChannel", []))

    @jsii.member(jsii_name="resetMentionGroups")
    def reset_mention_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMentionGroups", []))

    @jsii.member(jsii_name="resetMentionUsers")
    def reset_mention_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMentionUsers", []))

    @jsii.member(jsii_name="resetRecipient")
    def reset_recipient(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecipient", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetText")
    def reset_text(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetText", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="resetUrl")
    def reset_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrl", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointUrlInput")
    def endpoint_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="iconEmojiInput")
    def icon_emoji_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iconEmojiInput"))

    @builtins.property
    @jsii.member(jsii_name="iconUrlInput")
    def icon_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iconUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="mentionChannelInput")
    def mention_channel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mentionChannelInput"))

    @builtins.property
    @jsii.member(jsii_name="mentionGroupsInput")
    def mention_groups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mentionGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="mentionUsersInput")
    def mention_users_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mentionUsersInput"))

    @builtins.property
    @jsii.member(jsii_name="recipientInput")
    def recipient_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recipientInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b41829f5b4afa72f6c33ffb4690c8801d9c24701a9f4b56d33ba885c19b496e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="endpointUrl")
    def endpoint_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointUrl"))

    @endpoint_url.setter
    def endpoint_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbd6a8ef62baec016145dd0c31a7c3a2ff5dcf3ca8baa33b59d6f540a1edf663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointUrl", value)

    @builtins.property
    @jsii.member(jsii_name="iconEmoji")
    def icon_emoji(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iconEmoji"))

    @icon_emoji.setter
    def icon_emoji(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de24734c6faa25705207812a0390d7abf5032272cdc2efc0471d81ba6d9601bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iconEmoji", value)

    @builtins.property
    @jsii.member(jsii_name="iconUrl")
    def icon_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iconUrl"))

    @icon_url.setter
    def icon_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__256403ebd076a801dc77c01ac269724ec8a7b6506ddffd969de415ab04022046)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iconUrl", value)

    @builtins.property
    @jsii.member(jsii_name="mentionChannel")
    def mention_channel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mentionChannel"))

    @mention_channel.setter
    def mention_channel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f85d1d4f27824724a051d30f554ef5a283409dc0ce8f2e202ed12ec78fb138)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mentionChannel", value)

    @builtins.property
    @jsii.member(jsii_name="mentionGroups")
    def mention_groups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mentionGroups"))

    @mention_groups.setter
    def mention_groups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eba729e252cc450ae4657ad43f148a6c4216f9e41aa109c0891d01bcb3e072df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mentionGroups", value)

    @builtins.property
    @jsii.member(jsii_name="mentionUsers")
    def mention_users(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mentionUsers"))

    @mention_users.setter
    def mention_users(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__827bd1b2792677309e02e3d14df98d0ad1f8ba9ff216147d69bfb34bb6f6709a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mentionUsers", value)

    @builtins.property
    @jsii.member(jsii_name="recipient")
    def recipient(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recipient"))

    @recipient.setter
    def recipient(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b7638d1bb1b2f0c9228b6a274fbf090e7ac06d9577b5dd342f86c8c8607488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipient", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc5aefd131e6cd931c5047669327ad4509b758fdad231c637ecc27f88c19c84a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d50afe4c0517d2ad457d3ef118faef9b841b0159f11618bb9e8eaf74e362a95d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a72fbeb13a9f5305ceb4b9b0dda306b8ef15f72758be22cf60896314602a1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bade15857e26d6918c803fc4d5fd16035cdb00fe49ccea874fe40075b5b2563)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2de6430fa99b3a992b9e2ef29dab40e049a8c33858673ba959fdb6614935e80a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6cd7c7ca02dbcb90a4c4dd38051cf36a6ec53382654dfce14ae64aa05ed8cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointSlack, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointSlack, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointSlack, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b33048163d80b3a9a59d6ca2ed9180d764f511635aa6c4f6dbb1f83c0569f140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointTeams",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "section_title": "sectionTitle",
        "settings": "settings",
        "title": "title",
    },
)
class ContactPointTeams:
    def __init__(
        self,
        *,
        url: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        section_title: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: A Teams webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated message content to send. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param section_title: The templated subtitle for each message section. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#section_title ContactPoint#section_title}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param title: The templated title of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#title ContactPoint#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d54d9f975d28c1dec116542a9f5cda49536bfa83a03bc9f6a665286ba6683db0)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument section_title", value=section_title, expected_type=type_hints["section_title"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if section_title is not None:
            self._values["section_title"] = section_title
        if settings is not None:
            self._values["settings"] = settings
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def url(self) -> builtins.str:
        '''A Teams webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated message content to send.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def section_title(self) -> typing.Optional[builtins.str]:
        '''The templated subtitle for each message section.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#section_title ContactPoint#section_title}
        '''
        result = self._values.get("section_title")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''The templated title of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#title ContactPoint#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointTeams(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointTeamsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointTeamsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c042aac6cda205bad3ae6d6738921058379629a8ebffc5ea25673558d23c48d1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointTeamsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d964a2dd4f698b1d0536b018a60cbdba88918ff57ba176e4429dee6a0e60a12)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointTeamsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aec072170ce97b5b71bcddab0bda26724060f6467c3221e5053a67c59d4cf68)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c00af004757138f20b30a194a52f92ba13c4c30d8c5386fe0b7b9295c4468594)
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
            type_hints = typing.get_type_hints(_typecheckingstub__05981874f5d1dc140fa8173e32cb80a9132783e2cdc370a50b582839e7b9d107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTeams]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTeams]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTeams]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab497c9bb66e418c00519076f8cd4135e192ec0c19bb893e2f1e0f1a1b5da107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointTeamsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointTeamsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__05e777d0fb0774a1579c3eb3900cbdab486352bfad0e8baf18cab4c2412de4f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetSectionTitle")
    def reset_section_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSectionTitle", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="sectionTitleInput")
    def section_title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sectionTitleInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79bcfec232789c771b32af705b73dd54834d470140986cd461922c59b45fd517)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04de0f21d0cce2e911732b300805c9be5bc3e3e51c595a0f4624c1fa6e5f0a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="sectionTitle")
    def section_title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sectionTitle"))

    @section_title.setter
    def section_title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e31890756cfe22e52bda2102f33b3434e133162f11be8d86c5ebc65a3cf3c35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sectionTitle", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ef6362dc2d3c44029991d40bf9b15b7ea2431e7ac7b569873065d620078414a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f18ac0b2072c51f30a987feabb3cad3a123efcd01906600ab7af50efe1d657ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69d289b0b85276e0a2a636f3bf5456acd0dcae98ec2ddb57d8a08e15a4abd748)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointTeams, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointTeams, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointTeams, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67288a850ba0dd87d188c613d4bd7dcdd3ca54b1ac7e33daf99e88d3f8f934fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointTelegram",
    jsii_struct_bases=[],
    name_mapping={
        "chat_id": "chatId",
        "token": "token",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "settings": "settings",
    },
)
class ContactPointTelegram:
    def __init__(
        self,
        *,
        chat_id: builtins.str,
        token: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param chat_id: The chat ID to send messages to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#chat_id ContactPoint#chat_id}
        :param token: The Telegram bot token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#token ContactPoint#token}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8c133ff2d171f19a5cf9aa31c8a3fe51792e5a480d499492f53b9499a2be512)
            check_type(argname="argument chat_id", value=chat_id, expected_type=type_hints["chat_id"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "chat_id": chat_id,
            "token": token,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def chat_id(self) -> builtins.str:
        '''The chat ID to send messages to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#chat_id ContactPoint#chat_id}
        '''
        result = self._values.get("chat_id")
        assert result is not None, "Required property 'chat_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token(self) -> builtins.str:
        '''The Telegram bot token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#token ContactPoint#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointTelegram(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointTelegramList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointTelegramList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0224048fb5038ade33108f0db60be7cbeec13b2bc9b92938c3c53c2639d8b347)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointTelegramOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66ed7955e7957e4f554300f182528adf612ddfc7e918b6b2d66bd2eac9663ff6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointTelegramOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456a1fd319175e7ca3fbed9bb2fcf625fd29933f529d922fbf5b1b4ba6b92395)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2bdf15d1e98ea7b8ab2e18e858109382de9758630337be86225bcaf9c2b065c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a761d2b4d8683d232764aeead966e884b6c470605dd61656978c9ed5e8f3360b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTelegram]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTelegram]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTelegram]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6edf3dc3557210e1c1b8ca9884bd4016ca09380ca58af6d611f44ff958674b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointTelegramOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointTelegramOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a1fefab0ce1f02614f69e7b82cf6d8561446c532c5ef9bbae65ffb73e8e800d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="chatIdInput")
    def chat_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "chatIdInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="chatId")
    def chat_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "chatId"))

    @chat_id.setter
    def chat_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b66a972e3da4145a5ed3d05a016141abf8babd8bb33007c5f88167c8fc7070c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "chatId", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f640e7e17d2f10f2cd71437b3b2fca8f9c035584dc72f82d90d37df61fe3dff0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c1fd985400bc2fe32f1876ffcd678067a959680c20663893b55c8e4eb744db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a57c03e1af6812b4670eca637f6e38cc9bdada7d9da39b0624c29741fe73383)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__051867d6cadd97cf0eca8d1b873a2c0948250e4f01eb92ed8909903f9ce40d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointTelegram, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointTelegram, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointTelegram, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08576c1ddc64701cc5b5657a41cc1f570f7a2690618bdebcd9b5b528606098fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointThreema",
    jsii_struct_bases=[],
    name_mapping={
        "api_secret": "apiSecret",
        "gateway_id": "gatewayId",
        "recipient_id": "recipientId",
        "disable_resolve_message": "disableResolveMessage",
        "settings": "settings",
    },
)
class ContactPointThreema:
    def __init__(
        self,
        *,
        api_secret: builtins.str,
        gateway_id: builtins.str,
        recipient_id: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param api_secret: The Threema API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_secret ContactPoint#api_secret}
        :param gateway_id: The Threema gateway ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#gateway_id ContactPoint#gateway_id}
        :param recipient_id: The ID of the recipient of the message. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#recipient_id ContactPoint#recipient_id}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00fac38220abd2fa709b92d9e320ea5f4b5bccc7bd346ebcf2cf9c484f7b953e)
            check_type(argname="argument api_secret", value=api_secret, expected_type=type_hints["api_secret"])
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
            check_type(argname="argument recipient_id", value=recipient_id, expected_type=type_hints["recipient_id"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_secret": api_secret,
            "gateway_id": gateway_id,
            "recipient_id": recipient_id,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def api_secret(self) -> builtins.str:
        '''The Threema API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#api_secret ContactPoint#api_secret}
        '''
        result = self._values.get("api_secret")
        assert result is not None, "Required property 'api_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def gateway_id(self) -> builtins.str:
        '''The Threema gateway ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#gateway_id ContactPoint#gateway_id}
        '''
        result = self._values.get("gateway_id")
        assert result is not None, "Required property 'gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recipient_id(self) -> builtins.str:
        '''The ID of the recipient of the message.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#recipient_id ContactPoint#recipient_id}
        '''
        result = self._values.get("recipient_id")
        assert result is not None, "Required property 'recipient_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointThreema(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointThreemaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointThreemaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a513e8b18a22a21df2e4bff9c4a2b84e4e2a89025b561ba0f221e72c3446d72c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointThreemaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a993da7b2d832e2799a8ff6a4b9286052683c5a3496ec8fd8a6d4e6713b95de)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointThreemaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f166f7d58d725603a5956d9426b691582724d8d7c9eeb825ac03b22dd804df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d014dd4e419463d42eb344f4e5680f75699f7c3a1d4cc9423de4caca7cb4793)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cac7664f37ecc7ddeeacbaf219853be734aa4883fa766776e497e8e7c6b5bbd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointThreema]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointThreema]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointThreema]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77aa320b0e06057ac1b5e1d67a5e36dc186315af31ff07b56b75a1da8941766d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointThreemaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointThreemaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4da2d89d694df44fb8517fea6fd91b2de0a65a3612b8f88a06ab556a90ef4896)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="apiSecretInput")
    def api_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="gatewayIdInput")
    def gateway_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIdInput"))

    @builtins.property
    @jsii.member(jsii_name="recipientIdInput")
    def recipient_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "recipientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiSecret")
    def api_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiSecret"))

    @api_secret.setter
    def api_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf6d7b8ebf52605c0d53cad158c140df93beb0a20feba8e9d155e90f8c64211)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiSecret", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d75400cbcbcb01019fae547644abc4dbb46522565cf18a747d32d521ba450511)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @gateway_id.setter
    def gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a8f9ccae37d94b9f2df04d7ad5061e35a206f7c230d67a1fa630b07c6396a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayId", value)

    @builtins.property
    @jsii.member(jsii_name="recipientId")
    def recipient_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "recipientId"))

    @recipient_id.setter
    def recipient_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8eaa6b976bedd2ed4a9c6ebde7328cf0ad2e10f10c982ec5ab21f3eb9b1938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recipientId", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c081a3a6a30add56fd35c0ce57aeee92a1c91dab86f2b107724d1950e40ba8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointThreema, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointThreema, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointThreema, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9d79dfd31e1a64882a3b2e9fc20b2d90b7cbf57f664aec8a0fe932dc15daf6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointVictorops",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "disable_resolve_message": "disableResolveMessage",
        "message_type": "messageType",
        "settings": "settings",
    },
)
class ContactPointVictorops:
    def __init__(
        self,
        *,
        url: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message_type: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: The VictorOps webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message_type: The VictorOps alert state - typically either ``CRITICAL`` or ``RECOVERY``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message_type ContactPoint#message_type}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699fd5524aa517ff3b438ac5cd8bbf5f77f9890179f26299d153f3bf4934022c)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message_type", value=message_type, expected_type=type_hints["message_type"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message_type is not None:
            self._values["message_type"] = message_type
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def url(self) -> builtins.str:
        '''The VictorOps webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message_type(self) -> typing.Optional[builtins.str]:
        '''The VictorOps alert state - typically either ``CRITICAL`` or ``RECOVERY``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message_type ContactPoint#message_type}
        '''
        result = self._values.get("message_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointVictorops(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointVictoropsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointVictoropsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b3f0be014a7f31e3714e7079032d711bc06a609605bf98a3b1b745aef37dd66)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointVictoropsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25c8f607a6b72f8c01719bcc3e764a16c93be90ca903bad8631e0b0e2b4f043b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointVictoropsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cadb6209d558a42c880fc6a6b6b7a3fa10e35762ac5391530d098441590cc2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2f68f43b261d6e97e720b65419602a0fda27b01be4eda1eae829b7afa7137ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71d7402cad81a9d0ccfb3be0e365ccb931352695527bd122c9a4b2cd566db666)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointVictorops]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointVictorops]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointVictorops]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce730ebc311aac1d527e5b9a2c12c2b802c9907be3d33c281f7e4a6fd919f7d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointVictoropsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointVictoropsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__31b707b2a50ae0781efd54ee97e032a5e906a4fde7ce8eda5cf8ab0e4579351c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessageType")
    def reset_message_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessageType", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageTypeInput")
    def message_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f107009334723533b306757378d6195fffe9d472d1b05bb0251cbabfed45449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="messageType")
    def message_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageType"))

    @message_type.setter
    def message_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23be4b2619c66c01d8fdc7ef622212000d9bc218c2879a01021ada56c6690586)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageType", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e6af5487ea7bfe747ca35721cee2b59ec19eada977453fc16a95f59180a68b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f92c0e0444c6defc6506d39b7453045ce71e7381136aa523b6c5e7efc5f5d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointVictorops, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointVictorops, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointVictorops, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb7f1b044edcec4892e5bf96f3a7fa8cb58cf6f5e3f20992d36229fdeb2eaf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointWebhook",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "authorization_credentials": "authorizationCredentials",
        "authorization_scheme": "authorizationScheme",
        "basic_auth_password": "basicAuthPassword",
        "basic_auth_user": "basicAuthUser",
        "disable_resolve_message": "disableResolveMessage",
        "http_method": "httpMethod",
        "max_alerts": "maxAlerts",
        "settings": "settings",
    },
)
class ContactPointWebhook:
    def __init__(
        self,
        *,
        url: builtins.str,
        authorization_credentials: typing.Optional[builtins.str] = None,
        authorization_scheme: typing.Optional[builtins.str] = None,
        basic_auth_password: typing.Optional[builtins.str] = None,
        basic_auth_user: typing.Optional[builtins.str] = None,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        http_method: typing.Optional[builtins.str] = None,
        max_alerts: typing.Optional[jsii.Number] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param url: The URL to send webhook requests to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param authorization_credentials: Allows a custom authorization scheme - attaches an auth header with this value. Do not use in conjunction with basic auth parameters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#authorization_credentials ContactPoint#authorization_credentials}
        :param authorization_scheme: Allows a custom authorization scheme - attaches an auth header with this name. Do not use in conjunction with basic auth parameters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#authorization_scheme ContactPoint#authorization_scheme}
        :param basic_auth_password: The username to use in basic auth headers attached to the request. If omitted, basic auth will not be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_password ContactPoint#basic_auth_password}
        :param basic_auth_user: The username to use in basic auth headers attached to the request. If omitted, basic auth will not be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_user ContactPoint#basic_auth_user}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param http_method: The HTTP method to use in the request. Defaults to ``POST``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#http_method ContactPoint#http_method}
        :param max_alerts: The maximum number of alerts to send in a single request. This can be helpful in limiting the size of the request body. The default is 0, which indicates no limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#max_alerts ContactPoint#max_alerts}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41435e324c95942d4bee93c09ebd724bffa180ec4cab8cbc09b331e604ebc996)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument authorization_credentials", value=authorization_credentials, expected_type=type_hints["authorization_credentials"])
            check_type(argname="argument authorization_scheme", value=authorization_scheme, expected_type=type_hints["authorization_scheme"])
            check_type(argname="argument basic_auth_password", value=basic_auth_password, expected_type=type_hints["basic_auth_password"])
            check_type(argname="argument basic_auth_user", value=basic_auth_user, expected_type=type_hints["basic_auth_user"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument max_alerts", value=max_alerts, expected_type=type_hints["max_alerts"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if authorization_credentials is not None:
            self._values["authorization_credentials"] = authorization_credentials
        if authorization_scheme is not None:
            self._values["authorization_scheme"] = authorization_scheme
        if basic_auth_password is not None:
            self._values["basic_auth_password"] = basic_auth_password
        if basic_auth_user is not None:
            self._values["basic_auth_user"] = basic_auth_user
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if http_method is not None:
            self._values["http_method"] = http_method
        if max_alerts is not None:
            self._values["max_alerts"] = max_alerts
        if settings is not None:
            self._values["settings"] = settings

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL to send webhook requests to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_credentials(self) -> typing.Optional[builtins.str]:
        '''Allows a custom authorization scheme - attaches an auth header with this value.

        Do not use in conjunction with basic auth parameters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#authorization_credentials ContactPoint#authorization_credentials}
        '''
        result = self._values.get("authorization_credentials")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorization_scheme(self) -> typing.Optional[builtins.str]:
        '''Allows a custom authorization scheme - attaches an auth header with this name.

        Do not use in conjunction with basic auth parameters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#authorization_scheme ContactPoint#authorization_scheme}
        '''
        result = self._values.get("authorization_scheme")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_auth_password(self) -> typing.Optional[builtins.str]:
        '''The username to use in basic auth headers attached to the request.

        If omitted, basic auth will not be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_password ContactPoint#basic_auth_password}
        '''
        result = self._values.get("basic_auth_password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def basic_auth_user(self) -> typing.Optional[builtins.str]:
        '''The username to use in basic auth headers attached to the request.

        If omitted, basic auth will not be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#basic_auth_user ContactPoint#basic_auth_user}
        '''
        result = self._values.get("basic_auth_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def http_method(self) -> typing.Optional[builtins.str]:
        '''The HTTP method to use in the request. Defaults to ``POST``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#http_method ContactPoint#http_method}
        '''
        result = self._values.get("http_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_alerts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of alerts to send in a single request.

        This can be helpful in limiting the size of the request body. The default is 0, which indicates no limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#max_alerts ContactPoint#max_alerts}
        '''
        result = self._values.get("max_alerts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointWebhook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointWebhookList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointWebhookList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b3d046fed3d86d6ef7565feff1849f395e19d5c493e5be6101ad69ebffc3046)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointWebhookOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__200c97ecc6493ea105daef71a035ee5d6d96b899131d0ebf8038ddf542484f6c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointWebhookOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022deca57d03996dbbcafbb6999abb12d745b72f08beed4f5968293263c59867)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eac8f98b2921c112f5d042df762458115aa9dcb8dfb05ce55bd81ef0e2097833)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bf157e08bcf499b8fae7ae557fb0028a81bf8434222740fccb463454c1b5a91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWebhook]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWebhook]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWebhook]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd5d5904335afc712bcc284162a43b31a1aa5ee866d1246d3433c9200b99610)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointWebhookOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointWebhookOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dada53544076046841a2c85dcde97ff6286c84f6c5f67ce47a92904a48b3c38f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAuthorizationCredentials")
    def reset_authorization_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationCredentials", []))

    @jsii.member(jsii_name="resetAuthorizationScheme")
    def reset_authorization_scheme(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizationScheme", []))

    @jsii.member(jsii_name="resetBasicAuthPassword")
    def reset_basic_auth_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthPassword", []))

    @jsii.member(jsii_name="resetBasicAuthUser")
    def reset_basic_auth_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasicAuthUser", []))

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetHttpMethod")
    def reset_http_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpMethod", []))

    @jsii.member(jsii_name="resetMaxAlerts")
    def reset_max_alerts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAlerts", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="authorizationCredentialsInput")
    def authorization_credentials_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationSchemeInput")
    def authorization_scheme_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationSchemeInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthPasswordInput")
    def basic_auth_password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="basicAuthUserInput")
    def basic_auth_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basicAuthUserInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="httpMethodInput")
    def http_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAlertsInput")
    def max_alerts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAlertsInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizationCredentials")
    def authorization_credentials(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationCredentials"))

    @authorization_credentials.setter
    def authorization_credentials(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dad0d188ce57c89500cec611ecaaa370400a8a3a6387a33ac992b68cde16587c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationScheme")
    def authorization_scheme(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authorizationScheme"))

    @authorization_scheme.setter
    def authorization_scheme(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fae5604e5e0fcb841e25795329d96526a585f06b58083e0fcb94f0a9c2fe4657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationScheme", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthPassword")
    def basic_auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthPassword"))

    @basic_auth_password.setter
    def basic_auth_password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f8db3c59fc1272fef77e4b26a747ccbb2f210681bbf0c310cd285798740ee06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthPassword", value)

    @builtins.property
    @jsii.member(jsii_name="basicAuthUser")
    def basic_auth_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "basicAuthUser"))

    @basic_auth_user.setter
    def basic_auth_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3747b29277e5ee06f5a2d34f2f18238a0b9ddd0a40f01299f08955ff67fcbab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basicAuthUser", value)

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b706cdb04d819ac573d27b53797ed2aa0b8f200f0cbc5aac9138e0346534eb8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def http_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpMethod"))

    @http_method.setter
    def http_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__553271ea544fcfbe3909ca193cdc0e318bb9a69bd7e85377a0cc9a18b26eeb51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="maxAlerts")
    def max_alerts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAlerts"))

    @max_alerts.setter
    def max_alerts(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51522b494de93f462ff401951dc474ebe6946181d0007f224c1a3e6a26c063d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAlerts", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2677758945457652e176af3da0142fda5dd0756a7f694e55e2687317022b844a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__164ad477bb44a6f24029a19ec6d59e85b34c7f46cec2a497d9885b445d1c1fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointWebhook, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointWebhook, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointWebhook, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e89a02141b2969e90370573d502734a214c67d26139bda3bdf5001ecdfa603)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="grafana.contactPoint.ContactPointWecom",
    jsii_struct_bases=[],
    name_mapping={
        "url": "url",
        "disable_resolve_message": "disableResolveMessage",
        "message": "message",
        "settings": "settings",
        "title": "title",
    },
)
class ContactPointWecom:
    def __init__(
        self,
        *,
        url: builtins.str,
        disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        message: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param url: The WeCom webhook URL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        :param disable_resolve_message: Whether to disable sending resolve messages. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        :param message: The templated content of the message to send. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        :param settings: Additional custom properties to attach to the notifier. Defaults to ``map[]``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        :param title: The templated title of the message to send. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#title ContactPoint#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6648e36c89f5337ec42994e0c4d6e7ee2f167bccd7769e6f92cf3ae8d9bfeedc)
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument disable_resolve_message", value=disable_resolve_message, expected_type=type_hints["disable_resolve_message"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "url": url,
        }
        if disable_resolve_message is not None:
            self._values["disable_resolve_message"] = disable_resolve_message
        if message is not None:
            self._values["message"] = message
        if settings is not None:
            self._values["settings"] = settings
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def url(self) -> builtins.str:
        '''The WeCom webhook URL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#url ContactPoint#url}
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disable_resolve_message(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Whether to disable sending resolve messages. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#disable_resolve_message ContactPoint#disable_resolve_message}
        '''
        result = self._values.get("disable_resolve_message")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def message(self) -> typing.Optional[builtins.str]:
        '''The templated content of the message to send.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#message ContactPoint#message}
        '''
        result = self._values.get("message")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Additional custom properties to attach to the notifier. Defaults to ``map[]``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#settings ContactPoint#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''The templated title of the message to send.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/contact_point#title ContactPoint#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactPointWecom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContactPointWecomList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointWecomList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bbb56d44bea829c5617482b32189deae6ddb1d09daf880da7b046d370dc20db)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ContactPointWecomOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13a1edd9beb2c0e73fa08a0356daeab992bb58fce6fc0f6065980a93df9c3a24)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ContactPointWecomOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f38b0570423e90fce61e593f9e8a3853e0bf46874eec28abea072a17874a0fd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__65e2e2eeae00110e49f523b4942a23b0039f2e775186a7a84a259e311bedd6b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__641bbd5446491782d387c4b5877f464e35966e7e075eb8b364d0050f9146f309)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWecom]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWecom]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWecom]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c561d60e769af539950958b419153c78c882fed0c82b0a664080ba7b370d15c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ContactPointWecomOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.contactPoint.ContactPointWecomOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5901dcb0f7f2f7fb248b41f0fd44d4341645dc0c817971968df409c4f669119d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisableResolveMessage")
    def reset_disable_resolve_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableResolveMessage", []))

    @jsii.member(jsii_name="resetMessage")
    def reset_message(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMessage", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessageInput")
    def disable_resolve_message_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "disableResolveMessageInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="urlInput")
    def url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlInput"))

    @builtins.property
    @jsii.member(jsii_name="disableResolveMessage")
    def disable_resolve_message(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "disableResolveMessage"))

    @disable_resolve_message.setter
    def disable_resolve_message(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c50f0c01a93f57567bc29a4f799b8df19157d7ce6aed194622fc92980121db0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableResolveMessage", value)

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @message.setter
    def message(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca4cb6a251ce9fb46c2de848cc6119e31fc6c89ff396bebabb1ac76e061e7ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "message", value)

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "settings"))

    @settings.setter
    def settings(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60ae510e3aa8aae3a2e5d2f91ef21ae9c62f13652ab8af8be8956ed7402f055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settings", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69498b351c42834748ca382ee1e9c3b2a36f9fa54ad282a70798f15526fffb3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2ec871eff08c8b4a8fb394883efcde081bfc6428204b892404cee48b478b06a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ContactPointWecom, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ContactPointWecom, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ContactPointWecom, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5506d726364e45153cbbdb94748d464414cb943c2569aada99268c6fa12f5fa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContactPoint",
    "ContactPointAlertmanager",
    "ContactPointAlertmanagerList",
    "ContactPointAlertmanagerOutputReference",
    "ContactPointConfig",
    "ContactPointDingding",
    "ContactPointDingdingList",
    "ContactPointDingdingOutputReference",
    "ContactPointDiscord",
    "ContactPointDiscordList",
    "ContactPointDiscordOutputReference",
    "ContactPointEmail",
    "ContactPointEmailList",
    "ContactPointEmailOutputReference",
    "ContactPointGooglechat",
    "ContactPointGooglechatList",
    "ContactPointGooglechatOutputReference",
    "ContactPointKafka",
    "ContactPointKafkaList",
    "ContactPointKafkaOutputReference",
    "ContactPointOpsgenie",
    "ContactPointOpsgenieList",
    "ContactPointOpsgenieOutputReference",
    "ContactPointPagerduty",
    "ContactPointPagerdutyList",
    "ContactPointPagerdutyOutputReference",
    "ContactPointPushover",
    "ContactPointPushoverList",
    "ContactPointPushoverOutputReference",
    "ContactPointSensugo",
    "ContactPointSensugoList",
    "ContactPointSensugoOutputReference",
    "ContactPointSlack",
    "ContactPointSlackList",
    "ContactPointSlackOutputReference",
    "ContactPointTeams",
    "ContactPointTeamsList",
    "ContactPointTeamsOutputReference",
    "ContactPointTelegram",
    "ContactPointTelegramList",
    "ContactPointTelegramOutputReference",
    "ContactPointThreema",
    "ContactPointThreemaList",
    "ContactPointThreemaOutputReference",
    "ContactPointVictorops",
    "ContactPointVictoropsList",
    "ContactPointVictoropsOutputReference",
    "ContactPointWebhook",
    "ContactPointWebhookList",
    "ContactPointWebhookOutputReference",
    "ContactPointWecom",
    "ContactPointWecomList",
    "ContactPointWecomOutputReference",
]

publication.publish()

def _typecheckingstub__afc80a278584220f835a99bc85f94cf459424ad6764b82be466c0c73f6188141(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    alertmanager: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointAlertmanager, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dingding: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointDingding, typing.Dict[builtins.str, typing.Any]]]]] = None,
    discord: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointDiscord, typing.Dict[builtins.str, typing.Any]]]]] = None,
    email: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointEmail, typing.Dict[builtins.str, typing.Any]]]]] = None,
    googlechat: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointGooglechat, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointKafka, typing.Dict[builtins.str, typing.Any]]]]] = None,
    opsgenie: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointOpsgenie, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pagerduty: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointPagerduty, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pushover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointPushover, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sensugo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointSensugo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointSlack, typing.Dict[builtins.str, typing.Any]]]]] = None,
    teams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointTeams, typing.Dict[builtins.str, typing.Any]]]]] = None,
    telegram: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointTelegram, typing.Dict[builtins.str, typing.Any]]]]] = None,
    threema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointThreema, typing.Dict[builtins.str, typing.Any]]]]] = None,
    victorops: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointVictorops, typing.Dict[builtins.str, typing.Any]]]]] = None,
    webhook: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointWebhook, typing.Dict[builtins.str, typing.Any]]]]] = None,
    wecom: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointWecom, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__9ea99c45a08226c084235dd59d275eef28bf09cc6b967a7de354963ec187af4f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointAlertmanager, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33e7150102067ecc09e2ae98297edb45b1489dd536aff0dfe9a9cef0ebdded2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointDingding, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ed28e02536b2823d3866f10a36ddb70d73c0c7f750f31d0562f22eb77d0c23(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointDiscord, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc27e2f0bbb735a944dd870351565aae4f2d2e297b6e4573beb8e404e681f85e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointEmail, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7083efbc23bc53b9088417a12ada89b64d7f96374199e200739a5a3a6ef9749(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointGooglechat, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2c9d273ade5d88a5e720e81147878712602765ea1bfac1fcfcad1830d66919(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointKafka, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7a65acc24519808577034d4cdfbc14b3097a2be985a2e010f552e5d63f5124(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointOpsgenie, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a11f89a0d4f0ffdb4ef243c8b9ad2c3dcc51a513c130e7020900c48a14af1ce(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointPagerduty, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ca1d086dd3137464e5be1e9f48c77bb9fd6e3f4641588d1b4a6a5584421245d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointPushover, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ca755cbd0c328d0ac7ed428b82bb8711247be30c01f826e7e7273f2ab28f82(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointSensugo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0133b1ee9714baa647af3a78da9fde3d0805a3005fa273d89a416b41a3eb77a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointSlack, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b7c90bd438497d1da51e4e0ccccc08f305690f979bda49957c8989c9f1c78e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointTeams, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2e43c74ea7453d857dbbcaffb8b4435590e34546de40655abdd019a21147f31(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointTelegram, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__351f62c78ba3cb8e420931ae7bad38740eaadf5c5feb3f8765c91823efa1614c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointThreema, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caad4350a0366229f4ba9fd33a49d39011ab1e2f4ffa344b4a6e348b36738c83(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointVictorops, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f73486e4d3b39d524d216fbbd11b45ec0e1b05f09aa9ed4e70f47669f0fb81dd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointWebhook, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f8bc15393c591689eb184be0da383312d7931241511449e93e4a42cecfe3ee(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointWecom, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b8de0c515f98a91b1e5e7691e8bf219173ccfd643f387ec540b8c8bdcabf3ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dec3fb2b5421a1a161b4bc6ed518741c32fa8514c16e8e9c75675c668f5ff22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a55bcd5375b4ee9e72866c4580e189b78b7c8c0ab82e321b1df0614a2676bbf(
    *,
    url: builtins.str,
    basic_auth_password: typing.Optional[builtins.str] = None,
    basic_auth_user: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__787a4cbd1c0469cd309ddb7462830d9c358b20bd7c95a6164e33e81fb0177ded(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1424d08f7c770acfc30e5c5c416b79a185fba88f160d0265ca321d367e37b5c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9281650a84e647e4acd3a6efab6f717fad969715e1d85996a6f57bf2e0a9bc94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58a4a5802eae1692fbb76d1612767c7ce4e5b1ac4bb334bf788b917597e482a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f3a9d18c41ca701da1e74e9a95cd5f4a9d17cb050da41beb2f9023338c46d6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ec8a4d4a584ee15553a48c171852f0d5d6af4b548e362c69187cbbf79444c7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointAlertmanager]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712dc88141e23acea4244721f2435ef95adb2c61962240cc8d5526af6415c50f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b39767906afe43281da628c4a9557525b572b0011907f5f66b98daadaca958(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f443a6c7183bd7dab1b3a0e5ba38c395fb4da1654736e2e46e8ee3357ac1134(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b63c0ba15c07fa75bc0417f0119d773c2e6da5e8980223b5b0252e826ee8f2d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab101edd6e2518a44d2d0cfc140033ed3aaf97a6ce3a4d6d2501fe5ffa11b98(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a2fb4a6bdc7b13dc683f58fd06af57a2b719a0b4ab61953ac6f3467d549bd99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd8f02d4317bad2d39c1ff66ac2544cfc8b5368db83f2d08cfbeba85db33895(
    value: typing.Optional[typing.Union[ContactPointAlertmanager, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fc238d2d24ae713a63a82f534398dd72797dd983125d560c8132cee41237621(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    alertmanager: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointAlertmanager, typing.Dict[builtins.str, typing.Any]]]]] = None,
    dingding: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointDingding, typing.Dict[builtins.str, typing.Any]]]]] = None,
    discord: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointDiscord, typing.Dict[builtins.str, typing.Any]]]]] = None,
    email: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointEmail, typing.Dict[builtins.str, typing.Any]]]]] = None,
    googlechat: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointGooglechat, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    kafka: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointKafka, typing.Dict[builtins.str, typing.Any]]]]] = None,
    opsgenie: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointOpsgenie, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pagerduty: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointPagerduty, typing.Dict[builtins.str, typing.Any]]]]] = None,
    pushover: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointPushover, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sensugo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointSensugo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    slack: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointSlack, typing.Dict[builtins.str, typing.Any]]]]] = None,
    teams: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointTeams, typing.Dict[builtins.str, typing.Any]]]]] = None,
    telegram: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointTelegram, typing.Dict[builtins.str, typing.Any]]]]] = None,
    threema: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointThreema, typing.Dict[builtins.str, typing.Any]]]]] = None,
    victorops: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointVictorops, typing.Dict[builtins.str, typing.Any]]]]] = None,
    webhook: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointWebhook, typing.Dict[builtins.str, typing.Any]]]]] = None,
    wecom: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[ContactPointWecom, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce516f44549665b4315b456247d27c74345955251c56f3c2f04fc11970bb9976(
    *,
    url: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    message_type: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4555b6a362698f0e7adee54cb62a4630d2c426739c4fabe6d612977598f49b04(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd54b50489a894d71683302b297c14c29bd22f81e8579ecab555828ad84c92c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2964c821eead79201d1a79222dd994e57b01ef6a65418e5167b27704077f40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__541b64beb92df4544a04627bddab27033ca8440b3c0ed3996c57287aa89de6af(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ec16c5dc1c291c74d10878e470ce89be7b5faa9a8b40fb81b45b71c44c6687(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e769eea5ce88d293dae0d05f6636f4658b75171e79ca68b372d83c88bfd9916f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDingding]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53236e6a22d46894546c39dffcba89d7ce01a222f5b55b31e47c2dc8ac811840(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef68a5e71cf871f117b8a8348d801ea6a893fc1c8e1d9c46eebb4eaff3574310(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e45b40b760783d972687e36ace5dc1d17fd2f9947d72a8c03a5915539ea960(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97be0bbcea4a294b133063d474a5dddcfeaba87235b1a2d9d489c60144fbb1d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7917ed878ebb1b85e1c9012e401c97acfad81adac7b6e7df2ac80eb4af3cefa3(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f015f9d8c31abac25dfd9c4844ba52a7fd170a9c4faa4e6e0ce13e70c8eaf5da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c5547e91268fa7e7688e8a3edc7a7f02e43a86ec4b0b6e60296844b080f26b9(
    value: typing.Optional[typing.Union[ContactPointDingding, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21671d67f40a466a84a2f3035ac79fc59e94093a011ff82c3acc28487a19183d(
    *,
    url: builtins.str,
    avatar_url: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    use_discord_username: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e0838d90b0135d525487a8ba66b221efb53db3fee976e62b54761f4c1457f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6d6bb8d4b21727448c36a0df50f70699e388418a3e3d7d011f2d463f2e224bd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bfe74ca3674361c68320ef85f3f83cf58d143869736dbf0a3f07491ea46e2f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e34f969a99854b93542c491a74f908384f7ee8542e0cd5a2f2e06283c06a4f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81bc7d622d67c5046cdda5b45fc049b345e11a8737a2bef00cebafe2e2bdfdf7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b122d7cb966b212d1f702b3b77389fd28abd729926e30b6c657ca527558e5470(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointDiscord]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9801fe98239e0d4d5ae5c36b796b124da0969e04595dc43289c53db8e1850079(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d39ade1b95bdbe2b2ce4619c7820047a2f842dadb992aef66851d45e7bdca0a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45da6cbb0118057cf8b0af22d9f4d7bfb1ea86f35e389d7bdf29998dc043ff98(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053e585030ff736dcfe2031792985c33a4cbcef48118034c6563fab3aebee888(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53dc28b1509caf61cd0296e927837786b4f9994c28ca0a2cc2f7becd7cc189f9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f9f66b6aa071258206610439b1414e793e7ada9bda61ff3c07c177c7df7f887(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dfeda7819bc84fa803c7dadfe9b6abfe19ddd99a538c550edd05b94a048edcb(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab021e46a5c17ea868e14254a69a4e6155f014af13d439c46c1aa8298f959032(
    value: typing.Optional[typing.Union[ContactPointDiscord, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4269019fc00f0de419e54f9a715b514093644a7445ae21e22c0fbc3d1af5d1cc(
    *,
    addresses: typing.Sequence[builtins.str],
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    single_email: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    subject: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6389b84a77ebc99d771bfbe60b505405344f7823b0ab8d3ec4a601f7d6c93704(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5942df88a19521f466a547daabfbdce46c311d1cd61e2712a4f0238b3cdb6839(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59ce5888ad0deaa2299f34a98e6f041b2ae5b75977809260d7ea65c6f9261992(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8052f2f499c3a1acde8e22d38468d032ab4a3d69c80311eabea71d56b760de4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f85109a5bb1cfc37fc87ca494343d61392793cfff76b6e8ce117fe95313e18b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0d1652dbd5319426e4bcc43b82c6ef9b1cbaaf39fb916d4340f6d4984e00ae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointEmail]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30e6620f431920f894215c8ad8bd6552d7dae4612247ba0ca5dc8774e226b0ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d138327d63207d481aca0ed04997f493f13549da1052293b0bb3f2ac81543e1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71fc7d595793c54532ef31f73f73a03bc4a04b7028f101af5c0e319a62e9cb8c(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66f614a22ddf5ee222fd8df3499f490721d096d8ea916bf9c83f57904209bec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac9a2e4d23c950fc00aeed0f1e5881cd608e30550b357b6359a6c5d624037203(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8887bc71fbb87e81f4ff5d87b53fe25f9bcae44326c51a2b2c6375a08c799e39(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e47e579b80dbf156fb0d38632bf56f717c6418887f894b27fd314c99c542c2d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fee4027ecb2f7aa9742f32c6b3733b5e4f0fcf0529b8f034e85bd680098019c8(
    value: typing.Optional[typing.Union[ContactPointEmail, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fd10f897fb30618d8b2d7b28d757f43f7452a5e47e6c4df44e85cb171089597(
    *,
    url: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84741afa1cd63474c26359781d4f6762f8c087371ddce116e2cec2ab98ac79ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7d2e29e7c4790d34e650e32dc6714963efef968f820ca215c13cdbb916daad6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011fa6e2ef0119a4fedf7b82ac376ba2ddb20d6ef3ff94c5f28c8625abf140d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad18e9c031df9e513bdbfad2fb62616c8b296dfaaddc81071e6ed1a212bb823(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb9eb4076e0948f54f90b11fb6f521429b87a48ab191ffa007aedc366f9dc25e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb56de7ee7f5819e6ab16f307a619ffd4124a2984231976eb594cb8caf09873f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointGooglechat]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27da6acec29e1e9fd40ae3f8fd07c7645af5c96cd173f69fa63f89067ed495f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2985422d6fec16a47665cf52da581062f24dc222feb938dd91068385520e80dc(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9485dc1d2bed2f29e9331eb760f443f8796a585c62a79daf9413d087eb2fbde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58532e18eb2502cb1130bfa908f522f0628a7c875a89a23e0034695934fbb8fa(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9645291af46aa99c0ef127530d701d788dd08525c77baea977e91e73d392e6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bdfcfa9e714485b6207111397b2e47836bc326756710bcd4b240ecde99062aa(
    value: typing.Optional[typing.Union[ContactPointGooglechat, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c70d241204f0f72bc61170295bf9596aa8879f354ac1e5dd849686ad1d88d4(
    *,
    rest_proxy_url: builtins.str,
    topic: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74417e8aaee577fb3a84cd729d3c8bbc0a66958c9c08f62a1774dd6d062a2299(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2a230f94563884717d49d0dbd0b4976df10674ef4a4dc39d024bb9147960def(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88beb186ca3227615078cde0e2bc17b00bab0177b3c21b16cc0a345269be02be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e78b5d4d57e9695ab9f9ea98caa98d7ed7a29db268f87c4aa068da737f84d90d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b28a4469c762e11e28396ff7cee718b452e111c65d60c644b54d54f51baacf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef3b2882182ad6ba05eb600d98d64058a5c101ab5c9562816d4e75398eeb83c2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointKafka]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ceb7f6c511aea551e505345544fb2c8e366e9aff8292edc5de0d2d752d15aa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbc20dd772d13ee89b26bc38d988d7950c0a2863f97290119c6d7de7ce2e335(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aae7e3245797ecf7ff2015e87c6b577915a8215c1421c8d50f3cd4f1bba475d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d460755cb557f86e97fad8799dabee4d32d2539641269adfe55741cda4e143bb(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a607971cf377fff009e7d98541ea9d4ca5aceee3f7319ca9bc4998f7114c430c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0dd6d94776a6032362605642a66469fe6d2dd0a6acb41169f7f8ea7349b7aaa(
    value: typing.Optional[typing.Union[ContactPointKafka, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7103341ac45f3fad6897dd639017df76da2e6c2da1db6e0fcbe23d17399e1d26(
    *,
    api_key: builtins.str,
    auto_close: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    description: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    override_priority: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    send_tags_as: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55530d0a694c8eec8a91adbcdd8b054d7d247050024a06903e5eb9c903a5687d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb2d507f6a9616fdd3893ea0c48b68bcb8aa6cde4226dccf6b6cb5185fbdf34(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b963a08520687ba04763bfe77a88dc223898638effda3fc71f0a6267c8d634aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a7e7c7ec274b26aa3995c43f385f68c34464d78f7753c3f39f2cea9147fad32(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83cd8b0faa1229c132a1dfbf850162e0da2a91607aa71fa5951a04c6748c8551(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7aaefb73a7595338c83d99b36e313689f04f2eb0e26049b770e26ae75596857(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointOpsgenie]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6937f109d6f5d77ba4f21204be9ca82229fe4947bba09b28e67af76ce856ba9b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7336114acd6ba4b57247ddf2779419c871e87291d431c3126a61087326bc3393(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a297b48a2218e592cd5c289f560b9004f63d55b04ba623875a9cad4dbdcdf6f3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0499464080499e51bcad94a8ea992681fef8d3210904278565e37b680c8ce7b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e0076e85a0dac3d7c4cfbfd8057d58b7efc73780d76f2682b6844571096cdc6(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba13a14a4e4ee227aa96e33a73e68809e7bf2476af1b4e88ef1c92aae4ed31d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3e76dbcc654d636186ef6b150c0b81ff1fad89fa59aa7752a5cbd990f363588(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d9bf75106d92411b2f90b47d8c17cfe029ada4a0e80210499620892b59db04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37d89ed2509906b9e58d3ead3eed6e6c36c2aa0aeac5d4cebffe0d083eb0b12f(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c75f6e795e555c90500b8da97f2cfa1a319c19e0bbfdb3866dee1fcd6a945e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9e2edb7c451bfcdfb1eaa447f3735e90e99d37cbbeb921d61d37fc6c6b57fa1(
    value: typing.Optional[typing.Union[ContactPointOpsgenie, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0176f8b2fc03154506059271a0c24b9adede7c02d3ee95f747548cbdf9d08710(
    *,
    integration_key: builtins.str,
    class_: typing.Optional[builtins.str] = None,
    component: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    group: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    severity: typing.Optional[builtins.str] = None,
    summary: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11f6bc42c1a86d651f6e1859eee8e42c1fd3db0066cab44d369de376b836e99(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c3891ca9af075ebb3840abeff44eb48e3fb3c8192a5847f41503dbc512add0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a4e2a689ef79f8418a961490410fa66bf2c610144dba012534c68fd5dd8546(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658efe29ea72e10fc44ed6d475de92125948150fb3a37c7e98255798b9bd70dd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdb74056f5f5554c5becde6808e170d0a0da8f7a96a9eb49bf3cda2563cb94a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3978a7370606b06424ac5120d478e8b06c6d60ed7aa74876c3d26c002ec049d9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPagerduty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd9b0de236147d06bb0630f154d5c0d90b3d6d0cc6ad194bf0547b45296df64(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d79935a104db179cb945f4ca95c2f0568b31834f5dedaa9282d2e97bbdfaf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ec3af39a017ead9cfef85396ebbac8da61f9942bdccac1b3ff448954cdccff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__044ee8c2a28d908d27537323655e3e655b421e6dcbe90001eec5815f37d68d35(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ac11013f1693576885f06dbca7e4e5803ff48eabce03dda2fd80cd677267727(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adfd03c965db9577e9ea3149835b0740865637b36c4609b0867664c8b255fc0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83be30ba4e29a2bce19fd5073b023a5ad916075d29c949761a93c4d73e65e678(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3068d7ae210483da75b5905557235a0f393d4b31dfc200326e13db7f9c830dce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8dd12b6207572bcba47f974e66b19c64d90d7a9e6a2b77cd4a9ae98dde4d192(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d2cf4fb8cc24c8a8ff9eb64c01e72cb1b10721955026a0644b55b240128792(
    value: typing.Optional[typing.Union[ContactPointPagerduty, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6430a3c5e4fa5822bfefa26379175c3418875010f05e6f14206d2635d71e17a0(
    *,
    api_token: builtins.str,
    user_key: builtins.str,
    device: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    expire: typing.Optional[jsii.Number] = None,
    message: typing.Optional[builtins.str] = None,
    ok_priority: typing.Optional[jsii.Number] = None,
    ok_sound: typing.Optional[builtins.str] = None,
    priority: typing.Optional[jsii.Number] = None,
    retry: typing.Optional[jsii.Number] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    sound: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c638d278fed138cd89f7e8daf3439058b286933a6573cb67ec0c2fe68878e4ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1331af03b6f597e8e2106366677074fb53d8cbdceddc58da6f3936d254348b84(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b3c26161f9b5b763974b41416a23f3a01320791f9456ef8a07e96fcd4f44e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685f694a16ea7643238d2f3b2cbd3c8f9778acff14b8f100311fa65bd5c0e36f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b70baccbcfa29da1199e901930f01c4a4162088ec94285f27beb9a9b9177d9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7ec2428becd8480f8fe76e8c37ba9ae0768c7067cc46c3b1ce47b2217cd4ea(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointPushover]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a35501697c5aff5ee88c5543978e105ef376612c0a0bc0599bbe25e1df9ae6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__563a1bb7192f8d572205b83ab7df0fc96188e64ecfc912fc3dcc5b0b7f4e1097(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3614fa412342e8a690636865d2091cfa4c9c11ca9fd7502b45ddbb8583141088(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9292fe09caac19ad3b47dca00f8058c83f0fc05c31efb3bd4037cfe993377f5f(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21f18c0030286a0942c17cb8e907fced4095e3e4acb8cd02eb23daf68ccf2c3e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97fbb8ca99ee02f3f3f765bcfc988783a8c37ee92c57a41f7e23a54fd35d75e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bb754b6c695a503ae785acbbfa73fa4405d55eefcb3ddf9fcadc56768d07eb6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__687484980c9340f575437d79c94c2e475b8d06d39238e31221f93e561a058444(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5554f33d2e262d1dbe743870ce6a65a530aa1545002e88958a86ecb863841ad(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88a51044c0eac55733fcd91d61ea7bf277c4a0361b0dacc7b1253f582820ab5f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef99295f6408b4824a7bf46c8147463104521409fc9e31690bdb3691e7a134a9(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f55d0c77c483d664d4b3d9ae7112e2363c9af688e5bf4c763d4ec344b0bc730e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0b71978e94515dffe037d4351c2f768318f3b12c4388c4b8fe8906f27f5db18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d1dcef806ae800816878c14a809f12b72e76125f0d0f95f8b0469fb4bf0d350(
    value: typing.Optional[typing.Union[ContactPointPushover, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74d879225b6c3d742743e8aad6851e15881458543b034b9b82089ce7316daebb(
    *,
    api_key: builtins.str,
    url: builtins.str,
    check: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    entity: typing.Optional[builtins.str] = None,
    handler: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de3f1c391b3d5420ad8bd5762bca5243bd7c50527862cc1db91ef088dca0b74e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4e889965feb2d7220f94a20349253cc420f441e58d58508f50d6ba89267b48(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b967917c8683557d626511ba15c60695545cfc59d3e687f20c40079352d14e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa8a94ea4532d8fe2c400cd963f69aee9d847bdb9a90a38bf0da7080a1e8917c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea05fe351c2f0a394f94f58c4c474ac13f164a1b7bfbd6db74b649b15680949(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d653cc177b7cab492b101c6f7efc502141ae939153730ccaf7d4b1c918c48130(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSensugo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff1cd3a26e42f6414032a265c1f4dbfb318e054db3b913686e9a8480f0b9c25d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cc8cc16e2ff35fe390a67e9ed98c5151dcfe2e9feb8fb9451e02f2650243c4a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8469db4827b94eca18b1115e14ed8b1c055ac112a8db255e1e13b3ad2094ecad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9f097e8de0e862a5946f8d21d28703ec79c4287a609509abe94702827540df(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb034828a2c6724d859ad1fda4a2d5fe1f7d5e682ba2e04caa3528be906993a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ed38b3323164947d35cc74feb2dda5e845508e8811a826c739c876c4e27446(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f595e4b3a948c8242a5c290a99b2cafc09f518d7b3a6c68d3265727877817b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be44f161e7f8e34e98f064f7a4b47b12f80c3481eedb3e17bca36f7926b6b7d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775c1b6ef8b4a494c3cee0837cbf1819a16b86d530910a608285e924bd1d6ea6(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d33962ac80abb061ec9bbc9965a23f5b657ae1955de4f91ff322927b6ffcbb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429773d92bd5fe841043bc248d91ad499934ddba3edfcd30763aea07f4628093(
    value: typing.Optional[typing.Union[ContactPointSensugo, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7574723ee47f77f4da05ec2720b374b156c39e8c7b8a5bb5b9af8e0aee1ea843(
    *,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    endpoint_url: typing.Optional[builtins.str] = None,
    icon_emoji: typing.Optional[builtins.str] = None,
    icon_url: typing.Optional[builtins.str] = None,
    mention_channel: typing.Optional[builtins.str] = None,
    mention_groups: typing.Optional[builtins.str] = None,
    mention_users: typing.Optional[builtins.str] = None,
    recipient: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    text: typing.Optional[builtins.str] = None,
    title: typing.Optional[builtins.str] = None,
    token: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6532f72bc30f1e272942d92f2508decf96a2ad05b78a12a696c69edc9686893b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5166163e79af5e92381eb8e41bca67f4507eafba949180becac7509311e5ef6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be677b248fd57a57b7edfc348959c6b6e9d47fb048c12c795a526097f570608b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b82d22c2a02823358c36335dd116b759a02a060460560a63f3e1e34ffa3af1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dedebd2a40b51659b363916fc4e1bfd2b46f74bf17bed7be212ca27593e15e2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f60730c1bee7540491b06319bca64f1de11367f1fcaa9da811b8c3d61d4572c3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointSlack]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c2c3b7871d4219a8173c3c9fefd0acbf51218b3135a4f416b3687e16d36960(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b41829f5b4afa72f6c33ffb4690c8801d9c24701a9f4b56d33ba885c19b496e(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd6a8ef62baec016145dd0c31a7c3a2ff5dcf3ca8baa33b59d6f540a1edf663(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de24734c6faa25705207812a0390d7abf5032272cdc2efc0471d81ba6d9601bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__256403ebd076a801dc77c01ac269724ec8a7b6506ddffd969de415ab04022046(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f85d1d4f27824724a051d30f554ef5a283409dc0ce8f2e202ed12ec78fb138(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eba729e252cc450ae4657ad43f148a6c4216f9e41aa109c0891d01bcb3e072df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__827bd1b2792677309e02e3d14df98d0ad1f8ba9ff216147d69bfb34bb6f6709a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b7638d1bb1b2f0c9228b6a274fbf090e7ac06d9577b5dd342f86c8c8607488(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc5aefd131e6cd931c5047669327ad4509b758fdad231c637ecc27f88c19c84a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50afe4c0517d2ad457d3ef118faef9b841b0159f11618bb9e8eaf74e362a95d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a72fbeb13a9f5305ceb4b9b0dda306b8ef15f72758be22cf60896314602a1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bade15857e26d6918c803fc4d5fd16035cdb00fe49ccea874fe40075b5b2563(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2de6430fa99b3a992b9e2ef29dab40e049a8c33858673ba959fdb6614935e80a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6cd7c7ca02dbcb90a4c4dd38051cf36a6ec53382654dfce14ae64aa05ed8cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33048163d80b3a9a59d6ca2ed9180d764f511635aa6c4f6dbb1f83c0569f140(
    value: typing.Optional[typing.Union[ContactPointSlack, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d54d9f975d28c1dec116542a9f5cda49536bfa83a03bc9f6a665286ba6683db0(
    *,
    url: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    section_title: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c042aac6cda205bad3ae6d6738921058379629a8ebffc5ea25673558d23c48d1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d964a2dd4f698b1d0536b018a60cbdba88918ff57ba176e4429dee6a0e60a12(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aec072170ce97b5b71bcddab0bda26724060f6467c3221e5053a67c59d4cf68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00af004757138f20b30a194a52f92ba13c4c30d8c5386fe0b7b9295c4468594(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05981874f5d1dc140fa8173e32cb80a9132783e2cdc370a50b582839e7b9d107(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab497c9bb66e418c00519076f8cd4135e192ec0c19bb893e2f1e0f1a1b5da107(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTeams]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e777d0fb0774a1579c3eb3900cbdab486352bfad0e8baf18cab4c2412de4f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79bcfec232789c771b32af705b73dd54834d470140986cd461922c59b45fd517(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04de0f21d0cce2e911732b300805c9be5bc3e3e51c595a0f4624c1fa6e5f0a3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e31890756cfe22e52bda2102f33b3434e133162f11be8d86c5ebc65a3cf3c35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef6362dc2d3c44029991d40bf9b15b7ea2431e7ac7b569873065d620078414a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f18ac0b2072c51f30a987feabb3cad3a123efcd01906600ab7af50efe1d657ba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d289b0b85276e0a2a636f3bf5456acd0dcae98ec2ddb57d8a08e15a4abd748(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67288a850ba0dd87d188c613d4bd7dcdd3ca54b1ac7e33daf99e88d3f8f934fc(
    value: typing.Optional[typing.Union[ContactPointTeams, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8c133ff2d171f19a5cf9aa31c8a3fe51792e5a480d499492f53b9499a2be512(
    *,
    chat_id: builtins.str,
    token: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0224048fb5038ade33108f0db60be7cbeec13b2bc9b92938c3c53c2639d8b347(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66ed7955e7957e4f554300f182528adf612ddfc7e918b6b2d66bd2eac9663ff6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456a1fd319175e7ca3fbed9bb2fcf625fd29933f529d922fbf5b1b4ba6b92395(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2bdf15d1e98ea7b8ab2e18e858109382de9758630337be86225bcaf9c2b065c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a761d2b4d8683d232764aeead966e884b6c470605dd61656978c9ed5e8f3360b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6edf3dc3557210e1c1b8ca9884bd4016ca09380ca58af6d611f44ff958674b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointTelegram]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1fefab0ce1f02614f69e7b82cf6d8561446c532c5ef9bbae65ffb73e8e800d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b66a972e3da4145a5ed3d05a016141abf8babd8bb33007c5f88167c8fc7070c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f640e7e17d2f10f2cd71437b3b2fca8f9c035584dc72f82d90d37df61fe3dff0(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c1fd985400bc2fe32f1876ffcd678067a959680c20663893b55c8e4eb744db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a57c03e1af6812b4670eca637f6e38cc9bdada7d9da39b0624c29741fe73383(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__051867d6cadd97cf0eca8d1b873a2c0948250e4f01eb92ed8909903f9ce40d98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08576c1ddc64701cc5b5657a41cc1f570f7a2690618bdebcd9b5b528606098fa(
    value: typing.Optional[typing.Union[ContactPointTelegram, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00fac38220abd2fa709b92d9e320ea5f4b5bccc7bd346ebcf2cf9c484f7b953e(
    *,
    api_secret: builtins.str,
    gateway_id: builtins.str,
    recipient_id: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a513e8b18a22a21df2e4bff9c4a2b84e4e2a89025b561ba0f221e72c3446d72c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a993da7b2d832e2799a8ff6a4b9286052683c5a3496ec8fd8a6d4e6713b95de(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f166f7d58d725603a5956d9426b691582724d8d7c9eeb825ac03b22dd804df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d014dd4e419463d42eb344f4e5680f75699f7c3a1d4cc9423de4caca7cb4793(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cac7664f37ecc7ddeeacbaf219853be734aa4883fa766776e497e8e7c6b5bbd8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77aa320b0e06057ac1b5e1d67a5e36dc186315af31ff07b56b75a1da8941766d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointThreema]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da2d89d694df44fb8517fea6fd91b2de0a65a3612b8f88a06ab556a90ef4896(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf6d7b8ebf52605c0d53cad158c140df93beb0a20feba8e9d155e90f8c64211(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d75400cbcbcb01019fae547644abc4dbb46522565cf18a747d32d521ba450511(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a8f9ccae37d94b9f2df04d7ad5061e35a206f7c230d67a1fa630b07c6396a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8eaa6b976bedd2ed4a9c6ebde7328cf0ad2e10f10c982ec5ab21f3eb9b1938(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c081a3a6a30add56fd35c0ce57aeee92a1c91dab86f2b107724d1950e40ba8d(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9d79dfd31e1a64882a3b2e9fc20b2d90b7cbf57f664aec8a0fe932dc15daf6e(
    value: typing.Optional[typing.Union[ContactPointThreema, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699fd5524aa517ff3b438ac5cd8bbf5f77f9890179f26299d153f3bf4934022c(
    *,
    url: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message_type: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3f0be014a7f31e3714e7079032d711bc06a609605bf98a3b1b745aef37dd66(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25c8f607a6b72f8c01719bcc3e764a16c93be90ca903bad8631e0b0e2b4f043b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cadb6209d558a42c880fc6a6b6b7a3fa10e35762ac5391530d098441590cc2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2f68f43b261d6e97e720b65419602a0fda27b01be4eda1eae829b7afa7137ae(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d7402cad81a9d0ccfb3be0e365ccb931352695527bd122c9a4b2cd566db666(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce730ebc311aac1d527e5b9a2c12c2b802c9907be3d33c281f7e4a6fd919f7d8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointVictorops]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31b707b2a50ae0781efd54ee97e032a5e906a4fde7ce8eda5cf8ab0e4579351c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f107009334723533b306757378d6195fffe9d472d1b05bb0251cbabfed45449(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23be4b2619c66c01d8fdc7ef622212000d9bc218c2879a01021ada56c6690586(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e6af5487ea7bfe747ca35721cee2b59ec19eada977453fc16a95f59180a68b(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f92c0e0444c6defc6506d39b7453045ce71e7381136aa523b6c5e7efc5f5d52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb7f1b044edcec4892e5bf96f3a7fa8cb58cf6f5e3f20992d36229fdeb2eaf9(
    value: typing.Optional[typing.Union[ContactPointVictorops, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41435e324c95942d4bee93c09ebd724bffa180ec4cab8cbc09b331e604ebc996(
    *,
    url: builtins.str,
    authorization_credentials: typing.Optional[builtins.str] = None,
    authorization_scheme: typing.Optional[builtins.str] = None,
    basic_auth_password: typing.Optional[builtins.str] = None,
    basic_auth_user: typing.Optional[builtins.str] = None,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    http_method: typing.Optional[builtins.str] = None,
    max_alerts: typing.Optional[jsii.Number] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3d046fed3d86d6ef7565feff1849f395e19d5c493e5be6101ad69ebffc3046(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__200c97ecc6493ea105daef71a035ee5d6d96b899131d0ebf8038ddf542484f6c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022deca57d03996dbbcafbb6999abb12d745b72f08beed4f5968293263c59867(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eac8f98b2921c112f5d042df762458115aa9dcb8dfb05ce55bd81ef0e2097833(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf157e08bcf499b8fae7ae557fb0028a81bf8434222740fccb463454c1b5a91(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd5d5904335afc712bcc284162a43b31a1aa5ee866d1246d3433c9200b99610(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWebhook]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dada53544076046841a2c85dcde97ff6286c84f6c5f67ce47a92904a48b3c38f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dad0d188ce57c89500cec611ecaaa370400a8a3a6387a33ac992b68cde16587c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fae5604e5e0fcb841e25795329d96526a585f06b58083e0fcb94f0a9c2fe4657(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8db3c59fc1272fef77e4b26a747ccbb2f210681bbf0c310cd285798740ee06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3747b29277e5ee06f5a2d34f2f18238a0b9ddd0a40f01299f08955ff67fcbab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b706cdb04d819ac573d27b53797ed2aa0b8f200f0cbc5aac9138e0346534eb8d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__553271ea544fcfbe3909ca193cdc0e318bb9a69bd7e85377a0cc9a18b26eeb51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51522b494de93f462ff401951dc474ebe6946181d0007f224c1a3e6a26c063d0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2677758945457652e176af3da0142fda5dd0756a7f694e55e2687317022b844a(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__164ad477bb44a6f24029a19ec6d59e85b34c7f46cec2a497d9885b445d1c1fc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e89a02141b2969e90370573d502734a214c67d26139bda3bdf5001ecdfa603(
    value: typing.Optional[typing.Union[ContactPointWebhook, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6648e36c89f5337ec42994e0c4d6e7ee2f167bccd7769e6f92cf3ae8d9bfeedc(
    *,
    url: builtins.str,
    disable_resolve_message: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    message: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    title: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bbb56d44bea829c5617482b32189deae6ddb1d09daf880da7b046d370dc20db(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13a1edd9beb2c0e73fa08a0356daeab992bb58fce6fc0f6065980a93df9c3a24(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f38b0570423e90fce61e593f9e8a3853e0bf46874eec28abea072a17874a0fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e2e2eeae00110e49f523b4942a23b0039f2e775186a7a84a259e311bedd6b0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__641bbd5446491782d387c4b5877f464e35966e7e075eb8b364d0050f9146f309(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c561d60e769af539950958b419153c78c882fed0c82b0a664080ba7b370d15c0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[ContactPointWecom]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5901dcb0f7f2f7fb248b41f0fd44d4341645dc0c817971968df409c4f669119d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c50f0c01a93f57567bc29a4f799b8df19157d7ce6aed194622fc92980121db0d(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca4cb6a251ce9fb46c2de848cc6119e31fc6c89ff396bebabb1ac76e061e7ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60ae510e3aa8aae3a2e5d2f91ef21ae9c62f13652ab8af8be8956ed7402f055(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69498b351c42834748ca382ee1e9c3b2a36f9fa54ad282a70798f15526fffb3d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2ec871eff08c8b4a8fb394883efcde081bfc6428204b892404cee48b478b06a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5506d726364e45153cbbdb94748d464414cb943c2569aada99268c6fa12f5fa5(
    value: typing.Optional[typing.Union[ContactPointWecom, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
