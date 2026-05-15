"""
Nigerian cultural adaptation layer for Naija Eats.

Post-processes LLM-generated review text to ensure authentic Nigerian
English and Pidgin expressions. This module does NOT force artificial
Pidgin; rather it refines the output to match how a real Nigerian
reviewer would naturally write, consistent with the user's detected
language style.

Adaptation signals include:
  - Pidgin phrases and idioms (e.g., "e dey slap", "abeg", "sha")
  - Local food and place references
  - Nigerian slang and interjections
  - Sentence rhythm typical of Lagos street speech
"""

import os

import httpx

from app.config import settings


class Nigerianizer:
    """Adapts generated review text to authentic Nigerian voice."""

    def __init__(self):
        self.api_key = settings.openrouter_api_key or os.getenv("OPENROUTER_API_KEY")
        self.client = httpx.Client(
            base_url="https://openrouter.ai/api/v1",
            timeout=60.0,
            headers={
                "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8000",
                "X-Title": "Naija Eats",
            },
        )
        
        # Load prompt template
        template_path = os.path.join("models", "prompts", "cultural_adaptation.txt")
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                self.template = f.read()
        else:
            self.template = "Adapt this review to a Nigerian voice: {review_text}"

    def adapt(self, review_text: str, uses_pidgin: bool = False) -> str:
        """
        Refine a review to sound like an authentic Nigerian writer.
        """
        if not settings.enable_cultural_layer:
            return review_text

        if not self.api_key:
            # Basic rule-based adaptation as fallback
            adapted = review_text
            if uses_pidgin:
                # Very simple substitutions for demonstration
                adapted = adapted.replace("I really enjoyed", "Honestly, e dey slap")
                adapted = adapted.replace("The food was great", "The food was on point")
                adapted = adapted.replace(".", ". Sha.")
            return adapted

        prompt = self.template.format(
            review_text=review_text,
            uses_pidgin=str(uses_pidgin).lower(),
        )

        try:
            response = self.client.post(
                "/chat/completions",
                json={
                    "model": "nvidia/nemotron-3-super-120b-a12b:free",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.4,
                },
            )
            response.raise_for_status()

            payload = response.json()
            content = payload["choices"][0]["message"]["content"]
            return content.strip()
        except Exception:
            return review_text
