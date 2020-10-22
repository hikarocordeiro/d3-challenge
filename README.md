# D3 Challenge

This is a lovingly coded challenge for the D3 Company's backend position.

## About

This challenge was planned to be coded using machine learning, but due to the lack of time I decided to use a linear regression calculation, using the formula: 

```
m.x + b = y
```

Where:

```
m = the transmission factor
x = number of cases (today)
b = a weight to adjust the predicted final value
y = the number of cases predicted for given information x
```

The values of some constants of this formula was extract from [there](https://medium.com/@caiquecoelho/intelig%C3%AAncia-artificial-e-sir-na-predi%C3%A7%C3%A3o-do-fim-da-primeira-onda-do-coronav%C3%ADrus-no-brasil-parte-5-f3c2bc682fdc).

This app consumes the total of new cases from the API [thevirustracker.com](https://thevirustracker.com/free-api?global=stats)

```
docker-compose build
docker-compose up
```

## Getting started

Install [docker](https://docs.docker.com/engine/installation/) and run:

```
docker-compose build
docker-compose up
```
The tests will run on build
You can access the app on browser on : http://localhost:5000

---

Made with ♥ by Hikaro Cordeiro :wave: [Get in touch!](https://www.linkedin.com/in/hikaro-cordeiro/)

