% include('headerIndex.tpl')
<h1>Champion search </h1>
 <form action="/Ficha" method="post">
		    <label><h1>Champion name:</h1></label>
		    <input type="text" name="name"/>
		    <p></p>
		    <label><h1>Languaje(ej. es_ES,en_US...):</h1></label>
		    <input type="text" name="Language"/>
		  </br >
		  <input type="submit" value="Send"/>
		  </form>
% include('footer.tpl')
