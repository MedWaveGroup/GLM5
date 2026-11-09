"""`brain` command line. Rules-only when Ollama is absent."""

from __future__ import annotations

import argparse
import json
import sys

from brain.ask import ask
from brain.commands import assign
from brain.decide import decide
from brain.ingest import ingest
from brain.report import build_report, render_report
from brain.triage import triage_lead


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="brain",
        description="MedWave manager brain. Local rules and local models before paid tokens.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ingest = sub.add_parser("ingest", help="Rebuild the Obsidian vault from notes or a raw export")
    p_ingest.add_argument("--raw", help="Path to a raw export (directory of memory/*.txt, or its parent)")
    p_ingest.add_argument("--notes", help="Notes directory (default: sources/notes)")
    p_ingest.add_argument("--out", help="Vault directory (default: vault/)")
    p_ingest.add_argument("--reindex-workspace", action="store_true")
    p_ingest.add_argument("--json", action="store_true")

    p_ask = sub.add_parser("ask", help="Retrieve facts and answer with a local model when one is up")
    p_ask.add_argument("question")
    p_ask.add_argument("--k", type=int, default=6)
    p_ask.add_argument("--model", help="Ollama model override, for example qwen2.5:7b")
    p_ask.add_argument("--json", action="store_true")

    p_decide = sub.add_parser("decide", help="Apply the decision model")
    p_decide.add_argument("situation")
    p_decide.add_argument("--model")
    p_decide.add_argument("--json", action="store_true")

    p_triage = sub.add_parser("triage-lead", help="HQ yes/no, calendar, and owner")
    p_triage.add_argument("payload", nargs="?", help="JSON object. Reads stdin when omitted.")
    p_triage.add_argument("--json", action="store_true", default=True)

    p_assign = sub.add_parser("assign", help="Simplest owner and next step")
    p_assign.add_argument("task")
    p_assign.add_argument("--model")
    p_assign.add_argument("--json", action="store_true")

    p_report = sub.add_parser("report", help="Team performance skeleton")
    p_report.add_argument("--numbers", help="JSON object of actuals, keys hq, whatsapps, sales")
    p_report.add_argument("--hq", type=float)
    p_report.add_argument("--whatsapps", type=float)
    p_report.add_argument("--sales", type=float)
    p_report.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)
    if args.cmd == "ingest":
        from pathlib import Path
        stats = ingest(
            raw=Path(args.raw) if args.raw else None,
            notes=Path(args.notes) if args.notes else None,
            out=Path(args.out) if args.out else None,
            reindex_workspace=args.reindex_workspace,
        )
        if args.json:
            print(json.dumps(stats, indent=2))
        else:
            print(
                f"Vault written to {stats['out']} "
                f"({stats['note_files']} notes, {stats['facts']} facts)."
            )
        return 0

    if args.cmd == "ask":
        result = ask(args.question, k=args.k, model=args.model)
        _emit(result, args.json, _format_ask)
        return 0

    if args.cmd == "decide":
        result = decide(args.situation, model=args.model)
        _emit(result, args.json, _format_decide)
        return 0

    if args.cmd == "triage-lead":
        raw = args.payload if args.payload else sys.stdin.read()
        payload = json.loads(raw)
        result = triage_lead(payload)
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == "assign":
        result = assign(args.task, model=args.model)
        _emit(result, args.json, _format_assign)
        return 0

    if args.cmd == "report":
        numbers = {}
        if args.numbers:
            numbers.update(json.loads(args.numbers))
        if args.hq is not None:
            numbers["hq"] = args.hq
        if args.whatsapps is not None:
            numbers["whatsapps"] = args.whatsapps
        if args.sales is not None:
            numbers["sales"] = args.sales
        result = build_report(numbers)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(render_report(result), end="")
        return 0

    parser.error(f"unknown command {args.cmd}")
    return 2


def _emit(result: dict, as_json: bool, formatter) -> None:
    if as_json:
        print(json.dumps(result, indent=2))
    else:
        print(formatter(result))


def _format_ask(result: dict) -> str:
    lines = [result.get("answer") or "(no answer)"]
    if result.get("rule"):
        lines.append(f"Rule: {result['rule']}")
    lines.append(
        f"Route: {result['route']}. Paid model: {_yes(result['escalate_paid'])}. "
        f"Human: {_yes(result['escalate_human'])}."
    )
    if result.get("reason"):
        lines.append(f"Reason: {result['reason']}")
    if result.get("model"):
        lines.append(f"Model: {result['model']} on {result.get('host')}")
    lines.append("")
    lines.append("Facts:")
    for fact in result.get("facts") or []:
        source = fact.get("source") or fact.get("note")
        lines.append(f"- {fact['text'][:400]}")
        lines.append(f"  source: {source} ({fact.get('note')})")
    return "\n".join(lines)


def _format_decide(result: dict) -> str:
    lines = [
        f"Ruling: {result.get('answer') or '(none)'}",
        f"Rule: {result.get('rule') or '(none)'}",
        f"Paid model needed: {_yes(result.get('escalate_paid'))}",
        f"Human needed: {_yes(result.get('escalate_human'))}",
        f"Route: {result.get('route')}",
    ]
    if result.get("reason"):
        lines.append(f"Reason: {result['reason']}")
    return "\n".join(lines)


def _format_assign(result: dict) -> str:
    lines = [
        f"Owner: {result.get('owner') or '(unassigned)'}",
        f"Next step: {result.get('next_step') or result.get('answer') or '(none)'}",
        f"Rule: {result.get('rule') or '(none)'}",
        f"Paid model needed: {_yes(result.get('escalate_paid'))}",
        f"Human needed: {_yes(result.get('escalate_human'))}",
        f"Route: {result.get('route')}",
    ]
    if result.get("reason"):
        lines.append(f"Reason: {result['reason']}")
    return "\n".join(lines)


def _yes(flag) -> str:
    return "yes" if flag else "no"


if __name__ == "__main__":
    raise SystemExit(main())
