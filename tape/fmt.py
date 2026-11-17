"""Formatting shared by the terminal report and the dashboard. Kept free of pandas so it's cheap to import."""

from __future__ import annotations

import math


def fmt_metric(value: float | None, spec: str, suffix: str = "") -> str:
    """`value` formatted with `spec`, or "n/a" when the metric is undefined (None from JSON, or NaN)."""
    if value is None or not math.isfinite(value):
        return "n/a"
    return f"{value:{spec}}{suffix}"
