import { useState } from 'react';
import LoadingScreen from './components/LoadingScreen';
import HomePage from './components/HomePage';

function App() {
  const [isLoading, setIsLoading] = useState(true);

  return (
    <>
      {isLoading ? (
        <LoadingScreen onComplete={() => setIsLoading(false)} />
      ) : (
        <HomePage />
      )}
    </>
  );
}

export default App;
