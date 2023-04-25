Task class parameters
- code
- description
- durations[List]
- predecessors

Task attributes
- All dates
- boolean critical
- random duration determination
- duration


Class methods:
- Calculate random duration
- add and clear predecessors and successors
- self.successors.append(successor)
        if self not in successor.predecessors:
            successor.addPredecessor(self)
- Get date(s)
- Calculate dates
- IsCritical?



ConstructionProject CLASS

Attributes:
- Name
- List of tasks
- early and late project duration
  - These are determined by 


early completion date = duration

late start date 



classificiation results to aim for
0.8 = 980 success
1.0 = 800 success
1.2 = 200 success
1.4 = 20 success



-------- outout as of 25.04.2023 with 1000 iterations ---------

Risk factor:  0.8
Minimum duration:  292.79415545431215
Maximum duration:  348.4636210881467
Mean duration:  323.97262468089195
Standard deviation:  9.59600568192961
Deciles:  [311.2081862729836, 315.49766186193636, 318.87241351363525, 321.897206695895, 324.24116576737026, 326.69044084406005, 329.37340055464, 332.1101284151522, 335.9648034772891]
Number of successes:  1000
Number of acceptables:  0
Number of failures:  0

Risk factor:  1.0
Minimum duration:  316.10018350948695
Maximum duration:  404.5150951630328
Mean duration:  364.069945242541
Standard deviation:  12.12884085883965
Deciles:  [347.925755248614, 353.8365057292219, 358.5173978864667, 361.77222954400423, 364.5947450416687, 367.45983204046036, 370.75899843013633, 374.51678087270295, 379.73283950302357]
Number of successes:  988
Number of acceptables:  12
Number of failures:  0

Risk factor:  1.2
Minimum duration:  353.35675782744454
Maximum duration:  437.0948531338049
Mean duration:  397.89311769884813
Standard deviation:  13.628121122468128
Deciles:  [379.3891712496948, 386.9333326396229, 391.6293548088843, 394.83623034503705, 397.90759206262436, 401.3841771584975, 405.4302671180806, 409.71760399446123, 415.3469376112222]
Number of successes:  260
Number of acceptables:  732
Number of failures:  8

Risk factor:  1.4
Minimum duration:  361.0814828154372
Maximum duration:  473.7560823880955
Mean duration:  426.80444698028606
Standard deviation:  16.081533515581206
Deciles:  [406.3211377813569, 414.5911477148662, 418.5732306340709, 422.49660947928953, 426.83550430855564, 430.8708985498345, 435.83638557699817, 441.29353730848044, 447.00594531554225]
Number of successes:  16
Number of acceptables:  479
Number of failures:  505