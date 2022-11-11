string = "PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm"
Decrypt_zin = "" 
next = False



for x in string:
    
    
    
    if next:
        Decrypt_zin += x
        next = False

    
    vraagteken_gevonden = x == "?"
    next = vraagteken_gevonden and uitroepteken_gevonden
    uitroepteken_gevonden = x == "!"

print(Decrypt_zin)
   
