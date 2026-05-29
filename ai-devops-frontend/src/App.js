import React, { useState } from "react";
import axios from "axios";

function App() {
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState("");

  const fetchAnalysis = async () => {
    try {
      setLoading(true);

      const response = await axios.get(
        "http://127.0.0.1:8000/fetch-and-analyze"
      );

      setAnalysis(response.data.analysis);
    } catch (error) {
      console.error(error);
      setAnalysis("Failed to fetch AI analysis.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#0f172a",
        color: "white",
        padding: "40px",
        fontFamily: "Arial",
      }}
    >
      <h1
        style={{
          fontSize: "42px",
          marginBottom: "20px",
        }}
      >
        AI DevOps Assistant
      </h1>

      <p
        style={{
          color: "#cbd5e1",
          marginBottom: "30px",
          fontSize: "18px",
        }}
      >
        Analyze GitHub Actions CI/CD failures using AI.
      </p>

      <button
        onClick={fetchAnalysis}
        style={{
          padding: "14px 24px",
          backgroundColor: "#2563eb",
          color: "white",
          border: "none",
          borderRadius: "10px",
          cursor: "pointer",
          fontSize: "18px",
        }}
      >
        Fetch Latest CI/CD Failure
      </button>

      {loading && (
        <p
          style={{
            marginTop: "20px",
          }}
        >
          AI is analyzing logs...
        </p>
      )}

      {analysis && (
        <div
          style={{
            marginTop: "30px",
            backgroundColor: "#1e293b",
            padding: "25px",
            borderRadius: "14px",
            whiteSpace: "pre-wrap",
          }}
        >
          <h2>AI Analysis</h2>

          <p
            style={{
              lineHeight: "1.8",
              marginTop: "15px",
            }}
          >
            {analysis}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;