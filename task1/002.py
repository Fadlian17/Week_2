# SnakeCase
def snakeCase(str):

    return ''.join(['_'+i.lower() if i.isupper()
                    else i for i in str]).lstrip('_')


# Driver code
snakeword = "Hello World Again"
print(snakeCase(snakeword))
