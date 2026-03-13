import os
from typing import TypedDict

from python.helpers import dotenv


class IntegrationGroupStatus(TypedDict):
    configured: int
    total: int
    missing: int


class IntegrationsStatus(TypedDict):
    groups: dict[str, IntegrationGroupStatus]
    total_configured: int
    total_keys: int
    total_missing: int
    fully_connected: bool


INTEGRATION_GROUPS: dict[str, list[str]] = {
    "ai_models": [
        "OPENAI_API_KEY",
        "OPENROUTER_API_KEY",
        "DEEPSEEK_API_KEY",
        "PERPLEXITY_API_KEY",
        "TOGETHER_AI_API_KEY",
        "GROQ_API_KEY",
        "GOOGLE_API_KEY",
        "KIMI_API_KEY",
    ],
    "auth": [
        "NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY",
        "CLERK_SECRET_KEY",
        "GOOGLE_OAUTH_CLIENT_ID",
        "GOOGLE_OAUTH_CLIENT_SECRET",
    ],
    "payments": [
        "STRIPE_SECRET_KEY",
        "STRIPE_PUBLISHABLE_KEY",
    ],
    "communications": [
        "TWILIO_ACCOUNT_SID",
        "TWILIO_AUTH_TOKEN",
        "SENDGRID_API_KEY",
        "RESEND_API_KEY",
    ],
    "cloud": [
        "CLOUDFLARE_API_TOKEN",
        "CLOUDFLARE_ACCOUNT_ID",
    ],
    "automation": [
        "ZAPIER_API_KEY",
        "MAKE_API_KEY",
    ],
}


def _is_set(key: str) -> bool:
    value = os.getenv(key) or dotenv.get_dotenv_value(key)
    return bool(value and str(value).strip())


def get_integrations_status() -> IntegrationsStatus:
    dotenv.load_dotenv()

    groups: dict[str, IntegrationGroupStatus] = {}
    total_keys = 0
    total_configured = 0

    for group, keys in INTEGRATION_GROUPS.items():
        configured = sum(1 for key in keys if _is_set(key))
        total = len(keys)
        missing = total - configured
        groups[group] = IntegrationGroupStatus(
            configured=configured,
            total=total,
            missing=missing,
        )
        total_keys += total
        total_configured += configured

    total_missing = total_keys - total_configured
    return IntegrationsStatus(
        groups=groups,
        total_configured=total_configured,
        total_keys=total_keys,
        total_missing=total_missing,
        fully_connected=(total_missing == 0),
    )
