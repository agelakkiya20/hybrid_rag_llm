
from ingestion.document_loader import load_document


def test_load_txt_document(tmp_path):
    file_path = tmp_path / "sample.txt"

    file_path.write_text(
        "Hybrid RAG combines keyword and semantic search.",
        encoding="utf-8"
    )

    result = load_document(file_path)

    assert "Hybrid RAG" in result["text"]
    assert result["metadata"]["source"] == "sample.txt"
    assert result["metadata"]["file_type"] == ".txt"


def test_unsupported_file(tmp_path):
    file_path = tmp_path / "sample.docx"
    file_path.write_text("Sample")

    try:
        load_document(file_path)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
