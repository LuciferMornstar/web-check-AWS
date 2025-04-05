import React, { useEffect, useState } from 'react';

const ResultsDisplay = ({ scrapedData }) => {
    const [contacts, setContacts] = useState([]);

    useEffect(() => {
        if (scrapedData) {
            setContacts(scrapedData);
        }
    }, [scrapedData]);

    return (
        <div className="lucifer-tracker">
            <h2>Lucifer Morningstar's Tracker</h2>
            <p className="tracker-subtitle">Tracking demon and angel movements in real time</p>
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