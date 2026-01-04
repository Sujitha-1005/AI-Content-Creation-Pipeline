from utils.api_client import GroqClient

class ContentAgent:
    def __init__(self):
        self.client = GroqClient()
        self.name = "Content Agent"
    
    def generate_content(self, topic, outline, research_data):
        """
        Generate full article content based on outline and research
        """
        system_prompt = """You are an expert content writer who creates engaging, informative articles. Your writing should:

- Follow the provided outline structure exactly
- Use clear, accessible language
- Include specific details, examples, and evidence
- Maintain a consistent, professional yet friendly tone
- Be well-formatted with proper paragraphs
- Engage readers while being informative
- Use transitions between sections
- Include compelling opening and closing

Write comprehensive, high-quality content that readers will find valuable."""
        
        user_prompt = f"""Write a complete, professional article based on this outline and research:

Topic: {topic}

Outline:
{outline}

Research:
{research_data}

Write the full article with all sections fully developed. Make it informative, engaging, and well-structured. Include an introduction that hooks readers and a conclusion that provides value. Aim for approximately 1200-1500 words."""
        
        content = self.client.generate_response(system_prompt, user_prompt, max_tokens=8000)
        
        return {
            "agent": self.name,
            "status": "completed",
            "data": content
        }