# How to setup a Vanilla Tailwind CSS project

## Prerequisites

1. Node.js
2. Tailwind CSS Intellisense extension for VS Code.
3. Live Server : Full Reload [On]
4. CSS > Lint > Unknown @ rules : [Ignore]

## Steps

1. `npm init`
   - press enter to accept all the defaults.
   - New 🗃️ `package.json` created.
2. `npm install -D tailwindcss`
   - this will install tailwindcss as a dev dependency.
   - new 📂 generated `node_modules`.
3. `npx tailwindcss init`
   - a new 🗃️ `tailwind.config.js` will be created.
4. make new 📂 `build`.
   - can be of any name.
   - make a new 🗃️ `index.html` in `build`.
   - `content: ["./build/*.{html,js}"]` in `tailwind.config.js`.
5. make new 📂 `src`.
   - make new 🗃️ `input.css` in `src`.
6. inside `input.css` paste the following:

   ```css
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```

7. `npx tailwindcss -i ./src/input.css -o ./build/css/output.css --watch`
   - compiles `input.css` to `output.css` in `build/css`.
8. link output.css in `index.html`.
9. **Addtional Steps** to prevent remembering command in **Step: 7** Do this.
   1. Inside `package.json` add a new script:

       ```json
       "scripts": {
         "dev": "tailwindcss -i ./src/input.css -o ./build/css/output.css --watch"
       }
       ```

## To Run

1. Everytime you have to run command specified in **Step: 7** and keep that running.
2. Just Go Live with Live Server.
3. [Link to The Video](https://www.youtube.com/watch?v=arftp8kFBBg)
