import "./db";
import "./models/Video";
import app from "./server";

const port = 5000;

const handleListening = () =>
  console.log(`Server Listening on port https://localhost:${port}`);

app.listen(port, handleListening);
