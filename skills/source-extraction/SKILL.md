---
name: source-extraction
description: Extract text from source documents (PDF, DOCX) before spec work begins. Use when docs/sources contains binary files.
---

# Source Extraction

Before spec work can begin, source documents must be readable text.

## When to use

Run this skill when `docs/sources/` contains:
- PDF files (*.pdf)
- Word documents (*.docx)
- Any binary format the spec-agent cannot read directly

## Process

### PDF extraction
```powershell
python .kiro/scripts/extract-pdfs.py "docs/sources"
```
Output: `docs/sources/extracted_text.md`

### DOCX extraction
```powershell
python .kiro/scripts/extract-docx.py "docs/sources"
```
Or use pandoc if available:
```powershell
pandoc -f docx -t markdown "file.docx" -o "file.md"
```

## Output

Single markdown file with:
- One `# heading` per source file
- `## Page N` for each page (PDFs)
- Full text content preserved

## Next step

After extraction, proceed with orchestrator startup:
```text
התחל בפרויקט. חומר המקור ב-docs/sources/extracted_text.md
```

## Notes

- Hebrew text extracts correctly with UTF-8 encoding
- Tables may lose formatting — review manually if critical
- Images are not extracted — note their locations for later
