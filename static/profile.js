let username = document.querySelector("#username").textContent
let accountType = document.querySelector("#account-type")
let nameInput = document.querySelector("#profile-name")

async function changeAccountType(option) {
    let response = await fetch(`/user_profile/${username}`,{
        method: "POST",
        headers:{
            'content-type': 'application/json'

        },
        body:JSON.stringify({
            "operation": "change_type",
            "changed_type": option
        })
    })
    response = await response.json()
    
}

accountType.addEventListener("change",(e)=>{
    let choosedOption = e.target.value
    changeAccountType(choosedOption)
})

function debounce(func,time){
    clearTimeout(timer)
    timer = setTimeout(func,time)
};
async function changeProfileName(changed_name){
    let response = await fetch(`/user_profile/${username}`,{
        method: "POST",
        headers:{
            "Content-Type": "Application/json"
        },
        body: JSON.stringify({
            'changed_name':  changed_name,
            operation: 'name_change'
        })
    })
    response = await response.json()

    nameInput.value = response.changed_name
    document.querySelector(".profile-username").textContent = response.changed_name
}

let timer;

nameInput.addEventListener("input",(e)=>{
    let text = e.target.value;

    debounce(changeProfileName(text),2000)
})