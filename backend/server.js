const express = require("express");
const axios = require("axios");
const cors = require("cors");
const { ruleCheck } = require("./analyzer");
const app = express();
app.use(cors());
app.use(express.json());
app.post("/check-url", async (req, res) => {
    const { url }= req.body;
    try {
        const mlResponse= await axios.post("http://127.0.0.1:8000/predict", {
            url: url
        });
        
        const mlPrediction= mlResponse.data.prediction;
        const mlConfidence= mlResponse.data.confidence;
        const ruleScore= ruleCheck(url);
        let riskScore= ruleScore;
        if (mlPrediction === 1) riskScore += 2;
        let finalResult= riskScore>= 4 ? "Phishing" : "Safe";
        res.json({
            ml_prediction: mlPrediction,
            ml_confidence: mlConfidence,
            rule_score: ruleScore,
            final_result: finalResult
        });
    } catch(err) {
        res.status(500).send("Error");
    }
});
app.listen(3000, () => console.log("Server running on port 3000"));