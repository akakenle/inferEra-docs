#!/usr/bin/env python3
"""
Auto-translate Chinese (cn/) documentation to all target languages using Claude API.
Only processes files that were changed in the latest git commit.

Usage:
    python scripts/translate.py cn/foo/bar.mdx cn/baz.mdx
"""

import anthropic
import os
import sys
from pathlib import Path

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Target languages: directory name -> full language name
LANGUAGES = {
    "en": "English",
    "jp": "Japanese",
    "ko": "Korean",
    "zh-Hant": "Traditional Chinese",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "pt": "Portuguese",
}

# Cached system prompt — shared across all translation calls to reduce cost
SYSTEM_PROMPT = """You are a professional technical documentation translator for AiHubMix, an AI model API platform.
Translate MDX documentation files accurately and naturally while following these strict rules:

PRESERVE exactly — do not translate or modify:
- MDX/JSX component tags and their attribute names: <Card>, <Info>, <Tip>, <Warning>, <Tabs>, <Tab>, <CodeGroup>, <AccordionGroup>, <Accordion>, etc.
- All content inside code blocks (``` or ` delimiters)
- URLs, file paths, and image paths (e.g. /media/en/image.png, ../../public/cn/image.png)
- Frontmatter keys (the part before the colon, e.g. "title:", "description:")
- Variable names, API parameters, technical identifiers
- Email addresses (e.g. business@aihubmix.com)
- Import/export statements

TRANSLATE all human-readable text including:
- Frontmatter values (the text after "title:", "description:", "sidebarTitle:")
- Paragraph and heading text
- List item text
- Alt text in image references: the [...] part of ![alt text](path)
- Human-readable string attributes in components, e.g. title="Some text" in <Card title="Some text">

OUTPUT rules:
- Output ONLY the translated file content, no explanations or commentary
- Maintain the exact same file structure, blank lines, and indentation
- Do not add or remove any MDX component tags"""


def translate_content(content: str, target_lang: str, target_name: str) -> str:
    """Call Claude API with prompt caching on the system prompt."""
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=8096,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},  # cache the system prompt
            }
        ],
        messages=[
            {
                "role": "user",
                "content": (
                    f"Translate the following MDX documentation from Simplified Chinese to {target_name}.\n\n"
                    f"---\n{content}"
                ),
            }
        ],
    )
    return response.content[0].text


def translate_file(source_path: Path, lang_code: str, lang_name: str) -> None:
    """Translate a single source file and write it to the target language directory."""
    # cn/guides/quick-start.mdx -> en/guides/quick-start.mdx
    relative = source_path.relative_to("cn")
    target_path = Path(lang_code) / relative

    target_path.parent.mkdir(parents=True, exist_ok=True)

    content = source_path.read_text(encoding="utf-8")

    if not content.strip():
        print(f"  Skipping empty file: {source_path}")
        return

    print(f"  -> {target_name}: {target_path}", flush=True)
    translated = translate_content(content, lang_code, lang_name)
    target_path.write_text(translated, encoding="utf-8")


def main() -> None:
    changed_files = sys.argv[1:]

    if not changed_files:
        print("No changed files provided. Pass file paths as arguments.")
        sys.exit(0)

    mdx_files = [
        Path(f)
        for f in changed_files
        if f.startswith("cn/") and Path(f).suffix in (".mdx", ".md") and Path(f).exists()
    ]

    if not mdx_files:
        print("No translatable cn/ MDX files in the changed set.")
        sys.exit(0)

    print(f"Files to translate: {[str(f) for f in mdx_files]}\n")

    for source_path in mdx_files:
        print(f"Processing: {source_path}")
        for lang_code, lang_name in LANGUAGES.items():
            try:
                translate_file(source_path, lang_code, lang_name)
            except Exception as exc:
                print(f"  ERROR ({lang_name}): {exc}", flush=True)
                raise  # fail the workflow so the error is visible in Actions logs
        print()

    print("All translations complete.")


if __name__ == "__main__":
    main()
