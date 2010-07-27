<%include file="header.html"/>

<div class="span-16">
<h1 class="fancy">${name} - ${account.name}</h1>



<h2>running</h2>
<div id="accordion">
% for instance in instances:
        % if (instance.state == 'running'):
	<h3><a href="/instance/${instance.id}">(${instance.id}) ${instance.public_dns_name}</a></h3>
	<div>
		<p>instance id: ${instance.id}</p>
		<p>external dns: ${instance.public_dns_name}</p>
                <p>instance state: ${instance.state}</p>
                <p>instance_type: ${instance.instance_type}</p>
                <p>internal dns: ${instance.private_dns_name}</p>
		<p>availability zone: ${instance.placement} </p>
		<p>groups:
			<ul>
			% for group in instance.groups:
				<li>${group}</li>
			% endfor
			</ul>
		</p>
                <p>image id: <a href="/ami/${account.name}/${instance.image_id}">${instance.image_id}</a></p>
                
	</div>
        % endif
% endfor        
</div>

<h2>stopped</h2>
<div id="stoppedaccordion">
% for instance in instances:
        % if (instance.state != 'running'):
	<h3><a href="/instance/${instance.id}">(${instance.id}) ${instance.public_dns_name}</a></h3>
	<div>
		<p>instance id: ${instance.id}</p>
                <p>instance state: ${instance.state}</p>
                <p>instance_type: ${instance.instance_type}</p>
                <p>internal dns: ${instance.private_dns_name}</p>
		<p>availability zone: ${instance.placement} </p>
		<p>groups:
			<ul>
			% for group in instance.groups:
				<li>${group}</li>
			% endfor
			</ul>
		</p>
                <p>image id: <a href="/ami/${account.name}/${instance.image_id}">${instance.image_id}</a></p>
                
	</div>
        % endif
% endfor        
</div>

<script type="text/javascript">
$(function() {
        $("#accordion").accordion({ collapsible: true, active: false });
        $("#stoppedaccordion").accordion({ collapsible: true, active: false });
});
</script>
</div>
<div class="span-7 last">
    <p>&nbsp;</p>
   <p class="fancy large">Instances part of ${account.name}</p>
     <%include file="account_nav.tpl" />
</div>


<%include file="footer.html"/>

