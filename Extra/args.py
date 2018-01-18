# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

def arg_kwarg(name,*arg,**key):
    print("hello my name is ",name)
    print(name,"is cricketer")
    for a in arg:
        print(a)
    print("--keyword--" * 3)
    for k in key:
        print(k,":",key[k])
arg_kwarg("sachin","orange","banana","apple",color1="orange",color2="yellow",color3="red")
