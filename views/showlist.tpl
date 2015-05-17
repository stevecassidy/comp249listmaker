<html>
    <head><title>List Maker</title></head>
    <body>
         <h1>List: {{listname}}</h1>

         <ul>
             <li><a href="/">Home</a></li>
         </ul>

         <p>{{description}}</p>

         % if things:
         <ul>
             % for thing in things:
              <li>{{thing}}</li>
             % end
         </ul>
         % end

         <form method='POST' action='/list/{{listname}}'>
              <legend>Add something to this list.</legend>
              <ul>
                  <li><input name='thing'></li>
              </ul>
              <input type='submit'>
          </form>

    </body>
</html>