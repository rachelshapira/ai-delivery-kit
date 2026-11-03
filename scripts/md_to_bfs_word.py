# -*- coding: utf-8 -*-
"""
Markdown to Professional BFS Word Document Converter

Creates Word documents matching the organizational BFS format:
- Title page with system name, document type, version
- Document info table (שדה | ערך)
- Real Table of Contents
- Numbered sections
- Professional tables with headers
- Mermaid diagrams as images
"""

import re
import sys
import tempfile
import warnings
from pathlib import Path
from datetime import datetime

warnings.filterwarnings('ignore', message='IPython is not installed')

try:
    from docx import Document
    from docx.shared import Pt, Cm, RGBColor, Twips
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.style import WD_STYLE_TYPE
except ImportError:
    print("ERROR: python-docx not installed. Run: pip install python-docx")
    sys.exit(1)

try:
    from mermaid import Mermaid
    from mermaid.graph import Graph
    MERMAID_AVAILABLE = True
except ImportError:
    MERMAID_AVAILABLE = False


def make_rtl(paragraph):
    """Make paragraph RTL with proper bidirectional text support."""
    pPr = paragraph._p.get_or_add_pPr()
    
    # Set bidi (bidirectional) - makes paragraph RTL
    bidi = OxmlElement('w:bidi')
    pPr.insert(0, bidi)
    
    # Set alignment to right
    jc = OxmlElement('w:jc')
    jc.set(qn('w:val'), 'right')
    pPr.append(jc)
    
    # Set RTL for each run in the paragraph
    for run in paragraph.runs:
        rPr = run._r.get_or_add_rPr()
        rtl = OxmlElement('w:rtl')
        rPr.append(rtl)


def make_table_rtl(table):
    """Make table RTL with visual bidi and cell direction."""
    tblPr = table._tbl.tblPr
    if tblPr is None:
        tblPr = OxmlElement('w:tblPr')
        table._tbl.insert(0, tblPr)
    bidiVisual = OxmlElement('w:bidiVisual')
    tblPr.append(bidiVisual)
    
    # Set RTL for all cells
    for row in table.rows:
        for cell in row.cells:
            for para in cell.paragraphs:
                make_rtl(para)


def set_cell_shading(cell, color):
    """Set cell background color."""
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color)
    cell._tc.get_or_add_tcPr().append(shading)


def setup_document(doc):
    """Setup document styles and page settings for Hebrew RTL."""
    # Page setup - A4 with narrow margins
    for section in doc.sections:
        section.page_width = Cm(21)
        section.page_height = Cm(29.7)
        section.left_margin = Cm(1.8)
        section.right_margin = Cm(1.8)
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2)
        
        # Set section to RTL
        sectPr = section._sectPr
        bidi = OxmlElement('w:bidi')
        sectPr.append(bidi)
    
    # Normal style - RTL
    style = doc.styles['Normal']
    style.font.name = 'Arial'
    style.font.size = Pt(10)
    style._element.rPr.rFonts.set(qn('w:cs'), 'Arial')
    
    # Set paragraph format for Normal to RTL
    pPr = style._element.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    pPr.append(bidi)
    jc = OxmlElement('w:jc')
    jc.set(qn('w:val'), 'right')
    pPr.append(jc)
    
    # Heading styles - RTL
    heading_sizes = {1: 14, 2: 12, 3: 11, 4: 10}
    for level, size in heading_sizes.items():
        try:
            h_style = doc.styles[f'Heading {level}']
            h_style.font.name = 'Arial'
            h_style.font.size = Pt(size)
            h_style.font.bold = True
            h_style.font.color.rgb = RGBColor(0, 51, 102)  # Dark blue
            h_style._element.rPr.rFonts.set(qn('w:cs'), 'Arial')
            
            # Set heading to RTL
            pPr = h_style._element.get_or_add_pPr()
            bidi = OxmlElement('w:bidi')
            pPr.append(bidi)
        except:
            pass


