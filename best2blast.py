import re,sys

# input *2H 2H* *.tsv
infl1 = sys.argv[1]
infl2 = sys.argv[2]
outfile = sys.argv[3]

FL1 = open(infl1, 'r')
D1 = {} 
for Line in FL1:
	Line = Line.strip().replace('\n','')
	Elements = re.split('\t', Line)
	queryId = Elements[0]
	subjectId = Elements[1]
	if queryId not in D1.keys():
		D1[queryId] = []
		D1[queryId].append(subjectId)  
	else:
		D1[queryId].append(subjectId)

FL2 = open(infl2, 'r')
D2 = {} 
for Line in FL2:
	Line = Line.strip().replace('\n','')
	Elements = re.split('\t', Line)
	queryId = Elements[0]
	subjectId = Elements[1]
	if ( not ( queryId in D2.keys() ) ):
		D2[queryId] = []
		D2[queryId].append(subjectId)  
	else:
		D2[queryId].append(subjectId)

OF = open(outfile, 'w')


for id1 in D1.keys():
	for value1 in D1[id1]:
		if ( value1 in D2.keys() ):
			if ( id1 in D2[value1] ) :
				OF.write(value1+'\t'+id1+'\n')
