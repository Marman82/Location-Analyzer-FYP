import React, { useEffect, useState } from "react";
import { MapContainer, Marker, Popup, TileLayer, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import Pin from "leaflet";

//座標圖
const icon = Pin.icon({
  iconUrl: "./mapPin.png",
  iconSize: [25, 25],
});

export default function Maps(props) {
  const { selectPosition } = props;
  const map = useMap();

  useEffect(() => {
    if (selectPosition) {
      map.setView(
        Pin.latLng(selectPosition?.lat, selectPosition?.lon),
        map.getZoom(),
        { animate: true }
      );
    }
  }, [selectPosition]);

  return (
    <>
      <TileLayer
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        url="https://api.maptiler.com/maps/outdoor-v2/256/{z}/{x}/{y}.png?key=UikmaySRxmue4JJzAVLX"
      />
      {selectPosition && (
        <Marker
          position={[selectPosition?.lat, selectPosition?.lon]}
          icon={icon}
        >
          <Popup>Your Here!</Popup>
        </Marker>
      )}
    </>
  );
}
