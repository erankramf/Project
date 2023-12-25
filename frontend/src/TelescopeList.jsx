import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TelescopeList = ({ onTelescopeSelect }) => {
  const [telescopes, setTelescopes] = useState([]);
  const [selectedTelescope, setSelectedTelescope] = useState(null);

  useEffect(() => {
    const fetchTelescopes = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/telescopes');
        setTelescopes(response.data);
      } catch (error) {
        console.error('Error fetching telescopes:', error);
      }
    };

    fetchTelescopes();
  }, []);

  const handleTelescopeClick = (telescope) => {
    setSelectedTelescope(telescope);
    onTelescopeSelect(telescope);
  };

  return (
    <div>
      <h2>Telescope List:</h2>
      <ul>
        {telescopes.map((telescope) => (
          <li
            key={telescope.id}
            onClick={() => handleTelescopeClick(telescope)}
            style={{ cursor: 'pointer', fontWeight: telescope === selectedTelescope ? 'bold' : 'normal' }}
          >
            {telescope.name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TelescopeList;
