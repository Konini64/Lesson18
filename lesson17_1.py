import re 

"""
zen = Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!

m = re.findall("^If",zen,re.MULTILINE)
m = re.findall("[abc]",zen,re.MULTILINE)

string = "Two too. tio tiw tww to"
m = re.findall("t[ow]o", string , re.IGNORECASE)

line = "123 hi 34 hello."
#m = re.findall("\d", line , re.IGNORECASE)

t = "__one__ __two__ __theree__"
found = re.findall("__.*?__",t)
for match in found:
"""

text = """キリンは大昔から __複数名詞__ の興味の対象でした。キ
リンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのよ
うな長い  __体の一部__ をどうやって獲得したのか説明できません。キ
リンの身長は、 __数値__ __単位__ 近くあり、その高さのほとんどは脚
と  __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
    :param mls:文字列で、ユーザーに入力してもらいたい単語(=
ヒント)の部分は後を2つのアンダースコアで挟んでください。ヒントの単
語にはアンダースコアを含めないで下さい。 ___hint_hint__ はだめで
す。___hint__ はOKです。
    """
    hints = re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q = "{} を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print ('\n')
        mls = mls.replace ("\n", "" )
        print (mls)
    else:
        print("引数mlsが無効です")

mad_libs(text)

    


import re

line = "I love $."

m = re.findall("\\$", line , re.IGNORECASE)

print(m)

p = re.findall("$", line , re.IGNORECASE)

print(p)

