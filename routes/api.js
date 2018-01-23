/**
 * Created by Ariana on 2017/12/3.
 */
var express = require('express');
var router = express.Router();
var reuseFunc=require('./dao');

/* GET tech articles. */
router.get('/tech_articles',function (req,res,next) {
    reuseFunc.getArticleList(req,res,next);
});

module.exports = router;
