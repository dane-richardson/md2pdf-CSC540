import pypandoc


class Converter(object):
    def __init__(self): pass

    def convert2pdf(self, md):
        """
        :param md:
            A str containing the markdown document to be converted
            to a PDF

        :return:
            A bytearray containing the PDF

        Examples:

        >>> len(Converter().convert2pdf('title: hello2\\ntags:\\n\\nhello2'))
        43328

        """

        # convert the title: and tags: strings to markdown
        md = md.replace("title:", "#").replace("tags:", "##")

        # use the pypandoc library wrapper of pandoc to convert the markdown
        # to a temporary pdf file.
        output = pypandoc.convert_text(md, to='pdf', format='md', outputfile='temp.pdf')

        # read and return the temporary pdf files as a bytearray
        fh = open('../temp.pdf', 'rb')
        return bytearray(fh.read())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