def add_header_footer(doc, system_name, logo_path=None):
    """Add header and footer to all sections - matching BTL reference format."""
    for section in doc.sections:
        # Header
        header = section.header
        header.is_linked_to_previous = False
        
        # Clear existing
        for para in header.paragraphs:
            para.clear()
        
        # Line 1 - Logo (centered)
        p1 = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if logo_path and Path(logo_path).exists():
            run = p1.add_run()
            run.add_picture(str(logo_path), width=Cm(1.5))
        
        # Line 2 - Organization name
        p2 = header.add_paragraph()
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p2.add_run("הביטוח הלאומי")
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.name = 'Arial'
        make_rtl(p2)
        
        # Line 3 - Department
        p3 = header.add_paragraph()
        p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p3.add_run("מנהל תקשוב ומערכות מידע")
        run.font.size = Pt(10)
        run.font.name = 'Arial'
        make_rtl(p3)
        
        # Footer
        footer = section.footer
        footer.is_linked_to_previous = False
        
        # Clear existing
        for para in footer.paragraphs:
            para.clear()
        
        p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(f"{system_name} – אפיון פונקציונלי עסקי | מסמך לאישור יחידה עסקית")
        run.font.size = Pt(9)
        run.font.name = 'Arial'
        run.font.color.rgb = RGBColor(128, 128, 128)
        make_rtl(p)


def add_title_page(doc, system_name, version, description=None):
    """Add title page matching the reference format."""
    # Add spacing at top
    for _ in range(3):
        doc.add_paragraph()
    
    # System name - large, centered
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(system_name)
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.name = 'Arial'
    run.font.color.rgb = RGBColor(0, 51, 102)
    make_rtl(p)
    
    doc.add_paragraph()
    
    # Document type
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("מסמך אפיון פונקציונלי עסקי")
    run.font.size = Pt(18)
    run.font.name = 'Arial'
    make_rtl(p)
    
    doc.add_paragraph()
    
    # Version
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f"גרסה {version}")
    run.font.size = Pt(14)
    run.font.name = 'Arial'
    make_rtl(p)
    
    # Description if provided
    if description:
        doc.add_paragraph()
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(description)
        run.font.size = Pt(11)
        run.font.name = 'Arial'
        run.italic = True
        make_rtl(p)
    
    doc.add_page_break()


def add_document_info_table(doc, info_dict):
    """Add document info table (שדה | ערך)."""
    table = doc.add_table(rows=1 + len(info_dict), cols=2)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    make_table_rtl(table)
    
    # Set column widths
    for row in table.rows:
        row.cells[0].width = Cm(4)
        row.cells[1].width = Cm(12)
    
    # Header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "שדה"
    hdr_cells[1].text = "ערך"
    for cell in hdr_cells:
        set_cell_shading(cell, "D9E2F3")  # Light blue
        for para in cell.paragraphs:
            make_rtl(para)
            for run in para.runs:
                run.bold = True
    
    # Data rows
    for i, (field, value) in enumerate(info_dict.items(), 1):
        row_cells = table.rows[i].cells
        row_cells[0].text = field
        row_cells[1].text = value
        for cell in row_cells:
            for para in cell.paragraphs:
                make_rtl(para)
    
    doc.add_paragraph()


def add_heading_with_bookmark(doc, text, level, bookmark_id):
    """Add a heading with a bookmark for TOC linking."""
    h = doc.add_heading(text, level=level)
    make_rtl(h)
    
    # Add bookmark - must wrap the first run's content
    bookmark_name = f"_Toc{bookmark_id}"
    
    # Create bookmark start
    bookmark_start = OxmlElement('w:bookmarkStart')
    bookmark_start.set(qn('w:id'), str(bookmark_id))
    bookmark_start.set(qn('w:name'), bookmark_name)
    
    # Create bookmark end  
    bookmark_end = OxmlElement('w:bookmarkEnd')
    bookmark_end.set(qn('w:id'), str(bookmark_id))
    
    # Insert bookmark at the very beginning and end of paragraph
    # This ensures the whole heading is bookmarked
    first_child = h._p[0] if len(h._p) > 0 else None
    if first_child is not None:
        h._p.insert(0, bookmark_start)
    else:
        h._p.append(bookmark_start)
    h._p.append(bookmark_end)
    
    return bookmark_name


