import json
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [
        {"buildername": "html", "srcdir": "doc_test/doc_directive_only", "tags": ["tag_a"]},
    ],
    indirect=True,
)
def test_need_excluded_under_only_a(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    needs_list = json.loads(Path(app.outdir, "needs.json").read_text())

    assert "req_001" in html
    assert "req_002" not in html
    assert "req_003" in html
    assert "req_004" in html

    assert "req_001" in needs_list
    assert "req_002" not in needs_list
    assert "req_003" in needs_list
    assert "req_004" in needs_list


@pytest.mark.parametrize(
    "test_app",
    [
        {"buildername": "html", "srcdir": "doc_test/doc_directive_only", "tags": ["tag_a"]},
    ],
    indirect=True,
)
def test_need_excluded_under_only_b(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    needs_list = json.loads(Path(app.outdir, "needs.json").read_text())

    assert "req_001" not in html
    assert "req_002" in html
    assert "req_003" in html
    assert "req_004" in html

    assert "req_001" not in needs_list
    assert "req_002" in needs_list
    assert "req_003" in needs_list
    assert "req_004" in needs_list


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/doc_directive_only"}], indirect=True)
def test_need_excluded_under_only_no_tag(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    needs_list = json.loads(Path(app.outdir, "needs.json").read_text())

    assert "req_001" not in html
    assert "req_002" not in html
    assert "req_003" not in html
    assert "req_004" in html

    assert "req_001" not in needs_list
    assert "req_002" not in needs_list
    assert "req_003" not in needs_list
    assert "req_004" in needs_list
