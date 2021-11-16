import { withGoogleMap, GoogleMap, Marker, withScriptjs } from "react-google-maps";
import { LibraryLocation } from "../../../../accessors/types";

const Map = ({ latitude: lat, longitude: lng }: LibraryLocation) => (
    <GoogleMap
        defaultCenter={{ lat, lng }}>
        <Marker position={{ lat, lng }} />
    </GoogleMap>
);

export default withScriptjs(withGoogleMap(Map));
