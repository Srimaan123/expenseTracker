let button = document.querySelector(".follow-button")
let username = document.querySelector(".username").textContent
button.addEventListener("click",async ()=>{
    let response = await fetch(`/profile/${username}`,{
        method: 'POST',
        body:JSON.stringify({
            "requested_by": username
            
        })
    })
})