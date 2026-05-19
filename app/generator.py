"""
LLM review generation module for Naija Eats.

Orchestrates the reasoning chain using the OpenRouter free Nemotron model.
Takes the user's behavioral fingerprint, their retrieved similar reviews,
and the new restaurant details — then produces a predicted star rating,
a voice-matched written review, a confidence score, and a reasoning trace.
"""

import json
import os

import httpx

from app.config import settings
from app.profiler import BehavioralFingerprint


class ReviewGenerator:
    """LLM reasoning agent that generates voice-matched reviews."""

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
        template_path = os.path.join("models", "prompts", "review_generation.txt")
        if os.path.exists(template_path):
            with open(template_path, "r", encoding="utf-8") as f:
                self.template = f.read()
        else:
            self.template = "Generate a review for {restaurant_name}."

    def generate(
        self,
        fingerprint: BehavioralFingerprint,
        retrieved_reviews: list[dict],
        restaurant: dict,
    ) -> dict:
        """
        Generate a simulated review for a restaurant based on user fingerprint.
        """
        if not self.api_key:
            # Fallback to mock generation if no API key
            predicted_rating = 4
            if "slow service" in restaurant.get("common_tags", []):
                predicted_rating = 3
            
            review_text = (
                f"Mama Titi's {restaurant.get('name')}? Honestly, e dey slap. "
                "The food was on point. But this service ehn... I waited too long. (Simulated without AI key)"
            )
            
            return {
                "predicted_rating": predicted_rating,
                "review_text": review_text,
                "confidence": 0.7,
                "reasoning": "Simulated reasoning based on common tags and user history.",
            }

        # Format the prompt context
        prompt = self.template.format(
            fingerprint=json.dumps(fingerprint.__dict__, indent=2),
            retrieved_reviews=json.dumps(retrieved_reviews, indent=2),
            restaurant_name=restaurant.get("name", "Unknown"),
            restaurant_category=restaurant.get("category", "Unknown"),
            restaurant_location=restaurant.get("location", "Unknown"),
            restaurant_price_range=restaurant.get("price_range", "Unknown"),
            restaurant_menu_highlights=", ".join(restaurant.get("menu_highlights", [])),
            restaurant_common_tags=", ".join(restaurant.get("common_tags", [])),
        )

        try:
            response = self.client.post(
                "/chat/completions",
                json={
                    "model": "nvidia/nemotron-3-super-120b-a12b:free",
                    "messages": [
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                },
            )
            response.raise_for_status()

            payload = response.json()
            content = payload["choices"][0]["message"]["content"]
            
            # Extract JSON block mapping to expected Output (basic parsing)
            try:
                # Basic cleanup assuming LLM returns markdown format or direct JSON
                content = content.strip()
                if content.startswith("```json"):
                    content = content[7:]
                if content.endswith("```"):
                    content = content[:-3]
                
                result = json.loads(content.strip())
            except Exception as parse_exc:
                print(f"Failed to parse LLM response as JSON: {parse_exc}")
                print(f"Raw Output: {content}")
                
                # Fallback parsed result
                result = {
                    "predicted_rating": 3,
                    "review_text": f"[AI GEN ERROR] {str(content)[:100]}...",
                    "confidence": 0.0,
                    "reasoning": "Failed to parse JSON response."
                }
                
            return result
            
        except Exception as e:
            print(f"Error calling OpenRouter: {e}")
            return {
                "predicted_rating": 3,
                "review_text": "Error generating review.",
                "confidence": 0.0,
                "reasoning": str(e)
            }
