from utils.api_client import GroqClient

class OutlineAgent:
    def __init__(self):
        self.client = GroqClient()
        self.name = "Outline Agent"
    
    def create_outline(self, topic, research_data):
        """
        Create a structured outline based on research
        """
        system_prompt = """You are an expert content strategist and outliner. Create compelling, well-structured article outlines that:

- Have an attention-grabbing title
- Include an engaging introduction hook
- Contain 5-7 main sections with logical flow
- Have 2-4 subpoints under each main section
- Include a strong conclusion section
- Are organized for maximum reader engagement

Make outlines comprehensive, logical, and reader-friendly."""
        
        user_prompt = f"""Based on the research provided, create a detailed article outline for this topic:

Topic: {topic}

Research Data:
{research_data}

Create a complete, professional outline with:
1. Compelling title
2. Introduction approach
3. Main sections with subpoints
4. Conclusion strategy

Make it engaging and comprehensive."""
        
        outline = self.client.generate_response(system_prompt, user_prompt)
        
        return {
            "agent": self.name,
            "status": "completed",
            "data": outline
        }