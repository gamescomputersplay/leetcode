''' https://leetcode.com/problems/min-cost-to-connect-all-points/
'''

class Solution:
    def minCostConnectPoints(self, points):

        # [{point1, point2}, ..]
        clusters = [{tuple(point)} for point in points]

        # cost so far
        total_cost = 0

        while len(clusters) > 1:

            clusters.sort(key=lambda x: len(x))

            min_cost = float("inf")
            best_cluster_to_connect = None

            for point_from in clusters[0]:

                for cluster in clusters[1:]:

                    for point_to in cluster:

                        cost = abs(point_from[0] - point_to[0]) + abs(point_from[1] - point_to[1])
                        if cost < min_cost:
                            min_cost = cost
                            best_cluster_to_connect = cluster

            clusters[0] = clusters[0].union(best_cluster_to_connect)
            clusters.remove(best_cluster_to_connect)
            total_cost += min_cost

        return total_cost

def main():
    ''' Test minCostConnectPoints
    '''
    solution = Solution()

    test_cases = [
        [[0,0],[2,2],[3,10],[5,2],[7,0]],
        [[3,12],[-2,5],[-4,1]],
        [[6256,82052],[-72567,67051],[56891,-84722],[-14181,-57490],[48701,-71357],[-35115,-39249],[48670,-47566],[68218,-84224],[9718,-47508],[-60207,-42655],[-89557,35100],[94110,-42326],[85905,40304],[-3280,86284],[-62238,-63066],[9396,-30137],[35643,10621],[14679,82587],[24177,-85619],[-28188,-12948],[7670,-78940],[43752,88047],[70307,-76277],[61605,-20336],[60239,28791],[25726,78037],[-97858,74676],[49879,69618],[-66269,-18976],[-87034,89816],[9413,88124],[-52048,86764],[64218,82210],[14549,-25265],[-89296,-17396],[-88645,85905],[12297,51622],[-21822,51824],[-8360,87665],[-55354,-59360],[-44387,8624],[30147,43718],[95898,-3406],[82551,-54781],[-61829,-66747],[-77203,-80095],[84975,98752],[-44346,12289],[-21147,-39687],[-27000,32686],[-18533,-27199],[-13228,52090],[-76356,-70974],[-70388,-57667],[-16563,-60199],[-32030,-34217],[5880,58845],[35504,-3269],[-56270,-81285],[-40090,44178],[-21789,-58682],[-8161,-6375],[-91627,40409],[-87339,-8631],[21568,96693],[47694,-3063],[48954,1713],[-75893,-62108],[-83159,-88431],[68973,-4155],[15353,2700],[34237,96736],[-46189,-83935],[90591,-77223],[70515,44068],[75514,-75004],[-24784,64551],[98818,-14787],[-9770,80946],[-1190,99223],[58462,36010],[3311,52784],[-82837,-5534],[-58478,340],[79038,-80212],[-27783,-37044],[90834,48402],[51852,-32099],[-21915,-52205],[7939,-148],[-88637,-42599],[-8130,62966],[6868,-62026],[72605,70039],[-90243,-66990],[-56261,-78216],[-97816,-63467],[96868,-21159],[-36398,82562],[-89799,-76815],[32551,-19139],[64731,96780],[-28614,39916],[40625,-60697],[86592,24801],[-28943,-60069],[-73492,-34103],[-53377,64411],[-49652,21642],[-82950,-14001],[-38066,77837],[-26412,24813],[56548,-89911],[30466,10599],[-24187,-77682],[43880,-6768],[-96554,42489],[78154,-75827],[1151,-63024],[58157,-33965],[-9669,-337],[80945,-4680],[-95615,-54308],[79150,2404],[41482,-64432],[48866,-72362],[-86685,83534],[-19662,-62745],[8742,-6895],[-2753,46922],[-75627,-5376],[37926,71082],[-93686,65055],[-22943,-76125],[-84316,-8354],[-84934,99754],[-86631,49886],[-37286,58756],[-22767,-31710],[-19693,901],[58216,-73459],[9700,62690],[53956,27253],[-84834,77100],[17346,-20300],[-69786,-32973],[-21725,-74897],[-9811,81224],[-68194,5398],[29364,81860],[-38471,-32877],[-2228,-43017],[88978,-62359],[87959,37996],[-28497,-48542],[97848,59348],[54718,68769],[-16420,-4564],[41997,-55823],[-99921,74884],[93155,13377],[-85733,1393],[-30171,91032],[81030,23048],[56291,94596],[29407,-2870],[49534,-57480],[-99130,77002],[-43827,-33454],[9757,17128],[42587,38942],[-5340,-88453],[-99504,28729],[71217,-15484],[-45095,-44871],[-28065,85065],[-14630,-51325],[-57183,-63766],[-72670,-17017],[74435,48794],[13615,82547],[-17593,-25587],[-34549,-88449],[15804,-30596],[-53397,28745],[35697,-41568],[75399,-3082],[-55122,-52183],[84648,-58482],[-85347,83763],[-64111,-3438],[-46879,-16791],[-12918,-18605],[-34024,34309],[-48507,-70903],[16307,86010],[-50096,66986],[-22836,-43965],[-75101,-91418],[-72802,57743],[-31768,5439],[60619,-9247],[86388,-39773],[76619,44779],[-72618,37429],[10336,-12383],[-98743,-81600],[63527,37225],[-10380,-75906],[-83616,20172],[96969,-68808],[-35816,32176],[9998,-37201],[19477,-12832],[32968,-62911],[-89512,-67198],[20574,-8714],[-75825,-93752],[-82673,9202],[-4852,52411],[-51815,-18968],[82711,98434],[54453,-12400],[15043,11990],[54634,44379],[11306,-55101],[-98800,24618],[79792,-87911],[39418,-79616],[-40726,-20307],[-84006,-98242],[42834,-27618],[-99241,-6296],[51339,-61465],[38872,93147],[-79429,25263],[18168,83572],[32031,65641],[41317,-34461],[-57108,39240],[62250,-86556],[59221,-61418],[35619,-15672],[94918,74880],[-47610,13226],[-97881,83631],[-43645,75161],[21349,-13370],[-66133,-70427],[-73984,-63862],[-24419,-83866],[-94970,3704],[44122,-29366],[-96733,35504],[9880,-34296],[-57096,12415],[87555,-61142],[-99406,-77938],[-77859,-96717],[-31217,-14617],[-66134,68881],[4175,-11159],[-5051,-45707],[27261,-51713],[-95033,94199],[-92237,-112],[-76027,58730],[90634,67290],[10609,-63564],[7417,48286],[-41335,-14491],[-42400,-44441],[-32457,-13601],[-57092,64875],[-99946,-66497],[82813,31539],[37433,96081],[14534,-31787],[-90961,90917],[94108,-87660],[-1446,34702],[5207,-68945],[2009,22341],[44443,-59970],[63282,96569],[25050,-97416],[83431,-33383],[-43430,33172],[95607,-14367],[-72674,96386],[-1400,37286],[70707,82842],[87479,82992],[-3198,29441],[94324,-5870],[49874,-88688],[-88185,-35469],[71268,5985],[79768,6171],[30924,14528],[-1413,-31568],[-58951,93407],[-65963,38074],[-55369,-80758],[-58239,41903],[-67387,10935],[9709,84731],[3966,-69087],[17728,-79449],[-7013,91915],[11604,-86607],[-55713,-71278],[-20366,-61640],[75446,36131],[-54037,25583],[75030,99172],[22056,93520],[76264,91366],[-58696,-85525],[40709,84329],[-77883,19338],[-50049,60520],[-64453,44556],[62342,12229],[12847,-68071],[78304,25729],[25572,63020],[-29024,19362],[-83465,99558],[3238,8267],[18179,-69245],[-29037,-30323],[-90336,-28219],[-93131,33679],[44356,-29616],[88314,-7445],[-3142,90964],[-86632,93536],[-50126,13813],[-35367,-46678],[-15440,64064],[-78349,94519],[27796,64192],[11095,-36186],[14549,-62908],[-66662,-65058],[69958,-66371],[-56720,58745],[-77082,-47686],[-95981,4507],[-83903,-94500],[65862,81075],[74252,-23941],[99517,-56469],[3079,-59427],[65873,46129],[79916,96559],[-71298,1709],[-62471,29388],[65547,63981],[-74239,-61179],[-95981,-6506],[18446,90814],[-95525,-86877],[-27004,42778],[-91194,42162],[-44117,-43378],[-80573,-20693],[-240,88586],[59945,-13252],[-51543,-42935],[92662,17690],[-1872,26186],[88975,12569],[-71081,-52527],[-23902,-61066],[-18724,-86531],[-17547,-87630],[83709,28357],[89994,24841],[53129,-48096],[-64425,-70047],[-57749,11169],[-43480,-14818],[-5382,65465],[-47047,-67358],[45850,-30167],[83912,44233],[77367,97824],[-69765,82868],[-11002,-65012],[-68402,64537],[61744,19310],[20165,70711],[-42622,83760],[-45147,90814],[-66207,45711],[-50772,42882],[60644,-92990],[21920,-81025],[59875,-97223],[-54275,-86507],[29725,-14801],[-96832,-50153],[-19479,-45649],[11405,-32134],[27681,49686],[12172,-24469],[808,-91589],[-60028,-66573],[5245,-49734],[92643,44891],[69539,-82509],[-43449,15975],[75224,76525],[42325,-22566],[-75382,-36842],[-21688,11393],[61190,60695],[84238,62952],[-4569,-40171],[-452,16599],[7109,-44778],[85250,-50154],[-57980,-50366],[-51542,48153],[60707,32006],[54561,30970],[-89906,34143],[95142,83595],[6961,-83004],[82486,83237],[36692,-58419],[-28856,-41582],[-94933,83166],[-85787,52474],[22501,-41684],[6154,-5169],[37210,83637],[73967,-10874],[-1674,35184],[-30800,32961],[95301,16539],[-32742,58834],[-89550,-44035],[-45890,-51904],[-60879,-48831],[-13564,-39015],[45179,49026],[-48462,88849],[-80826,-22525],[-97305,-58270],[2584,-81212],[-56320,-52263],[50201,-99812],[41292,-85089],[-28380,15651],[-79801,87990],[-16398,86431],[-93295,8479],[20909,96256],[99324,-67558],[15840,-1482],[-71069,-19108],[13325,-82795],[71123,-62909],[85522,-99654],[-46740,3143],[-51798,-47425],[-29613,-57500],[-94715,34991],[-60190,4742],[96943,-81858],[-95496,-55284],[-30643,-41435],[72072,-19057],[-88412,-22411],[65310,-25202],[83540,92764],[58891,73061],[-30880,-81335],[-18560,-2910],[-79931,45517],[15090,6462],[11528,-37766],[12060,-83288],[5903,-77770],[56220,-87168],[37807,27412],[-70437,51212],[-75547,13306],[70873,-80029],[-44704,15739],[51928,-8602],[66319,-96595],[85052,58114],[-26392,96137],[63593,-41052],[61275,-69158],[-56901,-21644],[-86703,98085],[67327,-97877],[11334,-91379],[-57576,77106],[-97185,-12453],[-87054,-63906],[67186,23997],[-81415,45548],[-64753,25478],[-68323,82483],[-95909,-68368],[97371,3944],[73323,-29112],[69917,18388],[29203,-34023],[13249,43507],[90147,43803],[65970,42133],[28139,-64532],[-1126,-86509],[20245,68906],[-97626,-87513],[-9076,58421],[65153,-65199],[-11597,46590],[26726,-93292],[97359,41847],[-72364,56677],[83662,41449],[-97001,81172],[86436,-29644],[62888,-79472],[80244,-35953],[27628,-20958],[44056,17311],[38339,-11079],[42191,85968],[88944,-42782],[3347,83616],[-23528,-49212],[21695,56321],[98107,-69504],[60917,14272],[-45606,41782],[-44724,45917],[-13932,630],[68553,11515],[-12171,93623],[17165,40619],[-59709,-14538],[-72573,-69161],[58762,14548],[-59355,37225],[34610,-93811],[64815,68716],[8294,34012],[17742,-93927],[21914,52835],[-55632,81144],[20428,-8519],[-63155,6096],[-70098,99626],[18448,1058],[-26881,19266],[-72387,-89429],[14154,-64364],[-61945,-95036],[-73107,-57609],[-27051,-74296],[-81565,-8569],[51412,-66773],[23965,66395],[-54450,-90118],[-66897,-79131],[57491,8526],[13421,-62318],[40239,-16928],[-25552,-90884],[21010,-80993],[42902,-99058],[18336,-36479],[-71194,70721],[-36145,34693],[2158,-8997],[10900,-19141],[-49173,34077],[-58419,71538],[62582,53818],[-6378,-88755],[9344,-5989],[-82599,48009],[-43317,-54281],[-42179,-17479],[68677,-82811],[13969,49515],[87021,85207],[-51411,83681],[60979,88832],[44953,-86231],[-50465,32751],[7340,-13644],[42855,-22693],[-893,15769],[-28800,-77706],[53301,-61898],[70598,3630],[66765,83959],[25538,-31634],[35578,-47817],[-36894,-80611],[61249,-19628],[-24427,-67483],[62805,69758],[87379,-31570],[17682,-50686],[78923,-95917],[-59656,-43540],[91417,48769],[76765,-59402],[-92147,51936],[39253,33770],[83873,37703],[-6111,87543],[-28981,71870],[87108,-64536],[-17583,49180],[37466,-21042],[-25479,67439],[78565,9704],[25182,75281],[-82490,42161],[-30905,68256],[-62985,64528],[-36095,-76815],[-8503,58958],[-58656,88086],[-17470,-17362],[-3129,83866],[-34307,-23508],[13519,90202],[89964,45104],[-47161,-33818],[19741,-13575],[76564,98370],[-77063,-63894],[-3995,-86224],[-24154,70962],[-75297,92210],[-85800,31358],[1203,-98641],[-79162,-4701],[-79195,51761],[11029,73271],[86,74723],[18781,49220],[12603,57486],[96183,-14128],[38771,76790],[12496,31986],[-72699,-29255],[12710,-82617],[-14486,51695],[54559,26499],[-45798,75047],[-74730,-35604],[23093,-17034],[17289,98178],[85143,-83061],[-24155,13794],[-82847,-20238],[-77785,67048],[67616,-62936],[-18267,-41674],[93047,64786],[-90312,78429],[-62133,-26041],[200,22910],[95514,-56599],[43448,-14430],[-78483,-91524],[-717,36773],[-59876,92148],[-95048,68510],[-54091,13064]]
    ]
    for points in test_cases:
        result = solution.minCostConnectPoints(points)
        print(points, result)


if __name__ == "__main__":
    main()
