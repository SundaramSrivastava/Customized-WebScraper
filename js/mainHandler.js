let store = {};

let activeSubFile = "";
let continueSameIndex = false;

selectThisTag = (event) => {
  if (event.target.classList.value.includes("Scrapped")) {
    delete event.target.classList.remove("Scrapped");
    store[activeSubFile] = store[activeSubFile].filter(
      (value, index) => value != event.target.innerText
    );
  } else {
    event.target.classList.add("Scrapped");
    if (continueSameIndex) {
       
        store[activeSubFile][store[activeSubFile].length-1] += event.target.innerText
    } else {
        store[activeSubFile].push(event.target.innerText);
    }
    
  }

  console.log(store);
};

function modal(){
    document.getElementById("createFileModal").showModal();
}

function closeModal() {
  let newFile = document.getElementById("newFileName").value
  let activeFile = document.getElementById("selectActive").value
  
  if (newFile != "") {
    selectActive = document.getElementById("selectActive")
    store[newFile] = [];
    console.log(store);
    document.getElementById("newFileName").value = "";
    selectActive.add(new Option(newFile,newFile), undefined)
  }

  if(activeFile != ""){
      activeSubFile = activeFile
      console.log(activeSubFile)
  }

  document.getElementById("createFileModal").close();
}

continueLine = () =>{
    continueSameIndex = !continueSameIndex;
    if (continueSameIndex) {
        document.getElementById("continue").innerHTML='+'
    } else {
        document.getElementById("continue").innerHTML='new Line'
    }
}

generateFile = () => {
    download("OUTPUT.txt", store)
}

function download(filename, data) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(JSON.stringify(data)));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}