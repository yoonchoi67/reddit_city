import React, { createContext, useEffect, useState } from 'react';

export const MarkerDataContext = createContext();

export const MarkerDataProvider = ({ children }) => {
  const [markerData, setMarkerData] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [hasMorePages, setHasMorePages] = useState(true);

  return (
    <MarkerDataContext.Provider value={markerData}>
      {children}
    </MarkerDataContext.Provider>
  );
};
