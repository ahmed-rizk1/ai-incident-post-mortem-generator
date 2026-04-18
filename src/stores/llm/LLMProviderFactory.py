from abc import ABC, abstractmethod
from typing import Generator

class BaseLLMProvider(ABC):
    @abstractmethod
    def generate_post_mortem_stream(self, system_prompt: str, user_prompt: str) -> Generator[str, None, None]:
        pass

class OpenRouterProvider(BaseLLMProvider):
    def __init__(self, api_key: str):
        from openai import OpenAI
        self.api_key = api_key
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.api_key,
        )

    def generate_post_mortem_stream(self, system_prompt: str, user_prompt: str) -> Generator[str, None, None]:
        response = self.client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            stream=True,
        )
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

class LLMProviderFactory:
    @staticmethod
    def get_provider(provider_type: str, api_key: str) -> BaseLLMProvider:
        if provider_type == "openrouter":
            return OpenRouterProvider(api_key)
        raise ValueError(f"Unknown provider type: {provider_type}")
