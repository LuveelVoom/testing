pillar = {
    "name": "top", "hp": 800,
    "children": [
        { "name": "first 1", "hp": 150, "children": [] },
        { "name": "second 1", "hp": 220,
          "children": [
              { "name": "first 2", "hp": 60,
                "children": [
                    { "name": "first 3", "hp": 20, "children": [] },
                    { "name": "second 3", "hp": 25, "children": [] }
                ] }
          ] }
    ]
}



def gethp(x):
    c = x["children"]
    wsum = x["hp"]
    if c == []:
        return wsum
    l=len(c)
    for y in range(0,l):
        wsum = wsum + gethp(x["children"][y])
    return wsum

print(gethp(pillar["children"][1]))
