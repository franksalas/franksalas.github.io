import sys,os
from datetime import datetime
import subprocess
import errno
from string import punctuation


def template():
    post_template ="""
    Title: {title} \nDate: {year}-{month}-{day}\nSlug: {slug}\nStatus: published
    \n\n\n\n{{% notebook notebooks/{slug}/{slug}.ipynb %}}
    """
    return post_template

def copy_nb(nb_dir,slug):
    '''creates dir, copy blank jupyter notebook '''
    full = '{}/{}.ipynb'.format(nb_dir,slug)
    if not os.path.exists(full):
        bashcommand = 'cp ./temp/Untitled.ipynb {}/{}.ipynb'.format(nb_dir,slug)
        process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print("PYNB Created -> {}/{}".format(nb_dir,slug))
    else:
        print('{}\{}\tEXIST'.format(nb_dir,slug))



def fill_md(md_temp,title,slug):
    today = datetime.today()
    md_file= "content/articles/{}.md".format(slug)
    md_post = md_temp.strip().format(title=title,
                                    year = today.year,
                                    month = today.month,
                                    day = today.day, 
                                    slug = slug)
    if not os.path.exists(md_file):
        with open(md_file, 'w') as w:
            w.write(md_post)
        print("{}\tCREATED".format(md_file))
    else:
        print('{}\tEXIST'.format(md_file))


def clean_title(title):
    '''Clean the title'''
    rem_pun = ''.join(c for c in title if c not in punctuation)  # remove punctuations
    clean_title = ' '.join(rem_pun.split())  # remove spaces
    return clean_title

def slug_title(title):
    '''slug the title'''
    slug = title.lower().strip().replace(' ', '-')
    return slug

def make_dirs(slug):
    '''create directories'''
    img_dir = 'content/images/{}'.format(slug)  # images directory
    nb_dir = 'content/notebooks/{}'.format(slug)
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
        print("{}/\tCREATED".format(img_dir))
    else:
        print("{}/\tEXIST".format(img_dir))

def make_nb_dir(slug):
    '''create nb directories'''
    nb_dir = 'content/notebooks/{}'.format(slug)
    if not os.path.exists(nb_dir):
        os.makedirs(nb_dir)
        print("{}/\tCREATED".format(nb_dir))
        return nb_dir
    else:
        print("{}/\tEXIST".format(nb_dir))
        return None


def make_md(slug):
    '''String with location of markdown post '''
    md_post= "content/articles/{}.md".format(slug)
    if not os.path.exists(md_post):  # check if markdown file exist.
        with open(md_post, 'w') as f:  # create an emtpy file
            f.write('')
            # print(type(md_post))
            # print(md_post)
            return md_post
    else:
        print('.md Already Exist')


def main(title):
    """Main entry point for the script."""
    title_clean = clean_title(title)
    md_temp = template()  # load empty template function
    bg_slug = slug_title(title_clean)  # create slug
    nb_dir = make_nb_dir(bg_slug)
    copy_nb(nb_dir,bg_slug)  # create a notebook
    make_dirs(bg_slug)  # create image directory
    fill_md(md_temp,title,bg_slug)  # load empty template with data and save
    #test_copy_nb(bg_slug)





if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].strip() !="" :
        sys.exit(main(sys.argv[1]))
    else:
        print ("Not a valid title")






