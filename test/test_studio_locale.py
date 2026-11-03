"""Regression checks for the initial Spanish studio experience."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
I18N = ROOT / "webui" / "i18n"


def _locale(language: str) -> dict:
    return json.loads((I18N / f"{language}.json").read_text(encoding="utf-8"))


def test_studio_tagline_is_translated():
    english = _locale("en")["Translation"]
    spanish = _locale("es")["Translation"]
    assert "Studio Tagline" in english
    assert "Studio Tagline" in spanish
    assert "videos" in spanish["Studio Tagline"].lower()


def test_spanish_locale_uses_known_translation_keys():
    english = _locale("en")["Translation"]
    spanish = _locale("es")["Translation"]
    assert set(spanish).issubset(english)
    assert all(isinstance(value, str) and value.strip() for value in spanish.values())


def test_video_creation_labels_are_available_in_spanish():
    spanish = _locale("es")["Translation"]
    for key in (
        "Video Script Settings",
        "Video Subject",
        "Generate Video",
        "Video Settings",
        "Audio Settings",
        "Subtitle Settings",
        "Generation Rendering",
        "Generation Downloading",
    ):
        assert key in spanish
