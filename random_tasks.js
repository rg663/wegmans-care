let age = document.getElementById("age")
let age_value = Number(age_value["value"])
  //declare variable for disability 
let phy_disability = document.getElementById("physd")
let phy_disability_status = phy_disability["value"]

let visd = document.getElementById("visd")
let visd_status = visd["value"]

let hrd = document.getElementById("hrd")
let hrd_status = hrd["value"]



function find_age_range(age_value){
  if ((age_value >= 18) && (age_value <= 35) ){
    return 1 
  }else if ((age_value >= 36) && (age_value <= 50)){
    return 2 
  }else if ((age_value >= 51)&& (age_value <= 80)){
    return 3 
  }
} 

let not_disabled_random_tasks = {"Go outside" : [1,2,3], "Pet an animal" : [1,2,3], "Drink a glass of water" : [1,2,3] , "Call a friend or a loved one" : [1,2,3], "Try a new hobby" : [1,2,3], "Read a book" : [1,2,3] ,"Watch your favorite show" : [1,2], "Cook a meal" :[1,2,3], "Take a nap" :[1,2,3],"Drink tea" : [1,2,3], "Listen to music " : [1,2], "Watch Youtube": [1]}

let physd_tasks = { "Pet an animal" : [1,2,3], "Drink a glass of water" : [1,2,3] , "Call a friend or a loved one" : [1,2,3], "Try a new hobby" : [1,2,3], "Read a book" : [1,2,3] ,"Watch your favorite show" : [1,2], "Cook a meal" :[1,2,3], "Take a nap" :[1,2,3],"Drink tea" : [1,2,3], "Listen to music " : [1,2], "Watch Youtube": [1]}

let visd_tasks = {"Go outside" : [1,2,3], "Pet an animal" : [1,2,3], "Drink a glass of water" : [1,2,3] , "Call a friend or a loved one" : [1,2,3], "Try a new hobby" : [1,2,3], "Cook a meal" :[1,2,3], "Take a nap" :[1,2,3],"Drink tea" : [1,2,3], "Listen to music " : [1,2]}

let hrd_tasks = {"Go outside" : [1,2,3], "Pet an animal" : [1,2,3], "Drink a glass of water" : [1,2,3] , "Call a friend or a loved one" : [1,2,3], "Try a new hobby" : [1,2,3], "Read a book" : [1,2,3] ,"Watch your favorite show" : [1,2], "Cook a meal" :[1,2,3], "Take a nap" :[1,2,3],"Drink tea" : [1,2,3], "Watch Youtube": [1]}

function random_tasks(){
  age_range = find_age_range(age_value)
  if (phy_disability_status == true){
    let list_of_possible_tasks = []
    for (let key of Object.keys(physd_tasks)){
      for ( let item of physd_tasks[key]){
        if (item == age_range){
          list_of_possible_tasks.push(key); } 
    let index = Math.floor(Math.random() * list_of_possible_tasks.length)
    return list_of_possible_tasks[index]
        }      
    }
    
  }
  else if (visd_status == true ){
    let list_of_possible_tasks = []
    for(let key of Object.keys(visd_tasks)){
      for(let item of visd_tasks[key]){
        if (item == age_range){
          list_of_possible_tasks.push(key)
        }
      }
    }
    let random_index = Math.floor(Math.random() * list_of_possible_tasks.length)
    return list_of_possible_tasks[random_index]
  }
  else if (hrd_status == true){
    let list_of_possible_tasks = []
    for(let key of Object.keys(hrd_tasks)){
      for(let item of hrd_tasks[key]){
        if (item == age_range){
          list_of_possible_tasks.push(key)
        }
      }
    }
    let random_index = Math.floor(Math.random() * list_of_possible_tasks.length)
    return list_of_possible_tasks[random_index]

  }
  else{
    let list_of_possible_tasks = []
    for(let key of Object.keys(not_disabled_random_tasks){
      for(let item of not_disabled_random_tasks[key]){
        if (item == age_range){
          list_of_possible_tasks.push(key)
        }
      }
    }
    let random_index = Math.floor(Math.random() * list_of_possible_tasks.length)
    return list_of_possible_tasks[random_index]

  
  }
  
}
tasks = document.getElementById("tasks")
tasks["innerHTML"] = random_tasks()
