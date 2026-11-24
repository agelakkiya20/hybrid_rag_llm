
import pytest

from ingestion.chunker import chunk_document


def test_chunk_document():

    document = {
        "text": " ".join(["AI"] * 1000),
        "metadata": {
            "source": "sample.txt",
            "file_type": ".txt"
        }
    }

    chunks = chunk_document(
        document,
        chunk_size=400,
        chunk_overlap=60
    )

    assert len(chunks) == 3

    assert len(chunks[0]["text"].split()) == 400

    assert len(chunks[1]["text"].split()) == 400

    assert len(chunks[2]["text"].split()) == 320


def test_chunk_metadata():

    document = {
        "text": "Artificial Intelligence " * 10,
        "metadata": {
            "source": "sample.txt",
            "file_type": ".txt"
        }
    }

    chunks = chunk_document(document, 10, 2)

    assert chunks[0]["metadata"]["source"] == "sample.txt"

    assert chunks[0]["metadata"]["chunk_index"] == 0


def test_invalid_chunk_size():

    document = {
        "text": "Sample text",
        "metadata": {}
    }

    with pytest.raises(ValueError):
        chunk_document(document, 0, 0)


def test_invalid_overlap():

    document = {
        "text": "Sample text",
        "metadata": {}
    }

    with pytest.raises(ValueError):
        chunk_document(document, 10, 10)
