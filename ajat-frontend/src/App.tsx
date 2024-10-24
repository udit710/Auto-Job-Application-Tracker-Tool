import React, { useState, ChangeEvent, FormEvent } from "react";
import axios from "axios";

function App() {
  const [jobLink, setJobLink] = useState<string>("");
  const [message, setMessage] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  // Handler for form submission
  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true); // Set loading state to true

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
      setLoading(false); // Reset loading state
    }
  };

  // Handler for input change
  const handleInputChange = (e: ChangeEvent<HTMLInputElement>) => {
    setJobLink(e.target.value);
  };

  return (
    <div className="App">
      <h1 style={{ textAlign: 'center' }}>Auto Job Application Tool</h1>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={jobLink}
            style={{ width: '400px', padding: '2px', fontSize: '16px' }}
            onChange={handleInputChange}
            placeholder="Enter the job link"
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Submitting...' : 'Submit'}
          </button>
        </form>
      </div>
      {message && <p style={{ textAlign: 'center' }}>{message}</p>}
    </div>
  );
}

export default App;
