#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Serhii Horelskyi (https://github.com/kt315ua)

# JSON Library
from json import load as json_load
import random

# Constants Library
from constants import (
    SCRIPT_PATH, CONST, TEXT
)


def get_data():
    with open(CONST["F_UKRAINER"], 'r') as f:
      data = json_load(f)
    return data


def get_poll():
    data = get_data()
    quesrtion_id = random.randrange(0, len(data))
    _question = data[quesrtion_id]["Poll_Q"]
    _answers = list(data[quesrtion_id]["Poll_A"])
    _correct_id = data[quesrtion_id]["Poll_C_A"]
    q_data = {
        "Poll_Q": _question,
        "Poll_A": _answers,
        "Poll_C_A": _correct_id
    }
    return q_data
