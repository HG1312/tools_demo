// API gateway: forwards order requests to the Python worker.
const express = require("express");
const axios = require("axios");
require("dotenv").config();

const app = express();
app.use(express.json());

const WORKER_URL = process.env.WORKER_URL || "http://localhost:8000";

app.post("/api/orders", async (req, res) => {
  try {
    const r = await axios.post(`${WORKER_URL}/orders`, req.body);
    res.status(201).json(r.data);
  } catch (e) {
    res.status(502).json({ error: "worker unavailable" });
  }
});

app.listen(3000, () => console.log("gateway on :3000"));
