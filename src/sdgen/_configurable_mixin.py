# -*- coding: utf-8 -*-
from copy import deepcopy

from sdgen.config import render_config, safeget


class ConfigurableMixin(object):
    _render_config_key = None
    _render_config_default_key = "default"

    def __init__(self, render_config_key=None, *args, **kwargs):
        # overwrite default class value for this instance
        if render_config_key:
            self._render_config_key = render_config_key
        # set to class name
        elif not self._render_config_key:
            self._render_config_key = self.__class__.__name__.lower()
        self._passed_config = kwargs
        self._parse_args(**kwargs)

    def _parse_args(self, **kwargs):
        """
        Parse all params and set object attributes.

        Priority of configs:
        __init__ argument > config for class > class attribute > default config
        """
        default_config = self._flat_dict(deepcopy(safeget(render_config, self._render_config_default_key)) or {})
        class_config = self._flat_dict(deepcopy(safeget(render_config, self._render_config_key)) or {})

        # update by class variables
        default_config.update(self._get_self_attributes())
        # update by config for this class
        default_config.update(class_config)
        # update by params passed to __init__
        default_config.update(kwargs)

        for (key, value) in default_config.items():
            if not key.startswith('_'):
                setattr(self, key, value)

    def _get_self_attributes(self):
        """
        Returns dict of all instance attributes (not stating with _)
        """
        attrs = {}
        for key in dir(self):
            if key.startswith('_'):
                continue
            attr = getattr(self, key)
            # check for not functions
            if not hasattr(attr, '__call__'):
                attrs[key] = attr
        return attrs

    def _flat_dict(self, d):
        """
        Transform multi-level dict into one-level dict
        """
        flat = {}
        for (k, v) in d.items():
            k = str(k)
            if isinstance(v, dict):
                v = self._flat_dict(v)
                for (kv, vv) in v.items():
                    flat['_'.join((k, kv))] = vv
            else:
                flat[k] = v
        return flat
