Title: liquid test
Date: 2017-4-12 18:56
Tags:
Slug: liquid-test
Status: published


  <!-- No title  -->


## images


```rb
{% img rounded mx-auto d-block /images/liquid-test/ image desc %}
```


{% img rounded mx-auto d-block /images/liquid-test/shopify.png logo %}




## Gyphy

```rb
{% giphy aMSJFS6oFX0fC 'ive had some free time' %}
```

{% giphy aMSJFS6oFX0fC 'ive had some free time' %}

## graphviz

```rb
{% graphviz
    dot {
        digraph graphname {
            a -> b -> c;
            b -> d;
        }
    }
%}

```




{% graphviz
    dot {
        digraph graphname {
            a -> b -> c;
            b -> d;
        }
    }
%}


## youtube


```rb
{% youtube dQw4w9WgXcQ 640 480 %}

```


{% youtube dQw4w9WgXcQ 640 480 %}