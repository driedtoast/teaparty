<%include file="header.html"/>

<div class="span-23 last">
<h1 class="fancy">${name} - ${account.name}</h1>
</div>



<style type="text/css" media="screen">
	.dataTables_info { padding-top: 0; }
	.dataTables_paginate { padding-top: 0; }
	.css_right { float: right; }

</style>

<div class="span-24 last" style="margin-top: 1em;"> 
<table class="display" cellpadding="0" cellspacing="0" border="0" id="instancestable" > 
<thead> 
	<tr> 
		<th>public dns</th>
		<th>instance id</th>
		<th>instance type</th>
		<th>availability zone</th>
		<th>state</th>
		<th>internal dns</th>
		<th>internal ip</th>
		<th>image id</th>
	</tr>
</thead>
<tbody>
% for instance in instances:
        <tr>
		<td>${instance.public_dns_name}</td>
		<td>${instance.id}</td>
		<td>${instance.instance_type}</td>
		<td>${instance.placement}</td>
		<td>${instance.state}</td>
		<td>${instance.private_dns_name}</td>
		<td>${instance.private_ip_address}</td>
		<td><a href="/ami/${account.name}/${instance.image_id}">${instance.image_id}</a></td>
	</tr>
% endfor
</tbody>
</table>
</div>

<script type="text/javascript">
$(function() {
        $("#instancestable").dataTable({"bJQueryUI": true, "sPaginationType": "full_numbers" });
});
</script>
<div class="container">
<%include file="footer.html"/>

