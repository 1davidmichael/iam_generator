from policy_sentry.util import arns
from policy_sentry.writing.template import get_actions_template_dict
from policy_sentry.command.write_policy import write_policy_with_template
from policy_sentry.writing.template import get_crud_template_dict
import json

def generate_iam_policy(arn, type):
    crud_template = get_crud_template_dict()
    crud_template[type].append(arn)

    policy = write_policy_with_template(crud_template)

    response = {
        "arn": arn,
        "type": type,
        "service": arns.get_service_from_arn(arn),
        "policy": json.dumps(policy, indent=4)
    }
    return(response)