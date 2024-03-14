let livros =["Harry Potter", "As Crônicas de Nárnia", "O Senhor dos Aneis", "Iracema", "Dom Casmurro", "Memórias Póstumas de Brás Cubas", "Macunaíma"]

function funcao(livro, index){
    return livro + " - " + {index +1}
}

let livro2 = livros.map(funcao)

console.log(livros2)