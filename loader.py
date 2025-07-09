from pypdf import PdfReader

def load_pdf_text(filepath: str) -> list[str]:
    import os
    reader = PdfReader(os.path.join(os.path.dirname(__file__), "..", "..", filepath))

    all_text = []

    for page in reader.pages:
        text = page.extract_text()
        all_text.append(text)

    return all_text

if __name__ == "__main__":
    pages = load_pdf_text("../../data/invoice.pdf")
    print(pages[:1])

    from splitter import split_text

    chunks = split_text(pages, chunk_size=1000, overlap=200)
    print(f"Total chunks: {len(chunks)}")
    print(chunks[0][:300])
