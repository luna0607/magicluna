var express = require('express');
var router = express.Router();
var reuseFunc=require('./resuseFunctions');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('Magicluna', { title: 'Magicluna' });
});
router.get('/article_list',function (req,res,next) {
    var type=req.query.type;
    res.render('../views/article_list',{ type:type });
});
router.get('/get_article_list',function (req,res,next) {
    reuseFunc.getArticleList(req,res,next);
});
router.get('/get_article',function (req,res,next) {
    var type=req.query.type;
    var id=req.query.id;
    var article=req.query.article;
    if(article==="1"){
        reuseFunc.getArticle(req,res,next);
    }else {
        res.render('../views/article',{type:type,id:id})
    }
});
module.exports = router;
