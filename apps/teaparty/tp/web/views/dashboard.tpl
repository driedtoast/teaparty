<%include file="header.html"/>

<div class="span-16">
<h1 class="fancy">${name}</h1>


<div id="accordion">
% for account in accounts:
	<h3><a href="/account/${account.name}">${account.name}</a></h3> 
	<div>
        	<p>account id: ${account.id}</p>
                <p>account key: ${account.access_key}</p>
                <p>secret key: ${account.secret_key}</p>
                <p><a href="/account/${account.name}">instances</a></p>
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
   <p class="fancy large"> Select an account on the left </p>
</div>


<%include file="footer.html"/>

