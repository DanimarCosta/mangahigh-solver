# Mangahigh solver
This project solves any math activity on the [Mangahigh](https://www.mangahigh.com/) platform.

<img id="mangahigh_logo" src="https://user-images.githubusercontent.com/72043658/176778110-55d065fa-817d-49f7-a41a-0bf54832e9b0.png" width="30%">

- **How works ?**
> A plataforma apresenta uma vunerabilidade de Cross-site Scripting (XSS), que permite a injeção de javascript no console utilizando indevidamente o recurso de resposta grátis ofertado pela plataforma. Dessa forma, através da injeção do comando: `document.querySelector('#solutions');` a página retorna script html que quando renderizado,  mostra a resposta final para a tarefa.

- **How to fix the vulnerability**
