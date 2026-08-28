from __future__ import annotations

from gaussian_scraper import extractor, fetcher
from gaussian_scraper.extractor import extract_relevant_passages
from gaussian_scraper.fetcher import fetch_page_text


# --- extractor tests ---

def test_extract_returns_passages_containing_keywords():
    text = "\n".join([
        "Load the Gaussian module before submitting your job.",
        "This line has nothing relevant in it at all and is long enough.",
        "Use %mem and %nproc in your Gaussian input file to request resources.",
        "Another irrelevant line that contains no matching keywords whatsoever.",
    ])

    results = extract_relevant_passages(text, keywords=["gaussian", "%mem"])

    assert any("Gaussian" in p for p in results)
    assert any("%mem" in p for p in results)


def test_extract_ignores_short_lines():
    text = "\n".join([
        "Gaussian",              # too short
        "g16",                   # too short
        "Use Gaussian 16 with the appropriate memory settings in your Slurm script.",
    ])

    results = extract_relevant_passages(text, keywords=["gaussian", "g16"])

    assert len(results) == 1
    assert "Use Gaussian 16" in results[0]


def test_extract_returns_empty_when_no_matches():
    text = "\n".join([
        "This documentation page is about a completely unrelated topic.",
        "There are no chemistry keywords anywhere in this passage at all.",
    ])

    results = extract_relevant_passages(text, keywords=["gaussian", "g16"])

    assert results == []


def test_extract_caps_results_at_max_passages(monkeypatch):
    monkeypatch.setattr(extractor, "MAX_PASSAGES_PER_SOURCE", 3)

    # Build more lines than the cap allows.
    lines = [
        f"Use Gaussian with nproc and mem settings for job number {i}."
        for i in range(10)
    ]
    text = "\n".join(lines)

    results = extract_relevant_passages(text, keywords=["gaussian"])

    assert len(results) == 3


def test_extract_deduplicates_repeated_lines():
    text = "\n".join([
        "Load the Gaussian module before submitting your job.",
        "Use %mem and %nproc in your Gaussian input file for resources.",
        "Load the Gaussian module before submitting your job.",
    ])

    results = extract_relevant_passages(text, keywords=["gaussian"])

    assert len(results) == 2
    assert results.count("Load the Gaussian module before submitting your job.") == 1


def test_extract_prioritizes_higher_scoring_passages_when_over_cap(monkeypatch):
    monkeypatch.setattr(extractor, "MAX_PASSAGES_PER_SOURCE", 1)

    weak_line = "Gaussian is mentioned here once and nothing else relevant."
    strong_line = "Use Gaussian with slurm sbatch and %mem settings for the job."

    # Weak line appears first in the document -- under the old first-match
    # behavior it would win the single cap slot. Scoring should prefer the
    # line that matches more keywords instead.
    text = "\n".join([weak_line, strong_line])

    results = extract_relevant_passages(
        text, keywords=["gaussian", "slurm", "sbatch", "%mem"]
    )

    assert results == [strong_line]


def test_extract_preserves_document_order_for_equal_scores():
    line_a = "Gaussian job number one for this test case here."
    line_b = "Gaussian job number two for this test case here."

    text = "\n".join([line_a, line_b])

    results = extract_relevant_passages(text, keywords=["gaussian"])

    assert results == [line_a, line_b]


# --- fetcher tests ---

def test_fetch_returns_none_on_request_error(monkeypatch):
    import requests

    def fake_get(*args, **kwargs):
        raise requests.RequestException("connection refused")

    monkeypatch.setattr(requests, "get", fake_get)

    text, status = fetch_page_text("http://fake-url.example.com")

    assert text is None
    assert status is None


def test_fetch_returns_none_on_non_200_status(monkeypatch):
    import requests
    from types import SimpleNamespace

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=404, text=""),
    )

    text, status = fetch_page_text("http://fake-url.example.com")

    assert text is None
    assert status == 404


def test_fetch_extracts_text_from_html(monkeypatch):
    import requests
    from types import SimpleNamespace

    fake_html = """
    <html>
      <body>
        <nav>Skip this nav content</nav>
        <p>Load the Gaussian module before submitting your job.</p>
        <li>Request memory carefully in your Slurm script.</li>
        <footer>Skip this footer</footer>
      </body>
    </html>
    """

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=200, text=fake_html, headers={}),
    )

    text, status = fetch_page_text("http://fake-url.example.com")

    assert text is not None
    assert status == 200
    assert "Load the Gaussian module" in text
    assert "Request memory carefully" in text
    assert "Skip this nav content" not in text
    assert "Skip this footer" not in text


