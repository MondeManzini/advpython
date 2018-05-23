from pympler import muppy
all_objects = muppy.get_objects()
len(all_objects)


import types
my_types = muppy.filter(all_objects, Type=types.ClassType)
len(my_types)

for t in my_types:
   print t

from pympler import summary
sum1 = summary.summarize(all_objects)
summary.print_(sum1)   

sum2 = summary.summarize(muppy.get_objects())
diff = summary.get_diff(sum1, sum2)
summary.print_(diff)     

from pympler import refbrowser
root = "some root object"
root_ref1 = [root]
root_ref2 = (root, )
def output_function(o):
     return str(type(o))

cb = refbrowser.ConsoleBrowser(root, maxdepth=2, str_func=output_function)
#ib = refbrowser.InteractiveBrowser(root)
#ib.main()
