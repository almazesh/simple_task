import React from 'react';
import ItemsList from './components/ItemsList';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>🚀 Simple Fullstack App</h1>
        <p>PostgreSQL + FastAPI + React + Docker</p>
      </header>
      
      <main className="App-main">
        <ItemsList />
      </main>
      
      <footer className="App-footer">
        <p>🐳 Powered by Docker Compose</p>
      </footer>
    </div>
  );
}

export default App;
