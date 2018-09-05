#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 11:12:01 2018

@author: can
"""

import pandas as pd

f=pd.read_excel("datalar/al2.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)
ff=pd.read_excel("datalar/cu2.xlsx",header=None, names=["Wavelength","Sum"],skiprows=4)
s=f['Sum'].values
start=100
source=ff.query('Sum > '+str(start))