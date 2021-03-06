var inputImage = document.getElementById("inputImage");
var fileList = [];

//the below logic is keeping track of whenever user enters that input button for inputting the file
//we keep saving those files in fileList array(even if files are not images, because it's been done in other two similar assignments)
inputImage.addEventListener("change", function(e) {
  for (var i = 0; i < inputImage.files.length; i++) {
   
    //check if the extension of file is valid
    name = String(inputImage.files[i].name);
    var l = name.split(".", 2);
    var extn = String(l[1]);
    //if valid sendFile otherwise not
    if (
      extn.localeCompare("png") == 0 ||
      extn.localeCompare("jpg") == 0 ||
      extn.localeCompare("jpeg") == 0
    ) {
      var node = document.createElement("LI"); // Create a <li> node
      var textnode = document.createTextNode(name); // Create a text node
      node.appendChild(textnode); // Append the text to <li>
      document.getElementById("displayFile").appendChild(node);
      fileList.push(inputImage.files[i]);
      console.log("sending Document");
    } else {
      console.log("it's not a valid extension");
      var node = document.createElement("LI"); // Create a <li> node
      var textnode = document.createTextNode(
        "only png,jpeg,jpg are allowed, please enter file with valid extensions"
      ); // Create a text node
      node.appendChild(textnode); // Append the text to <li>
      document.getElementById("displayFile").appendChild(node);
    }
  }
});

//the below logic is activated when the user hits submit button, one by one we make ajax
//request to the server for sending the files in fileList array
var fileCatcher = document.getElementById("file-catcher");
fileCatcher.addEventListener("submit", function(e) {
  e.preventDefault();
  fileList.forEach(function(file) {
    sendFile(file);
    console.log("sending the files");
  });
  //after sending all the files making a get request to viewImage
  setTimeout(getRequest, 1000);
});

//sending get request after 1000ms to make sure that the server has saved all the files 
//which we sent through ajax
getRequest = function() {
  window.location.href = "/fossee1/viewImage";
};

//ajax logic for sending the files to the server
sendFile = function(file) {
  var title = document.getElementById("title").value;
  var description = document.getElementById("description").value;

  var formData = new FormData();
  formData.append("image", file);
  formData.append("title", title);
  formData.append("description", description);

  jQuery.ajax({
    url: "",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function() {
      console.log("done successfully");
    }
  });
};
