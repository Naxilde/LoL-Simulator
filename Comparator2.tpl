% include('headerComparator2.tpl',name1=campeon1,name2=campeon2,champ1=campeon1+"1",champ2=campeon2+"1")
	<table>
	<tr>
		<td><strong>stat</stong></td>
		<td><strong>{{campeon1}}</strong></td>
		<td><strong>{{campeon2}}</strong></td>
	</tr>
	%for i,e in map(None,Info1,Info2):
		<tr>
			<td>{{i}}</td>
			<td>{{Info1[i]}}</td>
			<td>{{Info2[e]}}</td>
	%end
		</tr>
	</table>
% include('footer.tpl')
