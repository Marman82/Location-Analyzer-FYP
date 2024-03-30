import React, { useState, useEffect } from "react";
import Search from "./Search";
import Maps from "./Maps";
import "./style.css";
import { MapContainer, Marker, Popup, TileLayer, useMap } from "react-leaflet";

function App() {
  const [selectPosition, setSelectPosition] = useState(null);
  const pos = [22.397, 114.327];

  return (
    <div
      style={{
        border: "2px solid red",
        display: "flex",
        flexDirection: "row",
        width: "100vw",
        height: "100vh",
      }}
    >
      <div style={{ border: "2px solid red", width: "50vw", height: "100vh" }}>
        <MapContainer
          center={pos}
          zoom={13}
          scrollWheelZoom={true}
          style={{ width: "100%", height: "100%" }}
        >
          <Maps selectPosition={selectPosition} />
        </MapContainer>
      </div>
      <div style={{ border: "2px solid red", width: "50vw" }}>
        <Search
          selectPosition={selectPosition}
          setSelectPosition={setSelectPosition}
        />
      </div>
    </div>
  );
}

export default App;
