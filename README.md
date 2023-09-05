# BTA Modding

Mod repository website for Better Than Adventure!

## Contributing

> To set up your development environment, follow this quick guide:

After cloning the project you must install pip and npm dependencies.
```shell
pip install -r requirements.txt
npm install
```

Don't forget to migrate to your database (by default `./db.sqlite`)
```shell
python manage.py migrate
```

And now you *in theory* can run Django's server using
```shell
python manage.py runserver
```

And don't forget to run nodemon to listen for `.html` and `.css` changes, useful TailwindCSS
```shell
npm run dev
```

## Todo

- [ ] Mods
  - [x] List
    - [x] Search
    - [ ] Filters
  - [x] Detail
  - [x] Edit
  - [x] Markdown
    - [ ] WYSIWYG
  - [x] Logo
  - [ ] Remove

- [ ] Versions
  - [x] Detail
  - [x] Download
  - [x] List by mods
  - [x] Do an update
  - [ ] Remove

- [ ] Users
  - [x] Sign in
  - [x] Register
  - [x] Email
    - [ ] Forget password
  - [ ] Profile
  - [ ] Settings *(useless for now)*
  - [ ] Remove
