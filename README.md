# Mangahigh solver
This project solves any math activity on the [Mangahigh](https://www.mangahigh.com/) platform.

<img id="mangahigh_logo" src="https://user-images.githubusercontent.com/72043658/176778110-55d065fa-817d-49f7-a41a-0bf54832e9b0.png" width="450">

- **How works ?**
> A plataforma apresenta uma vunerabilidade conhecida na comunidade, a falha de Cross-site Scripting (XSS), permite a injeção de javascript no console utilizando indevidamente o recurso de resposta grátis ofertado pela plataforma. Dessa forma, através da injeção do comando: `document.querySelector('#solutions');` a página retorna script html que quando renderizado,  mostra a resposta final para a tarefa.

- **How to fix the vulnerability** 
> Apesar da plataforma possuir uma leve proteção contra XSS automatizados, a mesma permite que o cliente envie a injeção manualmente retornando a resposta. Além disso, para que a vunerabilidade aconteça, o usuario precisa selecionar e inspecionar qualquer elemento do `<body</body>`. A solução desse problema é simples, criar uma autenticação no recurso de resposta grátis, adicionando um `id=''` unico para cada resposta, desse modo, a verificação no servidor permitiria que mesmo com a injeção de javascript no console do navegador, uma unica solução grátis seria enviada para o cliente.

<img id="javascript_logo" src="https://user-images.githubusercontent.com/72043658/176784579-0f06d48f-e213-4351-95ca-be3a263c2cef.png" width="50">


- **Constatação final da plataforma:**
- [x] Proteção contra softwares automatizados que impeçam a inspeção de elementos (Necesário para o funcionamento da vunerabilidade)
- [ ] Proteção contra XSS
- [ ] Criptografia nas respostas
- [ ] Verificação da requisição de respostas

- **Ferramentas que foram usadas nos testes:**

<img src="https://user-images.githubusercontent.com/72043658/176787395-8eacd81e-e59d-4784-bd3e-f9f84c1ce293.png" width=100> <img src="https://user-images.githubusercontent.com/72043658/176787843-b16900cd-3180-46fc-8dfc-30ba6fa1c152.png" width=100> <img width="100" alt="Selenium_Logo" src="https://user-images.githubusercontent.com/72043658/176787977-63826ff8-cc44-452f-b84c-85d554dd5476.png">
