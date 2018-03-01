import sys,os
from datetime import datetime




TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Tags:
Slug: {slug}
Status: published

[download this notebook](https://github.com/franksalas/franksalas.github.io/tree/src/content/notebooks)


{{% notebook notebooks/{slug}/ %}}


"""




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


if __name__ == '__main__':

    if len(sys.argv) > 1:
        make_entry(sys.argv[1])
    else:
        print ("No title given")
