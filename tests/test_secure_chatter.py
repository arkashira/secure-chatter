import json
from secure_chatter import SecureChatter, IntegrationConfig

def test_provide_api():
    config = IntegrationConfig("https://example.com/api", "https://example.com/docs", "support@example.com")
    secure_chatter = SecureChatter(config)
    api = secure_chatter.provide_api()
    assert api["endpoint"] == "https://example.com/api"
    assert api["methods"] == ["GET", "POST", "PUT", "DELETE"]

def test_provide_documentation():
    config = IntegrationConfig("https://example.com/api", "https://example.com/docs", "support@example.com")
    secure_chatter = SecureChatter(config)
    documentation_url = secure_chatter.provide_documentation()
    assert documentation_url == "https://example.com/docs"

def test_provide_support():
    config = IntegrationConfig("https://example.com/api", "https://example.com/docs", "support@example.com")
    secure_chatter = SecureChatter(config)
    support_contact = secure_chatter.provide_support()
    assert support_contact == "support@example.com"
