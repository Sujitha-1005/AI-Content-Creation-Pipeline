from agents.research_agent import ResearchAgent
from agents.outline_agent import OutlineAgent
from agents.content_agent import ContentAgent
from agents.image_agent import ImageAgent
from agents.factcheck_agent import FactCheckAgent
from agents.seo_agent import SEOAgent
import time

class PipelineOrchestrator:
    """
    Orchestrates the entire content creation pipeline using OpenAI GPT
    """
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.outline_agent = OutlineAgent()
        self.content_agent = ContentAgent()
        self.image_agent = ImageAgent()
        self.factcheck_agent = FactCheckAgent()
        self.seo_agent = SEOAgent()
        
    def run_pipeline(self, topic, progress_callback=None):
        """
        Run the complete content creation pipeline
        Returns a dictionary with all results
        """
        results = {
            "topic": topic,
            "steps": [],
            "start_time": time.time()
        }
        
        try:
            # Step 1: Research
            if progress_callback:
                progress_callback("🔍 Researching topic...", 15)
            research_result = self.research_agent.research(topic)
            results["steps"].append(research_result)
            results["research"] = research_result["data"]
            
            # Step 2: Create Outline
            if progress_callback:
                progress_callback("📋 Creating outline...", 30)
            outline_result = self.outline_agent.create_outline(topic, results["research"])
            results["steps"].append(outline_result)
            results["outline"] = outline_result["data"]
            
            # Step 3: Generate Content
            if progress_callback:
                progress_callback("✍️ Generating content...", 50)
            content_result = self.content_agent.generate_content(
                topic, results["outline"], results["research"]
            )
            results["steps"].append(content_result)
            results["content"] = content_result["data"]
            
            # Step 4: Suggest Images
            if progress_callback:
                progress_callback("🖼️ Finding images...", 65)
            image_result = self.image_agent.suggest_images(topic, results["content"])
            results["steps"].append(image_result)
            results["images"] = image_result["data"]
            
            # Step 5: Fact Check
            if progress_callback:
                progress_callback("✅ Fact-checking...", 80)
            factcheck_result = self.factcheck_agent.fact_check(topic, results["content"])
            results["steps"].append(factcheck_result)
            results["factcheck"] = factcheck_result["data"]
            
            # Step 6: SEO Optimization
            if progress_callback:
                progress_callback("🚀 Optimizing for SEO...", 95)
            seo_result = self.seo_agent.optimize(topic, results["content"])
            results["steps"].append(seo_result)
            results["seo"] = seo_result["data"]
            
            results["end_time"] = time.time()
            results["duration"] = round(results["end_time"] - results["start_time"], 2)
            
            if progress_callback:
                progress_callback("✨ Complete!", 100)
            
            return results
            
        except Exception as e:
            results["error"] = str(e)
            results["status"] = "failed"
            return results