# Auto Job Application Tracker  

## Overview  
**Auto Job Application Tracker (AJAT)** is a lightweight automation tool designed to streamline the process of tracking job applications. It uses web scraping to extract job details, summarizes the data using Generative AI, and updates a central spreadsheet for easy management and tracking.

**Keyword Extracter** is another tool that extracts the top keywords from a job description.

### Features  
- **Web Scraping**: Automatically extracts job-related data from portals.  
- **Generative AI Integration**: Summarizes extracted data for quick review and also used in keyword extraction.
- **Keyword Extracter**: Extracts top keywords from a job description.
- **Spreadsheet Integration**: Updates job details on a centralized Google Sheet.  
- **User-Friendly Interface**: Powered by Flask (backend) and React (frontend).  
- **Scalable Architecture**: Utilizes Google Spreadsheets and can use AWS EC2 for reliable data storage and deployment.  

---

## Tech Stack  
- **Backend**: Flask  
- **Frontend**: React  
- **Database**: Google Sheets
- **Deployment**: *Not deployed as its used for personal use*
- **Utilities**: Web Scraping, Generative AI integration, Google APIs, Pandas  
- **Version Control**: Git  

---

## Setup  

### Prerequisites  
- Python 3.11.7
- Node 20.15.1
- AWS account for EC2 setup
- ChromeDriver (for web scraping)  
- GenAI API key
- Google Sheet ID for tracking job applications
- Google API credentials for spreadsheet integration

### Configuration  
1. Create a `.env` file in the root directory with the following environment variables:  
   ```plaintext
   # configured for production
   PORTALUSERNAME=PORTALUSERNAME
   PORTALPASSWORD=PORTALPASSWORD
   CHROMEDRIVER=CHROMEDRIVER
   GEN_API_KEY=GEN_API_KEY
   SHEET_ID=SHEET_ID
   INSTRUCTIONS=INSTRUCTIONS
   ```
   - Replace placeholders with your specific values:  
     - **PORTALUSERNAME**: Username for the job portal.  
     - **PORTALPASSWORD**: Password for the job portal.  
     - **CHROMEDRIVER**: Path to your ChromeDriver executable.  
     - **GEN_API_KEY**: API key for Generative AI integration.  
     - **SHEET_ID**: Google Sheet ID to track job applications.  
     - **INSTRUCTIONS**: Instructions for summarizing the job data.  

---

## Directory Structure  
```plaintext
/ajat-backend
  - Flask application for backend services
  /ajat-backend/app
    - Main application directory
    /ajat-backend/components
      - Components for web scraping, summarization, and spreadsheet integration
/ajat-frontend
  - React application for frontend interface
```

---

## How to Run  

1. **Build Frontend**  
   Navigate to the `ajat-frontend` directory, install dependencies, and start the React server:  
   ```bash
   npm install  
   npm run build
   ```

2. **Run App** 
    Navigate to the `ajat-backend` directory, install dependencies, and start the Flask server:  
    ```bash
    pip install -r requirements.txt
    gunicorn -w 4 -t 120 -b localhost:5000 app:app
    ``` 

---

## Deployment  
- **Backend**: Deploy on AWS EC2 using Gunicorn.  
- **Frontend**: Serve React application using AWS or a CDN.  

---

## Acknowledgments  
- **Flask** for backend services.  
- **React** for frontend development.  
- **Google APIs** for spreadsheet integration.  
- **Generative AI** for job data summarization.  
- **Selenium** for extracting job details.