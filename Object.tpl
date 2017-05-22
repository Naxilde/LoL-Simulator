% include('headerObject.tpl',name=stats["name"])
<h1>Item</h1>
<p>Cost:{{stats["gold"]["total"]}}({{stats["gold"]["base"]}})</p>
<p>Description:{{stats["description"]}}</p>
% include('footer.tpl')
