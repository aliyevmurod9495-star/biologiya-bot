# -*- coding: utf-8 -*-
"""
10-sinf Biologiya (Yangi darslik - 2022/2025): Yopiq testlar (Javob yozish)
Barcha 10 ta mavzu bloki bo'yicha 440 ta test savollari va javoblari.
"""

import os
import json
from typing import List, Dict, Any

_base_dir = os.path.dirname(os.path.abspath(__file__))
_json_path = os.path.join(_base_dir, "yopiq_tests.json")

with open(_json_path, "r", encoding="utf-8") as _f:
    YOPIQ_TESTS_10: List[Dict[str, Any]] = json.load(_f)
