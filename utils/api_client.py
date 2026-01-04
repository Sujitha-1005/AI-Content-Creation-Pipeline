from groq import Groq
from config import Config

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL
        self.temperature = Config.TEMPERATURE
    
    def generate_response(self, system_prompt, user_prompt, max_tokens=None):
        """
        Generate a response from Groq (FREE & FAST!)
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=max_tokens or Config.MAX_TOKENS,
                temperature=self.temperature
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"