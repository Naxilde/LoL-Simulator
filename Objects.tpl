% include('headerObjects.tpl')
<h1>Object search </h1>
 <form action="/Object" method="post">
		    <label>Object ID:</label>
		    <input type="text" name="name"/>
		    <label>Languaje(ej. es_ES,en_US...):</label>
		    <input type="text" name="Language"/>
		  <input type="submit" value="Send"/>
		  </form>
% include('footer.tpl')
