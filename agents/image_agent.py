from utils.api_client import GroqClient

class ImageAgent:
    def __init__(self):
        self.client = GroqClient()
        self.name = "Image Agent"
    
    def suggest_images(self, topic, content):
        """
        Suggest relevant images for the content
        """
        system_prompt = """You are an image selection and visual content specialist. Suggest relevant, professional images for articles. For each suggestion provide:

- Detailed image description
- Recommended placement in the article (e.g., "Introduction", "Section 2", etc.)
- Search keywords for finding the image
- Alt text for accessibility
- Image style/type (photo, infographic, illustration, etc.)

Suggest 4-6 images that would enhance the article and improve reader engagement."""
        
        user_prompt = f"""Suggest professional, relevant images for this article:

Topic: {topic}

Content Preview:
{content[:1500]}...

Provide specific image suggestions with:
1. Description of what the image should show
2. Where to place it in the article
3. Search keywords
4. Alt text
5. Style/type

Make suggestions practical and relevant to the content."""
        
        suggestions = self.client.generate_response(system_prompt, user_prompt)
        
        return {
            "agent": self.name,
            "status": "completed",
            "data": suggestions
        }