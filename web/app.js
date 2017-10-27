import path from 'path';
import http from 'http';
import logger from 'morgan';
import multer from 'multer';
import Express from 'express';
import SocketIO from 'socket.io';

var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, './uploads');
  },
  filename: function (req, file, cb) {
    cb(null, 'image.png')
  }
});
var upload = multer({ storage: storage });

const port = process.env.port || 3000;
const app = Express();
const server = http.createServer(app);
const io = SocketIO();

io.attach(server);

app.set('port', port);
app.use(Express.static(path.join(__dirname, 'uploads')));

app.post('/upload', function (req, res, next) {
  console.log(req);
  var uploaded = upload.any();
  uploaded(req, res, function (err) {
    if (err) {
      res.status(500).end();
    }
    io.emit('goRefresh', { msg: 'The file is uploaded!' });
    res.status(204).end();
  });
});

server.listen(port);