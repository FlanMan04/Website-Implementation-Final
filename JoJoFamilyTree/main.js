const session = pl.create(100000);

const familyFacts=`
parent(george_i, jonathan).
parent(mary, jonathan).

parent(dario, dio).
parent(dio_mom, dio).
parent(george_i, dio).

parent(dio, giorno).
parent(giorno, mom).

parent(jonathan, george_ii).
parent(erina, george_ii).

parent(george_ii, joseph).
parent(elizabeth, joseph).

parent(joseph, holly).
parent(suzi, holly).

parent(joseph, shizuka).
parent(suzi, shizuka).

parent(joseph, josuke).
parent(tomoko, josuke).

parent(holly, jotaro).
parent(sadao, jotaro).

parent(jotaro, jolyne).
parent(jolyne_mom, jolyne).

male(george_i).
male(jonathan).
male(george_ii).
male(joseph).
male(jotaro).
male(josuke).
male(giorno).
male(sadao).
male(dario).
male(dio).

female(mary).
female(erina).
female(elizabeth).
female(suzi).
female(holly).
female(tomoko).
female(jolyne).
female(shizuka).
female(jolyne_mom).
female(dio_mom).

father(X, Y):- parent(X, Y), male(X).
mother(X, Y):- parent(X, Y), female(X).

uncle(X, Z):- brother(X, Y), parent(Y, Z).
aunt(X, Z):- sister(X, Y), parent(Y, Z).
greatuncle(X, Z):- parent(Y, Z), uncle(X, Y).
greataunt(X, Z):- parent(Y, Z), aunt(X, Y).
greatgreatuncle(X, Z):- parent(Y, Z), greatuncle(X, Y).
greatgreataunt(X, Z):- parent(Y, Z), greataunt(X, Y).
greatgreatgreatuncle(X, Z):- parent(Y, Z), greatgreatuncle(X, Y).
greatgreatgreataunt(X, Z):- parent(Y, Z), greatgreataunt(X, Y).
greatgreatgreatgreatuncle(X, Z):- parent(Y, Z), greatgreatgreatuncle(X, Y).
greatgreatgreatgreataunt(X, Z):- parent(Y, Z), greatgreatgreataunt(X, Y).

nephew(X, Z):- sibling(Z, Y), male(X), parent(Y, X).
niece(X, Z):- sibling(Z, Y), female(X), parent(Y, X).
greatnephew(X, Z):- parent(Z, Y), nephew(X, Y).
greatniece(X, Z):- parent(Z, Y), niece(X, Y).
greatgreatnephew(X, Z):- parent(Z, Y), greatnephew(X, Y).
greatgreatniece(X, Z):- parent(Z, Y), greatniece(X, Y).
greatgreatgreatnephew(X, Z):- parent(Z, Y), greatgreatnephew(X, Y).
greatgreatgreatniece(X, Z):- parent(Z, Y), greatgreatniece(X, Y).
greatgreatgreatgreatnephew(X, Z):- parent(Z, Y), greatgreatgreatnephew(X, Y).
greatgreatgreatgreatniece(X, Z):- parent(Z, Y), greatgreatgreatniece(X, Y).

son(Y, X):- parent(X, Y), male(Y).
daughter(Y, X):- parent(X, Y), female(Y).

grandfather(X, Z):- parent(X, Y), parent(Y, Z), male(X).
grandmother(X, Z):- parent(X, Y), parent(Y, Z), female(X).
greatgrandfather(A, D):- parent(A, B), parent(B, C), parent(C, D), male(A).
greatgrandmother(A, D):- parent(A, B), parent(B, C), parent(C, D), female(A).
greatgreatgrandfather(A, E):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), male(A).
greatgreatgrandmother(A, E):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), female(A).
greatgreatgreatgrandfather(A, F):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), male(A).
greatgreatgreatgrandmother(A, F):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), female(A).
greatgreatgreatgreatgrandfather(A, G):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), parent(F, G), male(A).
greatgreatgreatgreatgrandmother(A, G):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), parent(F, G), female(A).

grandson(Z, X):- parent(X, Y), parent(Y, Z), male(Z).
granddaughter(Z, X):- parent(X, Y), parent(Y, Z), female(Z).
greatgrandson(D, A):- parent(A, B), parent(B, C), parent(C, D), male(D).
greatgranddaughter(D, A):- parent(A, B), parent(B, C), parent(C, D), female(D).
greatgreatgrandson(E, A):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), male(E).
greatgreatgranddaughter(E, A):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), female(E).
greatgreatgreatgrandson(F, A):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), male(F).
greatgreatgreatgranddaughter(F, A):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), female(F).
greatgreatgreatgreatgrandson(G, A):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), parent(F, G), male(G).
greatgreatgreatgreatgranddaughter(G, A):- parent(A, B), parent(B, C), parent(C, D), parent(D, E), parent(E, F), parent(F, G), female(G).


sibling(Y, Z):- parent(X, Y), parent(X, Z), Y \\= Z.
brother(Y, Z):- parent(X, Y), parent(X, Z), male(Y), Y \\= Z.
sister(Y, Z):- parent(X, Y), parent(X, Z), female(Y), Y \\= Z.
sibling(dio, jonathan).
sibling(jonathan, dio).
brother(dio, jonathan).
brother(jonathan, dio).

relationship(X, Y, father) :- father(X, Y).
relationship(X, Y, mother) :- mother(X, Y).
relationship(X, Y, son) :- son(X, Y).
relationship(X, Y, daughter) :- daughter(X, Y).
relationship(X, Y, brother) :- brother(X, Y).
relationship(X, Y, sister) :- sister(X, Y).
relationship(X, Y, uncle) :- uncle(X, Y).
relationship(X, Y, aunt) :- aunt(X, Y).
relationship(X, Y, nephew) :- nephew(X, Y).
relationship(X, Y, niece) :- niece(X, Y).
relationship(X, Y, greatuncle) :- greatuncle(X, Y).
relationship(X, Y, greataunt) :- greataunt(X, Y).
relationship(X, Y, greatgreatuncle) :- greatgreatuncle(X, Y).
relationship(X, Y, greatgreataunt) :- greatgreataunt(X, Y).
relationship(X, Y, greatgreatgreatuncle) :- greatgreatgreatuncle(X, Y).
relationship(X, Y, greatgreatgreataunt) :- greatgreatgreataunt(X, Y).
relationship(X, Y, greatgreatgreatgreatuncle) :- greatgreatgreatgreatuncle(X, Y).
relationship(X, Y, greatgreatgreatgreataunt) :- greatgreatgreatgreataunt(X, Y).
relationship(X, Y, greatnephew) :- greatnephew(X, Y).
relationship(X, Y, greatniece) :- greatniece(X, Y).
relationship(X, Y, greatgreatnephew) :- greatgreatnephew(X, Y).
relationship(X, Y, greatgreatniece) :- greatgreatniece(X, Y).
relationship(X, Y, greatgreatgreatnephew) :- greatgreatgreatnephew(X, Y).
relationship(X, Y, greatgreatgreatniece) :- greatgreatgreatniece(X, Y).
relationship(X, Y, greatgreatgreatgreatnephew) :- greatgreatgreatgreatnephew(X, Y).
relationship(X, Y, greatgreatgreatgreatniece) :- greatgreatgreatgreatniece(X, Y).
relationship(X, Y, grandfather) :- grandfather(X, Y).
relationship(X, Y, grandmother) :- grandmother(X, Y).
relationship(X, Y, greatgrandfather) :- greatgrandfather(X, Y).
relationship(X, Y, greatgrandmother) :- greatgrandmother(X, Y).
relationship(X, Y, greatgreatgrandfather) :- greatgreatgrandfather(X, Y).
relationship(X, Y, greatgreatgrandmother) :- greatgreatgrandmother(X, Y).
relationship(X, Y, greatgreatgreatgrandfather) :- greatgreatgreatgrandfather(X, Y).
relationship(X, Y, greatgreatgreatgrandmother) :- greatgreatgreatgrandmother(X, Y).
relationship(X, Y, greatgreatgreatgreatgrandfather) :- greatgreatgreatgreatgrandfather(X, Y).
relationship(X, Y, greatgreatgreatgreatgrandmother) :- greatgreatgreatgreatgrandmother(X, Y).
relationship(X, Y, grandson) :- grandson(X, Y).
relationship(X, Y, granddaughter) :- granddaughter(X, Y).
relationship(X, Y, greatgrandson) :- greatgrandson(X, Y).
relationship(X, Y, greatgranddaughter) :- greatgranddaughter(X, Y).
relationship(X, Y, greatgreatgrandson) :- greatgreatgrandson(X, Y).
relationship(X, Y, greatgreatgranddaughter) :- greatgreatgranddaughter(X, Y).
relationship(X, Y, greatgreatgreatgrandson) :- greatgreatgreatgrandson(X, Y).
relationship(X, Y, greatgreatgreatgranddaughter) :- greatgreatgreatgranddaughter(X, Y).
relationship(X, Y, greatgreatgreatgreatgrandson) :- greatgreatgreatgreatgrandson(X, Y).
relationship(X, Y, greatgreatgreatgreatgranddaughter) :- greatgreatgreatgreatgranddaughter(X, Y).

sibling(dio, jonathan).
sibling(jonathan, dio).
brother(dio, jonathan).
brother(jonathan, dio).

uncle(dio, george_ii).
nephew(george_ii, dio).

greatuncle(dio, joseph).
greatnephew(joseph, dio).

greatgreatuncle(dio, holly).
greatgreatuncle(dio, josuke).
greatgreatuncle(dio, shizuka).
greatgreatnephew(holly, dio).
greatgreatnephew(josuke, dio).
greatgreatniece(shizuka, dio).

greatgreatgreatuncle(dio, jotaro).
greatgreatgreatnephew(jotaro, dio).

greatgreatgreatgreatuncle(dio, jolyne).
greatgreatgreatgreatniece(jolyne, dio).

`;
const characters = [

  { name: "George_I", img: "images/george_i.png" },
  { name: "Mary", img: "images/mary.png" },
  { name: "Dario", img: "images/dario.jpg" },
  { name: "Dio_mom", img: "images/dio_mom.jpg" },
  { name: "Jonathan", img: "images/jonathan.png" },
  { name: "Dio", img: "images/dio.jpg" },
  { name: "Erina", img: "images/erina.jpg" },
  { name: "George_II", img: "images/george_ii.jpg" },
  { name: "Elizabeth", img: "images/elizabeth.jpg" },
  { name: "Joseph", img: "images/joseph.jpg" },
  { name: "Suzi", img: "images/suzi.jpg" },
  { name: "Tomoko", img: "images/tomoko.jpg" },
  { name: "Holly", img: "images/holly.jpg" },
  { name: "Sadao", img: "images/sadao.jpg" },
  { name: "Josuke", img: "images/josuke.jpg" },
  { name: "Shizuka", img: "images/shizuka.jpg" },
  { name: "Jotaro", img: "images/jotaro.jpg" },
  { name: "Jolyne_mom", img: "images/jolyne_mom.png" },
  { name: "Jolyne", img: "images/jolyne.png" },
  { name: "Giorno", img: "images/giorno.jpg" },
  { name: "Giorno_mom", img: "images/giorno_mom.jpg" }


];

