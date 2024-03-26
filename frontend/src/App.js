import { useEffect } from 'react';
import './App.css';

function App() {
  useEffect(() => {
    console.log(import.meta.env); // Debugging: Check the structure of import.meta.env
    console.log(import.meta.env.API_URL); // Debugging: Check the value of API_URL
  }, []);

  return (
    <div className="App">
      home
    </div>
  );
}

export default App;
