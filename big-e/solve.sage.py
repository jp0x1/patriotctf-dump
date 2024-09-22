

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_0 = Integer(0); _sage_const_0xa0d9f425fe1246c25b8c3708b9f6d7747dd5b5e7f79719831c5cbe19fb7bab66ed62719b3fc6090120d2cfe1410583190cd650c32a4151550732b0fc97130e5f02aa26cb829600b6ab452b5b11373ec69d4eaae6c392d92da8bcbea85344af9d4699e36fdca075d33f58049fd0a9f6919f3003512a261a00985dc3d9843a822974df30b81732a91ce706c44bde5ff48491a45a5fa8d5d73bba5022af803ab7bd85250e71fc0254fcf078d21eaa5d38724014a85f679e8a7a1aad6ed22602465f90e6dd8ef95df287628832850af7e3628ad09ff90a6dbdf7a0e6d74f508d2a6235d4eae5a828ac95558bbdf72f39af5641dfe3edb0cdaab362805d926106e2af = Integer(0xa0d9f425fe1246c25b8c3708b9f6d7747dd5b5e7f79719831c5cbe19fb7bab66ed62719b3fc6090120d2cfe1410583190cd650c32a4151550732b0fc97130e5f02aa26cb829600b6ab452b5b11373ec69d4eaae6c392d92da8bcbea85344af9d4699e36fdca075d33f58049fd0a9f6919f3003512a261a00985dc3d9843a822974df30b81732a91ce706c44bde5ff48491a45a5fa8d5d73bba5022af803ab7bd85250e71fc0254fcf078d21eaa5d38724014a85f679e8a7a1aad6ed22602465f90e6dd8ef95df287628832850af7e3628ad09ff90a6dbdf7a0e6d74f508d2a6235d4eae5a828ac95558bbdf72f39af5641dfe3edb0cdaab362805d926106e2af); _sage_const_0x5af5dbe4af4005564908a094e0eabb0a921b7482483a753e2a4d560700cb2b2dc9399b608334e05140f54d90fcbef70cec097e3f75395d0c4799d9ec3e670aca41da0892a7b3d038acb7a518be1ced8d5224354ce39e465450c12be653639a8215afb1ba70b1f8f71fc1a0549853998e2337604fca7edac67dd1e7ddeb897308ebf26ade781710e6a2fe4c533a584566ea42068d0452c1b1ecef00a781b6d31fbab893de0c9e46fce69c71cefad3119e8ceebdab25726a96aaf02a7c4a6a38d2f75f413f89064fef14fbd5762599ca8eb3737122374c5e34a7422ea1b3d7c43a110d3209e1c5e23e4eece9e964da2c447c9e5e1c8a6038dc52d699f9324fd6b9 = Integer(0x5af5dbe4af4005564908a094e0eabb0a921b7482483a753e2a4d560700cb2b2dc9399b608334e05140f54d90fcbef70cec097e3f75395d0c4799d9ec3e670aca41da0892a7b3d038acb7a518be1ced8d5224354ce39e465450c12be653639a8215afb1ba70b1f8f71fc1a0549853998e2337604fca7edac67dd1e7ddeb897308ebf26ade781710e6a2fe4c533a584566ea42068d0452c1b1ecef00a781b6d31fbab893de0c9e46fce69c71cefad3119e8ceebdab25726a96aaf02a7c4a6a38d2f75f413f89064fef14fbd5762599ca8eb3737122374c5e34a7422ea1b3d7c43a110d3209e1c5e23e4eece9e964da2c447c9e5e1c8a6038dc52d699f9324fd6b9); _sage_const_0x731ceb0ac8f10c8ff82450b61b414c4f7265ccf9f73b8e238cc7265f83c635575a9381aa625044bde7b34ad7cce901fe7512c934b7f6729584d2a77c47e8422c8c0fe2d3dd12aceda8ef904ad5896b971f8b79048e3e2f99f600bf6bac6cad32f922899c00fdc2d21fcf3d0093216bfc5829f02c08ba5e534379cc9118c347763567251c0fe57c92efe0a96c8595bac2c759837211aac914ea3b62aae096ebb8cb384c481b086e660f0c6249c9574289fe91b683609154c066de7a94eafa749c9e92d83a9d473cc88accd9d4c5754ccdbc5aa77ba9a790bc512404a81fc566df42b652a55b9b8ffb189f734d1c007b6cbdb67e14399182016843e27e6d4e5fca = Integer(0x731ceb0ac8f10c8ff82450b61b414c4f7265ccf9f73b8e238cc7265f83c635575a9381aa625044bde7b34ad7cce901fe7512c934b7f6729584d2a77c47e8422c8c0fe2d3dd12aceda8ef904ad5896b971f8b79048e3e2f99f600bf6bac6cad32f922899c00fdc2d21fcf3d0093216bfc5829f02c08ba5e534379cc9118c347763567251c0fe57c92efe0a96c8595bac2c759837211aac914ea3b62aae096ebb8cb384c481b086e660f0c6249c9574289fe91b683609154c066de7a94eafa749c9e92d83a9d473cc88accd9d4c5754ccdbc5aa77ba9a790bc512404a81fc566df42b652a55b9b8ffb189f734d1c007b6cbdb67e14399182016843e27e6d4e5fca); _sage_const_p10 = RealNumber('.10')
import itertools
from Crypto.Util.number import long_to_bytes

