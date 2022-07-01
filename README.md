# Mangahigh solver
This project solves any math activity on the [Mangahigh](https://www.mangahigh.com/) platform.

<img id="mangahigh_logo" src="https://user-images.githubusercontent.com/72043658/176778110-55d065fa-817d-49f7-a41a-0bf54832e9b0.png" width="450">

- **How works ?**
> The platform has a known vulnerability in the community, the Cross-site Scripting (XSS) flaw, which allows the injection of javascript in the console, using the free response feature offered by the platform. In this way, by injecting the command: `document.querySelector('#solutions');` the page returns html script that when rendered, shows the final answer for the task.

- **How to fix the vulnerability** 
> Although the platform has a manual protection against automatic XSS, it allows the client to send the injection returning the response. Also, for the vulnerability to occur, the user must select and inspect any element of the `<body</body>`. The solution to this problem is simple, create an authentication in the free answer resource, adding a unique `id=''` to each answer, in this way, a check on the server would allow that even with a javascript injection in the browser console, a only free solution would be sent to customer.

<img id="javascript_logo" src="https://user-images.githubusercontent.com/72043658/176784579-0f06d48f-e213-4351-95ca-be3a263c2cef.png" width="50">


- **Final finding of the platform:**
- [x] Protection against automated software that prevents the inspection of elements (Necessary for the vulnerability to work)
- [ ] XSS protection
- [ ] Encryption in responses
- [ ] Response request verification

- **Tools that were used in the tests:**

<img src="https://user-images.githubusercontent.com/72043658/176787395-8eacd81e-e59d-4784-bd3e-f9f84c1ce293.png" width=100> <img src="https://user-images.githubusercontent.com/72043658/176787843-b16900cd-3180-46fc-8dfc-30ba6fa1c152.png" width=100> <img width="100" alt="Selenium_Logo" src="https://user-images.githubusercontent.com/72043658/176787977-63826ff8-cc44-452f-b84c-85d554dd5476.png">

- Developed by: Danimar Costa
