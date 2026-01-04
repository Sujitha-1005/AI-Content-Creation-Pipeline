from utils.api_client import GroqClient

class ResearchAgent:
    def __init__(self):
        self.client = GroqClient()
        self.name = "Research Agent"
    
    def research(self, topic):
        """
        Research a topic and gather key information
        """
        system_prompt = """You are a professional research assistant with expertise in comprehensive topic analysis. Your job is to provide thorough research on any given topic. 

Your research should include:
- Key facts and statistics with context
- Current trends and developments
- Important concepts and terminology
- Notable experts, organizations, or thought leaders
- Recent developments and innovations
- Historical context where relevant
- Different perspectives on the topic

Be thorough, accurate, and objective. Organize information logically."""
        
        user_prompt = f"""Conduct comprehensive research on the following topic:

Topic: {topic}

Provide detailed, well-organized research covering all important aspects of this topic. Include relevant facts, trends, key players, and recent developments. Make the research informative and useful for creating high-quality content."""
        
        research_data = self.client.generate_response(system_prompt, user_prompt)
        
        return {
            "agent": self.name,
            "status": "completed",
            "data": research_data
        }