# boker-api

> back end for haykkh/boker

![language](https://img.shields.io/badge/Python-blue.svg?style=flat-square)![language](https://img.shields.io/badge/FastAPI-green.svg?style=flat-square)![language](https://img.shields.io/badge/Docker-blue.svg?style=flat-square)

Back end RESTful API for [boker](github.com/haykkh/boker) written with [FastAPI](https://fastapi.tiangolo.com) and deployed using [Docker](https://www.docker.com). ⚡

## 📦 Installation

### 📋 Clone repo

```sh
git clone https://github.com/haykkh/boker-api.git

cd boker-api
```

### ⬇️ Direct download

[boker-api-master.zip](https://github.com/haykkh/boker-api/archive/master.zip)

## 🚀 Usage

### 🦄 Developing with Uvicorn

```sh
uvicorn boker_api:app --reload
```

### ⚓ Docking

```sh
docker build -t boker-api-image .

docker run -d -p 80:80 boker-api-image
```

## 📝 Contributing

1. Fork it (<https://github.com/haykkh/boker-api/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## 👨🏻 Meta

Hayk Khachatryan – [hi@hayk.io](mailto:hi@hayk.io)

[github.com/haykkh](https://github.com/haykkh/)
