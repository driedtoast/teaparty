<%include file="header.html"/>

<div class="span-16">
<h1 class="fancy">${name}</h1>

<div id="list">
<ul>
% for flow in flows:
    <li><a href="/jobs/flow/${flow}">${flow}</a></li>
% endfor
</ul>
</div>

</div>
<div class="span-7 last">
    <p>&nbsp;</p>
</div>


<%include file="footer.html"/>

