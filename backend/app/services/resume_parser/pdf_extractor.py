import re
import pymupdf


def clean_extracted_text(text: str) -> str:
    """
    Clean common formatting artifacts produced during PDF extraction.
    """

    # Join words broken across lines with a hyphen.
    # Example: ma-\nchine -> machine
    text = re.sub(r"-\s*\n\s*", "", text)

    # Remove extracted page numbers that appear alone on a line.
    text = re.sub(r"(?m)^\s*\d+\s*$", "", text)

    # Remove unnecessary spaces around line breaks.
    text = re.sub(r"[ \t]+\n", "\n", text)

    # Collapse excessive blank lines.
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extract and clean text from every page of a PDF.
    """

    document = pymupdf.open(file_path)

    pages = []

    for page in document:
        pages.append(page.get_text())

    document.close()

    text = "\n".join(pages)

    return clean_extracted_text(text)