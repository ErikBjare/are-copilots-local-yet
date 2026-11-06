import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from refresh import merge  # noqa: E402
from status import compute_status  # noqa: E402

AS_OF = date(2026, 11, 1)


def st(section="completion", entry=None, **meta):
    return compute_status(section, entry or {}, meta, AS_OF)


def test_archived_beats_recent_push():
    assert st(archived=True, pushed_at="2026-10-30") == "archived"


def test_age_thresholds():
    assert st(pushed_at="2026-09-01") == "active"
    assert st(pushed_at="2026-05-01") == "maintained-slowly"
    assert st(pushed_at="2025-10-01") == "abandoned"


def test_superseded_and_override():
    assert st(entry={"superseded_by": "X"}, pushed_at="2026-10-30") == "superseded"
    assert st(entry={"status": "archived"}, pushed_at="2026-10-30") == "archived"


def test_models_have_no_staleness_and_unknown_is_none():
    assert st("models", pushed_at="2020-01-01") is None
    assert compute_status("completion", {}, None, AS_OF) is None


def test_merge_keeps_fetched_at_when_unchanged():
    old = {"stars": 5, "fetched_at": "2026-01-01T00:00:00Z"}
    assert merge(old, {"stars": 5}, "2026-02-01T00:00:00Z") is old
    assert (
        merge(old, {"stars": 6}, "2026-02-01T00:00:00Z")["fetched_at"]
        == "2026-02-01T00:00:00Z"
    )
