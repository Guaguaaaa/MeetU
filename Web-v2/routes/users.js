const router = require("express").Router();

router.get("/", (req,res)=>{
    res.send("hey is user route");
});

module.exports = router