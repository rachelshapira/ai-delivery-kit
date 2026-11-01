# -*- coding: utf-8 -*-
"""
Extract text from PDF files in a directory.
Usage: python extract-pdfs.py <source_dir> [output_file]
"""
import sys
import os

def extract_pdfs(source_dir, output_file=None):
    try:
        from pypdf import PdfReader
    except ImportError:
        print("Installing pypdf...")
        os.system(f'"{sys.executable}" -m pip install pypdf --quiet')
        from pypdf import PdfReader
    
    if output_file is None:
        output_file = os.path.join(source_dir, 'extracted_text.md')
    
    with open(output_file, 'w', encoding='utf-8') as out:
        for f in sorted(os.listdir(source_dir)):
            if f.endswith('.pdf'):
                out.write(f'\n# {f}\n\n')
                print(f'Processing: {f}')
                try:
                    reader = PdfReader(os.path.join(source_dir, f))
                    for i, page in enumerate(reader.pages):
                        text = page.extract_text()
                        if text:
                            out.write(f'## Page {i+1}\n\n')
                            out.write(text)
                            out.write('\n\n')
                except Exception as e:
                    out.write(f'Error: {e}\n\n')
                    print(f'  Error: {e}')
    
    print(f'Done! Output: {output_file}')
    return output_file

if __name__ == '__main__':
    source_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_pdfs(source_dir, output_file)
