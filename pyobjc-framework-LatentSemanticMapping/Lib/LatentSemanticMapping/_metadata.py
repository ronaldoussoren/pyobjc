# Generated file, don't edit
# Source: BridgeSupport/LatentSemanticMapping.bridgesupport
# Last update: Thu Jul 21 08:48:28 2011

import objc, sys

if sys.maxint > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$'''
enums = '''$kLSMClusterAgglomerative@4$kLSMClusterCategories@0$kLSMClusterKMeans@0$kLSMClusterTokens@2$kLSMClusterWords@1$kLSMMapBadCluster@-6644$kLSMMapBadPath@-6643$kLSMMapDiscardCounts@1$kLSMMapHashText@256$kLSMMapLoadMutable@2$kLSMMapNoSuchCategory@-6641$kLSMMapOutOfState@-6640$kLSMMapPairs@1$kLSMMapTriplets@2$kLSMMapWriteError@-6642$kLSMResultBestWords@1$kLSMTextApplySpamHeuristics@4$kLSMTextPreserveAcronyms@2$kLSMTextPreserveCase@1$'''
misc.update({'kLSMAlgorithmDense': 'LSMAlgorithmDense', 'kLSMPrecisionFloat': 'LSMPrecisionFloat', 'kLSMSweepCutoffKey': 'LSMSweepCutoff', 'kLSMAlgorithmSparse': 'LSMAlgorithmSparse', 'kLSMDimensionKey': 'LSMDimension', 'kLSMAlgorithmKey': 'LSMAlgorithm', 'kLSMPrecisionKey': 'LSMPrecision', 'kLSMPrecisionDouble': 'LSMPrecisionDouble', 'kLSMSweepAgeKey': 'LSMSweepAge', 'kLSMIterationsKey': 'LSMIterations'})
functions = {'LSMMapGetCategoryCount': (sel32or64('l^{__LSMMap=}', 'q^{__LSMMap=}'),), 'LSMMapAddTextWithWeight': (sel32or64('l^{__LSMMap=}^{__LSMText=}If', 'i^{__LSMMap=}^{__LSMText=}If'),), 'LSMTextAddToken': (sel32or64('l^{__LSMText=}^{__CFData=}', 'i^{__LSMText=}^{__CFData=}'),), 'LSMMapSetStopWords': (sel32or64('l^{__LSMMap=}^{__LSMText=}', 'i^{__LSMMap=}^{__LSMText=}'),), 'LSMTextGetTypeID': (sel32or64('L', 'Q'),), 'LSMMapStartTraining': (sel32or64('l^{__LSMMap=}', 'i^{__LSMMap=}'),), 'LSMMapCompile': (sel32or64('l^{__LSMMap=}', 'i^{__LSMMap=}'),), 'LSMMapWriteToStream': (sel32or64('l^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}L', 'i^{__LSMMap=}^{__LSMText=}^{__CFWriteStream=}L'),), 'LSMResultCopyWordCluster': ('^{__CFArray=}^{__LSMResult=}l', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'LSMResultGetCount': (sel32or64('l^{__LSMResult=}', 'q^{__LSMResult=}'),), 'LSMResultGetCategory': ('I^{__LSMResult=}l',), 'LSMMapCreate': ('^{__LSMMap=}^{__CFAllocator=}L', '', {'retval': {'type': b'^{__LSMMap=}', 'already_cfretained': True}}), 'LSMResultGetTypeID': (sel32or64('L', 'Q'),), 'LSMResultCreate': ('^{__LSMResult=}^{__CFAllocator=}^{__LSMMap=}^{__LSMText=}lL', '', {'retval': {'type': b'^{__LSMResult=}', 'already_cfretained': True}}), 'LSMResultCopyWord': ('^{__CFString=}^{__LSMResult=}l', '', {'retval': {'type': b'^{__CFString=}', 'already_cfretained': True}}), 'LSMMapCreateClusters': ('^{__CFArray=}^{__CFAllocator=}^{__LSMMap=}^{__CFArray=}lL', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'LSMMapApplyClusters': (sel32or64('l^{__LSMMap=}^{__CFArray=}', 'i^{__LSMMap=}^{__CFArray=}'),), 'LSMTextAddWords': (sel32or64('l^{__LSMText=}^{__CFString=}^{__CFLocale=}L', 'i^{__LSMText=}^{__CFString=}^{__CFLocale=}L'),), 'LSMResultCopyTokenCluster': ('^{__CFArray=}^{__LSMResult=}l', '', {'retval': {'type': b'^{__CFArray=}', 'already_cfretained': True}}), 'LSMMapAddText': (sel32or64('l^{__LSMMap=}^{__LSMText=}I', 'i^{__LSMMap=}^{__LSMText=}I'),), 'LSMTextCreate': ('^{__LSMText=}^{__CFAllocator=}^{__LSMMap=}', '', {'retval': {'type': b'^{__LSMText=}', 'already_cfretained': True}}), 'LSMMapWriteToURL': (sel32or64('l^{__LSMMap=}^{__CFURL=}L', 'i^{__LSMMap=}^{__CFURL=}L'),), 'LSMResultGetScore': ('f^{__LSMResult=}l',), 'LSMMapCreateFromURL': ('^{__LSMMap=}^{__CFAllocator=}^{__CFURL=}L', '', {'retval': {'type': b'^{__LSMMap=}', 'already_cfretained': True}}), 'LSMMapSetProperties': ('v^{__LSMMap=}^{__CFDictionary=}',), 'LSMResultCopyToken': ('^{__CFData=}^{__LSMResult=}l', '', {'retval': {'type': b'^{__CFData=}', 'already_cfretained': True}}), 'LSMMapGetProperties': ('^{__CFDictionary=}^{__LSMMap=}',), 'LSMMapAddCategory': ('I^{__LSMMap=}',), 'LSMTextAddWord': (sel32or64('l^{__LSMText=}^{__CFString=}', 'i^{__LSMText=}^{__CFString=}'),), 'LSMMapGetTypeID': (sel32or64('L', 'Q'),)}
cftypes = []
cftypes.append(('LSMMapRef', '^{__LSMMap=}', 'LSMMapGetTypeID', None))
cftypes.append(('LSMResultRef', '^{__LSMResult=}', 'LSMResultGetTypeID', None))
cftypes.append(('LSMTextRef', '^{__LSMText=}', 'LSMTextGetTypeID', None))
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    pass
finally:
    objc._updatingMetadata(False)
