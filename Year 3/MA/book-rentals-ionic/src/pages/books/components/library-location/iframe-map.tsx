import { LibraryLocation } from "../../../../accessors/types";

const IFrameMap = ({ latitude, longitude }: LibraryLocation) => (
    <iframe
        src={`https://www.google.com/maps/embed/v1/place?q=${latitude},${longitude}&key=AIzaSyAIBbUmwHVhwjTxWXtKu_ROw1d9j-Of4bU`}
        width="100%"
        height="450"
        style={{border: 0}}
        loading="lazy"
    />
);

export default IFrameMap;
