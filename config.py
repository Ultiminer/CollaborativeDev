# -*- coding: utf-8 -*-
# Name: config.py
# Authors: Stephan Meighen-Berger
# Config file for the pdm package

import logging
import numpy as np
from typing import Dict, Any
import yaml

_baseconfig: Dict[str, Any]

_baseconfig = {
    ###########################################################################
    # General inputs
    ###########################################################################
    'source': {
        'x': 1,
        'y': 1,
        'z': 1,
    },
    
    'detector_pos': {
        'x': 1,
        'y': 1,
        'z': 1,
    },
    'detector_geo': {
        'no_layers' : 1,
        'layer_width' : 2,
        'layer_height' : 2,
        'layer_dist' : 2,        
    },
    'particle_char' : {
        'speed_const' : 1,
    },

    'detector_char' : {
        'resolution' : 5e-6
    },

    "general": {
        # Random state seed
        "random state seed": 1337,
        # Output level
        'debug level': logging.ERROR,
        # Location of logging file handler
        "log file handler": "../run/pdm.log",
        # Dump experiment config to this location
        "config location": "../run/config.txt",
        "detector": ["IceCube",   "POne", 'combined'],
        "pone type": ["new", "old"],
        "year": range(0, 10),
        'density': ['NFW', 'Burkert'],
        "channel": ["W", "\[Tau]", "b", "All", "\\[Nu]\\[Mu]", "\\[Nu]\\[Tau]",
                    "\\[Nu]e"],
    },

    "simulation parameters": {
        "mass grid": np.logspace(2, 6, 9),
        "sv grid": np.logspace(-26, -21, 9),
        "uptime": 10 * 365 * 24 * 60 * 60,
        "low energy cutoff": 5e2,  # GeV
        "high energy cutoff": 5e6,  # GeV
        "DM type k": 2
    },

}


class ConfigClass(dict):
    """ The configuration class. This is used
    by the package for all parameter settings. If something goes wrong
    its usually here.

    Parameters
    ----------
    config : dic
        The config dictionary

    Returns
    -------
    None
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # TODO: Update this
    def from_yaml(self, yaml_file: str) -> None:
        """ Update config with yaml file

        Parameters
        ----------
        yaml_file : str
            path to yaml file

        Returns
        -------
        None
        """
        yaml_config = yaml.load(open(yaml_file), Loader=yaml.SafeLoader)
        self.update(yaml_config)

    # TODO: Update this
    def from_dict(self, user_dict: Dict[Any, Any]) -> None:
        """ Creates a config from dictionary

        Parameters
        ----------
        user_dict : dic
            The user dictionary

        Returns
        -------
        None
        """
        self.update(user_dict)


config = ConfigClass(_baseconfig)