def add_toc_with_entries(doc, headings_info):
    """Add Table of Contents with clickable hyperlinks to headings."""
    # Add TOC Heading (not as a Heading style to avoid including in the TOC itself)
    h = doc.add_paragraph()
    h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = h.add_run("תוכן עניינים")
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.name = 'Arial'
    run.font.color.rgb = RGBColor(0, 51, 102)
    make_rtl(h)
    
    doc.add_paragraph()  # Space after heading
    
    # Add TOC entries with hyperlinks
    for heading_text, level, bookmark_name in headings_info:
        p = doc.add_paragraph()
        
        # Create hyperlink element - Word uses w:anchor for internal links
        hyperlink = OxmlElement('w:hyperlink')
        hyperlink.set(qn('w:anchor'), bookmark_name)
        
        # Create run with text
        run_elem = OxmlElement('w:r')
        
        # Style properties for hyperlink (blue, underline)
        rPr = OxmlElement('w:rPr')
        
        # Font
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:ascii'), 'Arial')
        rFonts.set(qn('w:hAnsi'), 'Arial')
        rFonts.set(qn('w:cs'), 'Arial')
        rPr.append(rFonts)
        
        # Color - blue
        color = OxmlElement('w:color')
        color.set(qn('w:val'), '0563C1')
        rPr.append(color)
        
        # Underline
        underline = OxmlElement('w:u')
        underline.set(qn('w:val'), 'single')
        rPr.append(underline)
        
        # Size - 11pt for level 1, 10pt for others
        sz = OxmlElement('w:sz')
        sz.set(qn('w:val'), '22' if level == 1 else '20')
        szCs = OxmlElement('w:szCs')
        szCs.set(qn('w:val'), '22' if level == 1 else '20')
        rPr.append(sz)
        rPr.append(szCs)
        
        # Bold for level 1
        if level == 1:
            bold = OxmlElement('w:b')
            boldCs = OxmlElement('w:bCs')
            rPr.append(bold)
            rPr.append(boldCs)
        
        # RTL for Hebrew
        rtl = OxmlElement('w:rtl')
        rPr.append(rtl)
        
        run_elem.append(rPr)
        
        # Add text with xml:space preserve
        text_elem = OxmlElement('w:t')
        text_elem.set(qn('xml:space'), 'preserve')
        text_elem.text = heading_text
        run_elem.append(text_elem)
        
        hyperlink.append(run_elem)
        p._p.append(hyperlink)
        
        # Set paragraph properties
        pPr = p._p.get_or_add_pPr()
        
        # RTL
        bidi = OxmlElement('w:bidi')
        pPr.append(bidi)
        
        # Right alignment for RTL
        jc = OxmlElement('w:jc')
        jc.set(qn('w:val'), 'right')
        pPr.append(jc)
        
        # Indent for sub-levels (RTL uses right indent)
        if level > 1:
            ind = OxmlElement('w:ind')
            ind.set(qn('w:right'), str(int(Cm(0.5 * (level - 1)).twips)))
            pPr.append(ind)
        
        # Spacing
        spacing = OxmlElement('w:spacing')
        spacing.set(qn('w:after'), '80')
        spacing.set(qn('w:line'), '276')  # 1.15 line spacing
        spacing.set(qn('w:lineRule'), 'auto')
        pPr.append(spacing)
    
    doc.add_page_break()


def render_mermaid_to_png(mermaid_code, output_path):
    """Render Mermaid diagram to PNG."""
    if not MERMAID_AVAILABLE:
        return None
    try:
        graph = Graph('diagram', mermaid_code)
        m = Mermaid(graph)
        m.to_png(str(output_path))
        if Path(output_path).exists() and Path(output_path).stat().st_size > 0:
            return output_path
        return None
    except Exception as e:
        print(f"WARNING: Failed to render diagram: {e}")
        return None


