from flask import Flask, render_template, request, jsonify
from config import Config
from utils.orchestrator import PipelineOrchestrator
import secrets
import traceback

app = Flask(__name__)
app.config.from_object(Config)

# Store pipeline results in memory (use Redis/DB in production)
pipeline_results = {}


@app.route('/')
def index():
    """Home page with input form"""
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """Start the content generation pipeline using GROQ"""
    data = request.get_json()
    topic = data.get('topic', '').strip()

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    # ✅ Correct API key check (GROQ)
    if not Config.GROQ_API_KEY:
        return jsonify({
            "error": "GROQ API key not configured. Please check your .env file"
        }), 500

    # Generate unique ID for this pipeline run
    pipeline_id = secrets.token_hex(8)

    try:
        print(f"🚀 Starting GROQ pipeline for topic: {topic}")

        orchestrator = PipelineOrchestrator()
        results = orchestrator.run_pipeline(topic)

        # Pipeline error handling
        if isinstance(results, dict) and "error" in results:
            return jsonify({
                "error": f"Pipeline failed: {results['error']}"
            }), 500

        # Store results
        pipeline_results[pipeline_id] = results

        print(f"✅ Pipeline completed in {results.get('duration', 0)} seconds")

        return jsonify({
            "success": True,
            "pipeline_id": pipeline_id,
            "duration": results.get("duration", 0),
            "message": "Content generation completed successfully using GROQ"
        })

    except Exception as e:
        print("❌ Error in pipeline execution")
        print(traceback.format_exc())
        return jsonify({
            "error": f"An unexpected error occurred: {str(e)}"
        }), 500


@app.route('/result/<pipeline_id>')
def result(pipeline_id):
    """Render results page"""
    if pipeline_id not in pipeline_results:
        return "Results not found. Invalid or expired pipeline ID.", 404

    return render_template(
        'result.html',
        results=pipeline_results[pipeline_id],
        pipeline_id=pipeline_id
    )


@app.route('/api/result/<pipeline_id>')
def api_result(pipeline_id):
    """Return pipeline results as JSON"""
    if pipeline_id not in pipeline_results:
        return jsonify({"error": "Results not found"}), 404

    return jsonify(pipeline_results[pipeline_id])


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "groq_api_configured": bool(Config.GROQ_API_KEY),
        "model": Config.GROQ_MODEL,
        "active_pipelines": len(pipeline_results)
    })


if __name__ == '__main__':
    print("=" * 60)
    print("🚀 Content Creation Pipeline - GROQ Edition")
    print("=" * 60)
    print(f"✓ GROQ API Key configured: {bool(Config.GROQ_API_KEY)}")
    print(f"✓ Model: {Config.GROQ_MODEL}")
    print("✓ Server running at http://localhost:5000")
    print("=" * 60)

    app.run(debug=True, port=5000)
