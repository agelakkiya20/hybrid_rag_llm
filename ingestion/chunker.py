
def chunk_document(document, chunk_size=400, chunk_overlap=60):
    """
    Split a document into smaller overlapping chunks.
    Chunk size and overlap are measured in words.
    """

    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError(
            "Chunk overlap must be non-negative and smaller than chunk size."
        )

    text = document["text"]
    metadata = document["metadata"]

    words = text.split()

    chunks = []

    start = 0
    chunk_index = 0

    while start < len(words):

        end = start + chunk_size

        chunk_words = words[start:end]

        chunk_text = " ".join(chunk_words)

        chunks.append({
            "text": chunk_text,
            "metadata": {
                **metadata,
                "chunk_index": chunk_index
            }
        })

        chunk_index += 1

        start = end - chunk_overlap

    return chunks
