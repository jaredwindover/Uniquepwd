import os
import sys
import time

def uniquePrefix(x, y):
  if len(x) > len(y) :
    y += "a"
  r = ""
  for xc, yc in zip(x,y):
    r += xc
    if xc!=yc:
      break
  return r

def uniquePrefixMulti(x, ys):
  ys.append("")
  ps = map(lambda y: uniquePrefix(x,y),ys)
  return max(ps, key= lambda z: len(z))

def uniqueListTree(xs, yss):
  assert len(xs) == len(yss)
  return list(map(uniquePrefixMulti, xs,yss))

def uniquePWD(path):
  curpath = os.path.abspath(path)
  upper, cur = os.path.split(curpath);    
  assert os.path.exists(curpath)
  if upper == curpath: #at root
    return [curpath]
  else:
    curdirs = [p
               for p in os.listdir(upper)
               if os.path.isdir(os.path.join(upper,p)) and
                  p != cur]
    curPrefix = uniquePrefixMulti(cur, curdirs)
    return uniquePWD(upper) + [curPrefix]

def main():
  print(os.path.join(*uniquePWD(sys.argv[1])) + "\\")
  
def test():
  def runTest(func, vals, e_str):
    for val in vals:
      e = e_str % ( val[0] + (val[1],) )
    try:
      res = func(*val[0])
      assert res == val[1], e
    except :
      print(e)
    
  valsUniquePrefix = [
    [("a","b"),"a"],
    [("a",""),"a"],
    [("",""),""],
    [("","a"),""],
    [("ab","ac"),"ab"],
    [("ab","abc"),"ab"],
    [("abc","ab"),"abc"]
  ]
  runTest(uniquePrefix,
          valsUniquePrefix,
          "error uniquePrefix(%r,%r) != %r")

  valsUniquePrefixMulti = [
    [
      ('a',[]),
      'a'
    ],
    [
      ('a',['ab']),
      'a'
    ],
    [
      ('ab',['a']),
      'ab'
    ],
    [
      ('ab',['a','abc']),
      'ab'
    ],
    [
      ('abcd',['ab','a','de','abc']),
      'abcd'
    ]
  ]
  runTest(uniquePrefixMulti,
          valsUniquePrefixMulti,
          "uniquePrefixMulti(%r,%r) != %r")

  
  valsUniqueListTree = [
    [([],[]),[]],
    [
      (['a','a','a'],
      [
        ['ab','abc'],
        ['ab','abc'],
        ['ab','abc']]),
     ['a','a','a']
    ],
    [
      (['a','b','c'],
      [
        ['ab','abc'],
        ['bc','bcd'],
        ['cd','cde']]),
     ['a','b','c']
    ],
    [
      (['abc','de','fghi'],
      [
        ['ac','abd'],
        ['f','e'],
        ['fg','hi']]),
     ['abc','d','fgh']
    ]
  ]
  runTest(uniqueListTree,
          valsUniqueListTree,
          "error: uniqueListTree(%r,%r) != %r")

if __name__=='__main__':
  main()
