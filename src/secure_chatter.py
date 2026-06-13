import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class IntegrationConfig:
    api_endpoint: str
    documentation_url: str
    support_contact: str

class SecureChatter:
    def __init__(self, config: IntegrationConfig):
        self.config = config

    def provide_api(self):
        return {
            "endpoint": self.config.api_endpoint,
            "methods": ["GET", "POST", "PUT", "DELETE"]
        }

    def provide_documentation(self):
        return self.config.documentation_url

    def provide_support(self):
        return self.config.support_contact

def main():
    parser = ArgumentParser(description="Secure Chatter Integration")
    parser.add_argument("--api-endpoint", help="API endpoint URL")
    parser.add_argument("--documentation-url", help="Documentation URL")
    parser.add_argument("--support-contact", help="Support contact information")
    args = parser.parse_args()

    config = IntegrationConfig(
        api_endpoint=args.api_endpoint,
        documentation_url=args.documentation_url,
        support_contact=args.support_contact
    )

    secure_chatter = SecureChatter(config)
    print(json.dumps(secure_chatter.provide_api()))
    print(secure_chatter.provide_documentation())
    print(secure_chatter.provide_support())

if __name__ == "__main__":
    main()
