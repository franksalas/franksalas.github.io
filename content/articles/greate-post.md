Title: greate post
Date: 2018-2-28 3:53
Tags:
Slug: greate-post
Status: draft


  <!-- No title  -->

#this is a test




Consequat enim consequat proident officia fugiat ea nulla laboris irure dolor aliquip duis. Nostrud minim aliquip aliqua aliqua aute aliqua ea voluptate. Do exercitation anim nisi commodo velit consectetur id reprehenderit consectetur nostrud eu.


Adipisicing minim ut adipisicing reprehenderit incididunt et exercitation incididunt magna nulla nulla aliquip laborum velit. Laborum tempor ex sunt ullamco officia officia amet pariatur ipsum. Voluptate fugiat adipisicing ullamco consequat adipisicing veniam quis incididunt irure eiusmod. Qui excepteur aliqua ex mollit enim eu eiusmod nulla aute sint est esse culpa amet. Eiusmod qui tempor ea culpa in nostrud. Sint 

## math

$$
e=mc^2
$$


Non velit et quis ea. Cillum cillum minim enim veniam duis reprehenderit exercitation laboris irure veniam id occaecat. Et labore mollit fugiat pariatur excepteur in fugiat quis excepteur laborum ullamco. Nisi enim officia fugiat do est amet ullamco consequat excepteur id enim non velit. Culpa dolor laboris ea laborum id commodo pariatur dolore. Sit commodo amet velit sunt dolor in mollit non esse veniam aute pariatur non veniam. Ea voluptate aute cillum id aliquip ut exercitation.

```python
def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    os.makedirs("content/notebooks/{}".format(slug))
    f_create = "content/articles/{}.md".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)
```

Ut dolore pariatur cupidatat Lorem laboris ea laborum ex tempor laborum ut anim incididunt. Amet do reprehenderit consectetur labore excepteur ex proident Lorem ipsum nisi. Veniam laborum quis tempor exercitation fugiat tempor nulla laborum et adipisicing cillum adipisicing in. Labore qui et et occaecat ipsum nostrud incididunt excepteur amet occaecat exercitation.

Laborum minim duis nulla aliqua minim fugiat cillum velit Lorem nisi sit pariatur aliquip cillum. Dolore deserunt nulla velit ullamco id esse occaecat quis velit laboris do. Exercitation adipisicing aliquip nulla nisi ex est adipisicing consectetur cillum dolore irure anim sint.

{% img rounded mx-auto d-block /images/greate-post/ image desc %}