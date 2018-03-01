import sys,os
from datetime import datetime
import subprocess

# bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
# import subprocess
# process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
# output, error = process.communicate()




TEMPLATE = """
Title: {title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Tags: notebook
Slug: {slug}
Status: published


{{% notebook notebooks/{slug}/{slug}.ipynb %}}

## Download
[download this notebook](https://github.com/franksalas/franksalas.github.io/tree/src/content/notebooks/{slug})
"""




def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    nb_dir = 'content/notebooks/{}'.format(slug)
    os.makedirs(nb_dir)
    bashcommand = 'cp ./temp/Untitled.ipynb {}/{}.ipynb'.format(nb_dir,slug)
    process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
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
