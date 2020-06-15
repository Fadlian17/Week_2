# kebabCase
def kebabCase(str):

    return ''.join(['-'+i.lower() if i.isupper()
                    else i for i in str]).lstrip('-')


# Driver code
kebabword = "HelloWorldAgain"
print(kebabCase(kebabword))
