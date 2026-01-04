from utils.api_client import GroqClient

class SEOAgent:
    def __init__(self):
        self.client = GroqClient()
        self.name = "SEO Agent"
    
    def optimize(self, topic, content):
        """
        Optimize content for SEO
        """
        system_prompt = """You are an SEO specialist with expertise in search engine optimization and digital marketing. Analyze content and provide comprehensive SEO recommendations including:

- Primary target keyword (high search volume, relevant)
- 5-8 secondary keywords
- Meta title (50-60 characters, compelling)
- Meta description (150-160 characters, action-oriented)
- URL slug (short, keyword-rich)
- Suggested H2/H3 headings optimization
- Internal linking opportunities (related topics)
- External linking suggestions (authoritative sources)
- Content improvements for better ranking
- Readability score assessment
- Keyword density recommendations

Focus on natural, white-hat SEO that serves both users and search engines."""
        
        user_prompt = f"""Provide comprehensive SEO optimization recommendations for this article:

Topic: {topic}

Content:
{content[:2500]}...

Provide complete SEO analysis including:
1. Primary & secondary keywords
2. Meta title & description
3. URL slug
4. Heading optimization suggestions
5. Internal/external linking ideas
6. Content improvements for SEO
7. Overall SEO score and recommendations

Be specific and actionable in your recommendations."""
        
        seo_recommendations = self.client.generate_response(system_prompt, user_prompt, max_tokens=2000)
        
        return {
            "agent": self.name,
            "status": "completed",
            "data": seo_recommendations
        }