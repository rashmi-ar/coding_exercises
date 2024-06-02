"use client";

import React, { useState } from 'react';
import axios from 'axios';
import styles from '../styles/Home.module.css';

export default function Home() {
  const [description, setDescription] = useState("");
  const [plantumlImage, setPlantumlImage] = useState("");
  const [plantumlCode, setPlantumlCode] = useState('');

  const handleSubmit = async (event: { preventDefault: () => void; }) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://127.0.0.1:8000/generate_plantuml/", { description });
      setPlantumlCode(response.data.plantuml_code);
      setPlantumlImage(response.data.image_url);
    } catch (error) {
      console.error("There was an error generating the PlantUML diagram!", error);
    }
  };

  return (
    <div className={styles.container}>
      <h1>PlantUML Generator</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Enter scenario description"
          className={styles.textarea}
        />
        <button type="submit" className={styles.button}>Generate</button>
      </form>
      {plantumlCode && (
        <div className={styles.codeContainer}>
          <h2>Generated PlantUML Code:</h2>
          <pre className={styles.codeBlock}>{plantumlCode}</pre>
        </div>
      )}
      {plantumlImage && (
        <div>
          <h2>Generated PlantUML Diagram:</h2>
          <img src={plantumlImage} alt="PlantUML Diagram" />
        </div>
      )}
    </div>
  );
}
