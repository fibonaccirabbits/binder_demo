from nbformat import v3, v4

content = open('abdb.py').read()

nb = v3.reads_py(content)
nb = v4.upgrade(nb)
nb_json = v4.writes(nb) + '\n'

outfile = open('abdb.ipynb', 'w')
outfile.write(nb_json)
outfile.close()
