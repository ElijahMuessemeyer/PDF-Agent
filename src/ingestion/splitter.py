def split_text(pages: list[str], chunk_size: int = 1000, overlap: int = 200) -> list[str]:

    chunks = []

    for page_text in pages:
        if not page_text:
            continue

        start = 0
        while start < len(page_text):
            end = start + chunk_size
            chunk = page_text[start:end]
            chunks.append(chunk)
            start += chunk_size

    return chunks
