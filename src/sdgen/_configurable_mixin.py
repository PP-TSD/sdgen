# -*- coding: utf-8 -*-
from copy import deepcopy

from sdgen.config import render_config, safeget


class ConfigurableMixin(object):
    render_config_key = "default"
    _render_config_default_key = "default"

    def __init__(self, render_config_key=None, *args, **kwargs):
        # overwrite default class value for this instance
        if render_config_key:
            self.render_config_key = render_config_key
        self._parse_args(**kwargs)

    def _parse_args(self, **kwargs):
        default_config = self._flat_dict(deepcopy(safeget(render_config, self._render_config_default_key)) or {})
        class_config = self._flat_dict(deepcopy(safeget(render_config, self.render_config_key)) or {})

        default_config.update(class_config)
        default_config.update(kwargs)

        for (key, value) in default_config.items():
            setattr(self, key, value)

    def _flat_dict(self, d):
        flat = {}
        for (k, v) in d.items():
            if isinstance(v, dict):
                v = self._flat_dict(v)
            flat[k] = v
        return flat

    # def from_render_config(self, key):
    #     return (safeget(render_config, ".".join((self.render_config_key, key))) or
    #             safeget(render_config, ".".join((self._render_config_default_key, key))))
