


class cleanTitle:

    def __init__(self):
        self.symbolsToRemove = [',', '.', '?', '-', '*', '"', '?', '!', ':', ';', "'", '"']

    def clean(self, title):
        cleanedTitle = []
        tag = ''
        tags = []

        title = title.lower()
        for c in range(len(title) - 1):
            if title[c] == '[':
                tag += '['
            elif title[c] == ']':
                tags.append(tag + ']')
                tag = ''
            elif tag != '' and tag[0] == '[':
                tag += title[c]
        for t in tags:
            title = title.replace(t, '')
            cleanedTitle.append(t)
        for t in self.removePunc(title).split():
            cleanedTitle.append(t)

        return cleanedTitle

    def removePunc(self, title):
        newT = ''
        for c in title:
            if c not in self.symbolsToRemove:
                newT += c
        return newT