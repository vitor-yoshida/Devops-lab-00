import requests

# Secrets expostos propositalmente para laboratório
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# API Key fictícia
API_KEY = "sk_test_51H8Xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Token fictício
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123456"

# Credencial de banco fictícia
DB_PASSWORD = "SuperSecretPassword123!"

DATABASE_URL = (
    "postgresql://admin:SuperSecretPassword123!"
    "@localhost:5432/banco"
)


def consultar_api():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(
        "https://api.exemplo.local/clientes",
        headers=headers
    )

    return response.json()


def main():
    print("Aplicação bancária iniciada")
    print(f"Database: {DATABASE_URL}")

    consultar_api()


if __name__ == "__main__":
    main()
