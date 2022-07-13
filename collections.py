class OrderedDict():
    def __init__(self,glossary):
        self.glossary=glossary
    def show_glossary(self):
        print(self.glossary,'\n')
        for i,j in glossary.items():
            print(i.title()+'↘\n\t'+j.title())
        
a=OrderedDict(glossary={'append':'1_argument',
         'insert':'2_arguments',
         'del':'1_argument',
         'remove':'2_arguments',
         'pop':'1_argument'
         })
a.show_glossary()