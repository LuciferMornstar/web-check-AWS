import Amplify from 'aws-amplify';
import awsconfig from './aws-exports';
import React from 'react';
import ReactDOM from 'react-dom';
import ResultsDisplay from './components/ResultsDisplay';
import './styles/app.css';

Amplify.configure(awsconfig);

const App = () => {
    return (
        <div className="App">
            <h1>Contact Information Scraper</h1>
            <ResultsDisplay />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById('root'));