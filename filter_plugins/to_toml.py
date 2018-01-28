import toml


class FilterModule(object):
    def filters(self):
        return dict(
            to_telegraf_toml=toml.dumps
        )
