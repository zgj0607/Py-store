must_set = ['数量', '单价', '小计', '总价', '单位', '备注']
attribute = ""
attribute_state = ""
for t in must_set:
    attribute += "{},".format(t)
    attribute_state += "1,"

attribute = attribute[:-1]
attribute_state = attribute_state[:-1]
