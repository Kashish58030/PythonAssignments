# Item Type Classification:
#    - Develop a Python program using the `match` statement to determine the type of a given item. 
# If it's a string, print "String"; if it's an integer, print "Integer"; if it's a boolean, print "Boolean"; otherwise, print "Unknown type."

item="string"

match item:
    case "string":
        print("String")
    case "integer":
        print("Integer")
    case "boolean":
        print("Boolean")
    case _:
        print("Unknown Type")
        