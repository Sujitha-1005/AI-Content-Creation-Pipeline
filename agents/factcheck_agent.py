from utils.api_client import GroqClient

class FactCheckAgent:
    def __init__(self):
        self.client = GroqClient()
        self.name = "Fact-Check Agent"
    
    def fact_check(self, topic, content):
        """
        Review content for factual accuracy and flag potential issues
        """
        system_prompt = """You are a meticulous fact-checker and content reviewer. Analyze content for:

- Factual accuracy and correctness
- Unsupported or exaggerated claims
- Potentially outdated information
- Misleading or ambiguous statements
- Statistics or data that need source citations
- Logical inconsistencies
- Balanced perspective

Provide a detailed fact-check report that:
1. Highlights any concerns or inaccuracies
2. Suggests corrections where needed
3. Confirms what is accurate
4. Recommends sources that should be cited

Be thorough but fair in your assessment."""
        
        user_prompt = f"""Conduct a thorough fact-check of this article:

Topic: {topic}

Content:
{content}

Review for:
- Factual accuracy
- Claims that need verification
- Outdated information
- Misleading statements
- Need for citations

Provide specific feedback on any issues found, or confirm if the content is accurate. Be detailed and constructive."""
        
        fact_check_report = self.client.generate_response(system_prompt, user_prompt, max_tokens=2000)
        
        return {
            "agent": self.name,
            "status": "completed",
            "data": fact_check_report
        }