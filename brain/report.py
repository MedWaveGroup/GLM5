"""Team-performance skeleton from the standing daily targets."""

from __future__ import annotations

TARGETS = {
    "hq_bookings": 20,
    "whatsapps": 2000,
    "sales": 2,
}

_ALIASES = {
    "hq": "hq_bookings",
    "hq_bookings": "hq_bookings",
    "bookings": "hq_bookings",
    "whatsapps": "whatsapps",
    "whatsapp": "whatsapps",
    "messages": "whatsapps",
    "wa": "whatsapps",
    "sales": "sales",
}


def normalise_numbers(numbers: dict | None) -> dict[str, float | None]:
    found: dict[str, float | None] = {key: None for key in TARGETS}
    for key, value in (numbers or {}).items():
        canonical = _ALIASES.get(str(key).lower().replace("-", "_"))
        if canonical is None or value is None or value == "":
            continue
        found[canonical] = float(value)
    return found


def _status(actual: float | None, target: float) -> str:
    if actual is None:
        return "no number yet"
    if actual >= target:
        return "on target"
    return "behind"


def build_report(numbers: dict | None = None) -> dict:
    actuals = normalise_numbers(numbers)
    rows = []
    for key, target in TARGETS.items():
        actual = actuals[key]
        gap = None if actual is None else round(target - actual, 2)
        rows.append(
            {
                "metric": key,
                "target": target,
                "actual": actual,
                "gap": gap,
                "status": _status(actual, target),
            }
        )
    return {
        "title": "Team performance",
        "period": "day",
        "targets_source": "Davide, 1 Nov 2026 engine-room targets",
        "rows": rows,
        "setters": "Erich, Eddie, Michael, Hazel — 3 to 5 HQ each.",
        "closers": "Andries (Discovery) and Elmien (Clinical). Davide takes calls when the closers are full.",
        "reporting_rule": "Report every HQ booking with both the setter and the calendar owner.",
        "route": "rule",
        "escalate_paid": False,
        "escalate_human": False,
        "reason": None,
    }


def render_report(report: dict) -> str:
    lines = [
        f"# {report['title']}",
        "",
        "Targets: 20 HQ bookings a day, 2,000 WhatsApps a day, 2 sales a day (40 a month).",
        f"Source: {report['targets_source']}.",
        "",
        "| metric | target | actual | gap | status |",
        "|---|---:|---:|---:|---|",
    ]
    labels = {
        "hq_bookings": "HQ bookings",
        "whatsapps": "WhatsApps",
        "sales": "Sales",
    }
    for row in report["rows"]:
        actual = "—" if row["actual"] is None else _fmt(row["actual"])
        gap = "—" if row["gap"] is None else _fmt(row["gap"])
        lines.append(
            f"| {labels[row['metric']]} | {_fmt(row['target'])} | {actual} | {gap} | {row['status']} |"
        )
    lines += [
        "",
        f"Setters: {report['setters']}",
        f"Closers: {report['closers']}",
        f"Rule: {report['reporting_rule']}",
        "",
        "Route: rule. Paid model: no. Human: no.",
    ]
    return "\n".join(lines) + "\n"


def _fmt(value: float) -> str:
    if float(value).is_integer():
        return str(int(value))
    return str(value)