const container = document.getElementById("characters");

characters.forEach(char => {
  const button = document.createElement("button");
  button.className = "character";

  button.onclick = () => selectCharacter(char.name);

  button.innerHTML = `
    <img src="${char.img}">
    <span>${char.name}</span>
  `;

  container.appendChild(button);
});

let selected = [];

function selectCharacter(name) {
  const char = characters.find(c => c.name === name);
  selected.push(name);

  if (selected.length === 1) {
    document.getElementById("pick1").innerText = name;
    document.getElementById("pick1img").src = char.img;
    document.getElementById("pick1img").style.display = "block";
    document.getElementById("pick2").innerText = "Second Member";
    document.getElementById("pick2img").style.display = "none";
    document.getElementById("result").innerText = "";
  } else if (selected.length === 2) {
    document.getElementById("pick2").innerText = name;
    document.getElementById("pick2img").src = char.img;
    document.getElementById("pick2img").style.display = "block";
    findRelationship(selected[0], selected[1]);
    selected = [];
  }
}

session.consult(familyFacts, {
    success: function() {
        console.log("Program loaded successfully!");

        // Function to query relationship dynamically
        window.findRelationship = function(a, b) {
            session.query(`relationship('${a.toLowerCase()}', '${b.toLowerCase()}', R).`, {
                success: function () {
                    session.answer({
                        success: function (answer) {
                            const rel = answer.links.R;
                            const result = session.format_answer(answer);
                            document.getElementById("result").innerText = `${a} is ${b}'s ${rel} `;
                        },
                        fail: function () {
                            document.getElementById("result").innerText = "No relation found.";
                        },
                        error: function (err) {
                            console.error("Error getting answer:", err);
                        }
                    }, 1000000) ;
                },
                error: function (err) {
                    console.error("Query error:", err);
                }
            });
        };
    },
    error: function(err) {
        console.error("Consult error:", err);
    }
});