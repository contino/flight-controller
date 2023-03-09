from publisher.drivers.checkov import Checkov
from publisher.drivers.open_policy_agent import OpenPolicyAgent

SOURCE = {
    "open_policy_agent": OpenPolicyAgent,
    "checkov": Checkov,
}
