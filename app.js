var express = require('express');
var path = require('path');
var logger = require('morgan');
var multer  = require('multer');

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './uploads');
  },
  filename: function (req, file, cb) {
    cb(null, 'image.png')
  }
});
var upload = multer({ storage: storage });

var app = express();
var socketIO = require('socket.io');
var io = socketIO();
app.io = io;

app.use(express.static(path.join(__dirname, 'uploads')));

app.post('/upload', function (req, res, next) {
  console.log(req);
  var uploaded = upload.any();
  uploaded(req, res, function(err) {
    if (err) {
      res.status(500).end();
    }
    io.emit('goRefresh', {msg:'The file is uploaded!'});
    res.status(204).end();
  });
});

module.exports = app;