def add_table_from_md(doc, table_lines):
    """Parse markdown table and add to document."""
    if len(table_lines) < 2:
        return
    
    # Parse headers
    headers = [c.strip() for c in table_lines[0].split('|') if c.strip()]
    if not headers:
        return
    
    # Skip columns that are purely technical (מזהה with IDs)
    skip_col_indices = []
    for idx, h in enumerate(headers):
        if h in ['מזהה', 'ID'] or re.match(r'^(PROC|REQ|AC|ADR|BR)-', h):
            skip_col_indices.append(idx)
    
    # Filter headers
    headers = [h for idx, h in enumerate(headers) if idx not in skip_col_indices]
    if not headers:
        return
    
    # Skip separator line
    data_start = 2 if '---' in table_lines[1] else 1
    
    # Parse data rows
    rows = []
    for line in table_lines[data_start:]:
        if line.startswith('|'):
            raw = line.split('|')[1:-1]
        else:
            raw = line.split('|')
        cells = [c.strip() for c in raw]
        # Filter out skipped columns and clean technical IDs
        cells = [clean_technical_ids(c) for idx, c in enumerate(cells) if idx not in skip_col_indices]
        if cells and any(c for c in cells):
            rows.append(cells)
    
    if not rows:
        return
    
    # Create table
    num_cols = len(headers)
    table = doc.add_table(rows=1 + len(rows), cols=num_cols)
    table.style = 'Table Grid'
    make_table_rtl(table)
    
    # Header row with shading
    for col_idx, header in enumerate(headers):
        cell = table.rows[0].cells[col_idx]
        cell.text = header
        set_cell_shading(cell, "D9E2F3")
        for para in cell.paragraphs:
            make_rtl(para)
            for run in para.runs:
                run.bold = True
    
    # Data rows
    for row_idx, row_data in enumerate(rows):
        for col_idx, cell_text in enumerate(row_data):
            if col_idx < num_cols:
                cell = table.rows[row_idx + 1].cells[col_idx]
                cell.text = cell_text
                for para in cell.paragraphs:
                    make_rtl(para)
    
    doc.add_paragraph()


def clean_technical_ids(text):
    """Remove technical IDs that business users don't need to see."""
    # Remove standalone IDs like PROC-01, REQ-001, AC-001-01, ADR-003, BR-005, Q-BIZ-004, DEC-002, NF-001
    text = re.sub(r'\b(PROC|REQ|AC|ADR|BR|Q-BIZ|Q-TECH|DEC|NF)-\d+(-\d+)?\b', '', text)
    
    # Remove references in parentheses like (ADR-003) or (Q-BIZ-004, ADR-004)
    text = re.sub(r'\s*\([^)]*(?:PROC|REQ|AC|ADR|BR|Q-BIZ|Q-TECH|DEC|NF)-\d+[^)]*\)', '', text)
    
    # Remove "קריטריוני קבלה:" sections with IDs
    text = re.sub(r'קריטריוני קבלה:\s*(?:REQ|AC)-[\d-]+(?:,\s*(?:REQ|AC)-[\d-]+)*', '', text)
    
    # Remove technical terms in backticks like `ProviderId`
    text = re.sub(r'`[A-Za-z_]+`', '', text)
    
    # Clean up double spaces and trailing dashes
    text = re.sub(r'\s*—\s*$', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text


def process_content(doc, content, temp_dir, diagram_counter):
    """Process markdown content and add to document."""
    lines = content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Mermaid diagram
        if line.strip().startswith('```mermaid'):
            mermaid_lines = []
            i += 1
            while i < len(lines) and lines[i].strip() != '```':
                mermaid_lines.append(lines[i])
                i += 1
            
            diagram_counter[0] += 1
            mermaid_code = '\n'.join(mermaid_lines)
            png_path = Path(temp_dir) / f"diagram_{diagram_counter[0]}.png"
            
            if render_mermaid_to_png(mermaid_code, png_path):
                try:
                    doc.add_picture(str(png_path), width=Cm(14))
                    p = doc.add_paragraph(f"תרשים {diagram_counter[0]}")
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    make_rtl(p)
                    print(f"  Added diagram {diagram_counter[0]}")
                except Exception as e:
                    print(f"  Warning: Could not add diagram: {e}")
            
            i += 1
            continue
        
        # Code block (not mermaid)
        if line.strip().startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            
            for code_line in code_lines:
                p = doc.add_paragraph(code_line)
                if p.runs:
                    p.runs[0].font.name = 'Courier New'
                    p.runs[0].font.size = Pt(9)
            
            i += 1
            continue
        
        # Table
        if '|' in line and i + 1 < len(lines) and '|' in lines[i + 1]:
            table_lines = []
            while i < len(lines) and '|' in lines[i]:
                table_lines.append(lines[i])
                i += 1
            add_table_from_md(doc, table_lines)
            continue
        
        # Empty line
        if not line.strip():
            i += 1
            continue
        
        # Blockquote
        if line.strip().startswith('>'):
            text = re.sub(r'^>\s*', '', line.strip())
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            text = clean_technical_ids(text)
            if not text:
                i += 1
                continue
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            run = p.add_run(text)
            run.italic = True
            run.font.color.rgb = RGBColor(80, 80, 80)
            make_rtl(p)
            i += 1
            continue
        
        # Bullet
        if line.strip().startswith('- '):
            text = line.strip()[2:]
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            text = clean_technical_ids(text)
            if not text:
                i += 1
                continue
            p = doc.add_paragraph(text, style='List Bullet')
            make_rtl(p)
            i += 1
            continue
        
        # Numbered list
        if re.match(r'^\d+\.\s', line.strip()):
            text = re.sub(r'^\d+\.\s*', '', line.strip())
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            text = clean_technical_ids(text)
            if not text:
                i += 1
                continue
            p = doc.add_paragraph(text, style='List Number')
            make_rtl(p)
            i += 1
            continue
        
        # Regular paragraph
        text = line.strip()
        if text:
            # Skip YAML frontmatter markers
            if text == '---':
                i += 1
                continue
            # Clean markdown formatting
            text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
            text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)  # Remove link syntax
            text = re.sub(r'`(.+?)`', r'\1', text)
            text = clean_technical_ids(text)
            if text and text != '---':
                p = doc.add_paragraph(text)
                make_rtl(p)
        
        i += 1


