# gather
Bringing an old collection management project, Gather (an MTG collection manager), back to life with flask. Following Miguel Grinberg's flask mega tutorial for the blog portion of the app.

- Create flaskenv to store environment/debug variables
- Install pip requirements to gather necessary packages
- `flask db init`
- Install npm
- Install tailwindcss
- `npx tailwindcss -i ./app/static/src/input.css -o ./app/static/dist/output.css --watch`
- `flask run` (don't forget to setup environment variables or .flaskenv)

#### To Do
Following [Miguel Grinberg's Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) to complete blog section. Adding collection manager as feature in blog posts.

- ༼つಠ益ಠ༽つ ─=≡ΣO))
- GET request after POST from editing profile doesn't return committed data?
- User created posts

##### To Do (Later-ish)

- User card library (add/remove)
- Card table (updates from scryfall)