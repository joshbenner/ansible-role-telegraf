import toml
import json

from ansible.plugins.filter.core import to_json


def to_telegraf_toml(data):
    # toml lib doesn't know what to make of Ansible strings, but passing it
    # through json lib first gets things into a shape toml recognizes.
    return toml.dumps(json.loads(to_json(data)))


class FilterModule(object):
    def filters(self):
        return dict(
            to_telegraf_toml=to_telegraf_toml
        )
