/**
 * Created by Ariana on 2017/12/3.
 */
var mysql = require('mysql');
var $conf = require('../conf/db');
var swig = require("swig");
var pool = mysql.createPool($conf.mysql);
module.exports={
   getArticleList:function (req,res,next) {
       var type=req.query.type;
       var query_sentence="";
       switch(type){
           case "0":
               query_sentence="SELECT id,title,create_time FROM tech_articles";
              break;
           case "1":
               query_sentence="SELECT id,title,create_time FROM life_articles";
               break;
           case "2":
               query_sentence="SELECT id,title,create_time FROM casual_articles";
               break;
       }
       pool.getConnection(function (err, connection) {
           if (err) {
               console.log("数据库连接出错");
               connection.release();
           }else {
               connection.query(query_sentence,function (err,result,fields) {
                   if(err){
                       console.log(err);
                   }else{
                      var titles=[];
                      result.forEach(function (value, index, array) {
                          var date=new Date(value.create_time);
                          var tmp=(1900+date.getYear())+"-"+(1+date.getMonth())+"-"+date.getDate();
                          value.create_time=tmp;
                          titles.push(value)
                      });
                       res.json(titles);
                   }
               });
           }
           connection.release();
       })
   },
   getArticle:function (req,res,next) {
       var type=req.query.type;
       var id=req.query.id;
       var query_sentence="";
       switch (type){
           case "0":
               query_sentence="SELECT * FROM tech_articles WHERE id="+id;
               break;
           case "1":
               query_sentence="SELECT * FROM life_articles WHERE id="+id;
               break;
           case "2":
               query_sentence="SELECT * FROM casual_articles WHERE id="+id;
               break;
       }
          pool.getConnection(function (err, connection) {
              if (err) {
                  console.log("数据库连接出错");
                  connection.release();
              }else {
                  connection.query(query_sentence,function (err,result,fields) {
                      if(err){
                          console.log(err);
                      }else{
                          var tmp={};
                          result.forEach(function (value, index, array) {
                              tmp.id=value.id;
                              tmp.title=value.title;
                              var content=value.content.replace(/</g,"&lt;");
                              content=content.replace(/>/g,"&gt;");
                               tmp.content=content.replace(/\n/g,"</br>");
                              var createDay=new Date(value.create_time);
                              tmp.createTime=(1900+createDay.getYear())+"-"+(1+createDay.getMonth())+"-"+createDay.getDate();
                              var modifyDay=new Date(value.modifiy_time);
                              tmp.modifyTime=(1900+modifyDay.getYear())+"-"+(1+modifyDay.getMonth())+"-"+modifyDay.getDate();
                          });
                          res.json(tmp);
                      }
                  });
              }
              connection.release();
          });
      }
};
