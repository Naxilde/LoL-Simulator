% include('headerIndex.tpl')
<h1>Champion search </h1>
 <form action="/Ficha" method="post">
		    <label>Champion name:</label>
		    <input type="text" name="name"/>
		    <p></p>
		    <label>Languaje(ej. es_ES,en_US...):</label>
		    <input type="text" name="Language"/>
		  <input type="submit" value="Send"/>
		  </form>
% include('footer.tpl')
