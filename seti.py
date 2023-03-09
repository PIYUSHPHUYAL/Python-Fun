R=input("Provide the rate of formation of stars in years")
Fp=input("Provide the fraction of those stars with planetary systems")
Ne=input("Provide the number of planets per solar system")
Fl=input("Provide the fraction of suitable planets on which life appears")
Fi=input("Provide the faction of life bearing planets on which intelligent life emerges")
Fc=input("Provide the fraction of civilizations that develop a technology that produce detectable signs of their existence")
L=input("Provide the average length of time such civilizations produce such signs in years")

N=int(R)*float(Fp)*int(Ne)*float(Fl)*float(Fi)*float(Fc)*int(L)

print("The number of civilizations in the Milky Way galaxy whose electromagnetic emissions are detectable is",N)