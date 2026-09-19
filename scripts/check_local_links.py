"""Validate internal anchors and local file references in index.html."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"


class ReferenceParser(HTMLParser):
    """Collect element IDs and local href/src references from HTML."""

    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[str] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        attributes = dict(attrs)

        element_id = attributes.get("id")
        if element_id:
            self.ids.add(element_id)

        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if value:
                self.references.append(value)


def is_external(reference: str) -> bool:
    """Return True when a reference points outside the local site."""

    parsed = urlparse(reference)
    return bool(parsed.scheme or parsed.netloc)


def main() -> int:
    parser = ReferenceParser()
    parser.feed(HTML_PATH.read_text(encoding="utf-8"))

    errors: list[str] = []

    for reference in parser.references:
        if reference.startswith("#"):
            target = reference.removeprefix("#")
            if target and target not in parser.ids:
                errors.append(f"Missing anchor target: {reference}")
            continue

        if is_external(reference):
            continue

        local_path = (ROOT / reference.split("#", 1)[0]).resolve()
        if not local_path.exists():
            errors.append(f"Missing local file: {reference}")

    if errors:
        print("Local link validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Local links and anchors are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
