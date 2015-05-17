<html>
    <head><title>List Maker</title></head>
    <body>
         <h1>List Maker</h1>

         % if lists:
         <ul>
             % for list in lists:
              <li><a href="/list/{{list}}">{{list}}</a></li>
             % end
         </ul>
         % end

         <form method='POST' action='/list'>
              <legend>Create a new list.</legend>
              <ul>
                  <li><label for='listname'>Name:</label> <input name='listname'</li>
                  <li><label for='description'>Description:</label><input name='description'></li>
              </ul>
              <input type='submit'>
          </form>

    </body>
</html>