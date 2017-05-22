<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">

<head>
  <title>LoL Simulator</title>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
  <link rel="stylesheet" type="text/css" href="/static/style/style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <h1>{{name}} </h1>
	<h1><span class="alternate_colour">{{title}}</span></h1>
      </div>
      <div id="menubar">
        <ul id="menu">
          <!-- put class="tab_selected" in the li tag for the selected page - to highlight which page you're on -->
	  <li class="tab_selected"><a href="/">Champion</a></li>
          <li><a href="/Comparator">Comparator</a></li>
          <li><a href="/Object">Objects</a></li>
         -- <li><a href="/Runes">Runes</a></li>
         -- <li><a href="/Masteries">Masteries</a></li>
        </ul>
      </div>
    </div>
    <div id="site_content">
      <div id="panel"><img src="/static/images/{{name}}.jpg" alt={{name}} /></div>
      <div class="sidebar">
        <!-- insert your sidebar items here -->
        <h1>Latest News</h1>
        <h2>New Website Launched</h2>
        <h3>May 10, 2017</h3>
        <p>Take a look around and let us know what you think.<br /><a href="#">Read more</a></p>
        <h1>Useful Links</h1>
        <ul>
          <li><a href="http://euw.leagueoflegends.com/">Oficial web</a></li>
          <li><a href="https://developer.riotgames.com/">API web</a></li>
        </ul>
        <h1>Useful Info</h1>
        <p>The language by default is en_UK</p>
      </div>
      <div id="content">
        <!-- insert the page content here -->
