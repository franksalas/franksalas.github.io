
## blog


create enviroment from file
```bash

conda env create -f environment.yml
```

activate enviroment

```bash
conda activate pelicanblog
```

#### dependencies
need graphviz

```bash
sudo apt-get install graphviz
```



### create a jupyter notebook post

- ` $ python nb_post.py "notebook post name"`
- creates folder with title in `content/notebooks/`
- creates notebook with title name inside the folder
- creates a mardown file with title  in `content/articles/`
- creates a folder with title in `content/images/`

```bash
content/notebooks/my-notebook-post/     CREATED
PYNB Created -> content/notebooks/my-notebook-post/my-notebook-post
content/images/my-notebook-post/        CREATED
content/articles/my-notebook-post.md    CREATED
```

markdown file

```md
Title: my notebook post 
Date: 2016-1-13
Tags: notebook
Slug: my-notebook-post
Status: published
    



{% notebook notebooks/my-notebook-post/my-notebook-post.ipynb %}
```

### create a blog post
- `python blog_post.py "blog post name"`
- creates a mardown file with title  in `content/articles/`
- creates a folder with title in `content/images/`

```bash
python blog_post.py "this is a test"

content/images/this-is-a-test/  CREATED
content/articles/this-is-a-test.md      CREATED

```

markdown file 

```md
Title: this is a test 
Date: 2016-2-10
Tags: 
Slug: this-is-a-test
Status: published
    



{% img rounded mx-auto d-block /images/this-is-a-test/ image desc %}
```
