<%include file="header.html"/>

<div class="span-16">
<h1 class="fancy">${name} - ${account.name}</h1>
 
<p>ami id: ${ami.id}</p>
<p>name: ${ami.name}</p>
<p>description: ${ami.description}</p>
<p>location: ${ami.location}</p>


    
    
</div>
<div class="span-7 last">
    <p>&nbsp;</p>
   <p class="fancy large">AMI image part of ${account.name}</p>
   <%include file="account_nav.tpl" />
</div>

<%include file="footer.html"/>
