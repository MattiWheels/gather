# gather
Bringing an old collection management project, Gather (and MTG collection manager), back to life with flask. Following Miguel Grinberg's flask mega tutorial for blog portion of the app.

- Create flaskenv to store environment/debug variables
- Install pip requirements to gather necessary packages
- `flask db init`
- Install npm
- Install tailwindcss
- `npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/output.css --watch`

#### To Do
Following [Miguel Grinberg's Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to complete blog section. Adding collection manager as feature in blog posts.

- Check if gravatar exists otherwise use generated avatar
- User based blog posts, add special formatting
- User card library
- Card table (updates from scryfall)