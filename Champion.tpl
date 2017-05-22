% include('headerChampion.tpl', name=campeon,title=mote)
<h1> Stats </h1>
	<table>
		<tr>
			<td><strong>stat</stong></td>
		</tr>
	%for i in Info :
		<tr>
			<td>{{i}}</td>
			<td>{{Info[i]}}</td>
	%end
		</tr>
	</table>
% include('footer.tpl')
