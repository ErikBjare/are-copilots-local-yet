"""Computed project status. Pure functions, no network."""

from datetime import date

# Months without a push before a project counts as abandoned / slow.
ABANDONED_MONTHS = 12
SLOW_MONTHS = 4

# Sections where staleness is meaningless (models and datasets don't get "abandoned").
NO_STALENESS = {"models", "datasets"}


def months_between(earlier: date, later: date) -> float:
    return (later - earlier).days / 30.4375


def compute_status(
    section: str, entry: dict, meta: dict | None, as_of: date
) -> str | None:
    """Return one of active / maintained-slowly / abandoned / archived / superseded.

    A hand-set `status` on the entry wins. Returns None when nothing can be
    said (no metadata for a non-superseded entry, or models/datasets).
    """
    if entry.get("status"):
        return entry["status"]
    if entry.get("superseded_by"):
        return "superseded"
    if section in NO_STALENESS:
        return None
    meta = meta or {}
    if meta.get("archived"):
        return "archived"
    pushed = meta.get("pushed_at")
    if not pushed:
        return None
    months = months_between(date.fromisoformat(pushed[:10]), as_of)
    if months >= ABANDONED_MONTHS:
        return "abandoned"
    if months >= SLOW_MONTHS:
        return "maintained-slowly"
    return "active"
