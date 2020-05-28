# Day 1 Built the development environment

1. asynchronous web framework
   * pip3 install aiohttp
2. pip3 install jinja2
   * pip3 install jinja2
3. download MySQL
   * remember root & password (you know)
   * MySQL Python asynchronous driver aiomysql
     * pip2 install aiomysql
3. build working directory, the structure is as below
   * tech_blog
     * backup -- backup directory
     * conf -- configuration file
     * dist -- packaged file
     * www/ -- web directory, store .py files
       * static/ -- static files
       * templates/ -- templates files
     * ios/ -- iOS App 
     * LICENSE -- LICENSE code
  
# Day 2

1. The Web App is based on asyncio, use aiohttp to write a app.py
2. use aiohttp
3. run app.py under www/, The Web App will listen for HTTP requests on port 9000, response on home page '/'
4. go to browser and check localhost:9000, it will return html header 'First Try'

# Day 3
  


