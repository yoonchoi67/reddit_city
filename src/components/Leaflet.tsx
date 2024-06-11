import React, { useEffect, useRef, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet.markercluster';

const myIcon = L.icon({
  iconSize: [25, 41],
  iconAnchor: [10, 41],
  popupAnchor: [2, -40],
  // specify the path here
  iconUrl: "https://unpkg.com/leaflet@1.5.1/dist/images/marker-icon.png",
  shadowUrl: "https://unpkg.com/leaflet@1.5.1/dist/images/marker-shadow.png"
});


function LeafletMap() {
  const mapRef = useRef<L.Map | null>(null);//useRef(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Initialize the map
    mapRef.current = L.map('mapid').setView([42.0, -9.0], 2);

    // Add tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      maxZoom: 18
    }).addTo(mapRef.current);

    // Fetch marker data
    fetch('/final_geojson_with_country.json')
      .then(response => response.json())
      .then(data => {
        const markers = L.markerClusterGroup();
        data.properties.forEach((rec: any) => {
          const marker = L.marker([rec.lat_y, rec.long_x], {icon: myIcon});
          // const marker = L.marker(new L.LatLng(rec.lat_y, rec.long_x));
          marker.bindPopup(`
            <b>Reddit Post Title:</b> ${rec.title} <br/>
            <b>Geocoded into:</b> ${rec.display} <br/>
            <b>Latitude:</b> ${rec.lat_y} <b>Longitude:</b> ${rec.long_x} <br/>
            <b>Click <a href="https://reddit.com${rec.permalink}" target="_blank">here</a> for the original post.</b>
          `);
          markers.addLayer(marker);
        });
        if (mapRef.current !== null) {
          mapRef.current.addLayer(markers);
          setLoading(false);
        }
      })
      .catch(error => {
        console.error('Error fetching marker data:', error);
        setLoading(false);
      });

    // Clean up the map on component unmount
    return () => {
      if (mapRef.current !== null) {
      mapRef.current.remove();
      }
    };
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h5 className="card-title">
          {loading ? (<p>World Map is loading... Please Wait</p>) : <p>World Map</p>}
        </h5>
        <div id="mapid" style={{ height: '500px' }}></div>
      </div>
    </div>
  );
}

export default LeafletMap;