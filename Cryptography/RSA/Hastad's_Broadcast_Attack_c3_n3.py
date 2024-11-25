from Crypto.Util.number import long_to_bytes, inverse
from gmpy2 import iroot

e = 3
c1 = 261345950255088824199206969589297492768083568554363001807292202086148198722402380676138078614774919011859552072663081496837339290624940098045941666974866866446747148793714978880579180140109296120579252064365079387725663301419872301919689576905808379498644521649965160582830113494402011911767969632749183893040
n1 = 1001191535967882284769094654562963158339094991366537360172618359025855097846977704928598237040115495676223744383629803332394884046043603063054821999994629411352862317941517957323746992871914047324555019615398720677218748535278252779545622933662625193622517947605928420931496443792865516592262228294965047903627
c2 = 147535246350781145803699087910221608128508531245679654307942476916759248493513464389047783263853539559909464172380863409036822999877585212049666595082028787841599217182491627615515631140110169864221202526469804843851098436855381511638675058329198719461892960196374373646640630449862633901416208177651026021529
n2 = 405864605704280029572517043538873770190562953923346989456102827133294619540434679181357855400199671537151039095796094162418263148474324455458511633891792967156338297585653540910958574924436510557629146762715107527852413979916669819333765187674010542434580990241759130158992365304284892615408513239024879592309
c3 = 633230627388596886579908367739501184580838393691617645602928172655297372327529230304236376306377467969593653208991026410622586986036527560756293113090229207730884534852421083696475045459334099812735568263375731682637178526500730184935921680548531576585762254329708094833083800017939729261922041250790796509661
n3 = 1204664380009414697639782865058772653140636684336678901863196025928054706723976869222235722439176825580211657044153004521482757717615318907205106770256270292154250168657084197056536811063984234635803887040926920542363612936352393496049379544437329226857538524494283148837536712608224655107228808472106636903723


def third_root(n):
    m, valid = iroot(n, e)
    if valid:
        print("Cleartext:", long_to_bytes(m))
    else:
        print("Unable to find the third root of:", n)

# Implement CRT function
def crt(remainders, moduli):
    N = 1
    for n in moduli:
        N *= n

    result = 0
    for (remainder, modulus) in zip(remainders, moduli):
        partial_N = N // modulus
        inverse_partial_N = inverse(partial_N, modulus)
        result += remainder * inverse_partial_N * partial_N

    return result % N

C = [c1, c2, c3]
N = [n1, n2, n3]

for c in C:
    third_root(c)

# Use CRT to combine the values
x = crt(C, N)
third_root(x)
