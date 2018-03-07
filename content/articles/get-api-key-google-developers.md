Title: Get API Key Google Developers 
Date: 2018-2-28
Tags: notebook, api
Slug: get-api-key-google-developers
Status: draft
    

{% img rounded mx-auto d-block /images/get-api-key-google-developers/google-dev.svg logo %}

## Tools
- Google maps API Key
- Python Client for Google Maps Services
- Jupyter Notebook

## Get Google Maps API Key

0. Go to [Google Maps APIs] and click on get started
0. Scroll down to the Web APIs section and select Google Maps JavaScrip API
0. On the top right side, click on the button `GET A KEY`
0. A pop up will show up asking you to select or create a project, click, on it and select `+ Create a new Project`, the default name will be My Project, click next.
0. A few second later the your generated API key will show up.


{% img rounded mx-auto d-block /images/get-api-key-google-developers/api6.png logo %}

## Enviroment

Create a directory and move into it

```bash
mkdir googleDev

cd googleDev
```


Inside your new directory create a new enviroment named: `googleDev` and activate
```bash
conda create -n googleDev python=3.6

source activate googleDev
```

Install required libraries:

Jupyter notebook
```bash
conda install jupyter  
```

Python Client for Google Maps Services
```bash
pip install -U googlemaps
```



## Notebook

{% notebook notebooks/get-api-key-google-developers/get-api-key-google-developers.ipynb %}


[Google Maps APIs ]: https://developers.google.com/maps/
