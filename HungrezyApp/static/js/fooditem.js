
const foodItem= [
    {
    id: 1,
    name: 'Sausage Carnival',
    category : 'pizzaburg',
    rating : 5,
    price: 415,
    img: '../images/pizzaburg/sasaugecarnival.jpg',
    // img: "{% static 'sasaugecarnival.jpg' %}",
    // img: 'sasaugecarnival.jpg',
    quantity: 1
},
{
    id: 2,
    name: 'Meaty Onion',
    category : 'pizzaburg',
    rating : 4.1,
    price: 375,
    img: 'images/pizzaburg/meatyonion.jpg',
    quantity: 1
},
{
    id: 3,
    name: 'Tender Beef',
    category : 'pizzaburg',
    rating :3.5,
    price: 395,
    img: 'images/pizzaburg/tenderbeef.jpg',
    quantity: 1
},
{
    id: 4,
    name: 'JuicyBomb',
    category : 'pizzaburg',
    rating : 4.3,
    price: 215,
    img: 'images/pizzaburg/juicybomb.jpg',
    quantity: 1
},
{
    id: 5,
    name: 'BBQ Burger(Chicken)',
    category : 'pizzaburg',
    rating : 3.5,
    price: 185,
    img: 'images/pizzaburg/bbq.jpg',
    quantity: 1
},
{
    id: 6,
    name: 'Set Menu-1',
    category : 'pizzaburg',
    rating : 4.4,
    price: 165,
    img: 'images/pizzaburg/setmenu.jpg',
    quantity: 1
},

{
    id: 7,
    name: 'Basmati Kacchi (1:1)',
    category : 'kacchibhai',
    rating : 4.9,
    price: 270,
    img: 'images/kacchibhai/basmatikacchi.jpg',
    quantity: 1
},
{
    id: 8,
    name: 'Kacchi Khadok',
    category : 'kacchibhai',
    rating : 4.4,
    price: 420,
    img: 'images/kacchibhai/kacchikhadok.jpg',
    quantity: 1
},
{
    id: 9,
    name: 'Polao Roast',
    category : 'kacchibhai',
    rating : 4.9,
    price: 250,
    img: 'images/kacchibhai/polao.jpg',
    quantity: 1
},
{
    id: 10,
    name: 'Chicken Roast',
    category : 'kacchibhai',
    rating : 4.3,
    price: 120,
    img: 'images/kacchibhai/chickenroast.jpg',
    quantity: 1
},
{
    id: 11,
    name: 'Jorda',
    category : 'kacchibhai',
    rating : 4.5,
    price: 60,
    img: 'images/kacchibhai/jorda.jpg',
    quantity: 1
},

{
    id: 12,
    name: 'Bashmati Kacchi',
    category : 'sultan',
    rating : 4.3,
    price: 269,
    img: 'images/sultan/sbashkacchi.jpg',
    quantity: 1

},
{
    id: 13,
    name: 'Mutton Tehari',
    category : 'sultan',
    rating : 4.2,
    price:199,
    img: 'images/sultan/muttontehari.jpeg',
    quantity: 1
},
{
    id: 14,
    name: 'Kacchi Platter',
    category : 'sultan',
    rating : 4.1,
    price: 15,
    img: 'images/sultan/kacchiplatter.jpg',
    quantity: 1

},
{
    id: 15,
    name: 'Nababi Kacchi',
    category : 'sultan',
    rating : 4.8,
    price: 320,
    img: 'images/sultan/nababikacchi.jpeg',
    quantity: 1

},
{
    id: 16,
    name: 'Murag Polaw',
    category : 'sultan',
    rating : 4.2,
    price: 299,
    img: 'images/sultan/murogpolao.jpg',
    quantity: 1
},
{
    id: 17,
    name: 'Hunter Beef Sub',
    category : 'khanas',
    rating : 4.2,
    price:273,
    img: 'images/khanas/hunterBeefsub.jpg',
    quantity: 1
},
{
    id: 18,
    name: 'Peri Peri Wings',
    category : 'khanas',
    rating : 4.3,
    price: 439 ,
    img: 'images/khanas/periperichickenwings.jpg',
    quantity: 1
},
{
    id: 19,
    name: 'Chicken Momo',
    category : 'khanas',
    rating : 4.3,
    price: 239,
    img: 'images/khanas/chickenmomo.jpg',
    quantity: 1
},
{
    id: 20,
    name: 'Truffle Fries',
    category : 'khanas',
    rating : 4.3,
    price: 224,
    img: 'images/khanas/trufflefries.jpg',
    quantity: 1
},
{
    id: 21,
    name: 'Chicken Burger',
    category : 'khanas',
    rating : 4.3,
    price: 334,
    img: 'images/khanas/khana_sspecialchickenburger.jpg',
    quantity: 1
},
{
    id: 22,
    name: 'Crimson Cup Mocha',
    category : 'crimson',
    rating : 3.3,
    price: 270,
    img: 'images/crimsoncup/crimsoncupmocha.jpg',
    quantity: 1
},
{
    id: 23,
    name: 'Cafe Mocha',
    category : 'crimson',
    rating : 4.5,
    price: 259,
    img: 'images/crimsoncup/cafemocha.jpg',
    quantity: 1
},
{
    id: 24,
    name: 'Matcha Latte',
    category : 'crimson',
    rating : 4.3,
    price: 330,
    img: 'images/crimsoncup/matchalatte.jpg',
    quantity: 1
},
{
    id: 25,
    name: 'Americanno',
    category : 'crimson',
    rating : 4.3,
    price: 16,
    img: 'images/crimsoncup/americanno.jpg',
    quantity: 1
},
{
    id: 26,
    name: 'Spicy Naga Pasta ',
    category : 'ozz',
    rating : 3.5,
    price:  260,
    img: 'images/ozzcafe/spicynagapasta.jpg',
    quantity: 1
},
{
    id: 27,
    name: 'Chili Fried Rice',
    category : 'ozz',
    rating : 4.2,
    price: 320,
    img: 'images/ozzcafe/chilifriedrice.jpg',
    quantity: 1
},
{
    id: 28,
    name: 'Chicken Vegetable',
    category : 'ozz',
    rating : 4.5,
    price: 212,
    img: 'images/ozzcafe/chickenvegetable.jpg',
    quantity: 1
},
{
    id: 29,
    name: 'Pad Thai Noodles',
    category : 'ozz',
    rating : 4.3,
    price: 250,
    img: 'images/ozzcafe/padthainoodles.jpg',
    quantity: 1
},
{
    id: 30,
    name: 'Chicken Chili Onion',
    category : 'ozz',
    rating : 3.2,
    price: 450,
    img: 'images/ozzcafe/chilichickenonion.jpg',
    quantity: 1
},

]

export {foodItem};