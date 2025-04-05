import React, { useEffect, useState } from 'react';

const ResultsDisplay = ({ scrapedData }) => {
    const [contacts, setContacts] = useState([]);

    useEffect(() => {
        if (scrapedData) {
            setContacts(scrapedData);
        }
    }, [scrapedData]);

    return (
        <div className="results-display">
            <h2>Contact Information</h2>
            {contacts.length > 0 ? (
                <ul>
                    {contacts.map((contact, index) => (
                        <li key={index}>
                            <p>Name: {contact.name}</p>
                            <p>Email: {contact.email}</p>
                            <p>Phone: {contact.phone}</p>
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No contact information available.</p>
            )}
        </div>
    );
};

export default ResultsDisplay;