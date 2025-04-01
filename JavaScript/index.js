// Servidor mínimo con Node.js
const http = require('http');
const fs = require('fs');
const path = require('path');

// Crear servidor
const server = http.createServer((req, res) => {
  console.log(`Petición: ${req.url}`);
 
  // Determinar qué archivo servir
  let filePath;
  if (req.url === '/' || req.url === '') {
    filePath = path.join(__dirname, 'public', 'index.html');
  } else {
    filePath = path.join(__dirname, 'public', req.url);
  }
 
  // Leer y servir el archivo
  fs.readFile(filePath, (err, content) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(content);
  });
});

// Iniciar servidor
const PORT = 3000;
server.listen(PORT, '0.0.0.0',  () => {
  console.log(`Servidor iniciado en puerto ${PORT}`);
});