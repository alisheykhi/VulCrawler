import re

# for tag in node.xpath('*'):
#     print self.get_name(tag)


def get_name(self, node):
    root = str(node.root)
    return re.search(r'(<Element )(.+)(at)', root).group(2)
