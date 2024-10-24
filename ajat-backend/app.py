from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from scraper import scrape_job_description
from summarize_description import summarize_description
from update_sheet import update_sheet

app = Flask(__name__)
CORS(app, resources={r"/process-job": {"origins": "http://localhost:3000"}})

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


if __name__ == "__main__":
    app.run(debug=True)
