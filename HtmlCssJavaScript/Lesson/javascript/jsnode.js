const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(`<!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>navbar</title>
      <style>
        * {
          box-sizing: border-box;
        }
        body {
          margin: 0px;
          padding: 0px;
        }
        .navbar {
          display: flex;
          justify-content: space-between;
          align-items: center;
          background-color: darkgrey;
          color: aliceblue;
        }
        .brand_title {
          font-size: 1.5rem;
          margin: 0.5rem;
        }
        .nav_links ul {
          margin: 0px;
          padding: 0px;
          display: flex;
          list-style: none;
        }
        .nav_links li a {
          text-decoration: none;
          color: azure;
          padding: 1rem;
          display: block;
        }
        .nav_links li:hover {
          background-color: aqua;
        }
        .toggle_button {
          position: absolute;
          top: 0.7rem;
          right: 1rem;
          display: none;
          flex-direction: column;
          justify-content: space-between;
          width: 30px;
          height: 21px;
        }
        .toggle_button .bar {
          height: 3px;
          width: 100%;
          background-color: azure;
          border-radius: 10px;
        }
        @media (max-width: 400px) {
          .toggle_button {
            display: flex;
          }
          .nav_links {
            display: none;
          }
          .navbar {
            flex-direction: column;
            align-items: flex-start;
          }
          .navbar_links ul {
            width: 100%;
            flex-direction: column;
          }
        }
      </style>
    </head>
    <body>
      <nav class="navbar">
        <div class="brand_title">Brand Name</div>
        <a href="#" class="toggle_button">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </a>
        <div class="nav_links">
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div>
      </nav>
    </body>
  </html>
  `);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});