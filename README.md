# joshbenner.telegraf

Install and configure [telegraf](https://github.com/influxdata/telegraf) metric collection agent.

## Requirements

* [toml](https://pypi.python.org/pypi/toml) Python package required on machine executing Ansible.

## Role Variables

See defaults.yml.

## Merged Variables

All telegraf configuration is done by merging all variables with specific suffixes:

Suffix                     | Description
---------------------------|-------------------------------------------
`*_telegraf_global_tags`   | Key/val pairs to set global tags.
`*_telegraf_agent_options` | Set agent-level configuration.
`*_telegraf_outputs`       | Configure telegraf outputs (ie: influxdb).
`*_telegraf_processors`    | Configure processors.
`*_telegraf_inputs`        | Configure inputs (the metric collectors).


## Example Playbook

```yaml
- hosts: telegraf_agents
  roles:
    - joshbenner.telegraf
  vars:
    my_telegraf_global_tags:
      foo: bar
      env: prod
    any_prefix_telegraf_agent_options:
      interval: 30s
    my_telegraf_outputs:
      influxdb:
        - urls: ['http://influx.example.com:8086']
          database: telegraf
          precision: s
    foo_telegraf_inputs:
      cpu:
        - percpu: true
          totalcpu: true
```

License
-------

BSD
