# kebabCase
def kebabCase(str):

    return ''.join(['-'+i.lower() if i.isupper()
                    else i for i in str]).lstrip('-')


kebabword = "HelloWorldAgain"
print(kebabCase(kebabword))
