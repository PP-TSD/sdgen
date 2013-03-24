# -*- coding: utf-8 -*-
from sdgen.config import render_config, safeget


class ConfigurableMixin(object):
    render_config_key = "default"
    _render_config_default_key = "default"
    default_render_config = {}

    def __init__(self, render_config_key=None, *args, **kwargs):
        # overwrite default class value for this instance
        if render_config_key:
            self.render_config_key = render_config_key
        self._parse_args(**kwargs)

    def _parse_args(self, **kwargs):
        for (key, default_value) in self.default_render_config.items():
            var_name = key.replace(".", "_")
            value = kwargs.get(var_name) or self.from_render_config(key) or default_value
            setattr(self, var_name, value)

    def from_render_config(self, key):
        return (safeget(render_config, ".".join((self.render_config_key, key))) or
                safeget(render_config, ".".join((self._render_config_default_key, key))))
