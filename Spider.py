import argparse
from argparse import RawTextHelpFormatter
import os

parser = argparse.ArgumentParser(description='Add/Remove new spider\n ITRC-MT', formatter_class=RawTextHelpFormatter)
parser.add_argument('-a','--AddSpider', help='add new spider\n usage: -a [spiderName.py ]',  type=argparse.FileType('r'))
parser.add_argument('-r','--RemoveSpider', help='Remove spider\n usage: -r [spiderName.py ]')
parser.add_argument('-p','--Pipline', help='add new Pipline\n usage: -p [SpiderName_Pipline.py ]',  type=argparse.FileType('r'))
parser.add_argument('-i','--Item', help='add new Item Class\n usage: -i [SpiderName_Item.py ]',  type=argparse.FileType('r'))

args = vars(parser.parse_args())

def save_crawler_spider(file,type="spiders"):
    save_file(file,type)
def save_crawler_pipline(file,type="pipelines"):
    save_file(file,type)
def save_crawler_item(file,type="items"):
    save_file(file,type)


def remove_spider(file,type ="spiders"):
    remove_file(file,type)
def remove_piplines(file,type ="pipelines"):
    remove_file(file,type)
def remove_item(file,type ="items"):
    remove_file(file,type)


def save_file(file,type):#type = [spiders, pipelines, items]
    print file.name
    spider_file_name = str(file.name).split("\\")[-1]
    print spider_file_name
    try:
        with file as f:
            content = f.read()
        out_direc = os.path.abspath(os.path.join('attackKB_crawler', type, spider_file_name))
        if not os.path.exists(out_direc):
            print out_direc
            with open(out_direc, 'w') as spider_file:
                spider_file.write(content)

        else:
            print "spider exists!!"
            exit()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)



def remove_file(file,type):
    if file:
        file_name = str(file)+"_%s.py" %type
        source = os.path.abspath(os.path.join('attackKB_crawler', type, file_name))
        print source
        try:
            os.remove(source)
            print file, " has been deleted successfully!"
        except OSError as e:
            print "there is no file ",file
            print "I/O error({0}): {1}".format(e.errno, e.strerror)


if __name__ == '__main__':
    if args['AddSpider']:
        save_crawler_spider(args['AddSpider'])
        save_crawler_pipline(args['Pipline'])
        save_crawler_item(args['Item'])

    if args['RemoveSpider']:
        remove_spider(args['RemoveSpider'])
        remove_piplines(args['RemoveSpider'])
        remove_item(args['RemoveSpider'])





