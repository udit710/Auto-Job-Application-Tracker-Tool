import React, { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";

function App() {
  const [jobLink, setJobLink] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [description, setDescription] = useState<string>("");
  const [keywords, setKeywords] = useState<[]>([]);
  const [loading1, setLoading1] = useState<boolean>(false);
  const [loading2, setLoading2] = useState<boolean>(false);

  // Handler for form submission
  const handleSubmitProcess = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading1(true); // Set loading state to true

    try {
      const response = await axios.post('http://127.0.0.1:5000/process-job', {
        job_link: jobLink,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });

      setMessage(response.data.message);
    } catch (error) {
      console.error('There was an error processing the job link!', error);
      setMessage('Error processing the job link. Please try again.');
    } finally {
      setLoading1(false); // Reset loading state
    }
  };

  // Handler for input change
  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setJobLink(e.target.value);
  };
  
  const handleSubmitExtract = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading2(true); // Set loading state to true

    try {
      const response = await axios.post('http://127.0.0.1:5000/extract-keywords', {
        description: description,
      }, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      
      let key = response.data.keywords.split(',');
      setKeywords(key);
      console.log(keywords);
    } catch (error) {
      console.error('There was an error extracting the keywords!', error);
      setMessage('Error extracting the keywords. Please try again.');
    } finally {
      setLoading2(false); // Reset loading state
    }
  };

  // Handler for input change
  const handleInputChange2 = (e: ChangeEvent<HTMLInputElement>) => {
    setDescription(e.target.value);
  };

  return (
    <div className="App">
      <h1 style={{ textAlign: 'center' }}>Auto Job Application Tool</h1>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <form onSubmit={handleSubmitProcess}>
          <input
            type="text"
            value={jobLink}
            style={{ width: '400px', padding: '2px', fontSize: '16px' }}
            onChange={handleInputChange}
            placeholder="Enter the job link"
            required
          />
          <button type="submit" disabled={loading1}>
            {loading1 ? 'Submitting...' : 'Submit'}
          </button>
        </form>
      </div>
      {message && <p style={{ textAlign: 'center' }}>{message}</p>}
      
      {/* Keyword extracter */}
      <h1 style={{ textAlign: 'center' }}>Keyword Extracter</h1>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <form onSubmit={handleSubmitExtract}>
          <input
            type="text"
            value={description}
            style={{ width: '400px', padding: '2px', fontSize: '16px' }}
            onChange={handleInputChange2}
            placeholder="Enter the job description"
            required
          />
          <button type="submit" disabled={loading2}>
            {loading2 ? 'Submitting...' : 'Submit'}
          </button>
        </form>
      </div>
      {keywords && <p style={{ textAlign: 'center' }}>{keywords.map((keyword: any) => <div><button onClick={() => {navigator.clipboard.writeText(keyword)}}>{keyword}</button></div>)
      }</p>}
      
    </div>
  );
}

export default App;
