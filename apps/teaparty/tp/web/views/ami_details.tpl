<%include file="header.html"/>

<div class="span-16">
<h1 class="fancy">${name} - ${account.name}</h1>
 
<p>ami id: ${ami.id}</p>
<p>name: ${ami.name}</p>
<p>description: ${ami.description}</p>
<p>location: ${ami.location}</p>
<p>owner id: ${ami.ownerId}</p>


<a href="#/api/amis/${account.name}" id="amilist_link" >get ami list</a>
   
   <div id="ajaxmain">
   </div>
   
   <script type="text/javascript">
    var count = 0;
    var app = $.sammy(function() {
        this.element_selector = '#ajaxmain';    
        this.use(Sammy.Template);
        this.get('#/api/amis/:name', function(context) {
          context.log(' Using account name: ' + this.params['name']);
          var nummy = this.params['name'];
          
           $.ajax({
            url: '/api/amis/'+nummy, 
            dataType: 'json',
            // dataFilter: function (data, type) {
            //    context.log('data is ' + data);
            //},
            success: function(amis) {
              $.each(amis.amis, function(i, ami) {
                context.log(ami.name);
                context.partial('/static/templates/ami.template', {obj: ami}, function(rendered) {
                    context.$element().append(rendered);
                });
              });
            }
          });
           
           return false; 
        }
        );
        
        
      });
    
   
   $('#amilist_link').click(function() {
        app.run('#/api/amis/${account.name}');
   });
   
   </script>
    
    
</div>


<div class="span-7 last">
    <p>&nbsp;</p>
   <p class="fancy large">AMI image part of ${account.name}</p>
   <%include file="account_nav.tpl" />
</div>

<%include file="footer.html"/>
