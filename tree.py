def tree_info(t_n,t_no,**t_info):
    tree={}
    tree['Tree name']=t_n
    tree['Numbers of Tree']=t_no
    for i,j in t_info.items():
        tree[i]=j
    return tree
a=tree_info('Neem',1200,park_name='gold Neem')
print(a)
b=tree_info('mango',120,production='100 touns',kind='laungra')
print(b)