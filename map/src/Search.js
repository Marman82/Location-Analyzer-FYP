import React, { useState, useEffect } from "react";
import { OutlinedInput, Button } from "@material-ui/core";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import Divider from "@material-ui/core/Divider";

const NOMINATION_BASE_URL = "https://nominatim.openstreetmap.org/search?";

export default function Search(props) {
  const { selectPosition, setSelectPosition } = props;
  const [searchText, setSearchText] = useState("");
  const [placeList, setPlaceList] = useState([]);
  const [searching, setSearching] = useState(false);

  const handleFileInputChange = (event) => {
    console.log("file change");

    if (!event.target.files[0]) {
      console.log("No file");
      return;
    }
    const formData = new FormData();
    formData.append("file", event.target.files[0]);

    setSearching(true);

    const endpoint = "http://localhost:8000/uploadfile";
    fetch(endpoint, {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((res) => {
        setSearchText(res.lon + " " + res.lat);
        setSearching(false);
        console.log({ lon: res.lon, lat: res.lat });
        setSelectPosition({ lon: res.lon, lat: res.lat });
      });
  };

  return (
    <div>
      <div class="file-upload-section">
        <h1>Predict Image</h1>
        <div className="custom-file-upload">
          <input type="file" onChange={handleFileInputChange} />
        </div>

        <input
          type="text"
          style={{ width: "100%" }}
          value={searchText}
          disabled={searching}
          onChange={(event) => {
            setSearchText(event.target.value);
          }}
        />
        <Button
          variant="contained"
          color="primary"
          disabled={searching}
          style={{ display: "flex", alignItems: "center" }}
          onClick={() => {
            const params = {
              q: searchText,
              format: "json",
              addressdetails: 1,
              polygon_geojson: 0,
            };
            const queryString = new URLSearchParams(params).toString();
            const requestOptions = {
              method: "GET",
              redirect: "follow",
            };
            fetch(`${NOMINATION_BASE_URL}${queryString}`, requestOptions)
              .then((response) => response.text())
              .then((result) => {
                setPlaceList(JSON.parse(result));
              })
              .catch((err) => console.log("err: ", err));
          }}
        >
          Search
        </Button>
      </div>
      <List component="nav" aria-label="main mailbox folders">
        {placeList.map((item) => {
          return (
            <div key={item?.place_id}>
              {" "}
              <ListItem
                button
                onClick={() => {
                  console.log({ lon: item.lon, lat: item.lat });
                  setSelectPosition({ lon: item.lon, lat: item.lat });
                }}
              >
                <ListItemIcon>
                  <img
                    src="./searchResultPin.png"
                    alt="pin"
                    style={{ width: "20px", height: "20px" }}
                  />
                </ListItemIcon>
                <ListItemText primary={item?.display_name} />
              </ListItem>
              <Divider />
            </div>
          );
        })}
      </List>
    </div>
  );
}
