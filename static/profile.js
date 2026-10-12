let username = document.querySelector("#username").textContent
let accountType = document.querySelector("#account-type")
let nameInput = document.querySelector("#profile-name")

async function changeAccountType(option) {
    let response = await fetch(`/profile/${username}`,{
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