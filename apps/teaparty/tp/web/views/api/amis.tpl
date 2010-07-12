{

    "account":{
        "name":"${account.name}"
    },
    "amis":[
    % for i in range(len(amis)):
        
        { 
        "name":"${amis[i].name}",
        "id":"${amis[i].id}",
        "description":"${amis[i].description}",
        "location":"${amis[i].location}"
        }
        % if len(amis) > (i+1) :
            ,
        % endif
    % endfor 
    
    ]

}
