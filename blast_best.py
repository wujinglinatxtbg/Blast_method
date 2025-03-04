import re,sys

infl = sys.argv[1]
outfile = sys.argv[2]

FL = open(infl, 'r')
D = {} #dictionary for BLAST file ONE
for Line in FL:
	if ( Line[0] != '#' ):
		Line.strip()
		Elements = re.split('\t', Line)
		queryId = Elements[0]
		subjectId = Elements[1]
		value = eval(Elements[8])
		if value == 0:
			if (not (queryId in D.keys())):
				D[queryId]=[]
				D[queryId].append(subjectId)
			else:
				D[queryId].append(subjectId)
		else:
			if ( not ( queryId in D.keys() ) ):
				D[queryId] = subjectId  #pick the first hit
OF = open(outfile, 'w')

for id in D.keys():
	if type(D[id]) is list:
		for d_value in D[id]:
			OF.write(id + '\t' + d_value + '\n')
	else:
		OF.write(id + '\t' + D[id] + '\n')

