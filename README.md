# Argos :eyes:

Simple web application to showcase a few computer vision features.

# Quick start
Most of the operations are automated for Linux using [GNU Make](https://www.gnu.org/software/make/) (you can find a simple tutorial [here](https://makefiletutorial.com/)).

They have not been tested / adapted for Windows & Mac, but the application should also work. However, you will need to use the underlying tools (Python, npm & docker) to install & run it.

Installing the application:

```bash
git clone https://github.com/cedricgoubard/argos.git
cd argos

make install
```

If you want to change the parameters before launching the application:
 - Use `make set-port XXXX` to change the port of the backend application in all configuration files
 - You can also edit the files individually: `back/config.yaml`, `front/argos/.env.development.local` & `docker-compose.yaml`

Once you are satisfied, create the docker images:
```bash
make build
```

Then, run the application
```bash
make run
```

The default address for the application is [localhost:3000](http://localhost:3000).

