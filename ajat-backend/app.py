from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from components.application_tracker.scraper import scrape_job_description
from components.application_tracker.summarize_description import summarize_description
from components.application_tracker.update_sheet import update_sheet
from components.keyword_extracter.keyword_extracter import extract_keyword

app = Flask(__name__)
CORS(app, resources={r"/process-job": {"origins": "http://localhost:3000"}})

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process-job', methods=['POST'])
def process_job():
    data = request.get_json()
    job_link = data.get("job_link")
    
    try:
        if not job_link:
            raise ValueError("No job link provided")

        description = scrape_job_description(job_link)
        summarised = summarize_description(description)
        update_sheet(summarised, job_link)
        
        return jsonify({"message": "Job description processed successfully!"})
    
    except Exception as e:
        print(f"Error: {e}")  # Print error for debugging
        return jsonify({"error": str(e)}), 500

@app.route('/extract-keywords', methods=['POST'])
def extract_keywords():
    data = request.get_json()
    description = data.get("description")
    
    try:
        if not description:
            raise ValueError("No description provided")
        
        keywords = extract_keyword(description)
        
        return jsonify({"keywords": keywords})
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