class _FakePdfPage:
    def __init__(self, text):
        self._text = text

    def extract_text(self):
        return self._text


class _FakePdfReader:
    def __init__(self, pages_text):
        self.pages = [_FakePdfPage(t) for t in pages_text]


def test_fetch_extracts_text_from_pdf_via_content_type_header(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(
        fetcher,
        "PdfReader",
        lambda pdf_bytes: _FakePdfReader(["Load the Gaussian module before submitting your job."]),
    )
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"%PDF-fake-bytes",
            headers={"Content-Type": "application/pdf"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/download?id=123")

    assert status == 200
    assert "Load the Gaussian module" in text


def test_fetch_extracts_text_from_pdf_via_url_suffix(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(
        fetcher,
        "PdfReader",
        lambda pdf_bytes: _FakePdfReader(["Request memory carefully in your Slurm script."]),
    )
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=200, content=b"%PDF-fake-bytes", headers={}),
    )

    text, status = fetch_page_text("http://fake-url.example.com/guide.pdf")

    assert status == 200
    assert "Request memory carefully" in text


def test_fetch_returns_none_for_empty_pdf_extraction(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(fetcher, "PdfReader", lambda pdf_bytes: _FakePdfReader(["", ""]))
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"%PDF-fake-bytes",
            headers={"Content-Type": "application/pdf"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/scanned.pdf")

    assert text is None
    assert status == 200


def test_fetch_returns_none_when_pdf_parsing_raises(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    def raise_on_parse(pdf_bytes):
        raise ValueError("corrupted PDF")

    monkeypatch.setattr(fetcher, "PdfReader", raise_on_parse)
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"not-actually-a-pdf",
            headers={"Content-Type": "application/pdf"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/corrupted.pdf")

    assert text is None
    assert status == 200


class _FakeDocxParagraph:
    def __init__(self, text):
        self.text = text


class _FakeDocxCell:
    def __init__(self, text):
        self.text = text


class _FakeDocxRow:
    def __init__(self, cell_texts):
        self.cells = [_FakeDocxCell(t) for t in cell_texts]


class _FakeDocxTable:
    def __init__(self, rows):
        self.rows = [_FakeDocxRow(r) for r in rows]


class _FakeDocxDocument:
    def __init__(self, paragraph_texts, tables=None):
        self.paragraphs = [_FakeDocxParagraph(t) for t in paragraph_texts]
        self.tables = [_FakeDocxTable(r) for r in (tables or [])]


def test_fetch_extracts_text_from_docx_via_content_type_header(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(
        fetcher,
        "Document",
        lambda docx_bytes: _FakeDocxDocument(["Load the Gaussian module before submitting your job."]),
    )
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"PK-fake-docx-bytes",
            headers={"Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/download?id=123")

    assert status == 200
    assert "Load the Gaussian module" in text


def test_fetch_extracts_text_from_docx_via_url_suffix(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(
        fetcher,
        "Document",
        lambda docx_bytes: _FakeDocxDocument(["Request memory carefully."], tables=[[["samtools sort"]]]),
    )
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=200, content=b"PK-fake-docx-bytes", headers={}),
    )

    text, status = fetch_page_text("http://fake-url.example.com/guide.docx")

    assert status == 200
    assert "Request memory carefully" in text
    assert "samtools sort" in text


def test_fetch_returns_none_for_empty_docx_extraction(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(fetcher, "Document", lambda docx_bytes: _FakeDocxDocument(["", ""]))
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"PK-fake-docx-bytes",
            headers={"Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/empty.docx")

    assert text is None
    assert status == 200


def test_fetch_returns_none_when_docx_parsing_raises(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    def raise_on_parse(docx_bytes):
        raise ValueError("corrupted docx")

    monkeypatch.setattr(fetcher, "Document", raise_on_parse)
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"not-actually-a-docx",
            headers={"Content-Type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/corrupted.docx")

    assert text is None
    assert status == 200


class _FakePptxTextFrame:
    def __init__(self, text):
        self.text = text


class _FakePptxShape:
    def __init__(self, text, has_text_frame=True):
        self.has_text_frame = has_text_frame
        if has_text_frame:
            self.text_frame = _FakePptxTextFrame(text)


class _FakePptxSlide:
    def __init__(self, shape_texts):
        self.shapes = [_FakePptxShape(t) for t in shape_texts]


class _FakePptxPresentation:
    def __init__(self, slides_shape_texts):
        self.slides = [_FakePptxSlide(shapes) for shapes in slides_shape_texts]


def test_fetch_extracts_text_from_pptx_via_content_type_header(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(
        fetcher,
        "Presentation",
        lambda pptx_bytes: _FakePptxPresentation([["Load the Gaussian module before submitting your job."]]),
    )
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"PK-fake-pptx-bytes",
            headers={"Content-Type": "application/vnd.openxmlformats-officedocument.presentationml.presentation"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/download?id=456")

    assert status == 200
    assert "Load the Gaussian module" in text


def test_fetch_extracts_text_from_pptx_via_url_suffix(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(
        fetcher,
        "Presentation",
        lambda pptx_bytes: _FakePptxPresentation([["Request memory carefully."], ["bwa mem alignment"]]),
    )
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=200, content=b"PK-fake-pptx-bytes", headers={}),
    )

    text, status = fetch_page_text("http://fake-url.example.com/slides.pptx")

    assert status == 200
    assert "Request memory carefully" in text
    assert "bwa mem alignment" in text


def test_fetch_returns_none_for_empty_pptx_extraction(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    monkeypatch.setattr(fetcher, "Presentation", lambda pptx_bytes: _FakePptxPresentation([[""], [""]]))
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"PK-fake-pptx-bytes",
            headers={"Content-Type": "application/vnd.openxmlformats-officedocument.presentationml.presentation"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/empty.pptx")

    assert text is None
    assert status == 200


def test_fetch_returns_none_when_pptx_parsing_raises(monkeypatch):
    import requests
    from types import SimpleNamespace

    import gaussian_scraper.fetcher as fetcher

    def raise_on_parse(pptx_bytes):
        raise ValueError("corrupted pptx")

    monkeypatch.setattr(fetcher, "Presentation", raise_on_parse)
    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            content=b"not-actually-a-pptx",
            headers={"Content-Type": "application/vnd.openxmlformats-officedocument.presentationml.presentation"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/corrupted.pptx")

    assert text is None
    assert status == 200


def test_fetch_extracts_text_from_txt_via_content_type_header(monkeypatch):
    import requests
    from types import SimpleNamespace

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            text="Load the Gaussian module before submitting your job.",
            headers={"Content-Type": "text/plain"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/download?id=789")

    assert status == 200
    assert "Load the Gaussian module" in text


def test_fetch_extracts_text_from_txt_via_url_suffix(monkeypatch):
    import requests
    from types import SimpleNamespace

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            text="Request memory carefully in your Slurm script.",
            headers={},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/readme.txt")

    assert status == 200
    assert "Request memory carefully" in text


def test_fetch_returns_none_for_empty_txt(monkeypatch):
    import requests
    from types import SimpleNamespace

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(status_code=200, text="   ", headers={"Content-Type": "text/plain"}),
    )

    text, status = fetch_page_text("http://fake-url.example.com/empty.txt")

    assert text is None
    assert status == 200


def test_fetch_rejects_legacy_ppt_via_content_type_header(monkeypatch):
    import requests
    from types import SimpleNamespace

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            text="\x00\x01binary garbage that happens to contain gaussian somewhere",
            content=b"\x00\x01binary garbage",
            headers={"Content-Type": "application/vnd.ms-powerpoint"},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/legacy.ppt")

    assert text is None
    assert status == 200


def test_fetch_rejects_legacy_doc_via_url_suffix(monkeypatch):
    import requests
    from types import SimpleNamespace

    monkeypatch.setattr(
        requests,
        "get",
        lambda *a, **kw: SimpleNamespace(
            status_code=200,
            text="\x00\x01binary garbage",
            content=b"\x00\x01binary garbage",
            headers={},
        ),
    )

    text, status = fetch_page_text("http://fake-url.example.com/legacy.doc")

    assert text is None
    assert status == 200