def bivariate(f, bounds, m=_sage_const_1 , d=None):
    if d is None:
        d = f.degree()

    R = f.base_ring()
    N = R.cardinality()
    f_ = (f // f.lc()).change_ring(ZZ)
    f = f.change_ring(ZZ)
    l = f.lm()

    M = []
    for k in range(m+_sage_const_1 ):
        M_k = set()
        T = set((f**(m-k)).monomials())
        for mon in (f**m).monomials():
            if mon//l**k in T: 
                for extra in itertools.product(range(d), repeat=f.nvariables()):
                    g = mon * prod(map(power, f.variables(), extra))
                    M_k.add(g)
        M.append(M_k)
    M.append(set())

    shifts = Sequence([], f.parent())
    for k in range(m+_sage_const_1 ):
        for mon in M[k] - M[k+_sage_const_1 ]:
            g = mon//l**k * f_**k * N**(m-k)
            shifts.append(g)

    B, monomials = shifts.coefficients_monomials()
    factors = [monomial(*bounds) for monomial in monomials]
    for i, factor in enumerate(factors):
        B.rescale_col(i, factor)

    B = B.dense_matrix().LLL()

    B = B.change_ring(QQ)
    for i, factor in enumerate(factors):
        B.rescale_col(i, _sage_const_1 /factor)
    B = B.change_ring(ZZ)
    H = [h for h in B * monomials if not h.is_zero()]

    for f1, f2 in itertools.combinations(H, r=_sage_const_2 ):
        x, y = f.parent().gens()
        x = f1.parent()(x)
        y = f1.parent()(y)
        res = f1.resultant(f2,y).univariate_polynomial()
        if res == _sage_const_0 :
            continue
        rs = res.roots()
        if rs:
            x = rs[_sage_const_0 ][_sage_const_0 ]
            y = f1.subs(x=x).univariate_polynomial().roots()
            if y != []:
                return (x, y[_sage_const_0 ][_sage_const_0 ])


N = _sage_const_0xa0d9f425fe1246c25b8c3708b9f6d7747dd5b5e7f79719831c5cbe19fb7bab66ed62719b3fc6090120d2cfe1410583190cd650c32a4151550732b0fc97130e5f02aa26cb829600b6ab452b5b11373ec69d4eaae6c392d92da8bcbea85344af9d4699e36fdca075d33f58049fd0a9f6919f3003512a261a00985dc3d9843a822974df30b81732a91ce706c44bde5ff48491a45a5fa8d5d73bba5022af803ab7bd85250e71fc0254fcf078d21eaa5d38724014a85f679e8a7a1aad6ed22602465f90e6dd8ef95df287628832850af7e3628ad09ff90a6dbdf7a0e6d74f508d2a6235d4eae5a828ac95558bbdf72f39af5641dfe3edb0cdaab362805d926106e2af 
e = _sage_const_0x5af5dbe4af4005564908a094e0eabb0a921b7482483a753e2a4d560700cb2b2dc9399b608334e05140f54d90fcbef70cec097e3f75395d0c4799d9ec3e670aca41da0892a7b3d038acb7a518be1ced8d5224354ce39e465450c12be653639a8215afb1ba70b1f8f71fc1a0549853998e2337604fca7edac67dd1e7ddeb897308ebf26ade781710e6a2fe4c533a584566ea42068d0452c1b1ecef00a781b6d31fbab893de0c9e46fce69c71cefad3119e8ceebdab25726a96aaf02a7c4a6a38d2f75f413f89064fef14fbd5762599ca8eb3737122374c5e34a7422ea1b3d7c43a110d3209e1c5e23e4eece9e964da2c447c9e5e1c8a6038dc52d699f9324fd6b9 
c = _sage_const_0x731ceb0ac8f10c8ff82450b61b414c4f7265ccf9f73b8e238cc7265f83c635575a9381aa625044bde7b34ad7cce901fe7512c934b7f6729584d2a77c47e8422c8c0fe2d3dd12aceda8ef904ad5896b971f8b79048e3e2f99f600bf6bac6cad32f922899c00fdc2d21fcf3d0093216bfc5829f02c08ba5e534379cc9118c347763567251c0fe57c92efe0a96c8595bac2c759837211aac914ea3b62aae096ebb8cb384c481b086e660f0c6249c9574289fe91b683609154c066de7a94eafa749c9e92d83a9d473cc88accd9d4c5754ccdbc5aa77ba9a790bc512404a81fc566df42b652a55b9b8ffb189f734d1c007b6cbdb67e14399182016843e27e6d4e5fca 


A = (N+_sage_const_1 )//_sage_const_2 
PR = PolynomialRing(Zmod(e), _sage_const_2 , names=('x', 'y',)); (x, y,) = PR._first_ngens(2)
f = x*(A+y) + _sage_const_1 
delta = _sage_const_p10  # guess
roots = bivariate(f, (_sage_const_2 *floor(N**delta), isqrt(N)), m=_sage_const_2 , d=_sage_const_2 )
d = f.change_ring(ZZ)(*roots)/e
flag = pow(c, d, N)
print(long_to_bytes(flag))

