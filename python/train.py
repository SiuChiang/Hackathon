import os
import sys
from clarifai_basic import ClarifaiCustomModel
concept = ClarifaiCustomModel()
filename = sys.argv[1]
tag = sys.argv[2]
tagArray = ['HeavyMetal','Rap', 'Alternative','Pop','Country','Classical','Electronic']
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        print line
        for genre in tagArray:
            try:
                if genre == tag:
                    print 'Yes'
                    concept.positive(line,tag)
                #else:
                    #concept.negative(line,tag)
            except:
                print 'Fail' , line
                pass
concept.train(tag)