def extract_metadata(md_content):
    """Extract document metadata from markdown."""
    info = {
        'system_name': 'NursingPortal',
        'version': '1.0',
        'status': 'טיוטה',
        'description': ''
    }
    
    # Check for YAML frontmatter
    yaml_match = re.search(r'^---\s*\n(.+?)\n---', md_content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        # Extract from YAML
        ver_match = re.search(r'גרסה:\s*(\S+)', yaml_content)
        if ver_match:
            info['version'] = ver_match.group(1)
        status_match = re.search(r'מצב:\s*(.+?)(?:\n|$)', yaml_content)
        if status_match:
            info['status'] = status_match.group(1).strip()
        sys_match = re.search(r'מערכת:\s*(.+?)(?:\n|$)', yaml_content)
        if sys_match:
            info['system_name'] = sys_match.group(1).strip()
    
    # Fallback: Title from first heading
    match = re.search(r'^#\s+.*?—\s*(.+?)$', md_content, re.MULTILINE)
    if match and not info.get('system_name'):
        info['system_name'] = match.group(1).strip()
    
    # Fallback: Version from bold text
    if info['version'] == '1.0':
        match = re.search(r'\*\*גרסה[:\*]*\s*(\d+\.\d+)', md_content)
        if match:
            info['version'] = match.group(1)
    
    # Fallback: Status from bold text
    match = re.search(r'\*\*מצב:\*\*\s*(.+?)(?:\n|$)', md_content)
    if match:
        info['status'] = match.group(1).strip()
    
    # Description/scope
    match = re.search(r'\*\*התכולה[^:]*:\*\*\s*(.+?)(?:\n|$)', md_content)
    if match:
        info['description'] = match.group(1).strip()
    
    return info


def parse_sections(md_content):
    """Parse markdown into sections."""
    sections = []
    current = None
    current_lines = []
    
    for line in md_content.split('\n'):
        heading = re.match(r'^(#{1,4})\s+(.+)$', line)
        if heading:
            if current:
                current['content'] = '\n'.join(current_lines)
                sections.append(current)
            
            level = len(heading.group(1))
            title = heading.group(2).strip()
            current = {'level': level, 'title': title, 'content': ''}
            current_lines = []
        else:
            current_lines.append(line)
    
    if current:
        current['content'] = '\n'.join(current_lines)
        sections.append(current)
    
    return sections


def convert(md_path, output_path):
    """Convert markdown to professional BFS Word document."""
    print(f"Reading: {md_path}")
    
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Extract metadata
    meta = extract_metadata(md_content)
    print(f"System: {meta['system_name']}, Version: {meta['version']}")
    
    # Create document
    doc = Document()
    setup_document(doc)
    
    # Add header and footer with logo
    script_dir = Path(__file__).parent.parent  # .kiro folder
    logo_path = script_dir / 'assets' / 'bituach_leumi_logo.png'
    add_header_footer(doc, meta['system_name'], logo_path)
    
    # Title page
    add_title_page(doc, meta['system_name'], meta['version'], meta['description'])
    
    # Document info table
    info_table = {
        "סטטוס המסמך": meta['status'],
        "גרסה": meta['version'],
        "מועד עדכון": datetime.now().strftime("%d.%m.%Y"),
        "קהל יעד": "אגף סיעוד, עובדי מטה, נותני שירותים, גורמי אישור עסקיים",
        "אופי המסמך": "עסקי-פונקציונלי; אינו מחליף אפיון טכני או מסמך ארכיטקטורה"
    }
    add_document_info_table(doc, info_table)
    
    # Parse sections first to build TOC
    sections = parse_sections(md_content)
    
    # Skip metadata sections and the manual TOC in the source markdown
    skip_titles = ['אפיון עסקי ופונקציונלי', 'פרטי המסמך', 'מסמך אפיון פונקציונלי עסקי', 'תוכן עניינים']
    
    # Collect headings for TOC
    headings_info = []
    bookmark_id = 100000
    
    for section in sections:
        if any(skip in section['title'] for skip in skip_titles):
            continue
        
        # Clean technical IDs from heading
        clean_title = clean_technical_ids(section['title'])
        clean_title = re.sub(r'^(PROC|REQ|AC|ADR|BR|DEC|NF)-\d+[:\s]*', '', clean_title)
        
        if not clean_title or clean_title == '---':
            continue
        
        level = min(section['level'], 3)  # Only include levels 1-3 in TOC
        if level <= 3:
            bookmark_name = f"_Toc{bookmark_id}"
            headings_info.append((clean_title, level, bookmark_name))
            bookmark_id += 1
    
    # Add Table of Contents with entries
    add_toc_with_entries(doc, headings_info)
    
    # Temp dir for diagrams
    temp_dir = tempfile.mkdtemp()
    diagram_counter = [0]
    bookmark_id = 100000  # Reset for actual headings
    
    # Process sections and add content with bookmarks
    for section in sections:
        if any(skip in section['title'] for skip in skip_titles):
            continue
        
        # Clean technical IDs from heading
        clean_title = clean_technical_ids(section['title'])
        clean_title = re.sub(r'^(PROC|REQ|AC|ADR|BR|DEC|NF)-\d+[:\s]*', '', clean_title)
        
        if not clean_title or clean_title == '---':
            continue
        
        # Add heading with bookmark
        level = min(section['level'], 4)
        if level <= 3:
            add_heading_with_bookmark(doc, clean_title, level, bookmark_id)
            bookmark_id += 1
        else:
            h = doc.add_heading(clean_title, level=level)
            make_rtl(h)
        
        # Add content
        if section['content'].strip():
            process_content(doc, section['content'], temp_dir, diagram_counter)
    
    # Save
    doc.save(str(output_path))
    print(f"Created: {output_path}")
    
    # Cleanup
    import shutil
    try:
        shutil.rmtree(temp_dir)
    except:
        pass
    
    return output_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python md_to_bfs_word.py input.md [output.docx]")
        sys.exit(1)
    
    md_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else md_path.with_suffix('.docx')
    
    convert(md_path, output_path)
