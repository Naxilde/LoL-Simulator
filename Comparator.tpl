% include('headerComparator.tpl')
<h1>Champions comparator </h1>
 <form action="/Ficha2" method="post">
		    <label>First champion name:</label>
		    <input type="text" name="name1" required/>
		    <p></p>
		    <label>Second champion name:</label>
		    <input type="text" name="name2" required/>
		    <p></p>
		    <label>Languaje(ej. es_ES,en_US...):</label>
		    <input type="text" name="Language"/>
		  <p></p>
		  <input type="submit" value="Send"/>
		  </form>
% include('footer.tpl')
