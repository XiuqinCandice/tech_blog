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
  
# Day 2 Build the Web App Structure

1. The Web App is based on asyncio, use aiohttp to write a app.py
2. use aiohttp
3. run app.py under www/, The Web App will listen for HTTP requests on port 9000, response on home page '/'
4. go to browser and check localhost:9000, it will return html header 'First Try'

# Day 3 Write ORM
[Day3](https://github.com/XiuqinCandice/tech_blog/tree/Day-3)
(use MySQL)
1. all the data, including user info, published blogs and comments are all stored in databasae
2. encapsulated 'SELECCT, INSERT, UPDATE and DELETE' to encapsulate functions
3. Web framework used asyncio aioheep based on coroutine asynchronous model, all users got servics from one thread, have to be fast, so we should use asynchronous
4. Once we use asynchronous, every step is asynchrous
5. **aiomysql** provided asynchronous IO drive for MySQL database
6. Build the connection pool
   1. every http request can get sql connection from the sql
   2. we don' have to turn on and off database connection, can reuse
   
# Day 4 Write model for user, blog, comment
[Day4](https://github.com/XiuqinCandice/tech_blog/tree/Day-4)

# Day 5 Write Web Framework
[Day5](https://github.com/XiuqinCandice/tech_blog/tree/Day-5)

# Day 6 Write Config Files
[Day6](https://github.com/XiuqinCandice/tech_blog/tree/Day-6)

# Day 7 Write MVC
[Day 7](https://github.com/XiuqinCandice/tech_blog/tree/Day-7)

# Day 8 Front-End
[Day 8](https://github.com/XiuqinCandice/tech_blog/tree/Day-8)

# Day 9 API
[Day 9](https://github.com/XiuqinCandice/tech_blog/tree/Day-9)

# Day 10 Login and signup
[Day 10](https://github.com/XiuqinCandice/tech_blog/blob/Day-10)

