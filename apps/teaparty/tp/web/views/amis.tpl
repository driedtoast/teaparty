<%include file="header.html"/>

<div class="span-16">
<h1 class="fancy">${name} - ${account.name}</h1>

<div id="accordion">
% for ami in amis:
        <h3><a href="/ami/${account.name}/${ami.id}">${ami.name}</a></h3>
	<div>
		<p>ami id: ${ami.id}</p>
                <p>name: ${ami.name}</p>
                <p>description: ${ami.description}</p>
                <p>location: ${ami.location}</p>
                <p>image id: <a href="/ami/${account.name}/${ami.id}">${ami.id}</a></p>
                
	</div>
        
% endfor        
</div>


<script type="text/javascript">
$(function() {
        $("#accordion").accordion({ collapsible: true, active: false });
});
</script>
</div>
<div class="span-7 last">
    <p>&nbsp;</p>
   <p class="fancy large">AMIs for ${account.name}</p>
     <%include file="account_nav.tpl" />
</div>


<%include file="footer.html"/>

