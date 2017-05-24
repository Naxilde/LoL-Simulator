% include('headerObjects.tpl')
<h1>Object search </h1>
 <form action="/Object" method="post">
		    <label>Item name:</label>
		    <input type="text" name="name3"/>
		    <p></p>
		    <label>Languaje(ej. es_ES,en_US...):</label>
		    <input type="text" name="Language"/>
		  <input type="submit" value="Send"/>
		  </form>
% include('footer.tpl')
