---
name: source-extraction
description: Extract context from source documents (PDF, DOCX) and existing code before spec work begins.
---

# Source Extraction

Extract readable text from source documents and relevant context from existing code.

## What It Reads

### Source Documents
- PDF files (*.pdf)
- Word documents (*.docx)
- Any binary format the spec-agent cannot read directly

### Existing Code
- Relevant source files in the codebase
- Existing patterns and conventions
- API contracts, data models, configurations

## When to Use

**Documents:** Run when `docs/sources/` contains binary files that need extraction before spec work.

**Existing code:** Run when building on an existing codebase to understand current patterns, conventions, and integration points.

## Process

### Document Extraction

PDF:
```powershell
python .kiro/scripts/extract-pdfs.py "docs/sources"
```

DOCX:
```powershell
python .kiro/scripts/extract-docx.py "docs/sources"
```

Or use pandoc:
```powershell
pandoc -f docx -t markdown "file.docx" -o "file.md"
```

Output: `docs/sources/extracted_text.md`

### Code Context Extraction

Identify and summarize:
- Directory structure relevant to the feature
- Existing patterns (naming, architecture, error handling)
- Related services, controllers, components
- Data models and API contracts
- Test patterns

Output: Summary in decisions.md or inline notes for spec-agent.

## Output Format

### Documents
Single markdown file with:
- One `# heading` per source file
- `## Page N` for each page (PDFs)
- Full text content preserved

### Code Context
Summary covering:
- Relevant existing files and their purpose
- Patterns to follow
- Integration points
- Conventions to maintain

## Notes

- Hebrew text extracts correctly with UTF-8 encoding
- Tables may lose formatting — review manually if critical
- Images are not extracted — note their locations for later
- For large codebases, focus extraction on the area being modified
