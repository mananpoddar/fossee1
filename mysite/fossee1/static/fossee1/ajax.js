
        var inputImage = document.getElementById('inputImage');
        var fileList = [];
        
        inputImage.addEventListener('change',function(e){
            for(var i =0;i<inputImage.files.length;i++){
                fileList.push(inputImage.files[i]);
                name = String(inputImage.files[i].name);
                console.log('is it adding image');
                var node = document.createElement("LI");                 // Create a <li> node
                var textnode = document.createTextNode(name);         // Create a text node
                node.appendChild(textnode);                              // Append the text to <li>
                document.getElementById("displayFile").appendChild(node);
            }
        })
      
        var fileCatcher = document.getElementById('file-catcher')
        fileCatcher.addEventListener('submit',function(e){
            e.preventDefault();
            fileList.forEach(function(file){
                
                sendFile(file);
                console.log("sending the files");
            });
           //after sending all the files making a get request to viewImage 
           setTimeout(getRequest, 1000);
           

        });
        getRequest = function(){
            window.location.href="/fossee1/viewImage";
        };
        
        sendFile = function(file){
           
            var title       =   document.getElementById('title').value
            var description =   document.getElementById('description').value
        
            var formData = new FormData();
            formData.append("image",file)
            formData.append("title",title)
            formData.append("description",description)


          
            jQuery.ajax({
                url: "",
                type: "POST",
                data:formData,
                processData: false,
                contentType: false,
                success:function(){
                    console.log("done successfully");
                }
            });
        };