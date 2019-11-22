#!/usr/bin/env
from collections import *;import os;from statistics import *;import sys;import rpy2.robjects as _rtzhc9UHNTo9cHDyEwyLwmIn0QFRgG;_lqjJeXcvoWyqYhcPq6gkLhRQbpqg7J = _rtzhc9UHNTo9cHDyEwyLwmIn0QFRgG.r;sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))));from fitness_of_statistical_tests_pkg.skpy import *

def umrOZU13WStRuwAb7yjy74py4P9nDW(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       _eAQj6AfxCjHiGjDCQv3j3sDYG5GlNs):
    _4vlLbfaYzxaqKIWKNQ3i13ZaTe4IA7 = namedtuple(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           '_4vlLbfaYzxaqKIWKNQ3i13ZaTe4IA7', 'regex mean rank')
    _hcHHHtcgtSbo3xoBi4ebbzZLcSVjVX = dict(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           )
    for _bK7HbIcPJKVNexVX06kCq8FuHo1ztf, _XUIpSD336BQTixWZPnHS81vWwkjyX7 in enumerate(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           _eAQj6AfxCjHiGjDCQv3j3sDYG5GlNs):
        _hcHHHtcgtSbo3xoBi4ebbzZLcSVjVX[_bK7HbIcPJKVNexVX06kCq8FuHo1ztf+1] = _XUIpSD336BQTixWZPnHS81vWwkjyX7[0]

    _FtO8Yau65WLKmh11N82q6Pzb16D6me = [] 
    _fi02Z8Gb6ZmPXEoeNJx6DtfKa91s2r = []
    for _XUIpSD336BQTixWZPnHS81vWwkjyX7 in _eAQj6AfxCjHiGjDCQv3j3sDYG5GlNs:
        for _ZCWQ8l5191AB4QUr9lh3r217zVu7Lk in _XUIpSD336BQTixWZPnHS81vWwkjyX7[1]:
            _FtO8Yau65WLKmh11N82q6Pzb16D6me.append(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   _ZCWQ8l5191AB4QUr9lh3r217zVu7Lk)
            _fi02Z8Gb6ZmPXEoeNJx6DtfKa91s2r.append(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   _XUIpSD336BQTixWZPnHS81vWwkjyX7[0])

    _rtzhc9UHNTo9cHDyEwyLwmIn0QFRgG.globalenv['y'] = _rtzhc9UHNTo9cHDyEwyLwmIn0QFRgG.FloatVector(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           _FtO8Yau65WLKmh11N82q6Pzb16D6me)
    _rtzhc9UHNTo9cHDyEwyLwmIn0QFRgG.globalenv['xf'] = _rtzhc9UHNTo9cHDyEwyLwmIn0QFRgG.FactorVector(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           _fi02Z8Gb6ZmPXEoeNJx6DtfKa91s2r)

    _lqjJeXcvoWyqYhcPq6gkLhRQbpqg7J(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'library(ScottKnott)')
    _lqjJeXcvoWyqYhcPq6gkLhRQbpqg7J(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'dfm <- data.frame(y,xf)')
    _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny = None
    _NQ26Xm45nVhQRPlMbS4IscbNximbY4 = []
    try:
        _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny = _lqjJeXcvoWyqYhcPq6gkLhRQbpqg7J(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               'summary(SK(dfm, y=y, model="y ~ xf", which="xf"))')
    except Exception as _Zg3nyB5TAE87Jk7AFjifamy6D13zo8:
        _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny = skpy.scottknott(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               [skpy.Num(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   _f9wnkJHAz6pHosi6UT5TSZLtmtwwHb[0], _f9wnkJHAz6pHosi6UT5TSZLtmtwwHb[1]) for _f9wnkJHAz6pHosi6UT5TSZLtmtwwHb in _eAQj6AfxCjHiGjDCQv3j3sDYG5GlNs])
        for _NNfel7ez8uCGlXneJy9Su4r1VrnJH4 in _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny:
            _NQ26Xm45nVhQRPlMbS4IscbNximbY4.append(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   _4vlLbfaYzxaqKIWKNQ3i13ZaTe4IA7(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       _NNfel7ez8uCGlXneJy9Su4r1VrnJH4.name, mean(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           _NNfel7ez8uCGlXneJy9Su4r1VrnJH4.all), _NNfel7ez8uCGlXneJy9Su4r1VrnJH4.rank+1))
    else:
        for _bK7HbIcPJKVNexVX06kCq8FuHo1ztf, _PVB41p4KA03UsmQif3rzj5rWRy0x22 in enumerate(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny[0]):
            _NQ26Xm45nVhQRPlMbS4IscbNximbY4.append(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   _4vlLbfaYzxaqKIWKNQ3i13ZaTe4IA7(

















                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       _hcHHHtcgtSbo3xoBi4ebbzZLcSVjVX[_PVB41p4KA03UsmQif3rzj5rWRy0x22], _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny[1][_bK7HbIcPJKVNexVX06kCq8FuHo1ztf], _VkIlqVpX5RIpTJ4GqUgYx1H6SQK6Ny[2][_bK7HbIcPJKVNexVX06kCq8FuHo1ztf]))
    
    return _NQ26Xm45nVhQRPlMbS4IscbNximbY4