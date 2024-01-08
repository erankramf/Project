import React, { useState } from 'react';
import { ChevronDown, ChevronRight } from 'react-feather';

const CollapsibleComponent = ({ title, children }) => {
  const [isCollapsed, setIsCollapsed] = useState(true);

  const toggleCollapse = () => {
    setIsCollapsed(!isCollapsed); 
  };

  return (
    <div>
      <div onClick={toggleCollapse} style={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }}>
        <span style={{ marginRight: '10px' }}>{title}</span>
        <span>{isCollapsed ? <ChevronRight/> : <ChevronDown/>}</span>
      </div>
      {!isCollapsed && <div>{children}</div>}
    </div>
  );
};

export default CollapsibleComponent;

