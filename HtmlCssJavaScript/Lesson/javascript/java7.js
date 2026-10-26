console.log("this is javascript7");

function greet(name, greetText="greeting from javascript"){
    let name1= "name1";
    console.log(greetText+" "+ name);
    console.log(name +" is a good boy");
}

function sum(a,b,c){
    let d= a + b + c;
    return d;
} 
let name = "rojan";
let name1 = "chandra";
let name2 = "poudel";
let name3 = "alikred";
let greetText = "Good Morring!"
greet(name, greetText);
greet(name1, greetText);
greet(name2, greetText);
// let returnval = greet(name3);
// console.log(returnval);

let returnval = sum(1,2,3);
console.log(returnval);

