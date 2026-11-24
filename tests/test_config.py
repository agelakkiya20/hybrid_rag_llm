
from utils.config import load_config

def test_config_loading():
    config = load_config()

    assert config["project"]["name"] == "Hybrid RAG"
    assert config["document"]["chunk_size"] == 400
    assert config["document"]["chunk_overlap"] == 60

    print("Configuration test passed!")