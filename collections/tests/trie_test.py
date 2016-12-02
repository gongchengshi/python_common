from trie import *

input = [['air', 'products'],
         ['anchor', 'chemical'],
         ['ancomer'],
         ['bangkok', 'cogeneration'],
         ['cryoservice'],
         ['dupont', 'air', 'products', 'nanomaterials'],
         ['epco', 'carbondioxide', 'products'],
         ['eurogas', 'calibration', 'services'],
         ['gasin', 'ii', 'gases', 'industriais', 'unipessoal'],
         ['harvest', 'energy', 'technology'],
         ['indura'],
         ['induramex'],
         ['lakeway', 'medical', 'rentals'],
         ['matgas', '2000', 'aie'],
         ['middletown', 'oxygen'],
         ['orlando', 'cogen'],
         ['poly', 'flow', 'engineering'],
         ['prodair'],
         ['protexeon'],
         ['pure', 'air'],
         ['roboprojekt'],
         ['rovi', 'cosmetics', 'international', 'gmbh'],
         ['saga'],
         ['siq', 'beteiligungs', 'gmbh'],
         ['sociedad', 'espa', 'ola', 'de', 'carburos', 'metalicos'],
         ['stockton', 'cogen'],
         ['terapias', 'medicas', 'domiciliarias']]

trie = Trie()

for i in input:
    trie.add(i, None)

for item in trie.items():
    print item

i = 9
